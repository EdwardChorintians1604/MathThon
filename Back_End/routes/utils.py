import math
import re
import json
import logging
from flask import session, g, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.routes.security_for_web import login_required, admin_required, user_required
from email.message import EmailMessage
import smtplib
import uuid
import os
from Back_End.config import Config

def send_email(app, subject, sender, recipient, body):
    """Send email using SMTP config."""
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        msg.set_content(body)

        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.send_message(msg)
        
        logging.info(f"Email sent to {recipient}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {recipient}: {e}")
        return False

def safe_calculate(app, expression):
    """Safe math expression evaluator (extracted from __init__.py)."""
    # Normalisasi & whitelist logic (full from original)
    expr = expression.replace(',', '.')
    expr = re.sub(r'\s+tambah\s+', ' + ', expr, flags=re.IGNORECASE)
    # ... (all regex replacements for Indonesian math terms)
    expr = re.sub(r'\s+mod\s+', ' % ', expr, flags=re.IGNORECASE)
    expr = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expr)
    expr = re.sub(r'akar\s+(\d+(\.\d+)?)', r'sqrt(\1)', expr, flags=re.IGNORECASE)
    # Fix kombinasi/permutasi: n Kombinasi/Permutasi r -> comb(n,r)/perm(n,r)\n    def replace_comb_perm(match):\n        n_str, r_str = match.groups()\n        try:\n            n, r = int(float(n_str)), int(float(r_str))\n            if 0 <= r <= n:\n                return f'comb({n},{r})' if 'kombinasi' in match.group(0).lower() or 'ncr' in match.group(0).lower() else f'perm({n},{r})'\n        except ValueError:\n            pass\n        return ''\n    \n    expr = re.sub(r'(\\d+(?:\\.\\d+)?)\\s*(kombinasi|nCr|permutasi|nPr)\\s*(\\d+(?:\\.\\d+)?)', replace_comb_perm, expr, flags=re.IGNORECASE)
    expr = expr.replace('^', '**')
    
    allowed_names = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "log": math.log, "log10": math.log10, "sqrt": math.sqrt,
        "pi": math.pi, "e": math.e, "exp": math.exp,
        "comb": math.comb, "perm": math.perm, "factorial": math.factorial,
        "abs": abs, "round": round
    }
    
    try:
        code = compile(expr, "<string>", "eval")
        result = eval(code, {"__builtins__": {}}, allowed_names)
        if isinstance(result, float):
            if result.is_integer():
                return int(result)
            return round(result, 10)
        session['last_answer'] = result
        return result
    except:
        return "Error"

def get_user_data_for_template(app):
    """Extracted helper for user data in templates."""
    from flask import url_for
    if 'user_id' not in session:
        return {"user": None, "users": None, "photo_url": url_for('static', filename='uploads/default.jpg')}
    
    conn = None
    try:
        user_id = session['user_id']
        conn = get_db_connection(app)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, username, photo, email, born_place, born_date FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        photo_url = url_for('static', filename=user.get('photo') or 'uploads/default.jpg') if user else url_for('static', filename='uploads/default.jpg')
        return {"user": user, "users": user, "photo_url": photo_url}
    except Exception as e:
        logging.error(f"get_user_data error: {e}")
        return {"user": None, "users": None, "photo_url": url_for('static', filename='uploads/default.jpg')}
    finally:
        if conn:
            close_db_connection(conn)

# Additional utils: secure_upload_path, etc.
def secure_upload_path(filename):
    return os.path.join(Config.UPLOAD_FOLDER, secure_filename(filename))

def ensure_upload_dir(app):
    os.makedirs(os.path.join(app.static_folder, 'uploads'), exist_ok=True)


def log_user_activity(app, user_id, activity_type, description):
    """Logs a user activity to the user_activities database table."""
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor()
        query = "INSERT INTO user_activities (user_id, activity_type, description) VALUES (%s, %s, %s)"
        cursor.execute(query, (user_id, activity_type, description))
        conn.commit()
    except Exception as e:
        logging.error(f"Error logging user activity: {e}")
    finally:
        if conn:
            cursor.close()
            close_db_connection(conn)


def get_recent_activities(app, user_id, limit=5):
    """Fetches and formats the recent user activities for display on the dashboard."""
    from datetime import datetime
    conn = None
    activities = []
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT activity_type, description, created_at 
            FROM user_activities 
            WHERE user_id = %s 
            ORDER BY created_at DESC 
            LIMIT %s
        """
        cursor.execute(query, (user_id, limit))
        rows = cursor.fetchall()
        
        # Mappings
        type_mappings = {
            'materi': {
                'title': 'Mempelajari Materi',
                'bg_class': 'bg-primary',
                'icon': 'fas fa-book'
            },
            'latihan': {
                'title': 'Mengerjakan Latihan Soal',
                'bg_class': 'bg-success',
                'icon': 'fas fa-pencil-alt'
            },
            'ai_chat': {
                'title': 'Diskusi dengan AI Tutor',
                'bg_class': 'bg-info',
                'icon': 'fas fa-robot'
            },
            'calculator': {
                'title': 'Menggunakan Kalkulator',
                'bg_class': 'bg-warning',
                'icon': 'fas fa-calculator'
            },
            'login': {
                'title': 'Masuk ke Sistem',
                'bg_class': 'bg-success',
                'icon': 'fas fa-sign-in-alt'
            },
            'pengaturan': {
                'title': 'Memperbarui Profil',
                'bg_class': 'bg-secondary',
                'icon': 'fas fa-user-cog'
            },
            'feedback': {
                'title': 'Mengirim Feedback',
                'bg_class': 'bg-danger',
                'icon': 'fas fa-comment'
            }
        }
        
        for row in rows:
            act_type = row['activity_type']
            mapping = type_mappings.get(act_type, {
                'title': 'Aktivitas Pengguna',
                'bg_class': 'bg-primary',
                'icon': 'fas fa-check'
            })
            
            # calculate time ago
            dt = row['created_at']
            now = datetime.now()
            diff = now - dt
            seconds = diff.total_seconds()
            
            if seconds < 0:
                seconds = 0
            
            if seconds < 60:
                time_ago = "Baru saja"
            elif seconds < 3600:
                time_ago = f"{int(seconds // 60)} menit yang lalu"
            elif seconds < 86400:
                time_ago = f"{int(seconds // 3600)} jam yang lalu"
            else:
                time_ago = f"{int(seconds // 86400)} hari yang lalu"
                
            activities.append({
                'title': mapping['title'],
                'description': row['description'],
                'bg_class': mapping['bg_class'],
                'icon': mapping['icon'],
                'time_ago': time_ago
            })
    except Exception as e:
        logging.error(f"Error fetching user activities: {e}")
    finally:
        if conn:
            cursor.close()
            close_db_connection(conn)
            
    return activities

