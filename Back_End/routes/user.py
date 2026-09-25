from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify, current_app
from Back_End.routes.utils import get_user_data_for_template, safe_calculate
from Back_End.routes.security_for_web import user_required
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import uuid
import os
import logging
from Back_End.config import Config


user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder='../../Front_End/templates')

@user_bp.route("/dashboard_user", methods=["GET", "POST"])
@user_required
def dashboard_user():
    user_data = get_user_data_for_template(current_app._get_current_object())
    if request.method == "POST":
        # Delete account logic
        password = request.form.get("password")
        user_id = session.get('user_id')
        
        if not password:
            flash("Password diperlukan untuk menghapus akun.", "danger")
            return redirect(url_for('user.dashboard_user'))

        conn = None
        try:
            conn = get_db_connection(current_app._get_current_object())
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT password, photo FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            
            if user:
                # Check password hash
                if user['password'] and check_password_hash(user['password'], password):
                    # Delete photo if it's not the default
                    photo_path = user.get('photo')
                    if photo_path and 'default.jpg' not in photo_path:
                        try:
                            full_path = os.path.join(current_app.static_folder, photo_path)
                            if os.path.exists(full_path):
                                os.remove(full_path)
                        except Exception as e:
                            logging.warning(f"Failed to delete user photo during account deletion: {e}")

                    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                    conn.commit()
                    session.clear()
                    flash("Akun Anda telah berhasil dihapus.", "success")
                    return redirect(url_for('main.home'))
                else:
                    flash("Password salah. Akun tidak dihapus.", "danger")
            else:
                flash("User tidak ditemukan.", "danger")
        except Exception as e:
            logging.error(f"Error deleting account: {e}")
            flash("Terjadi kesalahan sistem saat menghapus akun.", "danger")
        finally:
            if conn:
                close_db_connection(conn)
    
    from Back_End.routes.utils import get_recent_activities
    user_id = session.get('user_id')
    recent_activities = get_recent_activities(current_app._get_current_object(), user_id)
    
    # Calculate actual user stats
    stats = {
        'latihan_selesai': 0,
        'akurasi': 0,
        'streak': 0,
        'latihan_selesai_percentage': 0,
        'akurasi_percentage': 0,
        'streak_percentage': 0
    }
    
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        
        # 1. Total topics where the user has answered questions
        cursor.execute("SELECT COUNT(*) as count FROM user_progress WHERE user_id = %s AND questions_answered > 0", (user_id,))
        row_topics = cursor.fetchone()
        if row_topics:
            stats['latihan_selesai'] = row_topics['count']
            
        # 2. Total correct and answered questions for accuracy
        cursor.execute("SELECT SUM(correct_answers) as correct, SUM(questions_answered) as total FROM user_progress WHERE user_id = %s", (user_id,))
        row_progress = cursor.fetchone()
        if row_progress and row_progress['total'] and row_progress['total'] > 0:
            correct = row_progress['correct'] or 0
            total = row_progress['total']
            stats['akurasi'] = int(round((correct / total) * 100))
        
        # 3. Calculate Streak
        cursor.execute("SELECT DISTINCT DATE(created_at) as act_date FROM user_activities WHERE user_id = %s ORDER BY act_date DESC", (user_id,))
        rows_dates = cursor.fetchall()
        if rows_dates:
            from datetime import date, datetime, timedelta
            parsed_dates = []
            for r in rows_dates:
                val = r['act_date']
                if val:
                    if isinstance(val, date):
                        parsed_dates.append(val)
                    else:
                        try:
                            parsed_dates.append(datetime.strptime(str(val), "%Y-%m-%d").date())
                        except:
                            pass
            if parsed_dates:
                today = date.today()
                yesterday = today - timedelta(days=1)
                if parsed_dates[0] == today or parsed_dates[0] == yesterday:
                    streak = 0
                    current_date = parsed_dates[0]
                    for d in parsed_dates:
                        if d == current_date:
                            streak += 1
                            current_date -= timedelta(days=1)
                        else:
                            break
                    stats['streak'] = streak
                    
        # Map progress bar percentages (capped at 100%)
        stats['latihan_selesai_percentage'] = min(int(round((stats['latihan_selesai'] / 10) * 100)), 100) # Assuming 10 topics target
        stats['akurasi_percentage'] = stats['akurasi']
        stats['streak_percentage'] = min(int(round((stats['streak'] / 7) * 100)), 100) # Assuming 7 days target
        
    except Exception as e:
        logging.error(f"Error fetching user stats: {e}")
    finally:
        if conn:
            close_db_connection(conn)

    return render_template("user/dashboard_user.html", recent_activities=recent_activities, stats=stats, **user_data)

