from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request, jsonify, session
from Back_End.routes.security_for_web import user_required
from Back_End.routes.utils import get_user_data_for_template, log_user_activity
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from jinja2 import TemplateNotFound
import logging
import json

# Blueprint ini didaftarkan dengan url_prefix='/user/materi' di __init__.py
materi_bp = Blueprint('materi', __name__)

# =========================================================================
# 🎓 PREREQUISITE KNOWLEDGE GRAPH (Learning Path Bersyarat ala Bootcamp)
# =========================================================================
PREREQUISITES_MAP = {
    "operasi_kabataku": [],
    "desimal-pecahan-persen": ["operasi_kabataku"],
    "bangun_datar_dan_bangun_ruang": ["operasi_kabataku"],
    "aljabar": ["operasi_kabataku"],
    "eksponensial": ["aljabar"],
    "logaritma": ["eksponensial"],
    "matriks": ["aljabar"],
    "limit": ["aljabar"],
    "fungsi_turunan": ["limit"],
    "integral": ["fungsi_turunan"],
    "statistika": ["operasi_kabataku"],
    "matematika_diskrit": ["aljabar"]
}

TITLES_MAP = {
    "operasi_kabataku": "Operasi Ka-Ba-Ta-Ku & Hierarki",
    "desimal-pecahan-persen": "Pecahan, Desimal, & Persen",
    "bangun_datar_dan_bangun_ruang": "Geometri 2D & 3D",
    "aljabar": "Pengenalan Aljabar & PLSV",
    "eksponensial": "Eksponen & Fungsi Eksponensial",
    "logaritma": "Logaritma & Skala",
    "matriks": "Matriks & Aljabar Linear",
    "limit": "Limit Fungsi Aljabar",
    "fungsi_turunan": "Fungsi Turunan & Diferensial",
    "integral": "Integral & Luas Lengkung",
    "statistika": "Statistika & Analisis Data",
    "matematika_diskrit": "Matematika Diskrit & Logika"
}

def ensure_progress_table(conn):
    """Pastikan tabel granular analytics user_materi_progress ada."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_materi_progress (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                materi_slug VARCHAR(100) NOT NULL,
                checkpoint_stage INT DEFAULT 0,
                is_completed TINYINT(1) DEFAULT 0,
                time_spent_seconds INT DEFAULT 0,
                attempts_count INT DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                UNIQUE KEY uq_user_materi (user_id, materi_slug)
            )
        """)
        conn.commit()
        cursor.close()
    except Exception as e:
        logging.error(f"[DB Progress Check Error]: {e}")

# =========================================================================
# 🔹 API 1: FEEDBACK LOOP BERBASIS AI (Adaptive Micro-Tutor Hint)
# =========================================================================
@materi_bp.route("/api/adaptive-hint", methods=["POST"])
@user_required
def adaptive_hint():
    """
    Menganalisis jenis kesalahan matematika yang dilakukan pengguna pada checkpoint multi-step,
    kemudian memberikan petunjuk scaffolding khusus (tanpa membocorkan jawaban akhir).
    """
    data = request.get_json() or {}
    materi = data.get("materi", "matematika")
    step = data.get("step", 1)
    question = data.get("question", "")
    user_input = data.get("user_input", "")
    expected_concept = data.get("expected_concept", "")

    # Coba gunakan LLMClient yang sudah ada di sistem
    hint_text = ""
    try:
        from Back_End.ai.llm_client import LLMClient
        # Gunakan provider Gemini jika API key tersedia, fallback ke Ollama/Heuristik
        client = LLMClient(provider="gemini")
        prompt = (
            f"Kamu adalah AI Tutor Matematika MathThon yang ramah, ringkas, dan fokus pada metode Socratic/Scaffolding.\n"
            f"Siswa sedang belajar topik: {materi}.\n"
            f"Soal Tahap {step}: {question}.\n"
            f"Konsep yang diharapkan: {expected_concept}.\n"
            f"Jawaban/Input siswa yang keliru: '{user_input}'.\n"
            f"TUGAS: Analisis letak kekeliruan logika siswa dalam maksimal 2-3 kalimat santun dan bahasa Indonesia yang mudah dipahami. "
            f"Jelaskan MENGAPA logika tersebut keliru dan berikan arah petunjuk pemikiran. "
            f"JANGAN PERNAH memberikan jawaban angka akhir secara langsung!"
        )
        response = client.generate(prompt)
        hint_text = response.strip()
    except Exception as e:
        logging.warning(f"[Adaptive AI Hint Fallback]: {e}")
        # Pedagogical heuristic fallback jika API AI sedang limit / offline
        hint_text = generate_heuristic_hint(materi, step, user_input, expected_concept)

    return jsonify({
        "status": "success",
        "hint": hint_text,
        "materi": materi,
        "step": step
    })

