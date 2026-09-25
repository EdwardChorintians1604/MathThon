from flask import Blueprint, jsonify, current_app, request, session
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.routes.security_for_web import user_required
import logging
import math
import re

# Blueprint ini akan didaftarkan dengan url_prefix='/api' di __init__.py
api_bp = Blueprint('api', __name__)

@api_bp.route('/materi', methods=['GET'])
def get_all_materi():
    """
    API endpoint untuk mendapatkan daftar semua materi yang tersedia.
    Ini dipanggil oleh JavaScript pada halaman materi_user.html.
    """
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)

        # 1. Periksa kolom apa saja yang benar-benar ada di tabel database
        cursor.execute("SHOW COLUMNS FROM daftar_materi")
        existing_columns = {col['Field'].lower() for col in cursor.fetchall()}

        # 2. Tentukan kolom yang akan dipilih secara dinamis
        select_cols = ['id', 'judul_materi', 'deskripsi']
        optional_cols_with_defaults = {
            'status': 'active',
            'rating': 0,
            'image_url': None,
            'content': None
        }

        for col in optional_cols_with_defaults:
            if col in existing_columns:
                select_cols.append(col)
        
        # 3. Buat dan jalankan query yang aman
        query = f"SELECT {', '.join(select_cols)} FROM daftar_materi"
        cursor.execute(query)
        materi_list = cursor.fetchall()

        # 4. Pastikan semua materi memiliki struktur data yang konsisten untuk frontend
        for materi in materi_list:
            for col, default_value in optional_cols_with_defaults.items():
                if col not in materi:
                    materi[col] = default_value

        return jsonify(materi_list)

    except Exception as e:
        logging.error(f"Error fetching materi from API: {e}")
        # Mengembalikan pesan error JSON yang benar dengan status 500
        return jsonify({"error": "Internal server error while fetching materials."}), 500
    finally:
        if conn:
            close_db_connection(conn)

@api_bp.route('/latihan/submit', methods=['POST'])
@user_required
def submit_latihan_answer():
    """API endpoint untuk memeriksa jawaban soal latihan dari pengguna."""
    data = request.get_json()
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    user_id = session.get('user_id')

    if not all([question_id, user_answer, user_id]):
        return jsonify({'error': 'Data tidak lengkap'}), 400

    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT answer, topic_id FROM questions WHERE id = %s", (question_id,))
        question = cursor.fetchone()

        if not question:
            return jsonify({'error': 'Soal tidak ditemukan'}), 404

        correct_answer_str = question['answer']
        
        # Normalisasi jawaban pengguna
        normalized_user_answer = user_answer.strip().lower().replace(' ', '')
        
        # Logika baru: Bandingkan sebagai set untuk menangani urutan dan jawaban ganda
        # Ini akan menangani kasus seperti "4 atau -4" vs "-4 atau 4"
        correct_parts = {part.strip().lower().replace(' ', '') for part in correct_answer_str.split('atau')}
        user_parts = {part.strip().lower().replace(' ', '') for part in normalized_user_answer.split('atau')}
        
        is_correct = (user_parts == correct_parts)

        # Logika untuk update user_progress
        topic_id = question['topic_id']
        if is_correct:
            # Jika jawaban benar, tambah correct_answers dan questions_answered
            update_query = """
                INSERT INTO user_progress (user_id, topic_id, correct_answers, questions_answered)
                VALUES (%s, %s, 1, 1)
                ON DUPLICATE KEY UPDATE 
                    correct_answers = correct_answers + 1,
                    questions_answered = questions_answered + 1
            """
            cursor.execute(update_query, (user_id, topic_id))
        else:
            # Jika jawaban salah, hanya tambah questions_answered
            update_query = """
                INSERT INTO user_progress (user_id, topic_id, questions_answered)
                VALUES (%s, %s, 1)
                ON DUPLICATE KEY UPDATE 
                    questions_answered = questions_answered + 1
            """
            cursor.execute(update_query, (user_id, topic_id))
        
        conn.commit()

        return jsonify({
            'is_correct': is_correct,
            'correct_answer': correct_answer_str
        })

    except Exception as e:
        logging.error(f"Error submitting answer: {e}")
        if conn: conn.rollback()
        return jsonify({'error': 'Terjadi kesalahan internal'}), 500
    finally:
        if conn: close_db_connection(conn)

def safe_calculate(expression):
    """Mengevaluasi ekspresi matematika dengan aman."""
    expr = expression.replace(',', '.').lower()
    
    # Handle Kombinasi: 10 Kombinasi 2 -> comb(10, 2)
    expr = re.sub(r'(\d+)\s*(?:kombinasi|ncr|c)\s*(\d+)', r'comb(\1, \2)', expr, flags=re.IGNORECASE)
    # Handle Permutasi: 10 Permutasi 2 -> perm(10, 2)
    expr = re.sub(r'(\d+)\s*(?:permutasi|npr|p)\s*(\d+)', r'perm(\1, \2)', expr, flags=re.IGNORECASE)
    
    # Handle Faktorial (5! -> factorial(5))
    expr = re.sub(r'(\d+)\s*!', r'factorial(\1)', expr)
    
    expr = re.sub(r'(\d+)\s*%', r'(\1/100)', expr)
    expr = expr.replace('^', '**')
    expr = expr.replace('mod', '%')

    allowed_names = {
        "sin": lambda d: math.sin(math.radians(d)),
        "cos": lambda d: math.cos(math.radians(d)),
        "tan": lambda d: math.tan(math.radians(d)),
        "log": math.log,
        "log10": math.log10,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "exp": math.exp,
        "pow": pow,
        "factorial": math.factorial,
        "abs": abs,
        "comb": math.comb,
        "perm": math.perm
    }
    try:
        code = compile(expr, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Fungsi '{name}' tidak diizinkan.")
        
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return round(result, 10) if isinstance(result, float) else result
    except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
        logging.warning(f"Safe calculate error for '{expression}': {e}")
        return "Error"

@api_bp.route('/calculate', methods=['POST'])
@user_required
def calculate_api():
    """API endpoint untuk kalkulator pintar."""
    data = request.get_json()
    expression = data.get('expression', '')
    
    if 'Ans' in expression:
        last_result = session.get('last_result', 0)
        expression = expression.replace('Ans', str(last_result))

    result = safe_calculate(expression)
    
    if result == "Error":
        return jsonify({'status': 'error', 'result': 'Error Syntax'})
    
    session['last_result'] = result
    return jsonify({'status': 'success', 'result': str(result)})

from Back_End.bug_and_crime_detection.bug_and_crime_detection import SECURITY_LOG_PATH
from Back_End.routes.security_for_web import admin_required
import os
import json

@api_bp.route('/security/logs', methods=['GET'])
@admin_required
def get_security_logs():
    """Return recent security logs from JSON for admin dashboard."""
    if not os.path.exists(SECURITY_LOG_PATH):
        return jsonify([])
    
    try:
        with open(SECURITY_LOG_PATH, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        if not isinstance(logs, list):
            logs = []
        # Return recent 50, reversed (newest first) to match JS .reverse()
        return jsonify(logs[-50:][::-1])
    except (json.JSONDecodeError, OSError):
        return jsonify([])
