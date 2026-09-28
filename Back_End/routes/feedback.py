import csv
import io
import json
import logging
from flask import Blueprint, request, jsonify, current_app, Response, session
from Back_End.routes.security_for_web import admin_required, user_required
from Back_End.feedback.feedback_logic import (
    analyze_and_save_feedback,
    get_all_feedback,
    get_feedback_analytics,
    update_feedback_workflow,
    delete_feedback,
    reanalyze_all_feedback,
    generate_ai_smart_reply,
    generate_ai_executive_summary,
    generate_ai_ticket_action_plan,
    generate_ai_root_cause_diagnosis,
    generate_ai_developer_backlog,
    chat_with_feedback_ai,
    FEATURE_DEFINITIONS,
)

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit', methods=['POST'])
@user_required
def submit_feedback_route():
    """Endpoint untuk user mengirimkan feedback."""
    try:
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({'success': False, 'error': 'Data feedback tidak valid.'}), 400
        
        # Panggil logic dari feedback_logic.py
        analysis_result = analyze_and_save_feedback(data)
        
        return jsonify({
            'success': True,
            'message': 'Feedback berhasil dianalisis dengan Case-Based Reasoning (CBR)',
            'analysis': analysis_result
        })
    except Exception as e:
        logging.error(f"Feedback submission error: {e}", exc_info=True)
        return jsonify({'success': False, 'error': 'Terjadi kesalahan internal saat memproses feedback.'}), 500


