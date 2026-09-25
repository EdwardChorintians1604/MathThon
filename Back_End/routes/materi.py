from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from Back_End.routes.security_for_web import user_required
from Back_End.routes.utils import get_user_data_for_template
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from jinja2 import TemplateNotFound
import logging

# Blueprint ini didaftarkan dengan url_prefix='/user/materi' di __init__.py
materi_bp = Blueprint('materi', __name__)

@materi_bp.route("/")
@user_required
def materi_user():
    from flask import session
    from Back_End.routes.utils import log_user_activity
    user_data = get_user_data_for_template(current_app._get_current_object())
    log_user_activity(current_app._get_current_object(), session.get('user_id'), 'materi', 'Mengakses halaman daftar materi matematika')
    return render_template("user/materi_user.html", **user_data)

@materi_bp.route("/<path:materi_identifier>")
@user_required
def materi_detail(materi_identifier):
    """
    Menampilkan halaman detail materi secara dinamis.
    Fungsi ini menangkap nama materi dari URL, mencarinya di database,
    dan kemudian mencoba me-render file HTML yang sesuai.
    Jika file HTML spesifik tidak ada, ia akan menggunakan template umum.
    """
    user_data = get_user_data_for_template(current_app._get_current_object())
    conn = None
    materi = None
    
    # Debug print untuk memastikan rute terpanggil
    print(f"🔵 HIT Route Materi Detail: {materi_identifier}")

    try:
        conn = get_db_connection(current_app._get_current_object())
        cursor = conn.cursor(dictionary=True)

        # 1. Normalisasi identifier dari URL (misal: fungsi_turunan -> fungsi turunan)
        # Kita akan mencari kecocokan dengan memanipulasi judul di database agar sesuai format URL
        search_val = materi_identifier.lower().strip()

        # 2. Cari materi dengan membandingkan JUDUL_MATERI di DB (yang diformat) dengan identifier URL
        # Mendukung snake_case (judul_materi) atau kebab-case (judul-materi)
        query = """
            SELECT * FROM daftar_materi 
            WHERE (
                LOWER(REPLACE(judul_materi, ' ', '_')) = %s 
                OR LOWER(REPLACE(judul_materi, ' ', '-')) = %s
            ) 
            AND status = 'active'
        """
        cursor.execute(query, (search_val, search_val))
        materi = cursor.fetchone()

        if not materi:
            flash(f"Materi '{materi_identifier}' tidak ditemukan atau tidak aktif.", "warning")
            return redirect(url_for('materi.materi_user'))

        from flask import session
        from Back_End.routes.utils import log_user_activity
        log_user_activity(current_app._get_current_object(), session.get('user_id'), 'materi', f"Mempelajari materi: {materi['judul_materi']}")

        # 3. Logika Penentuan Nama Template
        # Menggunakan identifier dari URL (snake_case) sebagai nama file dasar
        possible_templates = []
        
        # Coba format asli dari URL (misal: user/materi/fungsi_turunan.html)
        possible_templates.append(f"user/materi/{materi_identifier}.html")
        # Coba format underscore (jika URL pakai dash)
        possible_templates.append(f"user/materi/{materi_identifier.replace('-', '_')}.html")

        # Coba render satu per satu dari variasi nama yang mungkin
        for template_path in possible_templates:
            try:
                # logging.debug(f"Mencoba me-render template: {template_path}")
                return render_template(template_path, materi=materi, **user_data)
            except TemplateNotFound:
                continue
        
        # Jika tidak ada satupun file HTML yang cocok, gunakan template umum (fallback)
        # Periksa apakah materi memiliki konten di database (CMS style)
        if materi.get('content') and str(materi['content']).strip():
            logging.info(f"Menggunakan konten database untuk '{materi_identifier}' dengan template fallback.")
        else:
            # Ubah level log menjadi INFO agar tidak dianggap sebagai error sistem
            logging.info(f"Template spesifik tidak ditemukan dan konten database kosong untuk '{materi_identifier}'. Menggunakan template default.")
            
        return render_template("user/detail_materi.html", materi=materi, **user_data)

    except Exception as e:
        logging.error(f"Error saat mengakses halaman materi '{materi_identifier}': {e}")
        flash("Terjadi kesalahan internal saat memuat halaman materi.", "danger")
        return redirect(url_for('materi.materi_user'))
    finally:
        if conn:
            close_db_connection(conn)
