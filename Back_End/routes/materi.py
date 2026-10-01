from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request, jsonify, session
from Back_End.routes.security_for_web import user_required
from Back_End.routes.utils import get_user_data_for_template, log_user_activity
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from jinja2 import TemplateNotFound
import logging
import json

# Blueprint didaftarkan dengan url_prefix='/user/materi' di __init__.py
materi_bp = Blueprint('materi', __name__)

# =========================================================================
# 🎓 PREREQUISITE KNOWLEDGE GRAPH (Learning Path Bersyarat)
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
    "matematika_diskrit": ["aljabar"],
    "vektor": ["matriks"],
    "probabilitas": ["statistika"],
    "persamaan_linear": ["aljabar"],
    "sistem_bilangan": ["operasi_kabataku"],
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
    "matematika_diskrit": "Matematika Diskrit & Logika",
    "vektor": "Vektor & Geometri Ruang",
    "probabilitas": "Probabilitas & Kombinatorik",
    "persamaan_linear": "Sistem Persamaan Linear (SPLDV & SPLTV)",
    "sistem_bilangan": "Sistem Bilangan (Biner, Oktal, Heksadesimal)",
}

# =========================================================================
# 📚 SUBJECT REGISTRY — Metadata per materi untuk routing per-bab
# =========================================================================
SUBJECT_REGISTRY = {
    "aljabar": {
        "title": "Pengenalan Aljabar & PLSV", "short": "Aljabar",
        "icon": "bi-calculator", "color": "#6366f1", "total_bab": 5,
        "folder": "aljabar", "slug_key": "aljabar",
        "bab_titles": [
            "Latar Belakang & Variabel",
            "Anatomi Bentuk Aljabar",
            "Operasi Aljabar & Sandbox Interaktif",
            "Persamaan Linear Satu Variabel (PLSV)",
            "Capstone Checkpoint"
        ]
    },
    "integral": {
        "title": "Integral & Kalkulus Integral", "short": "Integral",
        "icon": "bi-infinity", "color": "#10b981", "total_bab": 5,
        "folder": "integral", "slug_key": "integral",
        "bab_titles": [
            "Konsep Akumulasi & Luas Lengkung",
            "Antiturunan & Konstanta C",
            "Aturan Integral Dasar & Sandbox",
            "Integral Tertentu & Aplikasi Nyata",
            "Capstone Checkpoint"
        ]
    },
    "limit": {
        "title": "Limit Fungsi Aljabar", "short": "Limit",
        "icon": "bi-arrow-right-short", "color": "#f59e0b", "total_bab": 5,
        "folder": "limit", "slug_key": "limit",
        "bab_titles": [
            "Konsep Mendekati (Approaching)",
            "Limit Substitusi Langsung",
            "Bentuk Tak Tentu & Pemfaktoran",
            "Limit di Tak Hingga",
            "Capstone Checkpoint"
        ]
    },
    "fungsi_turunan": {
        "title": "Fungsi Turunan & Diferensial", "short": "Turunan",
        "icon": "bi-graph-up", "color": "#ef4444", "total_bab": 5,
        "folder": "fungsi_turunan", "slug_key": "fungsi_turunan",
        "bab_titles": [
            "Konsep Laju Perubahan",
            "Definisi Limit Turunan",
            "Aturan Diferensiasi & Sandbox",
            "Aplikasi Turunan: Maksimum & Minimum",
            "Capstone Checkpoint"
        ]
    },
    "eksponensial": {
        "title": "Eksponen & Fungsi Eksponensial", "short": "Eksponen",
        "icon": "bi-arrow-up-right-circle", "color": "#f97316", "total_bab": 5,
        "folder": "eksponensial", "slug_key": "eksponensial",
        "bab_titles": [
            "Bilangan Berpangkat & Notasi",
            "Sifat-sifat Eksponen",
            "Fungsi Eksponensial & Grafik",
            "Pertumbuhan & Peluruhan Eksponensial",
            "Capstone Checkpoint"
        ]
    },
    "logaritma": {
        "title": "Logaritma & Aplikasinya", "short": "Logaritma",
        "icon": "bi-reception-4", "color": "#8b5cf6", "total_bab": 5,
        "folder": "logaritma", "slug_key": "logaritma",
        "bab_titles": [
            "Logaritma sebagai Invers Eksponen",
            "Sifat-sifat Logaritma",
            "Persamaan & Pertidaksamaan Logaritma",
            "Aplikasi: pH, Desibel & Skala Richter",
            "Capstone Checkpoint"
        ]
    },
    "matriks": {
        "title": "Matriks & Aljabar Linear", "short": "Matriks",
        "icon": "bi-grid-3x3", "color": "#06b6d4", "total_bab": 5,
        "folder": "matriks", "slug_key": "matriks",
        "bab_titles": [
            "Pengenalan Matriks & Notasi",
            "Operasi Dasar Matriks",
            "Perkalian Matriks",
            "Determinan & Matriks Invers",
            "Capstone Checkpoint"
        ]
    },
    "statistika": {
        "title": "Statistika & Analisis Data", "short": "Statistika",
        "icon": "bi-bar-chart-fill", "color": "#ec4899", "total_bab": 5,
        "folder": "statistika", "slug_key": "statistika",
        "bab_titles": [
            "Pengumpulan & Jenis Data",
            "Ukuran Pemusatan Data",
            "Ukuran Penyebaran Data",
            "Distribusi Frekuensi & Histogram",
            "Capstone Checkpoint"
        ]
    },
    "probabilitas": {
        "title": "Probabilitas & Kombinatorik", "short": "Probabilitas",
        "icon": "bi-dice-5", "color": "#14b8a6", "total_bab": 5,
        "folder": "probabilitas", "slug_key": "probabilitas",
        "bab_titles": [
            "Ruang Sampel & Kejadian",
            "Peluang Klasik & Frekuensi Relatif",
            "Kaidah Pencacahan: Permutasi & Kombinasi",
            "Peluang Bersyarat & Teorema Bayes",
            "Capstone Checkpoint"
        ]
    },
    "vektor": {
        "title": "Vektor & Geometri Ruang", "short": "Vektor",
        "icon": "bi-arrows-move", "color": "#3b82f6", "total_bab": 5,
        "folder": "vektor", "slug_key": "vektor",
        "bab_titles": [
            "Besaran Skalar vs Vektor",
            "Operasi Vektor Dasar",
            "Perkalian Titik & Perkalian Silang",
            "Aplikasi Vektor dalam Fisika & Geometri",
            "Capstone Checkpoint"
        ]
    },
    "bangun_datar_dan_bangun_ruang": {
        "title": "Geometri: Bangun Datar & Ruang", "short": "Geometri",
        "icon": "bi-pentagon", "color": "#a855f7", "total_bab": 5,
        "folder": "bangun_datar_dan_bangun_ruang", "slug_key": "bangun_datar_dan_bangun_ruang",
        "bab_titles": [
            "Geometri Dasar: Titik, Garis & Sudut",
            "Bangun Datar & Formula Luas",
            "Bangun Ruang & Formula Volume",
            "Teorema Pythagoras & Aplikasi 3D",
            "Capstone Checkpoint"
        ]
    },
    "desimal": {
        "title": "Pecahan, Desimal & Persen", "short": "Desimal",
        "icon": "bi-percent", "color": "#84cc16", "total_bab": 5,
        "folder": "desimal", "slug_key": "desimal-pecahan-persen",
        "bab_titles": [
            "Sistem Bilangan Rasional",
            "Operasi Pecahan",
            "Desimal & Konversi",
            "Persen & Aplikasi Sehari-hari",
            "Capstone Checkpoint"
        ]
    },
    "operasi_kabataku": {
        "title": "Operasi Ka-Ba-Ta-Ku & Hierarki", "short": "Ka-Ba-Ta-Ku",
        "icon": "bi-plus-slash-minus", "color": "#64748b", "total_bab": 5,
        "folder": "operasi_kabataku", "slug_key": "operasi_kabataku",
        "bab_titles": [
            "Hierarki Operasi Matematika (BODMAS)",
            "Penjumlahan & Pengurangan Bilangan Bulat",
            "Perkalian & Pembagian",
            "Operasi Campuran & Strategi Cepat",
            "Capstone Checkpoint"
        ]
    },
    "matematika_diskrit": {
        "title": "Matematika Diskrit & Logika", "short": "Mat. Diskrit",
        "icon": "bi-diagram-3", "color": "#475569", "total_bab": 5,
        "folder": "matematika_diskrit", "slug_key": "matematika_diskrit",
        "bab_titles": [
            "Logika Proposisional",
            "Teori Himpunan",
            "Relasi & Fungsi",
            "Graf & Pohon (Tree)",
            "Capstone Checkpoint"
        ]
    },
    "persamaan_linear": {
        "title": "Sistem Persamaan Linear (SPLDV & SPLTV)", "short": "SPLDV/SPLTV",
        "icon": "bi-braces-asterisk", "color": "#d97706", "total_bab": 5,
        "folder": "persamaan_linear", "slug_key": "persamaan_linear",
        "bab_titles": [
            "Konsep Sistem Persamaan Linear",
            "SPLDV: Metode Substitusi",
            "SPLDV: Metode Eliminasi & Gabungan",
            "SPLTV: Tiga Variabel",
            "Capstone Checkpoint"
        ]
    },
    "sistem_bilangan": {
        "title": "Sistem Bilangan (Biner, Oktal, Hex)", "short": "Sistem Bilangan",
        "icon": "bi-cpu", "color": "#334155", "total_bab": 5,
        "folder": "sistem_bilangan", "slug_key": "sistem_bilangan",
        "bab_titles": [
            "Sistem Bilangan Desimal (Basis 10)",
            "Sistem Bilangan Biner (Basis 2)",
            "Sistem Bilangan Oktal (Basis 8)",
            "Sistem Bilangan Heksadesimal (Basis 16)",
            "Konversi Antar Sistem Bilangan"
        ]
    },
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
    """Memberikan petunjuk scaffolding berbasis AI tanpa membocorkan jawaban."""
    data = request.get_json() or {}
    materi = data.get("materi", "matematika")
    step = data.get("step", 1)
    question = data.get("question", "")
    user_input = data.get("user_input", "")
    expected_concept = data.get("expected_concept", "")

    hint_text = ""
    try:
        from Back_End.ai.llm_client import LLMClient
        client = LLMClient(provider="gemini")
        prompt = (
            f"Kamu adalah AI Tutor Matematika MathThon yang ramah, ringkas, dan fokus pada metode Socratic/Scaffolding.\n"
            f"Siswa sedang belajar topik: {materi}.\n"
            f"Soal Tahap {step}: {question}.\n"
            f"Konsep yang diharapkan: {expected_concept}.\n"
            f"Jawaban/Input siswa yang keliru: '{user_input}'.\n"
            f"TUGAS: Analisis letak kekeliruan logika siswa dalam maksimal 2-3 kalimat santun dalam bahasa Indonesia. "
            f"Jelaskan MENGAPA keliru dan berikan arah petunjuk. "
            f"JANGAN memberikan jawaban angka akhir secara langsung!"
        )
        response = client.generate(prompt)
        hint_text = response.strip()
    except Exception as e:
        logging.warning(f"[Adaptive AI Hint Fallback]: {e}")
        hint_text = generate_heuristic_hint(materi, step, user_input, expected_concept)

    return jsonify({"status": "success", "hint": hint_text, "materi": materi, "step": step})


def generate_heuristic_hint(materi, step, user_input, expected_concept):
    """Heuristik cerdas bila LLM offline."""
    user_str = str(user_input).lower().strip()
    if "0" in user_str and ("bagi" in expected_concept.lower() or "limit" in materi.lower()):
        return "Kamu mendapatkan bentuk 0/0 karena substitusi langsung. Ingat, 0/0 adalah bentuk tak tentu! Kamu perlu memfaktorkan terlebih dahulu."
    elif "-" in user_str or "+" in user_str:
        return "Perhatikan tanda positif/negatif. Ingat sifat aljabar: (a - b)² ≠ a² - b²."
    elif step == 1:
        return f"Fokuslah pada identifikasi bentuk aljabar dan pemfaktoran dasar: {expected_concept}."
    else:
        return f"Hampir tepat! Tinjau kembali konsep: {expected_concept}."


# =========================================================================
# 🔹 API 2: TRACKING PROGRES GRANULAR (Stateful Analytics)
# =========================================================================
@materi_bp.route("/api/track-progress", methods=["POST"])
@user_required
def track_progress():
    """Menyimpan metrik mikro per user per modul."""
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
                current_app._get_current_object(), user_id, 'materi_completed',
                f"Lulus modul: {TITLES_MAP.get(materi_slug, materi_slug)}"
            )

        cursor.execute(
            "SELECT materi_slug FROM user_materi_progress WHERE user_id = %s AND is_completed = 1", (user_id,)
        )
        completed_slugs = set(row['materi_slug'] for row in cursor.fetchall())
        unlocked_list = [s for s, reqs in PREREQUISITES_MAP.items() if all(r in completed_slugs for r in reqs)]
        cursor.close()

        return jsonify({
            "status": "success", "materi_slug": materi_slug,
            "stage_recorded": checkpoint_stage, "is_completed": bool(is_completed),
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
        cursor.execute(
            "SELECT checkpoint_stage, is_completed, time_spent_seconds, attempts_count FROM user_materi_progress WHERE user_id = %s AND materi_slug = %s",
            (user_id, slug)
        )
        row = cursor.fetchone()
        cursor.close()
        if row:
            return jsonify({"status": "success", "checkpoint_stage": row['checkpoint_stage'],
                            "is_completed": bool(row['is_completed']), "time_spent_seconds": row['time_spent_seconds'],
                            "attempts_count": row['attempts_count']})
        return jsonify({"status": "success", "checkpoint_stage": 0, "is_completed": False,
                        "time_spent_seconds": 0, "attempts_count": 0})
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
        cursor.execute(
            "SELECT materi_slug, checkpoint_stage, is_completed FROM user_materi_progress WHERE user_id = %s", (user_id,)
        )
        progress_dict = {row['materi_slug']: row for row in cursor.fetchall()}
        cursor.close()

        completed_set = {slug for slug, d in progress_dict.items() if d['is_completed'] == 1}
        result_path = []
        for slug, reqs in PREREQUISITES_MAP.items():
            is_unlocked = all(r in completed_set for r in reqs)
            user_prog = progress_dict.get(slug, {"checkpoint_stage": 0, "is_completed": 0})
            result_path.append({
                "slug": slug, "title": TITLES_MAP.get(slug, slug),
                "is_unlocked": is_unlocked, "is_completed": bool(user_prog['is_completed']),
                "checkpoint_stage": user_prog['checkpoint_stage'],
                "prerequisites": [TITLES_MAP.get(r, r) for r in reqs],
                "missing_prerequisites": [TITLES_MAP.get(r, r) for r in reqs if r not in completed_set]
            })

        return jsonify({
            "status": "success", "total_modules": len(PREREQUISITES_MAP),
            "completed_modules": len(completed_set), "learning_path": result_path
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)


# =========================================================================
# 🔹 API 5: PER-BAB PROGRESS (baru — untuk sistem bab terpisah)
# =========================================================================
@materi_bp.route("/api/bab-progress", methods=["POST"])
@user_required
def bab_progress():
    """Track progress per bab (slug format: aljabar_bab_1, integral_bab_3, dst.)"""
    user_id = session.get("user_id")
    data = request.get_json() or {}
    subject = data.get("subject", "").strip().lower()
    bab_num = int(data.get("bab_num", 1))
    is_completed = 1 if data.get("is_completed", False) else 0
    time_spent = int(data.get("time_spent", 0))
    exercise_score = int(data.get("exercise_score", 0))

    if not subject:
        return jsonify({"status": "error", "message": "subject wajib diisi"}), 400

    slug = f"{subject}_bab_{bab_num}"
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            INSERT INTO user_materi_progress 
                (user_id, materi_slug, checkpoint_stage, is_completed, time_spent_seconds, attempts_count)
            VALUES (%s, %s, %s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE
                checkpoint_stage = GREATEST(checkpoint_stage, VALUES(checkpoint_stage)),
                is_completed = GREATEST(is_completed, VALUES(is_completed)),
                time_spent_seconds = time_spent_seconds + VALUES(time_spent_seconds),
                attempts_count = attempts_count + 1
        """, (user_id, slug, exercise_score, is_completed, time_spent))
        conn.commit()

        subj_data = SUBJECT_REGISTRY.get(subject, {})
        total_bab = subj_data.get("total_bab", 5)
        completed_babs = 0
        for i in range(1, total_bab + 1):
            b_slug = f"{subject}_bab_{i}"
            cursor.execute(
                "SELECT is_completed FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
                (user_id, b_slug)
            )
            b_row = cursor.fetchone()
            if b_row and b_row['is_completed']:
                completed_babs += 1

        subject_completed = (completed_babs == total_bab)
        if subject_completed:
            slug_key = subj_data.get("slug_key", subject)
            cursor.execute("""
                INSERT INTO user_materi_progress 
                    (user_id, materi_slug, checkpoint_stage, is_completed, time_spent_seconds, attempts_count)
                VALUES (%s, %s, 5, 1, 0, 0)
                ON DUPLICATE KEY UPDATE is_completed=1, checkpoint_stage=5
            """, (user_id, slug_key))
            conn.commit()

        cursor.close()
        return jsonify({
            "status": "success", "slug": slug, "bab_completed": bool(is_completed),
            "subject_completed": subject_completed,
            "completed_babs": completed_babs, "total_bab": total_bab
        })
    except Exception as e:
        logging.error(f"[Bab Progress API Error]: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)


# =========================================================================
# 🔹 API 6: GET ALL BAB PROGRESS untuk suatu subject
# =========================================================================
@materi_bp.route("/api/subject-progress/<subject>", methods=["GET"])
@user_required
def subject_progress(subject):
    """Ambil status progress semua bab dalam satu subject."""
    user_id = session.get("user_id")
    subj_data = SUBJECT_REGISTRY.get(subject)
    if not subj_data:
        return jsonify({"status": "error", "message": "Subject tidak ditemukan"}), 404

    total_bab = subj_data.get("total_bab", 5)
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)

        bab_list = []
        for i in range(1, total_bab + 1):
            b_slug = f"{subject}_bab_{i}"
            cursor.execute(
                "SELECT checkpoint_stage, is_completed, time_spent_seconds FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
                (user_id, b_slug)
            )
            row = cursor.fetchone()
            bab_list.append({
                "bab_num": i, "title": subj_data["bab_titles"][i - 1], "slug": b_slug,
                "is_completed": bool(row['is_completed']) if row else False,
                "checkpoint_stage": row['checkpoint_stage'] if row else 0,
                "time_spent": row['time_spent_seconds'] if row else 0,
            })

        cursor.close()
        return jsonify({
            "status": "success", "subject": subject, "title": subj_data["title"],
            "total_bab": total_bab, "bab_progress": bab_list
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)


# =========================================================================
# 🔹 HALAMAN DAFTAR MATERI (materi_user) — Katalog
# =========================================================================
@materi_bp.route("/")
@user_required
def materi_user():
    user_data = get_user_data_for_template(current_app._get_current_object())
    log_user_activity(current_app._get_current_object(), session.get('user_id'), 'materi',
                      'Mengakses halaman katalog modul pembelajaran')
    return render_template("user/materi_user.html", **user_data)


# =========================================================================
# 🔄 ALIAS RESOLVER — Menjamin semua variasi slug URL terpetakan dengan tepat
# =========================================================================
SUBJECT_ALIASES = {
    "operasi_kabataku": "operasi_kabataku",
    "operasi-kabataku": "operasi_kabataku",
    "operasi-ka-ba-ta-ku": "operasi_kabataku",
    "operasi_ka_ba_ta_ku": "operasi_kabataku",
    "operasi_kabataku_hierarki": "operasi_kabataku",
    "operasi-kabataku-hierarki": "operasi_kabataku",
    "operasi_ka_ba_ta_ku_&_hierarki": "operasi_kabataku",
    "operasi-ka-ba-ta-ku-&-hierarki": "operasi_kabataku",
    "operasi_ka_ba_ta_ku___hierarki": "operasi_kabataku",
    "operasi-ka-ba-ta-ku---hierarki": "operasi_kabataku",
    "desimal_pecahan_persen": "desimal",
    "desimal-pecahan-persen": "desimal",
    "pecahan_desimal_persen": "desimal",
    "pecahan-desimal-persen": "desimal",
    "desimal": "desimal",
    "bangun_datar_dan_bangun_ruang": "bangun_datar_dan_bangun_ruang",
    "bangun-datar-dan-bangun-ruang": "bangun_datar_dan_bangun_ruang",
    "geometri": "bangun_datar_dan_bangun_ruang",
    "aljabar": "aljabar",
    "pengenalan_aljabar": "aljabar",
    "pengenalan-aljabar": "aljabar",
    "eksponensial": "eksponensial",
    "eksponen": "eksponensial",
    "logaritma": "logaritma",
    "matriks": "matriks",
    "limit": "limit",
    "limit_fungsi_aljabar": "limit",
    "limit-fungsi-aljabar": "limit",
    "fungsi_turunan": "fungsi_turunan",
    "fungsi-turunan": "fungsi_turunan",
    "turunan": "fungsi_turunan",
    "integral": "integral",
    "statistika": "statistika",
    "matematika_diskrit": "matematika_diskrit",
    "matematika-diskrit": "matematika_diskrit",
    "diskrit": "matematika_diskrit",
    "vektor": "vektor",
    "probabilitas": "probabilitas",
    "persamaan_linear": "persamaan_linear",
    "persamaan-linear": "persamaan_linear",
    "spldv": "persamaan_linear",
    "spltv": "persamaan_linear",
    "spldv_spltv": "persamaan_linear",
    "sistem_bilangan": "sistem_bilangan",
    "sistem-bilangan": "sistem_bilangan",
}

def resolve_subject_key(raw_key):
    """Normalisasi sembarang format slug atau judul materi menjadi key resmi di SUBJECT_REGISTRY."""
    if not raw_key:
        return None
    raw = str(raw_key).lower().strip().replace(" ", "_")
    if raw in SUBJECT_REGISTRY:
        return raw
    if raw in SUBJECT_ALIASES:
        return SUBJECT_ALIASES[raw]
    
    # Bersihkan tanda hubung dan karakter khusus
    cleaned = raw.replace("-", "_").replace("&", "_").replace("__", "_").strip("_")
    if cleaned in SUBJECT_REGISTRY:
        return cleaned
    if cleaned in SUBJECT_ALIASES:
        return SUBJECT_ALIASES[cleaned]

    for k, v in SUBJECT_ALIASES.items():
        if k in cleaned or cleaned in k:
            return v
    
    first_part = cleaned.split("_")[0]
    if first_part in SUBJECT_REGISTRY:
        return first_part
    return None


# =========================================================================
# 🔹 HALAMAN OVERVIEW SUBJECT
# Route: /user/materi/<subject>/
# =========================================================================
@materi_bp.route("/<subject>")
@materi_bp.route("/<subject>/")
@materi_bp.route("/<subject>/index")
@user_required
def subject_index(subject):
    """Halaman overview subject — daftar semua bab."""
    resolved_subject = resolve_subject_key(subject)
    if not resolved_subject:
        flash(f"Materi '{subject}' tidak ditemukan.", "warning")
        return redirect(url_for('materi.materi_user'))
    
    if resolved_subject != subject:
        return redirect(url_for('materi.subject_index', subject=resolved_subject))

    subj_data = SUBJECT_REGISTRY[resolved_subject]
    user_id = session.get("user_id")
    user_data = get_user_data_for_template(current_app._get_current_object())

    bab_progress = []
    conn = None
    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)
        for i in range(1, subj_data['total_bab'] + 1):
            b_slug = f"{resolved_subject}_bab_{i}"
            cursor.execute(
                "SELECT is_completed, checkpoint_stage FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
                (user_id, b_slug)
            )
            row = cursor.fetchone()
            bab_progress.append({
                "num": i, "title": subj_data["bab_titles"][i - 1], "slug": b_slug,
                "is_completed": bool(row['is_completed']) if row else False,
                "is_unlocked": i == 1 or (row is not None),
                "score": row['checkpoint_stage'] if row else 0,
                "url": url_for('materi.subject_bab', subject=resolved_subject, bab_num=i)
            })
        cursor.close()
    except Exception as e:
        logging.error(f"[Subject Index Progress Error]: {e}")
    finally:
        if conn:
            close_db_connection(conn)

    log_user_activity(current_app._get_current_object(), user_id, 'materi',
                      f"Membuka overview: {subj_data['title']}")

    template_path = f"user/materi/{subj_data['folder']}/index.html"
    try:
        return render_template(template_path, subject=resolved_subject, subject_data=subj_data,
                               bab_progress=bab_progress, **user_data)
    except TemplateNotFound:
        return redirect(url_for('materi.subject_bab', subject=resolved_subject, bab_num=1))


# =========================================================================
# 🔹 HALAMAN BAB SPESIFIK
# Route: /user/materi/<subject>/bab/<bab_num>
# =========================================================================
@materi_bp.route("/<subject>/bab/<int:bab_num>")
@user_required
def subject_bab(subject, bab_num):
    """Tampilkan halaman bab spesifik dengan tracking progress."""
    resolved_subject = resolve_subject_key(subject)
    if not resolved_subject:
        flash(f"Materi '{subject}' tidak ditemukan.", "warning")
        return redirect(url_for('materi.materi_user'))

    if resolved_subject != subject:
        return redirect(url_for('materi.subject_bab', subject=resolved_subject, bab_num=bab_num))

    subj_data = SUBJECT_REGISTRY[resolved_subject]
    total_bab = subj_data.get("total_bab", 5)
    if bab_num < 1 or bab_num > total_bab:
        flash(f"Bab {bab_num} tidak tersedia.", "warning")
        return redirect(url_for('materi.subject_index', subject=resolved_subject))

    user_id = session.get("user_id")
    user_data = get_user_data_for_template(current_app._get_current_object())

    slug_key = subj_data.get("slug_key", resolved_subject)
    conn = None
    progress = {"checkpoint_stage": 0, "is_completed": False, "time_spent": 0}
    all_bab_status = []

    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)

        # Prerequisite check (subject level, hanya untuk bab 1)
        reqs = PREREQUISITES_MAP.get(slug_key, [])
        if reqs and bab_num == 1:
            cursor.execute(
                "SELECT materi_slug FROM user_materi_progress WHERE user_id=%s AND is_completed=1", (user_id,)
            )
            completed_slugs = {row['materi_slug'] for row in cursor.fetchall()}
            missing = [TITLES_MAP.get(r, r) for r in reqs if r not in completed_slugs]
            if missing:
                flash(f"🔒 '{subj_data['title']}' terkunci! Selesaikan dulu: {', '.join(missing)}.", "warning")
                return redirect(url_for('materi.materi_user'))

        # Progress bab saat ini
        bab_slug = f"{resolved_subject}_bab_{bab_num}"
        cursor.execute(
            "SELECT checkpoint_stage, is_completed, time_spent_seconds FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
            (user_id, bab_slug)
        )
        row = cursor.fetchone()
        if row:
            progress = {"checkpoint_stage": row['checkpoint_stage'],
                        "is_completed": bool(row['is_completed']),
                        "time_spent": row['time_spent_seconds']}

        # Status semua bab untuk sidebar
        for i in range(1, total_bab + 1):
            b_slug = f"{resolved_subject}_bab_{i}"
            cursor.execute(
                "SELECT is_completed FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
                (user_id, b_slug)
            )
            b_row = cursor.fetchone()
            all_bab_status.append({
                "num": i, "title": subj_data["bab_titles"][i - 1],
                "is_completed": bool(b_row['is_completed']) if b_row else False,
                "is_current": i == bab_num,
                "url": url_for('materi.subject_bab', subject=resolved_subject, bab_num=i)
            })

        cursor.close()
    except Exception as e:
        logging.error(f"[Subject Bab Error]: {e}")
    finally:
        if conn:
            close_db_connection(conn)

    log_user_activity(current_app._get_current_object(), user_id, 'materi',
                      f"{subj_data['short']} — Bab {bab_num}: {subj_data['bab_titles'][bab_num - 1]}")

    prev_url = (url_for('materi.subject_bab', subject=resolved_subject, bab_num=bab_num - 1)
                if bab_num > 1 else url_for('materi.subject_index', subject=resolved_subject))
    next_url = (url_for('materi.subject_bab', subject=resolved_subject, bab_num=bab_num + 1)
                if bab_num < total_bab else url_for('materi.subject_index', subject=resolved_subject))

    template_path = f"user/materi/{subj_data['folder']}/bab_{bab_num}.html"
    try:
        return render_template(
            template_path,
            subject=resolved_subject, bab_num=bab_num,
            bab_slug=f"{resolved_subject}_bab_{bab_num}",
            subject_data=subj_data, progress=progress,
            all_bab_status=all_bab_status,
            prev_url=prev_url, next_url=next_url,
            **user_data
        )
    except TemplateNotFound:
        logging.warning(f"[TemplateNotFound] {template_path}")
        flash(f"Bab {bab_num} sedang dalam pengembangan. Jalankan: python generate_materi.py", "info")
        return redirect(url_for('materi.subject_index', subject=resolved_subject))

    user_id = session.get("user_id")
    user_data = get_user_data_for_template(current_app._get_current_object())

    slug_key = subj_data.get("slug_key", subject)
    conn = None
    progress = {"checkpoint_stage": 0, "is_completed": False, "time_spent": 0}
    all_bab_status = []

    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)

        # Prerequisite check (subject level, hanya untuk bab 1)
        reqs = PREREQUISITES_MAP.get(slug_key, [])
        if reqs and bab_num == 1:
            cursor.execute(
                "SELECT materi_slug FROM user_materi_progress WHERE user_id=%s AND is_completed=1", (user_id,)
            )
            completed_slugs = {row['materi_slug'] for row in cursor.fetchall()}
            missing = [TITLES_MAP.get(r, r) for r in reqs if r not in completed_slugs]
            if missing:
                flash(f"🔒 '{subj_data['title']}' terkunci! Selesaikan dulu: {', '.join(missing)}.", "warning")
                return redirect(url_for('materi.materi_user'))

        # Progress bab saat ini
        bab_slug = f"{subject}_bab_{bab_num}"
        cursor.execute(
            "SELECT checkpoint_stage, is_completed, time_spent_seconds FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
            (user_id, bab_slug)
        )
        row = cursor.fetchone()
        if row:
            progress = {"checkpoint_stage": row['checkpoint_stage'],
                        "is_completed": bool(row['is_completed']),
                        "time_spent": row['time_spent_seconds']}

        # Status semua bab untuk sidebar
        for i in range(1, total_bab + 1):
            b_slug = f"{subject}_bab_{i}"
            cursor.execute(
                "SELECT is_completed FROM user_materi_progress WHERE user_id=%s AND materi_slug=%s",
                (user_id, b_slug)
            )
            b_row = cursor.fetchone()
            all_bab_status.append({
                "num": i, "title": subj_data["bab_titles"][i - 1],
                "is_completed": bool(b_row['is_completed']) if b_row else False,
                "is_current": i == bab_num,
                "url": url_for('materi.subject_bab', subject=subject, bab_num=i)
            })

        cursor.close()
    except Exception as e:
        logging.error(f"[Subject Bab Error]: {e}")
    finally:
        if conn:
            close_db_connection(conn)

    log_user_activity(current_app._get_current_object(), user_id, 'materi',
                      f"{subj_data['short']} — Bab {bab_num}: {subj_data['bab_titles'][bab_num - 1]}")

    prev_url = (url_for('materi.subject_bab', subject=subject, bab_num=bab_num - 1)
                if bab_num > 1 else url_for('materi.subject_index', subject=subject))
    next_url = (url_for('materi.subject_bab', subject=subject, bab_num=bab_num + 1)
                if bab_num < total_bab else url_for('materi.materi_user'))

    template_path = f"user/materi/{subj_data['folder']}/bab_{bab_num}.html"
    try:
        return render_template(
            template_path,
            subject=subject, bab_num=bab_num,
            bab_slug=f"{subject}_bab_{bab_num}",
            subject_data=subj_data, progress=progress,
            all_bab_status=all_bab_status,
            prev_url=prev_url, next_url=next_url,
            **user_data
        )
    except TemplateNotFound:
        logging.warning(f"[TemplateNotFound] {template_path}")
        flash(f"Bab {bab_num} sedang dalam pengembangan. Jalankan: python generate_materi.py", "info")
        return redirect(url_for('materi.subject_index', subject=subject))


# =========================================================================
# 🔹 FALLBACK — URL monolitik lama (backward compatibility)
# Route: /user/materi/<path:materi_identifier>
# =========================================================================
@materi_bp.route("/<path:materi_identifier>")
@user_required
def materi_detail(materi_identifier):
    """Fallback untuk URL lama. Redirect ke sistem bab jika subject dikenali."""
    # Cek apakah prefix-nya adalah subject di SUBJECT_REGISTRY (termasuk alias slug lama)
    first_segment = materi_identifier.strip("/").split("/")[0].lower().replace("-", "_")
    ALIAS_MAP = {
        "desimal_pecahan_persen": "desimal",
        "desimal-pecahan-persen": "desimal",
        "bangun-datar-dan-bangun-ruang": "bangun_datar_dan_bangun_ruang",
        "operasi-kabataku": "operasi_kabataku",
        "matematika-diskrit": "matematika_diskrit",
        "persamaan-linear": "persamaan_linear",
        "sistem-bilangan": "sistem_bilangan",
        "fungsi-turunan": "fungsi_turunan",
    }
    target_subj = ALIAS_MAP.get(materi_identifier.strip("/").lower(), ALIAS_MAP.get(first_segment, first_segment))
    if target_subj in SUBJECT_REGISTRY:
        return redirect(url_for('materi.subject_index', subject=target_subj))

    user_id = session.get("user_id")
    user_data = get_user_data_for_template(current_app._get_current_object())
    conn = None
    materi = None

    clean_identifier = materi_identifier.lower().strip().replace("-", "_")
    slug_key = materi_identifier.lower().strip()
    if slug_key not in PREREQUISITES_MAP and clean_identifier in PREREQUISITES_MAP:
        slug_key = clean_identifier

    try:
        conn = get_db_connection(current_app._get_current_object())
        ensure_progress_table(conn)
        cursor = conn.cursor(dictionary=True)

        reqs = PREREQUISITES_MAP.get(slug_key, [])
        if reqs:
            cursor.execute(
                "SELECT materi_slug FROM user_materi_progress WHERE user_id = %s AND is_completed = 1", (user_id,)
            )
            completed_slugs = {row['materi_slug'] for row in cursor.fetchall()}
            missing = [TITLES_MAP.get(r, r) for r in reqs if r not in completed_slugs]
            if missing:
                flash(f"🔒 '{TITLES_MAP.get(slug_key, slug_key)}' terkunci! Selesaikan: {', '.join(missing)}.", "warning")
                return redirect(url_for('materi.materi_user'))

        cursor.execute("""
            SELECT * FROM daftar_materi 
            WHERE (LOWER(REPLACE(judul_materi, ' ', '_')) = %s 
                   OR LOWER(REPLACE(judul_materi, ' ', '-')) = %s) 
            AND status = 'active'
        """, (clean_identifier, materi_identifier))
        materi = cursor.fetchone()
        log_user_activity(current_app._get_current_object(), user_id, 'materi',
                          f"Mempelajari: {TITLES_MAP.get(slug_key, materi_identifier)}")

        for tpl in [f"user/materi/{materi_identifier}.html", f"user/materi/{clean_identifier}.html"]:
            try:
                return render_template(tpl, materi=materi, slug_key=slug_key, **user_data)
            except TemplateNotFound:
                continue

        return render_template("user/detail_materi.html", materi=materi, slug_key=slug_key, **user_data)

    except Exception as e:
        logging.error(f"Error mengakses materi '{materi_identifier}': {e}")
        flash("Terjadi kesalahan saat memuat halaman materi.", "danger")
        return redirect(url_for('materi.materi_user'))
    finally:
        if conn:
            close_db_connection(conn)
