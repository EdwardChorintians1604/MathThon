import mysql.connector
from Back_End.config import Config

def seed_curriculum():
    conn = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
    cursor = conn.cursor()

    print("[SEED] Seeding Courses, Modules, and Materials...")

    # Data Course & Modules
    curriculum = [
        {
            "course": {
                "title": "Fondasi Aritmatika & Aljabar",
                "slug": "fondasi-aljabar",
                "description": "Kuasai fondasi berpikir kuantitatif, kaidah hierarki operasi KaBaTaKu, dan seni pemodelan aljabar modern.",
                "order_index": 1
            },
            "modules": [
                {
                    "title": "Operasi Ka-Ba-Ta-Ku & Hierarki",
                    "slug": "operasi_kabataku",
                    "description": "Urutan operasi PEMDAS universal yang mendasari compiler komputer dan aritmatika presisi.",
                    "icon": "bi-calculator",
                    "order_index": 1,
                    "prereq_slug": None,
                    "materials": [
                        {"chapter": 1, "title": "Bab 1: Pendahuluan & Latar Belakang Konvensi", "slug": "kabataku-bab-1", "anchor": "bab1", "is_cp": 0},
                        {"chapter": 2, "title": "Bab 2: Hierarki Urutan Operasi (PEMDAS)", "slug": "kabataku-bab-2", "anchor": "bab2", "is_cp": 0},
                        {"chapter": 3, "title": "Bab 3: Sifat Aritmatika & Sandbox Hitung", "slug": "kabataku-bab-3", "anchor": "bab3", "is_cp": 0},
                        {"chapter": 4, "title": "Bab 4: Studi Kasus Nyata & Jebakan Viral", "slug": "kabataku-bab-4", "anchor": "bab4", "is_cp": 0},
                        {"chapter": 5, "title": "Bab 5: Capstone Scaffolding Checkpoint", "slug": "kabataku-bab-5", "anchor": "bab5", "is_cp": 1}
                    ]
                },
                {
                    "title": "Pengenalan Aljabar & PLSV",
                    "slug": "aljabar",
                    "description": "Seni berpikir generalisasi variabel warisan Al-Khwarizmi dan pemecahan persamaan satu peubah.",
                    "icon": "bi-diagram-3-fill",
                    "order_index": 2,
                    "prereq_slug": "operasi_kabataku",
                    "materials": [
                        {"chapter": 1, "title": "Bab 1: Pendahuluan & Latar Belakang Al-Khwarizmi", "slug": "aljabar-bab-1", "anchor": "bab1", "is_cp": 0},
                        {"chapter": 2, "title": "Bab 2: Anatomi Bentuk Aljabar", "slug": "aljabar-bab-2", "anchor": "bab2", "is_cp": 0},
                        {"chapter": 3, "title": "Bab 3: Operasi Aljabar & Sandbox Solver", "slug": "aljabar-bab-3", "anchor": "bab3", "is_cp": 0},
                        {"chapter": 4, "title": "Bab 4: Studi Kasus Nyata - Pemodelan Biaya", "slug": "aljabar-bab-4", "anchor": "bab4", "is_cp": 0},
                        {"chapter": 5, "title": "Bab 5: Capstone Scaffolding Checkpoint", "slug": "aljabar-bab-5", "anchor": "bab5", "is_cp": 1}
                    ]
                }
            ]
        },
        {
            "course": {
                "title": "Kalkulus & Analisis Fungsi",
                "slug": "kalkulus-dasar",
                "description": "Perjalanan intelektual memahami laju perubahan sesaat, akumulasi luas lengkung, dan jantung algoritma machine learning.",
                "order_index": 2
            },
            "modules": [
                {
                    "title": "Limit Fungsi Aljabar",
                    "slug": "limit",
                    "description": "Gerbang kalkulus modern: mengatasi bentuk tak tentu dan membaca kecepatan sesaat.",
                    "icon": "bi-bullseye",
                    "order_index": 1,
                    "prereq_slug": "aljabar",
                    "materials": [
                        {"chapter": 1, "title": "Bab 1: Pendahuluan & Latar Belakang Limit", "slug": "limit-bab-1", "anchor": "bab1", "is_cp": 0},
                        {"chapter": 2, "title": "Bab 2: Definisi Formal & Keberadaan Limit", "slug": "limit-bab-2", "anchor": "bab2", "is_cp": 0},
                        {"chapter": 3, "title": "Bab 3: Metode Penyelesaian & Sandbox", "slug": "limit-bab-3", "anchor": "bab3", "is_cp": 0},
                        {"chapter": 4, "title": "Bab 4: Studi Kasus Nyata - Spidometer & Fisika", "slug": "limit-bab-4", "anchor": "bab4", "is_cp": 0},
                        {"chapter": 5, "title": "Bab 5: Capstone Scaffolding Checkpoint", "slug": "limit-bab-5", "anchor": "bab5", "is_cp": 1}
                    ]
                },
                {
                    "title": "Fungsi Turunan & Diferensial",
                    "slug": "fungsi_turunan",
                    "description": "Konsep kemiringan garis singgung tangensial, laju perubahan sesaat, dan optimasi gradien AI.",
                    "icon": "bi-bezier",
                    "order_index": 2,
                    "prereq_slug": "limit",
                    "materials": [
                        {"chapter": 1, "title": "Bab 1: Pendahuluan & Latar Belakang Laju Sesaat", "slug": "turunan-bab-1", "anchor": "bab1", "is_cp": 0},
                        {"chapter": 2, "title": "Bab 2: Definisi Formal & Notasi Leibniz", "slug": "turunan-bab-2", "anchor": "bab2", "is_cp": 0},
                        {"chapter": 3, "title": "Bab 3: Aturan Diferensiasi & Live Sandbox", "slug": "turunan-bab-3", "anchor": "bab3", "is_cp": 0},
                        {"chapter": 4, "title": "Bab 4: Studi Kasus Nyata - Optimasi Laba Bisnis", "slug": "turunan-bab-4", "anchor": "bab4", "is_cp": 0},
                        {"chapter": 5, "title": "Bab 5: Capstone Scaffolding Checkpoint", "slug": "turunan-bab-5", "anchor": "bab5", "is_cp": 1}
                    ]
                },
                {
                    "title": "Integral & Luas Lengkung",
                    "slug": "integral",
                    "description": "Antiturunan, Teorema Dasar Kalkulus, dan akumulasi luas bidang lengkung serta jarak tempuh dinamis.",
                    "icon": "bi-slash-lg",
                    "order_index": 3,
                    "prereq_slug": "fungsi_turunan",
                    "materials": [
                        {"chapter": 1, "title": "Bab 1: Pendahuluan & Latar Belakang Akumulasi", "slug": "integral-bab-1", "anchor": "bab1", "is_cp": 0},
                        {"chapter": 2, "title": "Bab 2: Antiturunan & Misteri Konstanta (+C)", "slug": "integral-bab-2", "anchor": "bab2", "is_cp": 0},
                        {"chapter": 3, "title": "Bab 3: Aturan Pengintegralan & Live Sandbox", "slug": "integral-bab-3", "anchor": "bab3", "is_cp": 0},
                        {"chapter": 4, "title": "Bab 4: Studi Kasus Nyata - Jarak Tempuh Fisika", "slug": "integral-bab-4", "anchor": "bab4", "is_cp": 0},
                        {"chapter": 5, "title": "Bab 5: Capstone Scaffolding Checkpoint", "slug": "integral-bab-5", "anchor": "bab5", "is_cp": 1}
                    ]
                }
            ]
        },
        {
            "course": {
                "title": "Aljabar Linear & Komputasi",
                "slug": "aljabar-linear",
                "description": "Fondasi tensor kecerdasan buatan, manipulasi piksel kartu grafis GPU, dan operasi matriks n-dimensi.",
                "order_index": 3
            },
            "modules": [
                {
                    "title": "Matriks & Aljabar Linear",
                    "slug": "matriks",
                    "description": "Operasi baris kali kolom, determinan singularitas, inversi, dan transformasi rotasi grafis 2D/3D.",
                    "icon": "bi-grid-3x3-gap-fill",
                    "order_index": 1,
                    "prereq_slug": "aljabar",
                    "materials": [
                        {"chapter": 1, "title": "Bab 1: Pendahuluan & Matriks di Era AI", "slug": "matriks-bab-1", "anchor": "bab1", "is_cp": 0},
                        {"chapter": 2, "title": "Bab 2: Ordo & Notasi Elemen Matriks", "slug": "matriks-bab-2", "anchor": "bab2", "is_cp": 0},
                        {"chapter": 3, "title": "Bab 3: Operasi Matriks, Determinan & Sandbox", "slug": "matriks-bab-3", "anchor": "bab3", "is_cp": 0},
                        {"chapter": 4, "title": "Bab 4: Studi Kasus Nyata - Rotasi Grafis 2D", "slug": "matriks-bab-4", "anchor": "bab4", "is_cp": 0},
                        {"chapter": 5, "title": "Bab 5: Evaluasi & Checkpoint Mandiri", "slug": "matriks-bab-5", "anchor": "bab5", "is_cp": 1}
                    ]
                }
            ]
        }
    ]

    module_slug_to_id = {}
    material_slug_to_id = {}

    for c_data in curriculum:
        c = c_data["course"]
        cursor.execute("SELECT id FROM courses WHERE slug = %s", (c["slug"],))
        c_row = cursor.fetchone()
        if not c_row:
            cursor.execute("""
                INSERT INTO courses (title, slug, description, order_index)
                VALUES (%s, %s, %s, %s)
            """, (c["title"], c["slug"], c["description"], c["order_index"]))
            course_id = cursor.lastrowid
            print(f"[SEED] Created course: {c['title']} (ID: {course_id})")
        else:
            course_id = c_row[0]

        for m_data in c_data["modules"]:
            cursor.execute("SELECT id FROM modules WHERE slug = %s", (m_data["slug"],))
            m_row = cursor.fetchone()
            if not m_row:
                cursor.execute("""
                    INSERT INTO modules (course_id, title, slug, description, icon, order_index)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (course_id, m_data["title"], m_data["slug"], m_data["description"], m_data["icon"], m_data["order_index"]))
                module_id = cursor.lastrowid
                print(f"[SEED] Created module: {m_data['title']} (ID: {module_id})")
            else:
                module_id = m_row[0]
            module_slug_to_id[m_data["slug"]] = module_id

    # Update Prerequisite Module IDs
    for c_data in curriculum:
        for m_data in c_data["modules"]:
            if m_data.get("prereq_slug") and m_data["prereq_slug"] in module_slug_to_id:
                prereq_mod_id = module_slug_to_id[m_data["prereq_slug"]]
                cursor.execute("""
                    UPDATE modules SET prerequisite_module_id = %s WHERE slug = %s
                """, (prereq_mod_id, m_data["slug"]))

    # Seed Materials with chained prerequisites
    for c_data in curriculum:
        for m_data in c_data["modules"]:
            mod_id = module_slug_to_id[m_data["slug"]]
            prev_mat_id = None

            # Jika modul memiliki modul prasyarat, ambil bab terakhir modul prasyarat sebagai fondasi
            if m_data.get("prereq_slug") and m_data["prereq_slug"] in module_slug_to_id:
                prereq_m_id = module_slug_to_id[m_data["prereq_slug"]]
                cursor.execute("""
                    SELECT id FROM materials WHERE module_id = %s ORDER BY chapter_number DESC LIMIT 1
                """, (prereq_m_id,))
                prereq_mat_row = cursor.fetchone()
                if prereq_mat_row:
                    prev_mat_id = prereq_mat_row[0]

            for mat in m_data["materials"]:
                cursor.execute("SELECT id FROM materials WHERE module_id = %s AND slug = %s", (mod_id, mat["slug"]))
                mat_row = cursor.fetchone()
                if not mat_row:
                    content_type = "checkpoint" if mat["is_cp"] else ("sandbox" if mat["chapter"] == 3 else "reading")
                    cursor.execute("""
                        INSERT INTO materials (module_id, chapter_number, title, slug, content_type, is_checkpoint, prerequisite_id, order_index, anchor_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        mod_id,
                        mat["chapter"],
                        mat["title"],
                        mat["slug"],
                        content_type,
                        mat["is_cp"],
                        prev_mat_id,
                        mat["chapter"],
                        mat["anchor"]
                    ))
                    curr_mat_id = cursor.lastrowid
                    print(f"  [SEED Material] Chapter {mat['chapter']}: {mat['title']} (Prereq: {prev_mat_id})")
                else:
                    curr_mat_id = mat_row[0]
                    # Update prerequisite if needed
                    cursor.execute("""
                        UPDATE materials SET prerequisite_id = %s, anchor_id = %s, title = %s
                        WHERE id = %s
                    """, (prev_mat_id, mat["anchor"], mat["title"], curr_mat_id))

                material_slug_to_id[mat["slug"]] = curr_mat_id
                prev_mat_id = curr_mat_id

    conn.commit()
    conn.close()
    print("[SEED] Curriculum successfully seeded!")

if __name__ == "__main__":
    seed_curriculum()