def generate_heuristic_hint(materi, step, user_input, expected_concept):
    """Heuristik cerdas bila LLM offline."""
    user_str = str(user_input).lower().strip()
    if "0" in user_str and ("bagi" in expected_concept.lower() or "limit" in materi.lower()):
        return "Kamu mendapatkan bentuk 0/0 karena substitusi langsung. Ingat, 0/0 adalah bentuk tak tentu! Kamu perlu memfaktorkan pembilang terlebih dahulu untuk mencoret pembuat nol sebelum memasukkan nilainya."
    elif "-" in user_str or "+" in user_str:
        return f"Perhatikan tanda positif/negatif pada ekspresimu. Pastikan kamu mematuhi sifat aljabar: selisih dua kuadrat (a² - b²) = (a - b)(a + b)."
    elif step == 1:
        return f"Pada tahap 1, fokuslah pada identifikasi bentuk aljabar dan pemfaktoran dasar. Periksa kembali: {expected_concept}."
    else:
        return f"Hampir tepat! Tinjau kembali langkah perhitungan aljabar pada konsep: {expected_concept}. Hindari terburu-buru menghitung sebelum suku yang sama disederhanakan."

# =========================================================================
# 🔹 API 2: TRACKING PROGRES GRANULAR (Stateful Analytics)
# =========================================================================
@materi_bp.route("/api/track-progress", methods=["POST"])
@user_required
def track_progress():
    """
    Menyimpan metrik mikro per user: stage checkpoint yang diselesaikan,
    waktu yang dihabiskan, dan status kelulusan modul.
    """
    user_id = session.get("user_id")
    data = request.get_json() or {}
    materi_slug = data.get("materi_slug", "").strip().lower()
    checkpoint_stage = int(data.get("checkpoint_stage", 0))
    is_completed = 1 if data.get("is_completed", False) else 0
    time_spent = int(data.get("time_spent", 0))

    if not materi_slug:
        return jsonify({"status": "error", "message": "Slug materi wajib diisi"}), 400

    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)

        # Upsert user_materi_progress
        cursor.execute("""
            INSERT INTO user_materi_progress 
                (user_id, materi_slug, checkpoint_stage, is_completed, time_spent_seconds, attempts_count)
            VALUES (%s, %s, %s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE
                checkpoint_stage = GREATEST(checkpoint_stage, VALUES(checkpoint_stage)),
                is_completed = GREATEST(is_completed, VALUES(is_completed)),
                time_spent_seconds = time_spent_seconds + VALUES(time_spent_seconds),
                attempts_count = attempts_count + 1
        """, (user_id, materi_slug, checkpoint_stage, is_completed, time_spent))
        conn.commit()

        if is_completed:
            log_user_activity(
                current_app._get_current_object(),
                user_id,
                'materi_completed',
                f"Lulus modul materi: {TITLES_MAP.get(materi_slug, materi_slug)}"
            )

        # Cek materi apa saja yang sekarang terbuka (unlocked)
        cursor.execute("SELECT materi_slug FROM user_materi_progress WHERE user_id = %s AND is_completed = 1", (user_id,))
        completed_slugs = set(row['materi_slug'] for row in cursor.fetchall())

        unlocked_list = []
        for slug, reqs in PREREQUISITES_MAP.items():
            if all(r in completed_slugs for r in reqs):
                unlocked_list.append(slug)

        cursor.close()
        return jsonify({
            "status": "success",
            "materi_slug": materi_slug,
            "stage_recorded": checkpoint_stage,
            "is_completed": bool(is_completed),
            "unlocked_materials": unlocked_list
        })
    except Exception as e:
        logging.error(f"[Track Progress API Error]: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)

# =========================================================================
# 🔹 API 3: GET PROGRESS MODUL
# =========================================================================
@materi_bp.route("/api/get-progress/<path:materi_slug>", methods=["GET"])
@user_required
def get_materi_progress(materi_slug):
    """Mengambil status progres terkini untuk materi tertentu."""
    user_id = session.get("user_id")
    slug = materi_slug.strip().lower()
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT checkpoint_stage, is_completed, time_spent_seconds, attempts_count 
            FROM user_materi_progress 
            WHERE user_id = %s AND materi_slug = %s
        """, (user_id, slug))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return jsonify({
                "status": "success",
                "checkpoint_stage": row['checkpoint_stage'],
                "is_completed": bool(row['is_completed']),
                "time_spent_seconds": row['time_spent_seconds'],
                "attempts_count": row['attempts_count']
            })
        else:
            return jsonify({
                "status": "success",
                "checkpoint_stage": 0,
                "is_completed": False,
                "time_spent_seconds": 0,
                "attempts_count": 0
            })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)

# =========================================================================
# 🔹 API 4: LEARNING PATH & PREREQUISITE VALIDATOR
# =========================================================================
@materi_bp.route("/api/learning-path", methods=["GET"])
@user_required
def learning_path():
    """Mengembalikan peta kurikulum bersyarat dan status lock/unlock per modul."""
    user_id = session.get("user_id")
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT materi_slug, checkpoint_stage, is_completed FROM user_materi_progress WHERE user_id = %s", (user_id,))
        progress_dict = {row['materi_slug']: row for row in cursor.fetchall()}
        cursor.close()

        completed_set = set(slug for slug, d in progress_dict.items() if d['is_completed'] == 1)

        result_path = []
        for slug, reqs in PREREQUISITES_MAP.items():
            is_unlocked = all(r in completed_set for r in reqs)
            user_prog = progress_dict.get(slug, {"checkpoint_stage": 0, "is_completed": 0})
            
            missing_reqs = [TITLES_MAP.get(r, r) for r in reqs if r not in completed_set]

            result_path.append({
                "slug": slug,
                "title": TITLES_MAP.get(slug, slug),
                "is_unlocked": is_unlocked,
                "is_completed": bool(user_prog['is_completed']),
                "checkpoint_stage": user_prog['checkpoint_stage'],
                "prerequisites": [TITLES_MAP.get(r, r) for r in reqs],
                "missing_prerequisites": missing_reqs
            })

        return jsonify({
            "status": "success",
            "total_modules": len(PREREQUISITES_MAP),
            "completed_modules": len(completed_set),
            "learning_path": result_path
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)

# =========================================================================
# 🔹 HALAMAN DAFTAR MATERI (materi_user)
# =========================================================================
@materi_bp.route("/")
@user_required
def materi_user():
    user_data = get_user_data_for_template(current_app._get_current_object())
    log_user_activity(current_app._get_current_object(), session.get('user_id'), 'materi', 'Mengakses halaman katalog modul pembelajaran')
    return render_template("user/materi_user.html", **user_data)

# =========================================================================
# 🔹 HALAMAN DETAIL MATERI (materi_detail) DENGAN PREREQUISITE ENFORCEMENT
# =========================================================================
@materi_bp.route("/<path:materi_identifier>")
@user_required
def materi_detail(materi_identifier):
    """
    Menampilkan halaman detail materi secara dinamis dengan pengecekan
    prasyarat kelulusan (conditional learning path).
    """
    user_id = session.get("user_id")
    user_data = get_user_data_for_template(current_app._get_current_object())
    conn = None
    materi = None
    
    clean_identifier = materi_identifier.lower().strip().replace("-", "_")

    # Pengecekan Prasyarat (Prerequisite Check)
    slug_key = materi_identifier.lower().strip()
    if slug_key not in PREREQUISITES_MAP and clean_identifier in PREREQUISITES_MAP:
        slug_key = clean_identifier

    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)

        # Cek apakah modul ini memiliki prasyarat yang belum diselesaikan
        reqs = PREREQUISITES_MAP.get(slug_key, [])
        if reqs:
            cursor.execute("SELECT materi_slug FROM user_materi_progress WHERE user_id = %s AND is_completed = 1", (user_id,))
            completed_slugs = set(row['materi_slug'] for row in cursor.fetchall())
            missing = [TITLES_MAP.get(r, r) for r in reqs if r not in completed_slugs]
            if missing:
                missing_str = ", ".join(missing)
                flash(f"🔒 Modul '{TITLES_MAP.get(slug_key, slug_key)}' masih terkunci! Anda wajib menyelesaikan materi prasyarat: {missing_str} terlebih dahulu.", "warning")
                return redirect(url_for('materi.materi_user'))

        # Cari materi di database
        query = """
            SELECT * FROM daftar_materi 
            WHERE (
                LOWER(REPLACE(judul_materi, ' ', '_')) = %s 
                OR LOWER(REPLACE(judul_materi, ' ', '-')) = %s
            ) 
            AND status = 'active'
        """
        cursor.execute(query, (clean_identifier, materi_identifier))
        materi = cursor.fetchone()

        log_user_activity(current_app._get_current_object(), user_id, 'materi', f"Mempelajari materi: {TITLES_MAP.get(slug_key, materi_identifier)}")

        # Logika Penentuan Nama Template
        possible_templates = [
            f"user/materi/{materi_identifier}.html",
            f"user/materi/{clean_identifier}.html"
        ]

        for template_path in possible_templates:
            try:
                return render_template(template_path, materi=materi, slug_key=slug_key, **user_data)
            except TemplateNotFound:
                continue
        
        return render_template("user/detail_materi.html", materi=materi, slug_key=slug_key, **user_data)

    except Exception as e:
        logging.error(f"Error saat mengakses halaman materi '{materi_identifier}': {e}")
        flash("Terjadi kesalahan saat memuat halaman materi.", "danger")
        return redirect(url_for('materi.materi_user'))
    finally:
        if conn:
            close_db_connection(conn)
