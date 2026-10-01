"""
Service: Progress & Gatekeeping Business Logic
Mengelola status belajar pengguna, validasi prasyarat (gatekeeping),
dan pembukaan kunci (unlocking) materi secara berantai.
"""
from typing import Tuple, Dict, Any, Optional, List
from datetime import datetime
from sqlalchemy.orm import Session
from Back_End.database.connection import get_db_session
from Back_End.models.domain import Course, Module, Material, UserProgress, User
import logging

logger = logging.getLogger(__name__)

class ProgressService:
    def __init__(self, db_session: Optional[Session] = None):
        self.session = db_session or get_db_session()

    def get_material_by_slug(self, slug: str) -> Optional[Material]:
        """Cari record material berdasarkan slug unik."""
        clean_slug = slug.strip().lower()
        return self.session.query(Material).filter(Material.slug == clean_slug).first()

    def get_material_by_id(self, material_id: int) -> Optional[Material]:
        """Cari record material berdasarkan ID."""
        return self.session.query(Material).filter(Material.id == material_id).first()

    def get_user_progress(self, user_id: int, material_id: int) -> Optional[UserProgress]:
        """Mengambil record user_progress untuk material tertentu."""
        return self.session.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.material_id == material_id
        ).first()

    def can_user_access_material(self, user_id: int, material: Material) -> Tuple[bool, Optional[str], Optional[Material]]:
        """
        LOGIKA GATEKEEPING UTAMA:
        Mengecek apakah user berhak mengakses suatu materi.
        - Jika material tidak memiliki prerequisite_id -> Boleh akses (True).
        - Jika ada prerequisite_id -> Cek apakah user_progress untuk prerequisite_id berstatus 'Completed'.
        Return: (is_allowed, error_message, prerequisite_material)
        """
        if not material.prerequisite_id:
            return True, None, None

        # Ambil material prasyarat
        prereq = self.session.query(Material).filter(Material.id == material.prerequisite_id).first()
        if not prereq:
            # Jika prasyarat tidak ditemukan di database, izinkan akses default
            return True, None, None

        # Cek progres user pada material prasyarat
        prereq_progress = self.session.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.material_id == prereq.id
        ).first()

        if prereq_progress and prereq_progress.status == "Completed":
            return True, None, prereq

        # Jika belum completed -> Tolak akses dengan pesan edukatif
        error_msg = f"Selesaikan {prereq.title} terlebih dahulu."
        return False, error_msg, prereq

    def get_or_create_progress(self, user_id: int, material_id: int) -> UserProgress:
        """Mengambil atau menginisialisasi record progress user."""
        prog = self.get_user_progress(user_id, material_id)
        if not prog:
            prog = UserProgress(
                user_id=user_id,
                material_id=material_id,
                status="In_Progress",
                current_stage=0,
                attempts_count=0,
                time_spent_seconds=0
            )
            self.session.add(prog)
            self.session.commit()
        elif prog.status == "Locked":
            prog.status = "In_Progress"
            self.session.commit()
        return prog

    def complete_material(self, user_id: int, material_id: int, score: int = 100, time_spent: int = 0) -> Dict[str, Any]:
        """
        Menandai suatu materi sebagai 'Completed' dan membuka akses
        ke materi turunan berikutnya.
        """
        prog = self.get_user_progress(user_id, material_id)
        if not prog:
            prog = UserProgress(
                user_id=user_id,
                material_id=material_id,
                status="Completed",
                score=score,
                completed_at=datetime.utcnow(),
                time_spent_seconds=time_spent
            )
            self.session.add(prog)
        else:
            prog.status = "Completed"
            prog.score = max(prog.score or 0, score)
            prog.completed_at = datetime.utcnow()
            prog.time_spent_seconds = (prog.time_spent_seconds or 0) + time_spent

        self.session.commit()

        # Cari materi berikutnya yang prasyaratnya adalah materi ini
        next_materials = self.session.query(Material).filter(Material.prerequisite_id == material_id).all()
        unlocked_items = []
        for n_mat in next_materials:
            n_prog = self.get_user_progress(user_id, n_mat.id)
            if not n_prog:
                n_prog = UserProgress(
                    user_id=user_id,
                    material_id=n_mat.id,
                    status="In_Progress",
                    current_stage=0
                )
                self.session.add(n_prog)
            elif n_prog.status == "Locked":
                n_prog.status = "In_Progress"
            unlocked_items.append({"id": n_mat.id, "title": n_mat.title, "slug": n_mat.slug})

        self.session.commit()

        return {
            "material_id": material_id,
            "status": "Completed",
            "score": prog.score,
            "unlocked_next": unlocked_items
        }

    def get_full_syllabus(self, user_id: int) -> List[Dict[str, Any]]:
        """
        Menghasilkan kurikulum lengkap berjenjang (Course -> Module -> Material)
        beserta status gembok (Locked, In_Progress, Completed) untuk masing-masing item.
        """
        courses = self.session.query(Course).filter(Course.is_active == True).order_by(Course.order_index).all()
        
        # Ambil seluruh progres user untuk kalkulasi cepat
        user_progs = self.session.query(UserProgress).filter(UserProgress.user_id == user_id).all()
        prog_map = {p.material_id: p for p in user_progs}

        syllabus = []
        for c in courses:
            c_data = {
                "id": c.id,
                "title": c.title,
                "slug": c.slug,
                "description": c.description,
                "modules": [],
                "total_materials": 0,
                "completed_materials": 0
            }

            for m in c.modules:
                if not m.is_active:
                    continue
                
                m_data = {
                    "id": m.id,
                    "name": m.name,
                    "slug": m.slug,
                    "description": m.description,
                    "order_index": m.order_index,
                    "materials": [],
                    "total_materials": len(m.materials),
                    "completed_materials": 0
                }

                for mat in m.materials:
                    c_data["total_materials"] += 1
                    user_prog = prog_map.get(mat.id)
                    
                    # Tentukan status akses & status pengerjaan
                    status = "Locked"
                    score = 0
                    current_stage = 0
                    
                    if user_prog:
                        status = user_prog.status
                        score = user_prog.score
                        current_stage = user_prog.current_stage

                    # Cek gatekeeping apakah prasyarat terpenuhi jika belum completed
                    is_accessible = False
                    if status == "Completed":
                        is_accessible = True
                        m_data["completed_materials"] += 1
                        c_data["completed_materials"] += 1
                    else:
                        can_access, _, _ = self.can_user_access_material(user_id, mat)
                        is_accessible = can_access
                        if can_access and status == "Locked":
                            status = "In_Progress"

                    m_data["materials"].append({
                        "id": mat.id,
                        "title": mat.title,
                        "slug": mat.slug,
                        "chapter_number": mat.chapter_number,
                        "is_checkpoint": mat.is_checkpoint,
                        "prerequisite_id": mat.prerequisite_id,
                        "summary": mat.summary,
                        "status": status,
                        "score": score,
                        "current_stage": current_stage,
                        "is_accessible": is_accessible
                    })

                m_data["completion_percentage"] = round(
                    (m_data["completed_materials"] / m_data["total_materials"] * 100) if m_data["total_materials"] > 0 else 0, 1
                )
                c_data["modules"].append(m_data)

            syllabus.append(c_data)

        return syllabus