@feedback_bp.route('/list', methods=['GET'])
@admin_required
def get_feedback_list_route():
    """Endpoint untuk admin mengambil semua data feedback dengan filter dan pencarian opsional."""
    try:
        search = request.args.get('search', '').strip().lower()
        category_filter = request.args.get('category', '').strip()
        priority_filter = request.args.get('priority', '').strip()
        status_filter = request.args.get('status', '').strip()
        sort_by = request.args.get('sort', 'newest').strip()

        all_feedback = get_all_feedback(with_feature_meta=True)

        filtered = []
        for item in all_feedback:
            # Filter pencarian
            if search:
                user_match = search in item.get('user', '').lower()
                comment_match = search in item.get('comment', '').lower()
                cat_match = search in item.get('analysis', {}).get('category', '').lower()
                recom_match = search in item.get('analysis', {}).get('recommendation', '').lower()
                if not (user_match or comment_match or cat_match or recom_match):
                    continue

            # Filter kategori
            if category_filter and category_filter != 'all':
                if item.get('analysis', {}).get('category') != category_filter:
                    continue

            # Filter prioritas
            if priority_filter and priority_filter != 'all':
                if item.get('workflow', {}).get('priority') != priority_filter:
                    continue

            # Filter status workflow
            if status_filter and status_filter != 'all':
                if item.get('workflow', {}).get('status') != status_filter:
                    continue

            filtered.append(item)

        # Pengurutan
        if sort_by == 'oldest':
            filtered.sort(key=lambda x: x.get('timestamp', ''))
        elif sort_by == 'similarity':
            filtered.sort(key=lambda x: x.get('analysis', {}).get('similarity_raw', 0), reverse=True)
        elif sort_by == 'priority':
            priority_order = {'kritis': 4, 'tinggi': 3, 'normal': 2, 'rendah': 1}
            filtered.sort(key=lambda x: priority_order.get(x.get('workflow', {}).get('priority', 'normal'), 0), reverse=True)
        else: # 'newest' default
            filtered.sort(key=lambda x: x.get('timestamp', ''), reverse=True)

        return jsonify(filtered)
    except Exception as e:
        logging.error(f"Get feedback list error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal mengambil daftar feedback.'}), 500


@feedback_bp.route('/analytics', methods=['GET'])
@admin_required
def feedback_analytics_route():
    """Statistik teragregasi lengkap untuk visualisasi dashboard tindak lanjut admin."""
    try:
        records = get_all_feedback(with_feature_meta=False)
        return jsonify(get_feedback_analytics(records))
    except Exception as e:
        logging.error(f"Feedback analytics error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal membuat analisis feedback.'}), 500


@feedback_bp.route('/<feedback_id>/workflow', methods=['PATCH'])
@admin_required
def update_feedback_workflow_route(feedback_id):
    """Ubah status, prioritas, respons admin, dan rencana aksi internal."""
    try:
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({'error': 'Data pembaruan tidak valid.'}), 400

        admin_name = session.get('name') or session.get('username') or 'Administrator'
        record = update_feedback_workflow(feedback_id, data, admin_user=admin_name)
        if record is None:
            return jsonify({'error': 'Feedback tidak ditemukan.'}), 404
        return jsonify({'success': True, 'feedback': record})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f"Feedback workflow update error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal menyimpan tindak lanjut feedback.'}), 500


@feedback_bp.route('/<feedback_id>', methods=['DELETE'])
@admin_required
def delete_feedback_route(feedback_id):
    """Menghapus feedback spam atau data uji coba."""
    try:
        success = delete_feedback(feedback_id)
        if not success:
            return jsonify({'error': 'Feedback tidak ditemukan.'}), 404
        return jsonify({'success': True, 'message': 'Feedback berhasil dihapus.'})
    except Exception as e:
        logging.error(f"Delete feedback error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal menghapus feedback.'}), 500


@feedback_bp.route('/reanalyze', methods=['POST'])
@admin_required
def reanalyze_feedback_route():
    """Menjalankan ulang seluruh algoritma CBR & NLP pada seluruh feedback tersimpan."""
    try:
        updated_count = reanalyze_all_feedback()
        return jsonify({
            'success': True,
            'message': f'Berhasil menganalisis ulang {updated_count} feedback dengan algoritma CBR mutakhir.'
        })
    except Exception as e:
        logging.error(f"Reanalyze feedback error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal memproses ulang feedback.'}), 500


@feedback_bp.route('/<feedback_id>/ai-reply', methods=['POST'])
@admin_required
def ai_reply_feedback_route(feedback_id):
    """Membuat draf balasan solutif untuk pengguna menggunakan AI Gemini dengan tone terpilih."""
    try:
        data = request.get_json(silent=True) or {}
        tone = data.get('tone', 'friendly')

        records = get_all_feedback(with_feature_meta=True)
        target = next((r for r in records if r.get('id') == feedback_id), None)
        if not target:
            return jsonify({'error': 'Feedback tidak ditemukan.'}), 404

        draft_reply = generate_ai_smart_reply(target, tone=tone)
        return jsonify({'success': True, 'draft_reply': draft_reply, 'tone': tone})
    except Exception as e:
        logging.error(f"AI draft reply error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal membuat draf balasan AI.'}), 500


@feedback_bp.route('/<feedback_id>/ai-action-plan', methods=['POST'])
@admin_required
def ai_action_plan_feedback_route(feedback_id):
    """Membuat rencana aksi teknis internal otomatis untuk tiket feedback dengan AI."""
    try:
        records = get_all_feedback(with_feature_meta=True)
        target = next((r for r in records if r.get('id') == feedback_id), None)
        if not target:
            return jsonify({'error': 'Feedback tidak ditemukan.'}), 404

        action_plan = generate_ai_ticket_action_plan(target)
        return jsonify({'success': True, 'action_plan': action_plan})
    except Exception as e:
        logging.error(f"AI action plan error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal membuat rencana aksi internal AI.'}), 500


@feedback_bp.route('/ai-overview', methods=['GET'])
@admin_required
def ai_overview_feedback_route():
    """Menghasilkan ringkasan eksekutif strategis dengan AI Gemini."""
    try:
        records = get_all_feedback(with_feature_meta=False)
        summary = generate_ai_executive_summary(records)
        return jsonify({'success': True, 'summary': summary})
    except Exception as e:
        logging.error(f"AI overview error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal membuat ringkasan eksekutif AI.'}), 500


@feedback_bp.route('/ai/diagnose', methods=['POST', 'GET'])
@admin_required
def ai_diagnose_feedback_route():
    """Diagnosa akar masalah (Root Cause Analysis) dengan AI."""
    try:
        records = get_all_feedback(with_feature_meta=True)
        diagnosis = generate_ai_root_cause_diagnosis(records)
        return jsonify({'success': True, 'diagnosis': diagnosis})
    except Exception as e:
        logging.error(f"AI diagnose error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal membuat diagnosa akar masalah AI.'}), 500


@feedback_bp.route('/ai/backlog', methods=['POST', 'GET'])
@admin_required
def ai_backlog_feedback_route():
    """Membuat Sprint Backlog Developer dari keluhan siswa dengan AI."""
    try:
        records = get_all_feedback(with_feature_meta=True)
        backlog = generate_ai_developer_backlog(records)
        return jsonify({'success': True, 'backlog': backlog})
    except Exception as e:
        logging.error(f"AI backlog error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal membuat developer backlog AI.'}), 500


@feedback_bp.route('/ai/chat', methods=['POST'])
@admin_required
def ai_chat_feedback_route():
    """Chat interaktif dengan AI Copilot seputar masukan pengguna."""
    try:
        data = request.get_json(silent=True) or {}
        user_query = data.get('query', '').strip()
        if not user_query:
            return jsonify({'error': 'Pertanyaan tidak boleh kosong.'}), 400

        history = data.get('history', [])
        records = get_all_feedback(with_feature_meta=True)
        reply = chat_with_feedback_ai(user_query, records, history=history)
        return jsonify({'success': True, 'reply': reply})
    except Exception as e:
        logging.error(f"AI copilot chat error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal memproses pertanyaan copilot AI.'}), 500


@feedback_bp.route('/export', methods=['GET'])
@admin_required
def export_feedback_route():
    """Mengekspor seluruh data feedback ke format CSV atau JSON."""
    try:
        export_format = request.args.get('format', 'csv').lower()
        records = get_all_feedback(with_feature_meta=True)

        if export_format == 'json':
            json_str = json.dumps(records, indent=2, ensure_ascii=False)
            return Response(
                json_str,
                mimetype='application/json',
                headers={'Content-Disposition': 'attachment; filename=maththon_feedback_export.json'}
            )

        # Default: CSV dengan BOM UTF-8 untuk kompatibilitas sempurna dengan Microsoft Excel
        output = io.StringIO()
        output.write('\ufeff') # UTF-8 BOM
        writer = csv.writer(output)

        writer.writerow([
            'ID', 'Waktu', 'Pengguna', 'Komentar', 'Fitur Dipilih',
            'Kategori CBR', 'Status Analisis', 'Kemiripan CBR', 'Sentimen',
            'Rekomendasi CBR', 'Status Tindak Lanjut', 'Prioritas',
            'Respons Admin', 'Rencana Aksi', 'Diperbarui Pada', 'Diperbarui Oleh'
        ])

        for r in records:
            features_str = ', '.join([f['name'] for f in r.get('feature_details', [])]) if r.get('feature_details') else ', '.join(r.get('features', []))
            analysis = r.get('analysis', {})
            workflow = r.get('workflow', {})

            writer.writerow([
                r.get('id', ''),
                r.get('timestamp', ''),
                r.get('user', 'Anonymous'),
                r.get('comment', ''),
                features_str,
                analysis.get('category', ''),
                analysis.get('status', ''),
                analysis.get('similarity', ''),
                analysis.get('sentiment', ''),
                analysis.get('recommendation', ''),
                workflow.get('status', 'baru'),
                workflow.get('priority', 'normal'),
                workflow.get('admin_response', ''),
                workflow.get('action_plan', ''),
                workflow.get('updated_at', ''),
                workflow.get('updated_by', '')
            ])

        csv_content = output.getvalue()
        return Response(
            csv_content,
            mimetype='text/csv; charset=utf-8',
            headers={'Content-Disposition': 'attachment; filename=maththon_feedback_export.csv'}
        )
    except Exception as e:
        logging.error(f"Export feedback error: {e}", exc_info=True)
        return jsonify({'error': 'Gagal mengekspor data feedback.'}), 500


@feedback_bp.route('/features', methods=['GET'])
@admin_required
def get_feedback_features_route():
    """Mengembalikan daftar master definisi fitur untuk keperluan UI."""
    return jsonify(FEATURE_DEFINITIONS)
