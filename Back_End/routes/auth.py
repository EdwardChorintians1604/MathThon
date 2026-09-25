 # e:\MathThon\Back_End\blueprints\auth.py
import os
import uuid
import logging
import traceback
from datetime import datetime

import mysql.connector
from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, session, jsonify, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

# Adjust imports to be relative from the blueprint's location
from Back_End.db.database_mysql import get_db_connection, close_db_connection, execute_insert, execute_query
from Back_End.routes.security_for_web import user_required

# Create a Blueprint
# The 'user' prefix will be handled by url_prefix
auth_bp = Blueprint('auth', __name__, template_folder='../../Front_End/templates')

@auth_bp.route("/register_user", methods=["GET"])
def register_user():
# Tampilkan form registrasi
    return render_template("user/register_user.html")

@auth_bp.route("/register_user", methods=["POST"])
def submit_register_user():
    # Ambil data dari form
    name = request.form.get("name")
    born_place = request.form.get("born_place")
    username = request.form.get("username")
    born_date = request.form.get("born_date")
    if born_date == "":
        born_date = None
    else:
        try:
            # Coba parse tanggal ke format YYYY-MM-DD
            born_date = datetime.strptime(born_date, '%Y-%m-%d').date()
        except ValueError:
            logging.warning(f"Invalid date format for born_date: {born_date}. Setting to None.")
            born_date = None
    
    email = request.form.get("email")
    password = request.form.get("password")
    photo = request.files.get("foto") # Pastikan form pakai name="foto"

    # --- Validasi input wajib ---
    if not all([name, username, email, password]):
        flash("Semua field yang bertanda * wajib diisi.", "danger")
        return redirect(url_for('auth.register_user'))

    # --- Hash password ---
    hashed_password = generate_password_hash(password)

    # --- Penanganan Foto ---
    foto_data = "uploads/default.jpg"  # Default photo path

    try:
        if photo and photo.filename.strip() != "":
            # Gunakan UUID untuk nama file unik
            file_extension = os.path.splitext(photo.filename)[1]
            unique_filename = str(uuid.uuid4()) + file_extension
            # Use current_app.static_folder for consistency
            upload_dir = os.path.join(current_app.static_folder, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            foto_path = os.path.join(upload_dir, unique_filename)
            photo.save(foto_path)
            foto_data = f'uploads/{unique_filename}'
    except Exception as e:
        logging.error(f"Gagal menyimpan foto: {e}")
        flash("Gagal menyimpan foto.", "danger")
        return redirect(url_for('auth.register_user'))

    # --- Simpan ke database ---
    conn = None
    try:
        conn = get_db_connection(current_app)
        query = """
            INSERT INTO users (name, born_place, username, born_date, email, password, photo, google_sub)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NULL)
        """
        params = (name, born_place, username, born_date, email, hashed_password, foto_data)
        execute_insert(conn, query, params)
        conn.commit()

        flash("Registrasi berhasil! Silakan login.", "success")
        return redirect(url_for('auth.login_user'))

    except mysql.connector.Error as err:
        if err.errno == 1062:
            error_message = "Username atau Email sudah terdaftar."
        else:
            error_message = f"Registrasi gagal karena kesalahan database: {err.msg}"

        logging.error(f"Registration error: {err}")
        flash(error_message, "danger")
        return redirect(url_for('auth.register_user'))

    except Exception as e:
        logging.error(f"General error during registration: {e}")
        flash("Registrasi gagal karena kesalahan tak terduga.", "danger")
        return redirect(url_for('auth.register_user'))

    finally:
        if conn:
            conn.close()

@auth_bp.route("/login_user", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username dan password wajib diisi.", "danger")
            return render_template("user/login_user.html")

        conn = None
        try:
            conn = get_db_connection(current_app)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, username, password FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            cursor.close()

            if user and check_password_hash(user['password'], password):
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username']
                
                from Back_End.routes.utils import log_user_activity
                log_user_activity(current_app._get_current_object(), user['id'], 'login', 'Berhasil masuk ke dalam platform MathThon')
                
                flash("Login berhasil!", "success")
                return redirect(url_for('user.dashboard_user'))
            else:
                flash("Username atau password salah.", "danger")
                return render_template("user/login_user.html")

        except mysql.connector.Error as err:
            logging.error(f"Login error: {err}")
            flash("Terjadi kesalahan pada server. Coba lagi nanti.", "danger")
            return render_template("user/login_user.html")
        finally:
            if conn:
                close_db_connection(conn)

    # For GET request
    return render_template("user/login_user.html")

@auth_bp.route("/google_login", methods=["POST"])
def google_login():
    from google.auth.exceptions import InvalidValue
    from requests.exceptions import ConnectionError as RequestsConnectionError
    
    client_id = current_app.config.get('GOOGLE_CLIENT_ID')
    if not client_id:
        logging.error("GOOGLE_CLIENT_ID tidak diatur di server.")
        return jsonify({"error": "Konfigurasi server tidak lengkap."}), 500
    try:
        data = request.get_json(force=True, silent=False)
    except Exception:
        return jsonify({"error": "Data request tidak valid (bukan JSON)."}), 400
    if not data:
        return jsonify({"error": "Token tidak ditemukan."}), 400
    token = data.get('token')
    if not token:
        return jsonify({"error": "Token tidak ditemukan."}), 400

    conn = None
    cursor = None
    try:
        try:
            idinfo = id_token.verify_oauth2_token(
                token, google_requests.Request(), client_id, clock_skew_in_seconds=10
            )
        except InvalidValue as e:
            logging.error(f"Google token verification failed (InvalidValue): {e}")
            return jsonify({"error": "Verifikasi gagal. Token tidak valid."}), 401
        except RequestsConnectionError as e:
            logging.error(f"Google token verification failed (ConnectionError): {e}")
            return jsonify({"error": "Gagal terhubung ke server Google."}), 503
        except ValueError as e:
            logging.error(f"Google token verification failed (ValueError): {e}")
            return jsonify({"error": "Token kedaluwarsa atau tidak valid."}), 401
        except Exception as e:
            logging.error(f"Google token verification error: {type(e).__name__}: {e}")
            return jsonify({"error": "Terjadi kesalahan saat verifikasi token."}), 500

        google_sub = idinfo.get('sub')
        user_email = idinfo.get('email')
        user_name = idinfo.get('name') or (user_email or '')
        if not google_sub:
            logging.error("Google token tidak berisi 'sub'.")
            return jsonify({"error": "Data dari Google tidak lengkap (sub)."}), 400
        if not user_email:
            logging.error("Google token tidak berisi 'email'. Pastikan scope email diaktifkan di Google Cloud Console.")
            return jsonify({"error": "Akses email dari Google diperlukan. Silakan gunakan akun yang mengizinkan email."}), 400

        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id, username FROM users WHERE google_sub = %s", (google_sub,))
        user = cursor.fetchone()

        if user:
            user_id = user['id']
            session_username = user['username']
            logging.info(f"Existing Google user logged in: {session_username}")
        else:
            cursor.execute("SELECT id, username FROM users WHERE email = %s", (user_email,))
            existing_user = cursor.fetchone()

            if existing_user:
                user_id = existing_user['id']
                session_username = existing_user['username']
                update_query = "UPDATE users SET google_sub = %s WHERE id = %s"
                cursor.execute(update_query, (google_sub, user_id))
                conn.commit()
                logging.info(f"Google sub linked to existing user: {session_username}")
            else:
                username_base = user_email.split('@')[0]
                username = username_base
                counter = 1
                while True:
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    if not cursor.fetchone():
                        break
                    username = f"{username_base}_{counter}"
                    counter += 1
                
                hashed_password = generate_password_hash(str(uuid.uuid4()))
                default_photo = 'uploads/default.jpg'

                insert_query = """
                    INSERT INTO users (name, username, email, password, photo, google_sub)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                params = (user_name, username, user_email, hashed_password, default_photo, google_sub)
                cursor.execute(insert_query, params)
                conn.commit()
                user_id = cursor.lastrowid
                session_username = username
                logging.info(f"New user registered from Google login: {username}")

        session.clear()
        session['user_id'] = user_id
        session['username'] = session_username
        
        from Back_End.routes.utils import log_user_activity
        log_user_activity(current_app._get_current_object(), user_id, 'login', 'Berhasil masuk ke platform MathThon via Google')
        
        return jsonify({
            "success": True,
            "redirect": url_for('user.dashboard_user')
        }), 200

    except mysql.connector.Error as err:
        logging.error(f"Database error during Google auth: {err}")
        return jsonify({"error": "Kesalahan database saat otentikasi Google."}), 500
    except Exception as e:
        logging.error(f"General error during Google auth: {type(e).__name__}: {e}\n{traceback.format_exc()}")
        return jsonify({"error": "Terjadi kesalahan tak terduga saat proses otentikasi Google."}), 500
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass
        if conn:
            close_db_connection(conn) 

@auth_bp.route("/logout_user")
@user_required
def logout_user():
    """Membersihkan sesi pengguna dan mengarahkan ke halaman login."""  
    session.clear()
    flash("Anda telah berhasil logout.", "success")
    return redirect(url_for("auth.login_user"))

@auth_bp.route("/forget_password_user", methods=["GET", "POST"])
def forget_password_user():
    if request.method == "POST":
        step = request.form.get("step", "1")
        
        if step == "1":
            email = request.form.get("email", "").strip()
            if not email:
                flash("❌ Email wajib diisi.", "danger")
                return render_template("user/forget_password_user.html", step=1)

            conn = None
            try:
                conn = get_db_connection(current_app)
                cursor = conn.cursor(dictionary=True)

                cursor.execute("SELECT id, username FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()

                if user:
                    flash(f"✅ Email terverifikasi! Silakan buat password baru.", "success")
                    return render_template("user/forget_password_user.html", step=2, email=email)
                else:
                    flash("❌ Email tidak terdaftar di sistem. Silakan periksa kembali atau buat akun baru.", "danger")
                    return render_template("user/forget_password_user.html", step=1)

            except mysql.connector.Error as err:
                logging.error(f"Database error saat verifikasi email: {err}")
                flash(f"❌ Error Database: {str(err)[:50]}", "danger")
                return render_template("user/forget_password_user.html", step=1)
            except Exception as e:
                logging.error(f"Unexpected error step 1: {type(e).__name__}: {e}")
                flash(f"❌ Error: {str(e)[:100]}", "danger")
                return render_template("user/forget_password_user.html", step=1)
            finally:
                if conn:
                    close_db_connection(conn)

        elif step == "2":
            email = request.form.get("email", "").strip()
            new_password = request.form.get("new_password", "").strip()
            confirm_password = request.form.get("confirm_password", "").strip()

            if not all([email, new_password, confirm_password]):
                flash("❌ Semua field wajib diisi.", "danger")
                return render_template("user/forget_password_user.html", step=2, email=email)

            if new_password != confirm_password:
                flash("❌ Password tidak cocok!", "danger")
                return render_template("user/forget_password_user.html", step=2, email=email)

            if len(new_password) < 6:
                flash("❌ Password minimal 6 karakter!", "danger")
                return render_template("user/forget_password_user.html", step=2, email=email)

            conn = None
            try:
                conn = get_db_connection(current_app)
                cursor = conn.cursor(dictionary=True)

                cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()

                if not user:
                    flash("❌ Email tidak ditemukan.", "danger")
                    return render_template("user/forget_password_user.html", step=1)

                hashed_password = generate_password_hash(new_password)
                cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user['id']))
                conn.commit()

                flash("✅ Password berhasil direset! Silakan login dengan password baru Anda.", "success")
                return redirect(url_for('auth.login_user'))

            except mysql.connector.Error as err:
                logging.error(f"Database error saat reset password: {err}")
                flash(f"❌ Error Database: {str(err)[:50]}", "danger")
                return render_template("user/forget_password_user.html", step=2, email=email)
            except Exception as e:
                logging.error(f"Unexpected error step 2: {type(e).__name__}: {e}")
                flash(f"❌ Error: {str(e)[:100]}", "danger")
                return render_template("user/forget_password_user.html", step=2, email=email)
            finally:
                if conn:
                    close_db_connection(conn)

    return render_template("user/forget_password_user.html", step=1)