@user_bp.route("/calculator", methods=["GET", "POST"])
@user_required
def calculator():
    user_data = get_user_data_for_template(current_app._get_current_object())
    user_id = session.get('user_id')
    from Back_End.routes.utils import log_user_activity
    solution = None
    problem = ""
    
    if request.method == "POST":
        problem = request.form.get("problem")
        if problem:
            log_user_activity(current_app._get_current_object(), user_id, 'calculator', f"Menghitung ekspresi matematika: {problem}")
            # Menggunakan safe_calculate dari utils
            result = safe_calculate(current_app._get_current_object(), problem)
            if result == "Error":
                 flash("Format soal tidak valid atau tidak dapat dihitung.", "warning")
            else:
                 solution = result
        else:
            flash("Masukkan soal matematika.", "danger")
    else:
        log_user_activity(current_app._get_current_object(), user_id, 'calculator', 'Membuka kalkulator matematika')
            
    return render_template("user/calculator.html", solution=solution, problem=problem, **user_data)

@user_bp.route("/calculate_api", methods=["POST"])
@user_required
def calculate_api():
    data = request.get_json()
    expression = data.get("expression") if data else None
    
    if not expression:
        return jsonify({"status": "error", "message": "No expression provided"})

    result = safe_calculate(current_app._get_current_object(), expression)
    
    if result == "Error":
        return jsonify({"status": "error", "message": "Calculation error"})
    
    return jsonify({"status": "success", "result": result})

@user_bp.route("/progres_user")
@user_required
def progres_user():
    user_data = get_user_data_for_template(current_app._get_current_object())
    return render_template("user/progres_user.html", **user_data)


