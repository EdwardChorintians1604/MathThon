from flask import Blueprint, request, jsonify, current_app, render_template
from Back_End.routes.security_for_web import admin_required, user_required
from Back_End.feedback.feedback_logic import analyze_and_save_feedback, get_all_feedback
import logging

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit', methods=['POST'])
@user_required
def submit_feedback_route():
    """Endpoint untuk user mengirimkan feedback."""
    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'success': False, 'error': 'Data feedback tidak valid.'}), 400
        
        # Panggil logic dari feedback_logic.py
        analysis_result = analyze_and_save_feedback(data)
        
        return jsonify({
            'success': True,
            'message': 'Feedback berhasil dianalisis dengan CBR',
            'analysis': analysis_result
        })
    except Exception as e:
        logging.error(f"Feedback submission error: {e}")
        return jsonify({'success': False, 'error': 'Terjadi kesalahan internal saat memproses feedback.'}), 500

@feedback_bp.route('/list', methods=['GET'])
@admin_required
def get_feedback_list_route():
    """Endpoint untuk admin mengambil semua data feedback."""
    try:
        all_feedback = get_all_feedback()
        return jsonify(all_feedback)
    except Exception as e:
        logging.error(f"Get feedback list error: {e}")
        return jsonify({'error': 'Gagal mengambil daftar feedback.'}), 500