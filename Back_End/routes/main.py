from flask import Blueprint, render_template, jsonify, Response, send_from_directory, request, flash, redirect, url_for, session, current_app, abort
from Back_End.routes.utils import get_user_data_for_template, send_email
from werkzeug.utils import secure_filename
from Back_End.models import init_db_schema
from Back_End.jumlah_user.jumlah_user import get_user_statistics
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.config import Config
import pandas as pd
import io
import os
import re
import logging

main_bp = Blueprint('main', __name__, template_folder='../../Front_End/templates', static_folder='../../Front_End/static')

@main_bp.route("/", methods=["GET", "POST"])
def home():
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        
        # Testimonials from recent AI chats
        query_feedback = """
            SELECT u.name AS user_name, cm.content AS comment
            FROM chat_messages cm JOIN conversations c ON cm.conversation_id = c.id
            JOIN users u ON c.user_id = u.id
            WHERE cm.role = 'user' AND cm.content IS NOT NULL AND cm.content != ''
            ORDER BY cm.created_at DESC LIMIT 6
        """
        cursor.execute(query_feedback)
        feedbacks = cursor.fetchall()
        
        stats = get_user_statistics(current_app._get_current_object())
        
        return render_template("home.html", 
                             feedbacks=feedbacks, 
                             user_count=stats.get('user_count', 0), 
                             chat_count=stats.get('chat_count', 0))
    except Exception as err:
        logging.error(f"Home page error: {err}")
        try:
            return render_template("home.html", feedbacks=[], user_count=0, chat_count=0, db_error="Error loading data.")
        except Exception as e2:
            return f"Critical Error: {err}. Template Error: {e2}", 500
    finally:
        if conn:
            close_db_connection(conn)


@main_bp.route("/tentang", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@main_bp.route("/privasi_kebijakan", methods=["GET", "POST"])
def privacy():
    return render_template("privacy.html")

@main_bp.route("/syarat_dan_ketentuan", methods=["GET"])
def terms():
    return render_template("terms.html")


@main_bp.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Secure file serving."""
    safe_filename = secure_filename(os.path.basename(filename))
    upload_folder = os.path.join(current_app.static_folder, 'uploads')
    if not os.path.exists(os.path.join(upload_folder, safe_filename)):
        abort(404)
    return send_from_directory(upload_folder, safe_filename)

@main_bp.route('/<path:fontname>.woff2')
@main_bp.route('/<path:fontname>.woff')
@main_bp.route('/<path:fontname>.ttf')
def katex_fonts_fallback(fontname):
    """Handle KaTeX font asset requests without 404 error."""
    full_name = os.path.basename(fontname)
    if 'KaTeX' in full_name or 'katex' in full_name.lower():
        ext = request.path.split('.')[-1]
        # Clean hash suffix if present, e.g., KaTeX_Main-Regular-ARRPAO67 -> KaTeX_Main-Regular
        clean_name = re.sub(r'-[A-Za-z0-9]{6,8}$', '', full_name)
        return redirect(f"https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/fonts/{clean_name}.{ext}")
    abort(404)

@main_bp.route("/submit_testimonial", methods=["POST"])
def submit_testimonial():
    user_name = request.form.get("user_name")
    message = request.form.get("message")
    if user_name and message:
        conn = get_db_connection(current_app._get_current_object())
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO testimonials (user_name, message) VALUES (%s, %s)", (user_name, message))
            conn.commit()
        finally:
            cursor.close()
            close_db_connection(conn)
    return redirect(url_for('main.home'))

# Admin testimonial CRUD (simple)
@main_bp.route("/update_testimonial/<int:testimonial_id>", methods=["POST"])
def update_testimonial(testimonial_id):
    # Admin check via decorator in __init__
    user_name = request.form.get("user_name")
    message = request.form.get("message")
    conn = get_db_connection(current_app._get_current_object())
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE testimonials SET user_name = %s, message = %s WHERE id = %s", 
                      (user_name, message, testimonial_id))
        conn.commit()
    finally:
        cursor.close()
        close_db_connection(conn)
    return redirect(url_for('main.home'))

@main_bp.route("/delete_testimonial/<int:testimonial_id>", methods=["POST"])
def delete_testimonial(testimonial_id):
    conn = get_db_connection(current_app._get_current_object())
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM testimonials WHERE id = %s", (testimonial_id,))
        conn.commit()
    finally:
        cursor.close()
        close_db_connection(conn)
    return redirect(url_for('main.home'))

@main_bp.route("/api/education_data")
def api_education_data():
    csv_path = Config.CSV_PATH
    if not os.path.exists(csv_path):
        return jsonify({"error": "CSV not found"}), 404
    try:
        df = pd.read_csv(csv_path)
        return jsonify(df.to_dict('records'))
    except Exception as e:
        logging.error(f"CSV error: {e}")
        return jsonify({"error": "Processing error"}), 500

@main_bp.route("/chart/education.png")
def chart_education():
    # Extracted chart logic - simplified placeholder
    # Full matplotlib code from original can be added here
    buf = io.BytesIO()
    # ... plot code ...
    buf.seek(0)
    return Response(buf.getvalue(), mimetype='image/png')
