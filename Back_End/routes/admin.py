from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, session, current_app, jsonify
from Back_End.routes.utils import get_user_data_for_template
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.routes.security_for_web import admin_required
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pandas as pd
import io
import logging
import mysql.connector


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route("/", methods=["GET"])
def index():
    return render_template("admin/index.html")

@admin_bp.route("/login_admin", methods=["GET", "POST"])
def login_admin():
    """Portal Terpadu: Seluruh autentikasi disatukan ke portal terpadu (auth.login_user)."""
    if session.get('admin_logged_in'):
        return redirect(url_for('admin.dashboard_admin'))
    if session.get('user_id'):
        return redirect(url_for('user.dashboard_user'))

    if request.method == "POST":
        # Jika ada form POST langsung ke /admin/login_admin, verifikasi dengan aman
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'Edward_Kenway')
        ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Mentawai160604')
        import secrets
        if secrets.compare_digest(username, ADMIN_USERNAME) and secrets.compare_digest(password, ADMIN_PASSWORD):
            session.clear()
            session.permanent = True
            session['admin_logged_in'] = True
            session['username'] = ADMIN_USERNAME
            session['role'] = 'admin'
            session['name'] = 'Administrator'
            flash("Login admin berhasil!", "success")
            return redirect(url_for('admin.dashboard_admin'))
        flash("Username atau password admin salah.", "danger")
        return redirect(url_for('auth.login_user'))

    return redirect(url_for('auth.login_user'))

@admin_bp.route("/logout")
@admin_required
def logout_admin():
    session.pop('admin_logged_in', None)
    session.pop('username', None)
    session.pop('role', None)
    flash("Logout berhasil.", "success")
    return redirect(url_for('auth.login_user'))

@admin_bp.route("/dashboard")
@admin_required
def dashboard_admin():
    admin_user = {'name': 'Administrator', 'photo': 'uploads/default.jpg'}
    photo_url = url_for('static', filename='uploads/default.jpg')
    return render_template("admin/dashboard.html", users=admin_user, photo_url=photo_url)

@admin_bp.route("/manage_materi")
@admin_required
def manage_materi():
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, judul_materi, deskripsi, status, rating FROM daftar_materi ORDER BY id ASC")
        materis = cursor.fetchall()
        for m in materis:
            m["judul_materi"] = str(m.get("judul_materi") or "")
            m["deskripsi"] = str(m.get("deskripsi") or "")
            m["status"] = str(m.get("status") or "")
            m["rating"] = str(m.get("rating") or "")
        return render_template("admin/manage_materi.html", daftar_materi=materis)
    finally:
        if conn:
            close_db_connection(conn)

# Add/Edit/Delete Materi CRUD (full extracted logic)
@admin_bp.route("/add_materi", methods=["GET", "POST"])
@admin_required
def add_materi():
    if request.method == "GET":
        return render_template("admin/add_materi.html")
    judul_materi = request.form.get("judul_materi") or ""
    deskripsi = request.form.get("deskripsi") or ""
    status = request.form.get("status") or "inactive"
    rating = request.form.get("rating") or ""
    if not judul_materi:
        flash("Judul wajib!", "danger")
        return redirect(url_for("admin.add_materi"))
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        cursor.execute("INSERT INTO daftar_materi (judul_materi, deskripsi, status, rating) VALUES (%s, %s, %s, %s)", 
                      (judul_materi, deskripsi, status, rating))
        conn.commit()
        flash("Materi ditambahkan!", "success")
    finally:
        if conn:
            close_db_connection(conn)
    return redirect(url_for("admin.manage_materi"))

# ... (edit_materi, delete_materi - full logic from __init__.py abbreviated for brevity)

@admin_bp.route("/manage_users")
@admin_required
def manage_users():
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        # Ambil data user beserta total interaksi (pesan chat) untuk menghitung pengguna aktif
        cursor.execute("""
            SELECT u.id, u.name, u.username, u.email, u.born_place, u.born_date, u.photo,
                   (SELECT COUNT(*) FROM chat_messages cm 
                    JOIN conversations c ON cm.conversation_id = c.id 
                    WHERE c.user_id = u.id) as total_sessions
            FROM users u
        """)
        users = cursor.fetchall()

        total_users = len(users)
        active_users = sum(1 for u in users if (u.get("total_sessions") or 0) > 0)

        for user in users:
            photo_path = user.get("photo")
            user["photo_url"] = url_for('static', filename=photo_path) if photo_path else url_for('static', filename='uploads/default.jpg')
            # Siapkan sub-dict analysis agar sesuai dengan struktur pemanggilan di template
            user['analysis'] = {'total_sessions': user.get('total_sessions') or 0}
            
        return render_template("admin/manage_users.html", users=users, total_users=total_users, active_users=active_users)
    finally:
        if conn:
            close_db_connection(conn)

