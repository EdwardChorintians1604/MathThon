# e:\MathThon\Back_End\routes\auth.py
import os
import uuid
import logging
import traceback
import secrets
import re
from datetime import datetime

import bleach
import mysql.connector
from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, session, jsonify, current_app, abort
)
from werkzeug.security import check_password_hash, generate_password_hash
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

# Database & Security
from Back_End.db.database_mysql import get_db_connection, close_db_connection, execute_insert, execute_query
from Back_End.routes.security_for_web import user_required
from Back_End.bug_and_crime_detection.bug_and_crime_detection import limiter, SQLI_PATTERNS, log_incident

# Create a Blueprint
auth_bp = Blueprint('auth', __name__, template_folder='../../Front_End/templates')

@auth_bp.route("/register_user", methods=["GET"])
def register_user():
    """Tampilkan form pendaftaran akun pengguna baru."""
    return render_template("user/register_user.html")

@auth_bp.route("/register_user", methods=["POST"])
@limiter.limit("5 per minute")
def submit_register_user():
    """
    Pendaftaran Pengguna Baru:
    - Pre-filter anti-SQLi dan sanitasi input via bleach.
    - Mencegah impersonasi identitas administrator.
    - Query insert berparameter murni (%s) ke MySQL.
    """
    raw_name = request.form.get("name", "")
    raw_born_place = request.form.get("born_place", "")
    raw_username = request.form.get("username", "")
    raw_born_date = request.form.get("born_date", "")
    raw_email = request.form.get("email", "")
    password = request.form.get("password", "")
    photo = request.files.get("foto")

    # 1. Anti-SQL Injection & Sanitasi
    combined_inputs = f"{raw_name} {raw_born_place} {raw_username} {raw_email}"
    for pattern in SQLI_PATTERNS:
        if re.search(pattern, combined_inputs):
            log_incident("SQL Injection on Registration", "CRITICAL", f"Pola SQLi pada form register dari IP {request.remote_addr}: {bleach.clean(raw_username)[:40]}")
            flash("Karakter atau format input terlarang terdeteksi demi keamanan database.", "danger")
            return redirect(url_for('auth.register_user'))

    name = bleach.clean(raw_name).strip()
    born_place = bleach.clean(raw_born_place).strip() if raw_born_place else None
    username = bleach.clean(raw_username).strip()
    email = bleach.clean(raw_email).strip().lower()

    born_date = None
    if raw_born_date and raw_born_date.strip():
        try:
            born_date = datetime.strptime(raw_born_date.strip(), '%Y-%m-%d').date()
        except ValueError:
            logging.warning(f"Format tanggal lahir tidak valid: {raw_born_date}")
            born_date = None

    # Validasi field wajib
    if not all([name, username, email, password]):
        flash("Semua field yang bertanda * wajib diisi.", "danger")
        return redirect(url_for('auth.register_user'))

    if len(password) < 6:
        flash("Kata sandi minimal 6 karakter demi keamanan akun.", "danger")
        return redirect(url_for('auth.register_user'))

    # Proteksi nama akun Otoritas
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'Edward_Kenway')
    if username.lower() == ADMIN_USERNAME.lower() or 'admin' in username.lower():
        flash("Username tersebut dicadangkan untuk otoritas sistem dan tidak dapat digunakan.", "danger")
        return redirect(url_for('auth.register_user'))

    # Hash kata sandi pengguna
    hashed_password = generate_password_hash(password)

    # Penanganan file foto
    foto_data = "uploads/default.jpg"
    try:
        if photo and photo.filename.strip() != "":
            from Back_End.bug_and_crime_detection.bug_and_crime_detection import validate_file_safety
            if not validate_file_safety(photo):
                flash("File foto tidak memenuhi kriteria keamanan sistem.", "danger")
                return redirect(url_for('auth.register_user'))

            file_extension = os.path.splitext(photo.filename)[1].lower()
            unique_filename = str(uuid.uuid4()) + file_extension
            upload_dir = os.path.join(current_app.static_folder, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            foto_path = os.path.join(upload_dir, unique_filename)
            photo.save(foto_path)
            foto_data = f'uploads/{unique_filename}'
    except Exception as e:
        logging.error(f"Gagal menyimpan foto: {e}")
        flash("Gagal memproses file foto profil.", "danger")
        return redirect(url_for('auth.register_user'))

    # Simpan ke database via parameterized query
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

        flash("Pendaftaran akun berhasil! Silakan masuk ke Portal Terpadu.", "success")
        return redirect(url_for('auth.login_user'))

    except mysql.connector.Error as err:
        if err.errno == 1062:
            error_message = "Username atau Email sudah terdaftar. Silakan gunakan yang lain."
        else:
            error_message = f"Registrasi gagal karena kendala database: {err.msg}"

        logging.error(f"Registration database error: {err}")
        flash(error_message, "danger")
        return redirect(url_for('auth.register_user'))

    except Exception as e:
        logging.error(f"General error during registration: {e}")
        flash("Pendaftaran gagal karena kendala tak terduga.", "danger")
        return redirect(url_for('auth.register_user'))

    finally:
        if conn:
            conn.close()


@auth_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def login_user():
    """
    Portal Masuk Terpadu MathThon (Integrated Role-Aware Login Engine):
    - Otomatis mendeteksi role akun: Administrator atau Pengguna Biasa (Siswa/Umum).
    - Memisahkan kredensial admin dan user secara cerdas dan aman dari timing attack.
    - Parameterized MySQL query 100% immune terhadap SQL Injection.
    - Anti-bot Honeypot trap & submission timestamp heuristics.
    - Flask-Limiter proteksi anti-brute force per IP address.
    """
    # Jika sesi sudah aktif, langsung arahkan ke dashboard yang sesuai
    if session.get('admin_logged_in'):
        return redirect(url_for('admin.dashboard_admin'))
    if session.get('user_id'):
        return redirect(url_for('user.dashboard_user'))

    if request.method == "POST":
        identifier = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        honeypot = request.form.get("website_url_hp", "").strip()

        # 1. Anti-Bot Honeypot Trap
        if honeypot:
            log_incident("Bot Attack (Honeypot)", "CRITICAL", f"Bot terperangkap mengisi field honeypot dari IP {request.remote_addr}")
            flash("Akses diblokir: Terdeteksi bot otomatis.", "danger")
            return render_template("user/login_user.html"), 403

        # 2. Validasi input wajib
        if not identifier or not password:
            flash("Username/Email dan password wajib diisi.", "danger")
            return render_template("user/login_user.html")

        # 3. Pre-Filter Anti-SQL Injection & Signature Scanning
        raw_combined = f"{identifier} {password}"
        is_sqli = False
        for pattern in SQLI_PATTERNS:
            if re.search(pattern, raw_combined):
                is_sqli = True
                break

        if is_sqli:
            sanitized_id = bleach.clean(identifier)[:60]
            log_incident(
                attack_type="SQL Injection Attempt on Login",
                severity="CRITICAL",
                details=f"Pola SQLi terdeteksi pada login dari IP {request.remote_addr}: {sanitized_id}"
            )
            flash("Akses ditolak: Aktivitas mencurigakan terdeteksi oleh sistem keamanan MathThon.", "danger")
            return render_template("user/login_user.html"), 403

        # 4. RESOLUSI IDENTITAS (ALGORITMA DETEKSI ROLE)
        # -------------------------------------------------------------
        # Tahap A: Deteksi Apakah Kredensial Administrator
        ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'Edward_Kenway')
        ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Mentawai160604')

        # Bandingkan kredensial secara konstan (aman dari side-channel timing attack)
        is_admin_identifier = secrets.compare_digest(identifier, ADMIN_USERNAME)
        is_admin_password = secrets.compare_digest(password, ADMIN_PASSWORD)

        if is_admin_identifier:
            if is_admin_password:
                # Berhasil otentikasi sebagai Administrator
                session.clear()
                session.permanent = True
                session['admin_logged_in'] = True
                session['username'] = ADMIN_USERNAME
                session['role'] = 'admin'
                session['name'] = 'Administrator'

                log_incident(
                    attack_type="Admin Authentication",
                    severity="INFO",
                    details=f"Admin '{ADMIN_USERNAME}' berhasil masuk melalui Portal Terpadu dari IP {request.remote_addr}"
                )
                logging.info(f"[SECURITY] Administrator login successful: {ADMIN_USERNAME} (IP: {request.remote_addr})")
                flash(f"Login berhasil! Selamat datang di Portal Administrator, {ADMIN_USERNAME}.", "success")
                return redirect(url_for('admin.dashboard_admin'))
            else:
                # Identifier admin cocok tapi password salah
                log_incident(
                    attack_type="Failed Admin Login",
                    severity="HIGH",
                    details=f"Gagal login akun admin '{ADMIN_USERNAME}' dari IP {request.remote_addr}"
                )
                logging.warning(f"[SECURITY] Percobaan login admin gagal untuk '{ADMIN_USERNAME}' dari IP {request.remote_addr}")
                flash("Username/Email atau kata sandi tidak valid.", "danger")
                return render_template("user/login_user.html")

        # -------------------------------------------------------------
        # Tahap B: Deteksi Akun Pengguna Terdaftar di Database MySQL
        conn = None
        try:
            conn = get_db_connection(current_app)
            cursor = conn.cursor(dictionary=True)
            # Parameterized Query murni: memisahkan SQL query dari parameter input pengguna (kebal SQLi)
            cursor.execute(
                "SELECT id, name, username, email, password, photo FROM users WHERE username = %s OR email = %s",
                (identifier, identifier.lower())
            )
            user = cursor.fetchone()
            cursor.close()

            if user and check_password_hash(user['password'], password):
                # Berhasil otentikasi sebagai Pengguna (User)
                session.clear()
                session.permanent = True
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['name'] = user.get('name') or user['username']
                session['photo'] = user.get('photo') or 'uploads/default.jpg'
                session['role'] = 'user'
                session['admin_logged_in'] = False

                from Back_End.routes.utils import log_user_activity
                try:
                    log_user_activity(
                        current_app._get_current_object(),
                        user['id'],
                        'login',
                        'Berhasil masuk ke dalam platform MathThon melalui Portal Terpadu'
                    )
                except Exception as log_err:
                    logging.warning(f"Gagal mencatat log aktivitas login user: {log_err}")

                logging.info(f"[SECURITY] User login successful: {user['username']} (ID: {user['id']})")
                flash(f"Login berhasil! Selamat datang kembali, {user.get('name') or user['username']}.", "success")
                return redirect(url_for('user.dashboard_user'))

        except mysql.connector.Error as err:
            logging.error(f"[SECURITY] Database query error saat autentikasi login: {err}")
            flash("Terjadi kendala pada server database. Silakan coba kembali nanti.", "danger")
            return render_template("user/login_user.html")
        finally:
            if conn:
                close_db_connection(conn)

        # -------------------------------------------------------------
        # Tahap C: Kredensial Tidak Ditemukan / Tidak Valid
        logging.warning(f"[SECURITY] Login gagal untuk identitas '{bleach.clean(identifier)[:30]}' dari IP {request.remote_addr}")
        flash("Username/Email atau kata sandi tidak valid.", "danger")
        return render_template("user/login_user.html")

    # Untuk GET request
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
