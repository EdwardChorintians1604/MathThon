from flask import Blueprint, render_template, request, jsonify, current_app, flash, redirect, url_for
from Back_End.routes.security_for_web import user_required
from Back_End.routes.utils import get_user_data_for_template
from Back_End.db.database_mysql import get_db_connection, close_db_connection

latihan_bp = Blueprint('latihan', __name__)

@latihan_bp.route("/<int:topic_id>")
@user_required
def latihan_topic(topic_id):
    user_data = get_user_data_for_template(current_app._get_current_object())
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM topics WHERE id = %s", (topic_id,))
        topic = cursor.fetchone()
        if not topic:
            flash("Topik tidak ditemukan.", "warning")
            return redirect(url_for('user.latihan'))
        
        from flask import session
        from Back_End.routes.utils import log_user_activity
        log_user_activity(current_app._get_current_object(), session.get('user_id'), 'latihan', f"Mulai latihan soal pada topik: {topic['name']}")
        
        cursor.execute("SELECT id, content, difficulty FROM questions WHERE topic_id = %s ORDER BY RAND() LIMIT 10", (topic_id,))
        questions = cursor.fetchall()
        return render_template("user/latihan_session.html", topic=topic, questions=questions, **user_data)
    finally:
        if conn:
            close_db_connection(conn)