@user_bp.route("/latihan")
@user_required
def latihan():
    user_data = get_user_data_for_template(current_app._get_current_object())
    user_id = session.get('user_id')
    from Back_End.routes.utils import log_user_activity
    log_user_activity(current_app._get_current_object(), user_id, 'latihan', 'Mengakses halaman daftar latihan soal matematika')
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT t.*, 
                   COALESCE(up.correct_answers, 0) as correct_answers, 
                   COALESCE(up.questions_answered, 0) as questions_answered 
            FROM topics t 
            LEFT JOIN user_progress up ON t.id = up.topic_id AND up.user_id = %s
            ORDER BY t.name ASC
        """
        cursor.execute(query, (user_id,))
        topics = cursor.fetchall()
        return render_template("user/latihan_soal_user.html", topics=topics, **user_data)
    except Exception as e:
        logging.error(f"Error loading latihan soal: {e}")
        flash("Gagal memuat data latihan.", "danger")
        return redirect(url_for('user.dashboard_user'))
    finally:
        if conn:
            close_db_connection(conn)

@user_bp.route("/profile")
@user_required
def profile():
    user_data = get_user_data_for_template(current_app._get_current_object())
    return render_template("user/options.html", **user_data)

@user_bp.route("/ai_feature")
@user_required
def ai_feature():
    user_data = get_user_data_for_template(current_app._get_current_object())
    user_id = session.get('user_id')
    from Back_End.routes.utils import log_user_activity
    log_user_activity(current_app._get_current_object(), user_id, 'ai_chat', 'Membuka AI Tutor Chat untuk berdiskusi matematika')

    # Fetch conversation history for sidebar
    conversations = []
    conn = None
    try:
        user_id = session.get('user_id')
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, title, created_at FROM conversations WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
        conversations = cursor.fetchall()
    except Exception as e:
        logging.error(f"Error fetching conversations for ai_feature: {e}")
    finally:
        if conn:
            close_db_connection(conn)

    return render_template("user/ai_feature_user.html", conversations=conversations, **user_data)

@user_bp.route("/analyze")
@user_required
def analyze():
    user_data = get_user_data_for_template(current_app._get_current_object())
    user_id = session.get('user_id')
    from Back_End.routes.utils import log_user_activity
    log_user_activity(current_app._get_current_object(), user_id, 'materi', 'Mengakses halaman analisis hasil belajar')
    return render_template("user/analyze_user.html", **user_data)

@user_bp.route("/feedback")
@user_required
def feedback():
    user_data = get_user_data_for_template(current_app._get_current_object())
    user_id = session.get('user_id')
    from Back_End.routes.utils import log_user_activity
    log_user_activity(current_app._get_current_object(), user_id, 'feedback', 'Mengakses halaman feedback & saran')
    return render_template("user/feedback_user.html", **user_data)

@user_bp.route("/profile_user", methods=["POST"])
@user_required
def profile_user():
    user_data = get_user_data_for_template(current_app._get_current_object())
    return render_template("user/options.html", **user_data)

@user_bp.route("/update_profile", methods=["POST"])
@user_required
def update_profile():
    user_id = session.get('user_id')
    name = request.form.get("name")
    email = request.form.get("email")
    born_place = request.form.get("born_place")
    # Frontend profile.js mengirim 'date', backend lama pakai 'born_date'
    born_date_str = request.form.get("date") or request.form.get("born_date")

    born_date = None
    if born_date_str:
        try:
            born_date = datetime.strptime(born_date_str, '%Y-%m-%d').date()
        except ValueError:
            pass

    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        
        # Update profil dasar (nama, email, tempat/tgl lahir)
        sql = "UPDATE users SET name=%s, email=%s, born_place=%s, born_date=%s WHERE id=%s"
        params = (name, email, born_place, born_date, user_id)
        
        cursor.execute(sql, params)
        conn.commit()
        
        from Back_End.routes.utils import log_user_activity
        log_user_activity(current_app._get_current_object(), user_id, 'pengaturan', 'Memperbarui informasi profil akun')
        
        return jsonify({"success": True, "message": "Profil berhasil diperbarui."})
    except Exception as e:
        logging.error(f"Profile update error: {e}")
        return jsonify({"success": False, "message": "Gagal memperbarui profil."})
    finally:
        if conn:
            close_db_connection(conn)

@user_bp.route("/upload_profile_photo", methods=["GET", "POST"])
@user_required
def upload_profile_photo():
    """Menangani upload foto profil via Fetch API / Status (GET/POST)"""
    if request.method == "GET":
        return jsonify({
            'status': 'ready', 
            'accepts': 'POST',
            'message': 'Use POST with FormData(file) for upload'
        })

    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'Tidak ada file yang diunggah'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'Nama file kosong'}), 400

    user_id = session.get('user_id')
    
    conn = None
    try:
        filename = secure_filename(file.filename)
        file_ext = os.path.splitext(filename)[1]
        unique_name = str(uuid.uuid4()) + file_ext
            
        upload_dir = os.path.join(current_app.static_folder, 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
                
        file_path = os.path.join(upload_dir, unique_name)
        file.save(file_path)
        
        db_path = f"uploads/{unique_name}"
        
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET photo = %s WHERE id = %s", (db_path, user_id))
        conn.commit()
        
        return jsonify({
            'success': True, 
            'message': 'Foto berhasil diubah',
            'photo_url': url_for('static', filename=db_path)
        })
        
    except Exception as e:
        logging.error(f"Error uploading photo: {e}")
        return jsonify({'success': False, 'message': 'Gagal mengunggah foto'}), 500
    finally:
        if conn:
            close_db_connection(conn)

@user_bp.route("/delete_account", methods=["POST"])
@user_required
def delete_account():
    """Menghapus akun pengguna (API Endpoint)"""
    user_id = session.get('user_id')
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        session.clear()
        return jsonify({'success': True, 'message': 'Akun berhasil dihapus'})
    except Exception as e:
        logging.error(f"Error deleting account: {e}")
        return jsonify({'success': False, 'message': 'Gagal menghapus akun'}), 500
    finally:
        if conn:
            close_db_connection(conn)

@user_bp.route("/change_password", methods=["POST"])
@user_required
def change_password():
    """Mengganti password pengguna, menerima data JSON."""
    user_id = session.get('user_id')
    data = request.get_json()

    if not data:
        return jsonify({'success': False, 'message': 'Request body tidak valid (bukan JSON).'}), 400

    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if not old_password or not new_password:
        return jsonify({'success': False, 'message': 'Password lama dan baru wajib diisi.'}), 400
        
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT password FROM users WHERE id=%s", (user_id,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password'], old_password):
            new_hash = generate_password_hash(new_password)
            cursor.execute("UPDATE users SET password=%s WHERE id=%s", (new_hash, user_id))
            conn.commit()
            return jsonify({"success": True, "message": "Password berhasil diubah."})
        else:
            return jsonify({"success": False, "message": "Password lama salah."}), 400
    except Exception as e:
        logging.error(f"Password change error: {e}")
        return jsonify({"success": False, "message": "Terjadi kesalahan server."})
    finally:
        if conn:
            close_db_connection(conn)

@user_bp.route("/log_activity", methods=["POST"])
@user_required
def log_activity():
    """Endpoint untuk mencatat aktivitas pengguna secara dinamis dari frontend."""
    user_id = session.get('user_id')
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'Request body tidak valid'}), 400
    
    activity_type = data.get('activity_type')
    description = data.get('description')
    
    if not activity_type or not description:
        return jsonify({'success': False, 'message': 'activity_type dan description diperlukan'}), 400
        
    from Back_End.routes.utils import log_user_activity
    try:
        log_user_activity(current_app._get_current_object(), user_id, activity_type, description)
        return jsonify({'success': True})
    except Exception as e:
        logging.error(f"Error logging dynamic user activity: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500