@admin_bp.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
@admin_required
def edit_user(user_id):
    """Menampilkan form untuk mengedit data user dan memproses update."""
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        if request.method == "POST":
            name = request.form.get("name")
            username = request.form.get("username")
            email = request.form.get("email")
            born_place = request.form.get("born_place")
            born_date = request.form.get("born_date")

            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name = %s, username = %s, email = %s, born_place = %s, born_date = %s WHERE id = %s",
                           (name, username, email, born_place, born_date, user_id))
            conn.commit()
            cursor.close()
            flash("Data pengguna berhasil diperbarui!", "success")
            return redirect(url_for('admin.manage_users'))

        else: # GET request
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name, username, email, born_place, born_date FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            cursor.close()
            if not user:
                flash("Pengguna tidak ditemukan.", "danger")
                return redirect(url_for('admin.manage_users'))
            return render_template("admin/edit_user.html", user=user)

    except mysql.connector.Error as err:
        logging.error(f"Error with user edit/update: {err}")
        flash(f"Terjadi kesalahan: {err}", "danger")
        return redirect(url_for('admin.manage_users'))
    finally:
        if conn:
            close_db_connection(conn)

@admin_bp.route("/view_user/<int:user_id>", methods=["GET", "POST"])
@admin_required
def view_user(user_id): # Mengubah metode menjadi hanya GET
    """Menampilkan data detail pengguna."""
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, username, email, born_place, born_date, photo FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        if not user:
            flash("Pengguna tidak ditemukan.", "danger")
            return redirect(url_for('admin.manage_users'))
        user["photo_url"] = url_for('static', filename=user.get('photo') or 'uploads/default.jpg')
        return render_template("admin/view_user.html", user=user) # Mengarahkan ke template view_user.html

    except mysql.connector.Error as err:
        logging.error(f"Error with user edit/update: {err}")
        flash(f"Terjadi kesalahan: {err}", "danger")
        return redirect(url_for('admin.manage_users'))
    finally:
        if conn:
            close_db_connection(conn)



@admin_bp.route("/delete_user/<int:user_id>", methods=["POST"])
@admin_required
def delete_user(user_id):
    """Menghapus user berdasarkan ID."""
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        flash("Pengguna berhasil dihapus.", "success")
    except mysql.connector.Error as err:
        logging.error(f"Error deleting user by admin: {err}")
        flash("Terjadi kesalahan saat menghapus pengguna.", "danger")
    finally:
        if conn:
            close_db_connection(conn)
    return redirect(url_for('admin.manage_users'))

