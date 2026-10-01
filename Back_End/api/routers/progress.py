"""
Router: Progress & Active Recall Multi-Stage Validation
Menyediakan endpoint validasi langkah scaffolding (/api/progress/validate_step),
integrasi AI Tutor Socratic, dan pembaharuan status kelulusan materi.
"""
from flask import Blueprint, jsonify, request, g, session
from Back_End.core.security import get_current_user_id
from Back_End.services.progress_svc import ProgressService
from Back_End.services.ai_tutor_svc import AITutorService, CHECKPOINT_CURRICULUM
from Back_End.models.schemas import ValidateStepRequest
from Back_End.database.connection import get_db_session
from Back_End.models.domain import Material, UserProgress
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

progress_router = Blueprint("progress_router", __name__)

@progress_router.route("/progress/validate_step", methods=["POST"])
def validate_step():
    """
    ENDPOINT ACTIVE RECALL & MULTI-STAGE STEP VALIDATION:
    1. Pengguna mengirim jawaban bertahap ke /api/progress/validate_step.
    2. Jika jawaban salah -> AI Tutor menganalisis kesalahan dan mengembalikan petunjuk adaptif.
    3. Jika benar dan seluruh tahap selesai -> Server memperbarui status user_progress menjadi Completed!
    """
    try:
        body = request.get_json() or {}
        req_data = ValidateStepRequest(**body)
    except ValidationError as err:
        return jsonify({
            "status": "error",
            "error": "Validation Error",
            "details": err.errors()
        }), 422
    except Exception as e:
        return jsonify({"status": "error", "message": "Format request tidak valid"}), 400

    user_id = get_current_user_id() or session.get("user_id", 0)
    svc = ProgressService()

    # Identifikasi materi dan modul
    material = None
    if req_data.material_id:
        material = svc.get_material_by_id(req_data.material_id)
    elif req_data.material_slug:
        material = svc.get_material_by_slug(req_data.material_slug)

    # Identifikasi key modul (misal: 'integral', 'limit', 'aljabar')
    module_key = "integral"
    if req_data.module_slug:
        module_key = req_data.module_slug.strip().lower()
    elif material and material.module:
        module_key = material.module.slug.strip().lower()
    elif req_data.material_slug:
        for k in CHECKPOINT_CURRICULUM.keys():
            if k in req_data.material_slug.lower():
                module_key = k
                break

    # 1. Validasi Jawaban Menggunakan AITutorService
    is_correct, is_final, step_info = AITutorService.validate_step(
        module_key=module_key,
        step_index=req_data.step_index,
        user_answer=req_data.user_answer
    )

    prog = None
    if material and user_id:
        prog = svc.get_or_create_progress(user_id, material.id)
        prog.attempts_count = (prog.attempts_count or 0) + 1
        prog.time_spent_seconds = (prog.time_spent_seconds or 0) + (req_data.time_spent_seconds or 0)
        svc.session.commit()

    # KASUS A: Jawaban Salah
    if not is_correct:
        # Panggil AI Tutor untuk membangkitkan Socratic hint adaptif
        ai_hint = AITutorService.generate_socratic_hint(
            module_key=module_key,
            step_index=req_data.step_index,
            user_input=req_data.user_answer,
            step_info=step_info
        )
        return jsonify({
            "status": "incorrect",
            "is_correct": False,
            "is_final_step": False,
            "current_step": req_data.step_index,
            "feedback_message": "Jawaban pada tahap ini belum tepat. Cermati petunjuk dari AI Tutor di bawah ini:",
            "ai_hint": ai_hint,
            "user_progress_status": prog.status if prog else "In_Progress"
        }), 200

    # KASUS B: Jawaban Benar, Tapi Masih Ada Tahap Berikutnya
    if not is_final:
        if prog:
            prog.current_stage = max(prog.current_stage or 0, req_data.step_index)
            prog.status = "In_Progress"
            svc.session.commit()

        return jsonify({
            "status": "correct_step",
            "is_correct": True,
            "is_final_step": False,
            "current_step": req_data.step_index,
            "next_step": req_data.step_index + 1,
            "feedback_message": f"Tahap {req_data.step_index} berhasil divalidasi dengan tepat! Lanjutkan ke tahap {req_data.step_index + 1}.",
            "ai_hint": "Bagus sekali! Pemahaman konsepmu pada tahap ini sudah solid.",
            "user_progress_status": "In_Progress"
        }), 200

    # KASUS C: Jawaban Benar & Ini Adalah Tahap Terakhir (SELESAI)
    unlocked_next = []
    if material and user_id:
        res = svc.complete_material(
            user_id=user_id,
            material_id=material.id,
            score=100,
            time_spent=req_data.time_spent_seconds or 0
        )
        unlocked_next = res.get("unlocked_next", [])
        user_status = "Completed"
    else:
        user_status = "Completed"

    return jsonify({
        "status": "completed",
        "is_correct": True,
        "is_final_step": True,
        "current_step": req_data.step_index,
        "feedback_message": "Luar biasa! Seluruh tahapan scaffolding berhasil kamu selesaikan secara sempurna.",
        "ai_hint": "Selamat! Konsep ini telah berhasil kamu kuasai secara mendalam (Mastered).",
        "user_progress_status": user_status,
        "score": 100,
        "unlocked_next": unlocked_next
    }), 200

@progress_router.route("/progress/status", methods=["GET"])
def get_user_learning_summary():
    """Mengambil rangkuman progres pembelajaran pengguna."""
    user_id = get_current_user_id() or session.get("user_id", 0)
    svc = ProgressService()
    syllabus = svc.get_full_syllabus(user_id)
    
    total_mats = sum(c["total_materials"] for c in syllabus)
    completed_mats = sum(c["completed_materials"] for c in syllabus)
    overall_percentage = round((completed_mats / total_mats * 100) if total_mats > 0 else 0, 1)

    return jsonify({
        "status": "success",
        "user_id": user_id,
        "total_materials": total_mats,
        "completed_materials": completed_mats,
        "overall_percentage": overall_percentage,
        "is_certified": (completed_mats == total_mats and total_mats > 0)
    }), 200
