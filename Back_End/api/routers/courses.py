"""
Router: Courses, Modules & Materials Gatekeeping
Menyediakan endpoint kurikulum, silabus, dan akses materi dengan validasi prasyarat (403 Forbidden).
"""
from flask import Blueprint, jsonify, request, g, session
from Back_End.core.security import auth_required, get_current_user_id
from Back_End.services.progress_svc import ProgressService
from Back_End.database.connection import get_db_session
from Back_End.models.domain import Course, Module, Material
import logging

logger = logging.getLogger(__name__)

courses_router = Blueprint("courses_router", __name__)

@courses_router.route("/courses", methods=["GET"])
def list_courses():
    """Mengambil daftar semua kelas/kursus utama."""
    db_session = get_db_session()
    courses = db_session.query(Course).filter(Course.is_active == True).order_by(Course.order_index).all()
    return jsonify({
        "status": "success",
        "data": [c.to_dict() for c in courses]
    }), 200

@courses_router.route("/courses/syllabus", methods=["GET"])
def get_curriculum_syllabus():
    """
    Mengambil silabus berjenjang beserta status progres per materi
    (Locked, In_Progress, Completed) untuk user yang sedang aktif.
    """
    user_id = get_current_user_id() or 0
    svc = ProgressService()
    syllabus = svc.get_full_syllabus(user_id)
    return jsonify({
        "status": "success",
        "user_id": user_id,
        "syllabus": syllabus
    }), 200

@courses_router.route("/materials/<string:slug>", methods=["GET"])
def get_material_content(slug):
    """
    LOGIKA GATEKEEPING PENGUNCIAN MATERI (Level API):
    Request Materi: Saat pengguna mencoba mengakses /api/materials/<slug>.
    Validasi Backend:
      Fungsi di progress_svc.py mengecek tabel user_progress.
      Apakah user_id tersebut memiliki status Completed pada material prasyarat (prerequisite_id)?
    Response:
      - Jika sudah selesai: Kirimkan JSON berisi konten materi.
      - Jika belum selesai: Kembalikan error 403 Forbidden dengan pesan "Selesaikan [Bab sebelumnya] terlebih dahulu."
    """
    user_id = get_current_user_id()
    if not user_id:
        # Fallback guest user atau demonstrasi, tapi jika login diperlukan:
        user_id = session.get("user_id", 0)

    svc = ProgressService()
    material = svc.get_material_by_slug(slug)
    if not material:
        return jsonify({
            "status": "error",
            "error": "Not Found",
            "message": f"Materi dengan slug '{slug}' tidak ditemukan."
        }), 404

    # 1. Validasi Gatekeeping
    can_access, error_msg, prereq_material = svc.can_user_access_material(user_id, material)
    if not can_access:
        prereq_title = prereq_material.title if prereq_material else "materi prasyarat"
        return jsonify({
            "status": "forbidden",
            "error": "Forbidden",
            "is_locked": True,
            "message": f"Selesaikan {prereq_title} terlebih dahulu.",
            "prerequisite": {
                "id": prereq_material.id if prereq_material else None,
                "title": prereq_title,
                "slug": prereq_material.slug if prereq_material else None
            }
        }), 403

    # 2. Jika lolos gatekeeping, perbarui status menjadi In_Progress jika masih Locked
    prog = svc.get_or_create_progress(user_id, material.id)

    # Ambil materi berikutnya jika ada
    next_mat = svc.session.query(Material).filter(Material.prerequisite_id == material.id).first()

    return jsonify({
        "status": "success",
        "is_locked": False,
        "data": {
            "id": material.id,
            "title": material.title,
            "slug": material.slug,
            "chapter_number": material.chapter_number,
            "is_checkpoint": material.is_checkpoint,
            "module_id": material.module_id,
            "module_name": material.module.name if material.module else "",
            "module_slug": material.module.slug if material.module else "",
            "course_title": material.module.course.title if (material.module and material.module.course) else "",
            "summary": material.summary,
            "content": material.content,
            "user_progress": {
                "status": prog.status,
                "current_stage": prog.current_stage,
                "score": prog.score,
                "attempts_count": prog.attempts_count
            },
            "next_material": {
                "id": next_mat.id,
                "title": next_mat.title,
                "slug": next_mat.slug
            } if next_mat else None
        }
    }), 200