@admin_bp.route("/add_soal_materi", methods=["GET", "POST"])
@admin_required
def add_soal_materi():
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        if request.method == "GET":
            cursor = conn.cursor(dictionary=True)
            # 1. Ambil data materi aktif untuk dropdown utama
            cursor.execute("SELECT id, judul_materi FROM daftar_materi WHERE status = 'active' ORDER BY id")
            materis = cursor.fetchall()
            
            # 2. Ambil semua data dari tabel 'topics' dengan JOIN ke materi agar klasifikasi jelas
            cursor.execute("""
                SELECT t.id, t.materi_id, t.name as topic_name, dm.judul_materi, COUNT(q.id) as soal_count 
                FROM topics t 
                JOIN daftar_materi dm ON t.materi_id = dm.id
                LEFT JOIN questions q ON t.id = q.topic_id 
                GROUP BY t.id, t.materi_id, t.name, dm.judul_materi
                ORDER BY dm.judul_materi ASC, t.name ASC
            """)
            topics_table_data = cursor.fetchall()
            
            return render_template("admin/add_soal_materi.html", 
                                 materis=materis, 
                                 topics_table_data=topics_table_data)

        cursor = conn.cursor()
        topic_id = request.form.get('topic_id')
        content = request.form.get('content')
        answer = request.form.get('answer')
        difficulty = request.form.get('difficulty', 'easy')
        cursor.execute("INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, %s, %s, %s)", 
                       (topic_id, content, answer, difficulty))
        conn.commit()
        return jsonify({'success': True}), 201 # 201 Created for successful resource creation
    except Exception as e:
        logging.error(f"Error adding soal: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500 # 500 Internal Server Error
    finally:
        if conn:
            close_db_connection(conn)



@admin_bp.route("/topics")
@admin_required
def get_topics():
    materi_id = request.args.get('materi_id')
    if not materi_id:
        return jsonify([])
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT t.id, t.name as topic_name, dm.judul_materi, COUNT(q.id) as soal_count
            FROM topics t 
            JOIN daftar_materi dm ON t.materi_id = dm.id
            LEFT JOIN questions q ON t.id = q.topic_id
            WHERE t.materi_id = %s
            GROUP BY t.id, t.name, dm.judul_materi
            ORDER BY t.name ASC
        """, (materi_id,))
        topics = cursor.fetchall()
        return jsonify(topics)
    finally:
        if conn:
            close_db_connection(conn)

@admin_bp.route("/get_soal_stats")
@admin_required
def get_soal_stats():
    materi_id = request.args.get('materi_id')
    if not materi_id:
        return jsonify({'total_soal': 0, 'total_topik': 0})
    conn = None
    try:    
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT judul_materi FROM daftar_materi WHERE id = %s", (materi_id,))
        materi = cursor.fetchone()
        if materi:
            cursor.execute("""
                SELECT COUNT(q.id) as total_soal, COUNT(DISTINCT t.id) as total_topik 
                FROM topics t 
                LEFT JOIN questions q ON q.topic_id = t.id
                WHERE t.materi_id = %s
            """, (materi_id,))
            return jsonify(cursor.fetchone()), 200
        return jsonify({'total_soal': 0, 'total_topik': 0}), 200
    finally:
        if conn:
            close_db_connection(conn)


@admin_bp.route("/create_topic", methods=["POST"])
@admin_required
def create_topic():
    # Gunakan get_json() karena frontend mengirim payload JSON
    data = request.get_json() or {}
    materi_id = data.get('materi_id')
    name = data.get('name')
    description = data.get('description', '')
    
    if not name or not materi_id:
        return {'success': False, 'message': 'Materi ID dan Nama wajib diisi'}
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        cursor.execute("INSERT INTO topics (materi_id, name, description) VALUES (%s, %s, %s)", 
                       (materi_id, name, description))
        topic_id = cursor.lastrowid
        conn.commit()
        return {'success': True, 'topic': {'id': topic_id, 'name': name}}
    except Exception as e:
        logging.error(f"Error creating topic: {e}")
        return {'success': False, 'message': str(e)}
    finally:
        if conn:
            close_db_connection(conn)

@admin_bp.route("/manage_analisis_hasil")
@admin_required
def manage_analisis_hasil():
    return render_template("admin/manage_analisis_hasil.html")

@admin_bp.route("/manage_feedback")
@admin_required
def manage_feedback():
    admin_user = {'name': session.get('name') or session.get('username') or 'Administrator'}
    return render_template("admin/manage_feedback.html", users=admin_user)

@admin_bp.route("/crime_detection")
@admin_required
def crime_detection():
    from Back_End.bug_and_crime_detection.bug_and_crime_detection import get_security_summary
    summary = get_security_summary()
    return render_template("admin/crime_detection.html", summary=summary)

# ==============================================================================
# DATABASE MANAGEMENT, PERIODIC BACKUPS & EXPORT ENGINE
# ==============================================================================
from flask import send_file, send_from_directory, Response
from Back_End.db.db_management import (
    get_database_overview,
    get_backup_dir,
    load_backup_registry,
    load_backup_config,
    save_backup_config,
    create_backup_snapshot,
    delete_backup_file,
    restore_database_from_archive,
    restore_database_from_file_content,
    optimize_single_table,
    optimize_all_database_tables,
    generate_full_sql_dump,
    generate_multi_table_excel_bytes,
    generate_multi_table_csv_zip_bytes,
    check_and_run_scheduled_backup_if_due
)

@admin_bp.route("/export_database")
@admin_required
def export_database():
    """Halaman Pusat Manajemen Database & Backup Berkala."""
    app_obj = current_app._get_current_object()
    
    # Jalankan backup terjadwal jika waktu telah tiba
    check_and_run_scheduled_backup_if_due(app_obj)

    db_overview = get_database_overview(app_obj)
    backups = load_backup_registry()
    backup_config = load_backup_config()
    admin_user = {'name': session.get('name') or session.get('username') or 'Administrator'}

    return render_template(
        "admin/export_database.html",
        users=admin_user,
        overview=db_overview,
        backups=backups,
        config=backup_config
    )

@admin_bp.route("/database/backup/create", methods=["POST"])
@admin_required
def create_backup_route():
    """Membuat snapshot backup database secara instan (Manual Snapshot)."""
    try:
        app_obj = current_app._get_current_object()
        data = request.get_json(silent=True) or {}
        backup_format = data.get('format', 'zip')

        record = create_backup_snapshot(app_obj, backup_type='manual', backup_format=backup_format)
        return jsonify({
            'success': True,
            'message': f"Snapshot backup `{record['filename']}` berhasil dibuat ({record['size_formatted']}).",
            'backup': record
        })
    except Exception as e:
        logging.error(f"Error creating manual backup: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@admin_bp.route("/database/backup/download/<filename>", methods=["GET"])
@admin_required
def download_backup_route(filename):
    """Mengunduh berkas arsip backup dari server."""
    safe_filename = os.path.basename(filename)
    backup_dir = get_backup_dir()
    file_path = os.path.join(backup_dir, safe_filename)

    if not os.path.exists(file_path):
        flash("Berkas backup tidak ditemukan.", "danger")
        return redirect(url_for('admin.export_database'))

    return send_from_directory(
        backup_dir,
        safe_filename,
        as_attachment=True,
        download_name=safe_filename
    )

@admin_bp.route("/database/backup/delete/<filename>", methods=["DELETE"])
@admin_required
def delete_backup_route(filename):
    """Menghapus arsip backup dari disk dan registry."""
    try:
        safe_filename = os.path.basename(filename)
        success = delete_backup_file(safe_filename)
        if success:
            return jsonify({'success': True, 'message': f"Berkas `{safe_filename}` berhasil dihapus."})
        return jsonify({'success': False, 'error': 'Berkas tidak ditemukan atau gagal dihapus.'}), 404
    except Exception as e:
        logging.error(f"Error deleting backup: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@admin_bp.route("/database/backup/restore/<filename>", methods=["POST"])
@admin_required
def restore_backup_route(filename):
    """Memulihkan database dari berkas snapshot yang tersimpan di server."""
    try:
        app_obj = current_app._get_current_object()
        safe_filename = os.path.basename(filename)
        result = restore_database_from_archive(app_obj, safe_filename)
        if result['success']:
            return jsonify({
                'success': True,
                'message': f"Database berhasil dipulihkan dari `{safe_filename}` ({result.get('statements_executed', 0)} perintah dieksekusi)."
            })
        return jsonify({'success': False, 'error': result.get('error', 'Gagal memulihkan database.')}), 500
    except Exception as e:
        logging.error(f"Error restoring backup: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@admin_bp.route("/database/backup/upload-restore", methods=["POST"])
@admin_required
def upload_restore_backup_route():
    """Mengunggah berkas .sql atau .zip dari komputer admin lalu merestore database."""
    try:
        if 'backup_file' not in request.files:
            return jsonify({'success': False, 'error': 'Tidak ada berkas yang diunggah.'}), 400

        file = request.files['backup_file']
        if not file or not file.filename:
            return jsonify({'success': False, 'error': 'Pilih berkas backup terlebih dahulu.'}), 400

        filename = file.filename.lower()
        if not (filename.endswith('.sql') or filename.endswith('.zip')):
            return jsonify({'success': False, 'error': 'Format berkas harus berupa .sql atau .zip'}), 400

        app_obj = current_app._get_current_object()
        content = ""

        if filename.endswith('.zip'):
            import zipfile
            with zipfile.ZipFile(file.stream, 'r') as zf:
                sql_files = [n for n in zf.namelist() if n.endswith('.sql')]
                if not sql_files:
                    return jsonify({'success': False, 'error': 'Berkas ZIP tidak memuat file SQL.'}), 400
                content = zf.read(sql_files[0]).decode('utf-8', errors='replace')
        else:
            content = file.stream.read().decode('utf-8', errors='replace')

        result = restore_database_from_file_content(app_obj, content)
        if result['success']:
            return jsonify({
                'success': True,
                'message': f"Database berhasil dipulihkan dari berkas unggahan ({result.get('statements_executed', 0)} perintah dieksekusi)."
            })
        return jsonify({'success': False, 'error': result.get('error', 'Gagal memulihkan database.')}), 500
    except Exception as e:
        logging.error(f"Error in upload-restore: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@admin_bp.route("/database/backup/config", methods=["POST"])
@admin_required
def update_backup_config_route():
    """Memperbarui pengaturan jadwal backup berkala otomatis."""
    try:
        data = request.get_json(silent=True) or {}
        config = load_backup_config()

        if 'auto_backup_enabled' in data:
            config['auto_backup_enabled'] = bool(data['auto_backup_enabled'])
        if 'interval_type' in data:
            itype = str(data['interval_type']).lower()
            if itype in {'hourly', 'daily', 'weekly'}:
                config['interval_type'] = itype
                if itype == 'hourly':
                    config['interval_hours'] = 1
                elif itype == 'daily':
                    config['interval_hours'] = 24
                elif itype == 'weekly':
                    config['interval_hours'] = 168
        if 'retention_count' in data:
            try:
                config['retention_count'] = max(3, min(50, int(data['retention_count'])))
            except ValueError:
                pass
        if 'format' in data and data['format'] in {'sql', 'zip'}:
            config['format'] = data['format']

        # Hitung ulang jadwal berikutnya
        from datetime import datetime, timedelta
        now = datetime.now()
        config['next_backup_time'] = (now + timedelta(hours=config['interval_hours'])).strftime("%Y-%m-%d %H:%M:%S")

        save_backup_config(config)
        return jsonify({'success': True, 'message': 'Konfigurasi backup berkala berhasil disimpan.', 'config': config})
    except Exception as e:
        logging.error(f"Error updating backup config: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@admin_bp.route("/database/table/optimize", methods=["POST"])
@admin_required
def optimize_table_route():
    """Mengoptimasi satu tabel atau seluruh tabel database."""
    try:
        app_obj = current_app._get_current_object()
        data = request.get_json(silent=True) or {}
        target_table = data.get('table', 'all')

        if target_table == 'all':
            result = optimize_all_database_tables(app_obj)
        else:
            result = optimize_single_table(app_obj, target_table)

        return jsonify(result)
    except Exception as e:
        logging.error(f"Error optimizing tables: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500

# ==============================================================================
# UPGRADED UNIVERSAL EXPORTS (FULL DATABASE)
# ==============================================================================
@admin_bp.route("/submit_export_database_excel")
@admin_required
def submit_export_excel():
    """Ekspor seluruh tabel database ke berkas Excel Multi-Sheet."""
    try:
        app_obj = current_app._get_current_object()
        excel_buffer = generate_multi_table_excel_bytes(app_obj)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return send_file(
            excel_buffer,
            as_attachment=True,
            download_name=f"maththon_db_full_{timestamp}.xlsx",
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    except Exception as e:
        logging.error(f"Excel export error: {e}", exc_info=True)
        flash(f"Gagal mengekspor database ke Excel: {e}", "danger")
        return redirect(url_for('admin.export_database'))

@admin_bp.route("/submit_export_database_sql")
@admin_required
def submit_export_sql():
    """Ekspor seluruh skema dan baris data database ke format SQL Dump murni."""
    try:
        app_obj = current_app._get_current_object()
        sql_dump = generate_full_sql_dump(app_obj, include_data=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return Response(
            sql_dump,
            mimetype="application/sql",
            headers={"Content-Disposition": f"attachment; filename=maththon_db_dump_{timestamp}.sql"}
        )
    except Exception as e:
        logging.error(f"SQL export error: {e}", exc_info=True)
        flash(f"Gagal mengekspor SQL dump: {e}", "danger")
        return redirect(url_for('admin.export_database'))

@admin_bp.route("/submit_export_database_csv")
@admin_required
def submit_export_csv():
    """Ekspor seluruh tabel database sebagai arsip ZIP berisi berkas CSV terpisah."""
    try:
        app_obj = current_app._get_current_object()
        zip_buffer = generate_multi_table_csv_zip_bytes(app_obj)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name=f"maththon_csv_bundle_{timestamp}.zip",
            mimetype='application/zip'
        )
    except Exception as e:
        logging.error(f"CSV zip export error: {e}", exc_info=True)
        flash(f"Gagal mengekspor kumpulan CSV: {e}", "danger")
        return redirect(url_for('admin.export_database'))


@admin_bp.route("/import_soal_csv", methods=["POST"])
@admin_required
def import_soal_csv():
    if 'csv_file' not in request.files:
        return {'success': False, 'message': 'No file'}
    file = request.files['csv_file']
    materi_id = request.form.get('materi_id')
    if file.filename == '':
        return {'success': False, 'message': 'No file selected'}
    try:
        df = pd.read_csv(file)
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        success_count = 0
        failure_count = 0
        for _, row in df.iterrows():
            content = str(row.get('content', ''))
            answer = str(row.get('answer', ''))
            difficulty = str(row.get('difficulty', 'easy'))
            topic_name = str(row.get('topic_name', ''))
            if not content or not answer or not topic_name:
                failure_count += 1
                continue
            # Get or create topic
            cursor.execute("SELECT id FROM topics WHERE name = %s AND materi_id = %s", (topic_name, materi_id))
            topic = cursor.fetchone()
            if not topic:
                cursor.execute("INSERT INTO topics (materi_id, name, description) VALUES (%s, %s, %s)", 
                               (materi_id, topic_name, f'Auto-created topic via import'))
                topic_id = cursor.lastrowid
            else:
                topic_id = topic[0]
            cursor.execute("INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, %s, %s, %s)",
                           (topic_id, content, answer, difficulty))
            success_count += 1
        conn.commit()
        close_db_connection(conn)
        return {'success': True, 'success_count': success_count, 'failure_count': failure_count}
    except Exception as e:
        logging.error(f"CSV import error: {e}")
        return {'success': False, 'message': str(e)}

@admin_bp.route("/detail_materi/<int:materi_id>")
@admin_required
def detail_materi(materi_id):
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM daftar_materi WHERE id = %s", (materi_id,))
        materi = cursor.fetchone()
        return render_template("admin/detail_materi.html", materi=materi)
    finally:
        if conn:
            close_db_connection(conn)

@admin_bp.route("/edit_materi/<int:materi_id>", methods=["GET", "POST"])
@admin_required
def edit_materi(materi_id):
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        
        # 1. Ambil data materi yang ada untuk diisi ke form
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM daftar_materi WHERE id = %s", (materi_id,))
        materi = cursor.fetchone()
        cursor.close()

        if not materi:
            flash("Materi tidak ditemukan.", "danger")
            return redirect(url_for("admin.manage_materi"))

        if request.method == "GET":
            return render_template("admin/edit_materi.html", materi=materi, materi_id=materi_id)

        # Proses Update (POST)
        judul_materi = request.form.get("judul_materi")
        slug = request.form.get("slug")
        deskripsi = request.form.get("deskripsi")
        image_url = request.form.get("image_url")
        status = request.form.get("status")
        rating = request.form.get("rating")
        content = request.form.get("content")

        cursor = conn.cursor()
        cursor.execute("""
            UPDATE daftar_materi 
            SET judul_materi = %s, slug = %s, deskripsi = %s, image_url = %s, status = %s, rating = %s, content = %s 
            WHERE id = %s
        """, (judul_materi, slug, deskripsi, image_url, status, rating, content, materi_id))
        conn.commit()
        flash("Materi berhasil diperbarui!", "success")
        return redirect(url_for("admin.manage_materi"))

    finally:
        if conn:
            close_db_connection(conn)

@admin_bp.route("/delete_materi/<int:materi_id>", methods=["POST"])
@admin_required
def delete_materi(materi_id):
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor()
        cursor.execute("DELETE FROM daftar_materi WHERE id = %s", (materi_id,))
        conn.commit() 
    finally:
        if conn:
            close_db_connection(conn)
    return redirect(url_for("admin.manage_materi"))

@admin_bp.route("/export_to_csv")
@admin_required
def export_to_csv():
    return render_template("admin/export_database.html")

# ... (export_to_csv, export_to_sql, export_to_excel routes - full pandas/io logic)