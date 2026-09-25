from flask import Flask, render_template, g, session, redirect, url_for, request, send_from_directory, jsonify, Response
from dotenv import load_dotenv
import os
import sqlite3
import logging

# Import koneksi database dari modul eksternal
from .db.database import get_db_connection, close_db_connection, execute_query, execute_insert 

# Import fungsi keamanan
from .security_utils import encrypt_data, decrypt_data, generate_key, decrypt_json_data, encrypt_json_data
from matplotlib import pyplot as plt
from werkzeug.security import generate_password_hash, check_password_hash
import io
from flask import Flask, render_template, g, session, redirect, url_for, request, send_from_directory, jsonify, Response
import pandas as pd

# Load environment variables
load_dotenv()

# ==========================================
# SETUP APLIKASI
# ==========================================
def create_app():
    app = Flask(__name__,
        template_folder=os.path.join(os.path.dirname(__file__), "../Front_End/templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "../Front_End/static")
    )

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), 'db', 'database.db')
    # Folder untuk menyimpan file terenkripsi
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # CSV path
    CSV_PATH = os.path.join(os.path.dirname(__file__), 'api', 'education_data', 'IndonesiaEduaction.csv')

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Function to initialize the database
    def init_db():
        with app.app_context():
            conn = get_db_connection(app.config['DATABASE'])
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS testimonials (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);""")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    born_place TEXT,
                    username TEXT NOT NULL UNIQUE,
                    born_date TEXT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    Photo VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            cursor.close()
            close_db_connection(conn)

    init_db()
    # Pastikan kunci enkripsi ada saat aplikasi dimulai
    with app.app_context():
        generate_key()

    # ==========================================
    # DATABASE TEARDOWN
    # ==========================================
    @app.teardown_appcontext
    def teardown_db(exception):
        db = g.pop('db_conn', None)
        if db is not None:
            close_db_connection(db)

    # ==========================================
    # ROUTE: HOME — MENAMPILKAN TESTIMONIAL & GRAFIK
    # ==========================================
    @app.route("/", methods=["GET", "POST"])
    def home():
        conn = get_db_connection(app.config['DATABASE'])
        testimonials = execute_query(conn, "SELECT * FROM testimonials ORDER BY created_at DESC")
        close_db_connection(conn)
        return render_template("home.html", testimonials=testimonials)

    # ==========================================
    # ROUTE: ADMIN & USER
    # ==========================================
    @app.route("/admin")
    def admin():
        return render_template("admin/index.html")

    @app.route("/admin/login_admin", methods=["GET", "POST"])
    def login_admin():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'Erantus')
            ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Mentawai123')

            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                session['admin_logged_in'] = True
                return redirect(url_for('dashboard_admin'))
            else:
                return render_template("admin/login_admin.html", error="Username atau password salah.")
        
        return render_template("admin/login_admin.html")
    
    @app.route("/admin/logout")
    def logout_admin():
        session.pop('admin_logged_in', None)
        return redirect(url_for('login_admin'))

    @app.route("/admin/dashboard")
    def dashboard_admin():
        if 'admin_logged_in' not in session:
            return redirect(url_for('login_admin'))
        return render_template("admin/dashboard.html")

    # ==========================================
    # ROUTE: EKSPOR DATABASE (HANYA ADMIN)
    # ==========================================
    @app.route("/admin/export_database")
    def export_database():
        # Pastikan hanya admin yang bisa mengakses
        if 'admin_logged_in' not in session:
            return redirect(url_for('login_admin'))
        
        try:
            conn = get_db_connection(app.config['DATABASE'])
            # Gunakan .dump() untuk mendapatkan SQL dump
            sql_dump = "\n".join(conn.iterdump())
            close_db_connection(conn)

            # Simpan dump ke file sementara
            dump_filename = "database_dump.sql"
            dump_filepath = os.path.join(app.config['UPLOAD_FOLDER'], dump_filename)
            with open(dump_filepath, 'w', encoding='utf-8') as f:
                f.write(sql_dump)
            
            return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=dump_filename, as_attachment=True)
        except Exception as e:
            logging.error(f"Gagal mengekspor database: {e}")
            return "Terjadi kesalahan saat mencoba mengekspor database.", 500

    # ========================================== 
    # ROUTE: USER
    # ==========================================

    @app.route("/user")
    def user():
        return render_template("user/index.html")
    
    @app.route("/user/register_user")
    def register_user():
        return render_template("user/register_user.html")

    @app.route("/user/register_user", methods=["POST"])
    def submit_register_user():
        if request.method == "POST":
            # Ambil data dari form
            name = request.form.get("name")
            born_place = request.form.get("born_place")
            username = request.form.get("username")
            born_date = request.form.get("date")
            email = request.form.get("email")
            password = request.form.get("password")
            photo = request.files.get("foto")

            # Validasi input wajib
            if not all([name, username, email, password]):
                return render_template(
                    "user/register_user.html",
                    error="Semua field yang bertanda * wajib diisi."
                )

            # Hash password
            hashed_password = generate_password_hash(password)

            foto_data = None
            if photo and photo.filename.strip() != "":
                upload_folder = app.config['UPLOAD_FOLDER', filename]
                os.makedirs(upload_folder, exist_ok=True)
                foto_path = os.path.join(upload_folder, photo.filename)
                photo.save(foto_path)
                foto_data = foto_data = f'Back_End/uploads/{filename}'
            else:
                # Gunakan foto default jika user tidak upload
                foto_data = "static/uploads/default.jpg"
            # Simpan data ke database
            conn = get_db_connection(app.config['DATABASE'])
            try:
                execute_insert(conn, " INSERT INTO users (name, born_place, username, born_date, email, password, Photo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (name, born_place, username, born_date, email, hashed_password, foto_data)
                );
                conn.commit()
                close_db_connection(conn)

                # Redirect ke halaman login
                return redirect(url_for('dashboard_user', success="Registrasi berhasil! Silakan login."))
            except sqlite3.IntegrityError:
                close_db_connection(conn)
                return render_template("user/register_user.html", error="Username atau email sudah terdaftar.")
        return render_template("user/register_user.html")
          
    @app.route("/user/login_user")
    def login_user():
        return render_template("user/login_user.html")

# =============================
# LOGIN USER
# =============================
    @app.route("/user/login_user", methods=["GET", "POST"])
    def submit_login_user():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "").strip()

            # Validasi input
            if not username or not password:
                return render_template("user/login_user.html", error="Username dan password wajib diisi.")

            conn = get_db_connection(app.config['DATABASE'])
            user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
            close_db_connection(conn)

            # Jika user ditemukan dan password cocok
            if user and check_password_hash(user["password"], password):
                session["user_id"] = user["id"]
                session["username"] = user["username"]
                session["name"] = user["name"]
                session["photo"] = user["Photo"]  # simpan foto ke session juga

                return redirect(url_for("dashboard_user"))
            else:
                return render_template("user/login_user.html", error="Username atau password salah.")
        
        return render_template("user/login_user.html")


# =============================
# DASHBOARD USER
    @app.route("/user/dashboard")
    def dashboard_user():
        # Pastikan user sudah login
        if "user_id" not in session:
            return redirect(url_for("login_user"))

        # Ambil data user dari database
        user_id = session['user_id']
        conn = get_db_connection(app.config['DATABASE'])
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        close_db_connection(conn)

        # Jika user tidak ditemukan
        if not user:
            return redirect(url_for("login_user"))

        # Ambil path foto user dari database
        photo_path = user["Photo"]

        # Cek apakah foto ada, kalau tidak gunakan default
        if not photo_path or not os.path.exists(photo_path):
            photo_url = url_for('static', filename='uploads/default.jpg')
        else:
            filename = os.path.basename(photo_path)
            photo_url = url_for('static', filename=f'uploads/{filename}')
        return render_template("user/dashboard_user.html", users=user, photo_url=photo_url)

    @app.route("/user/logout")
    def logout_user():
        session.clear()
        return redirect(url_for("login_user"))

    # ==========================================
    # ROUTE: SUBMIT TESTIMONIAL (CREATE) 
    # ==========================================
    @app.route("/submit_testimonial", methods=["POST"])
    def submit_testimonial():
        user_name = request.form.get("user_name")
        message = request.form.get("message")
        if user_name and message:
            conn = get_db_connection(app.config['DATABASE'])
            execute_insert(conn,
                           "INSERT INTO testimonials (user_name, message) VALUES (?, ?)",
                           (user_name, message))
            conn.commit()
            close_db_connection(conn)
        return redirect(url_for("home"))

    # ==========================================
    # CRUD OPERATIONS FOR TESTIMONIALS
    # ==========================================
    
    @app.route("/update_testimonial/<int:testimonial_id>", methods=["POST"])
    def update_testimonial(testimonial_id):
        if "admin_logged_in" not in session:
            return redirect(url_for("login_admin"))
        
        user_name = request.form.get("user_name")
        message = request.form.get("message")
        
        if user_name and message:
            conn = get_db_connection(app.config['DATABASE'])
            conn.execute(
                "UPDATE testimonials SET user_name = ?, message = ? WHERE id = ?",
                (user_name, message, testimonial_id)
            )
            conn.commit()
            close_db_connection(conn)
        
        return redirect(url_for("home"))
    
    @app.route("/delete_testimonial/<int:testimonial_id>", methods=["POST"])
    def delete_testimonial(testimonial_id):
        if "admin_logged_in" not in session:
            return redirect(url_for("login_admin"))
        
        conn = get_db_connection(app.config['DATABASE'])
        conn.execute("DELETE FROM testimonials WHERE id = ?", (testimonial_id,))
        conn.commit()
        close_db_connection(conn)
        
        return redirect(url_for("home"))

    # ==========================================
    # CRUD OPERATIONS FOR USERS
    # ==========================================
    
    @app.route("/user/profile")
    def user_profile():
        if "user_id" not in session:
            return redirect(url_for("login_user"))
        
        conn = get_db_connection(app.config['DATABASE'])
        user = conn.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],)).fetchone()
        close_db_connection(conn)
        
        return render_template("user/profile.html", user=user)
    
    @app.route("/user/update_profile", methods=["POST"])
    def update_user_profile():
        if "user_id" not in session:
            return redirect(url_for("login_user"))
        
        name = request.form.get("name")
        born_place = request.form.get("born_place")
        born_date = request.form.get("date")
        email = request.form.get("email")
        photo = request.files.get("foto")
        
        foto_data = None
        if photo and photo.filename.strip() != "":
            upload_folder = app.config.get("UPLOAD_FOLDER", "static/uploads")
            os.makedirs(upload_folder, exist_ok=True)
            foto_path = os.path.join(upload_folder, photo.filename)
            photo.save(foto_path)
            foto_data = foto_path
        
        conn = get_db_connection(app.config['DATABASE'])
        
        if foto_data:
            conn.execute(
                "UPDATE users SET name = ?, born_place = ?, born_date = ?, email = ?, Photo = ? WHERE id = ?",
                (name, born_place, born_date, email, foto_data, session["user_id"])
            )
        else:
            conn.execute(
                "UPDATE users SET name = ?, born_place = ?, born_date = ?, email = ? WHERE id = ?",
                (name, born_place, born_date, email, session["user_id"])
            )
        
        conn.commit()
        close_db_connection(conn)
        
        return redirect(url_for("user_profile"))
    
    @app.route("/user/delete_account", methods=["POST"])
    def delete_user_account():
        if "user_id" not in session:
            return redirect(url_for("login_user"))
        
        conn = get_db_connection(app.config['DATABASE'])
        conn.execute("DELETE FROM users WHERE id = ?", (session["user_id"],))
        conn.commit()
        close_db_connection(conn)
        
        session.clear()
        return redirect(url_for("home"))

    # ==========================================
    # ROUTE: UPLOAD DAN ENKRIPSI FILE
    # ========================================== 
    @app.route("/upload_file", methods=["POST"])
    def upload_file():
        if 'file' not in request.files:
            return "Tidak ada file yang dipilih", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "Tidak ada file yang dipilih", 400

        if file:
            original_content = file.read()
            encrypted_content = encrypt_data(original_content)
            encrypted_filename = file.filename + ".enc"
            encrypted_filepath = os.path.join(app.config['UPLOAD_FOLDER'], encrypted_filename)
            
            with open(encrypted_filepath, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)

            return f"File '{file.filename}' berhasil diunggah dan dienkripsi sebagai '{encrypted_filename}'. <a href='{url_for('home')}'>Kembali</a>"

        return "Upload file gagal", 500

    # ==========================================
    # ROUTE: DOWNLOAD DAN DEKRIPSI FILE 
    # ========================================== 
    @app.route("/download_file/<filename>")
    def download_file(filename):
        encrypted_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if not os.path.exists(encrypted_filepath):
            return "File tidak ditemukan.", 404

        try:
            with open(encrypted_filepath, 'rb') as f:
                encrypted_content = f.read()

            decrypted_content = decrypt_data(encrypted_content)
            original_filename = filename.replace(".enc", "")
            temp_decrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_' + original_filename)
            with open(temp_decrypted_path, 'wb') as f:
                f.write(decrypted_content)
            
            return send_from_directory(
                directory=app.config['UPLOAD_FOLDER'], 
                path='temp_' + original_filename, 
                as_attachment=True, 
                download_name=original_filename
            )
        except Exception as e:
            logging.error(f"Gagal mendekripsi file {filename}: {e}")
            return "Gagal mendekripsi file. File mungkin rusak atau kunci salah.", 500

    # ==========================================
    # ROUTE: API DATA (PENDIDIKAN)
    # ========================================== 
    @app.route("/api/education_data")
    def api_education_data():
        if not os.path.exists(CSV_PATH):
            return jsonify({"error": "File CSV tidak ditemukan"}), 404
        try:
            df = pd.read_csv(CSV_PATH)
            return jsonify(df.to_dict(orient='records'))
        except Exception as e:
            logging.error(f"Error membaca CSV file {CSV_PATH}: {e}")
            return jsonify({"error": "Terjadi kesalahan saat memproses data."}), 500

    # ==========================================
    # ROUTE: GRAFIK PENDIDIKAN (.PNG)
    # ==========================================  
    @app.route("/chart/education.png")
    def chart_education():
        if not os.path.exists(CSV_PATH):
            return Response("File CSV tidak ditemukan", status=404)

        try:
            df = pd.read_csv(CSV_PATH)
            if not all(col in df.columns for col in ['Tahun', 'Enrolment', 'Literacy']):
                return Response("Kolom yang diperlukan tidak ditemukan di CSV.", status=500)

            tahun = df['Tahun']
            enrolment = df['Enrolment']
            literacy = df['Literacy']

            fig, ax1 = plt.subplots(figsize=(10, 5))
            ax1.plot(tahun, enrolment, marker='o', label='Tingkat Enrolment (%)', color='blue')
            ax1.plot(tahun, literacy, marker='s', label='Tingkat Melek Huruf (%)', color='green')
            ax1.set_xlabel('Tahun')
            ax1.set_ylabel('Persentase (%)')
            ax1.ticklabel_format(axis='y', style='plain')
            ax1.legend(loc='upper left')

            plt.title('📊 Tren Pendidikan 2015–2024')
            plt.tight_layout()

            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=150)
            plt.close(fig)
            buf.seek(0)
            return Response(buf.getvalue(), mimetype='image/png')
        except Exception as e:
            logging.error(f"Error membuat grafik pendidikan: {e}")
            return Response("Error membuat grafik.", status=500)

    return app


# ==========================================
# MAIN ENTRY POINT
# ==========================================
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
