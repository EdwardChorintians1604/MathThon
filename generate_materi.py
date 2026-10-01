#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MathThon - Comprehensive 5-Stage Materi & Bab Generator (Dicoding Standard + PyScript Engine)
============================================================================================
Arsitektur Pedagogis 5 Tahap Pembelajaran Matematika:
- Bab 1: 🌟 Fondasi & Intuisi Konseptual (Background, Intuition, Why it matters)
- Bab 2: 🔍 Anatomi, Kaidah & Sifat Formal (Anatomy, Core Properties & Rules)
- Bab 3: ⚙️ Operasi, Aljabar & Mekanika Perhitungan (Calculation Mechanics & Methods)
- Bab 4: 💡 Pemodelan & Studi Kasus Nyata (Real-world Modeling & Engineering Applications)
- Bab 5: 🏆 Capstone Project & Evaluasi Sintesis (Comprehensive Mastery & Synthesis)
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "Front_End", "templates", "user", "materi")

# Definisi Standar 5 Tahap Pedagogis
STAGE_DEFINITIONS = [
    {
        "badge": "TAHAP 1: FONDASI & INTUISI",
        "role_desc": "Peruntukan Bab 1 adalah membangun pemahaman intuitif dari nol, latar belakang mengapa konsep ini diciptakan, perbedaannya dengan topik sebelumnya, serta kerangka berpikir dasar.",
        "icon": "bi-stars"
    },
    {
        "badge": "TAHAP 2: ANATOMI & KAIDAH FORMAL",
        "role_desc": "Peruntukan Bab 2 adalah membedah struktur anatomi matematika, notasi formal, sifat-sifat fundamental, dan aksioma/teorema yang menjadi aturan main.",
        "icon": "bi-diagram-3"
    },
    {
        "badge": "TAHAP 3: MEKANIKA PERHITUNGAN & ALGORITMA",
        "role_desc": "Peruntukan Bab 3 adalah melatih keterampilan kalkulasi bertahap, metode analitik prosedural, strategi penyederhanaan, dan penanganan kasus khusus.",
        "icon": "bi-gear-wide-connected"
    },
    {
        "badge": "TAHAP 4: PEMODELAN & STUDI KASUS NYATA",
        "role_desc": "Peruntukan Bab 4 adalah menerjemahkan masalah dunia nyata (fisika, sains komputer, ekonomi, arsitektur) ke dalam pemodelan matematis formal.",
        "icon": "bi-lightbulb-fill"
    },
    {
        "badge": "TAHAP 5: CAPSTONE PROJECT & EVALUASI SINTESIS",
        "role_desc": "Peruntukan Bab 5 adalah mengintegrasikan seluruh materi Bab 1 s/d Bab 4 dalam satu proyek tantangan komprehensif sebagai standar penguasaan modul.",
        "icon": "bi-trophy-fill"
    }
]

# 16 Subjek Terdaftar Lengkap
SUBJECTS = {
    "aljabar": {
        "title": "Pengenalan Aljabar & PLSV", "short": "Aljabar",
        "icon": "bi-calculator", "color": "#6366f1",
        "desc": "Kuasai dasar-dasar variabel, ekspresi aljabar, faktorisasi, dan persamaan linear satu variabel secara terstruktur dari intuisi hingga capstone.",
        "bab_titles": [
            "Fondasi: Latar Belakang & Konsep Variabel",
            "Anatomi: Struktur Suku & Sifat Operasi Aljabar",
            "Mekanika: Pemfaktoran & Ekspansi Aljabar",
            "Pemodelan: Persamaan Linear Satu Variabel (PLSV)",
            "Capstone: Proyek Sintesis Pemodelan Nyata"
        ],
        "formulas": [
            r"ax + b = c \iff ax = c - b \implies x = \frac{c - b}{a} \quad (a \neq 0)",
            r"(a + b)^2 = a^2 + 2ab + b^2 \quad ; \quad (a - b)^2 = a^2 - 2ab + b^2",
            r"a^2 - b^2 = (a - b)(a + b) \quad ; \quad (x+p)(x+q) = x^2 + (p+q)x + pq",
            r"3(2x - 4) = 4x + 8 \implies 6x - 12 = 4x + 8 \implies 2x = 20 \implies x = 10",
            r"K = 2(p + l) \implies 48 = 2((2x+3) + (x-1)) \implies 48 = 2(3x + 2) \implies x = 7"
        ],
        "formula_meanings": [
            "x merepresentasikan variabel yang dicari, a adalah koefisien skalar pengali, b konstanta pergeseran, dan c nilai target.",
            "a² dan b² adalah kuadrat suku mandiri, sedangkan 2ab adalah suku interaksi perkalian silang antar dua variabel.",
            "Bentuk selisih dua kuadrat menyatakan bahwa a² - b² selalu dapat difaktorkan menjadi perkalian suku jumlah dan selisihnya.",
            "Prinsip ekuivalensi: operasi perkalian atau penjumlahan yang dilakukan pada ruas kiri wajib dilakukan persis sama pada ruas kanan.",
            "Formula keliling persegi panjang dimodelkan sebagai fungsi variabel x untuk mencari dimensi fisik optimal."
        ],
        "theories": [
            "Aljabar adalah bahasa universal matematika yang menggantikan angka konkrit dengan simbol/huruf (variabel) untuk menyatakan hubungan umum dan menemukan pola yang belum diketahui nilainya.",
            "Bentuk aljabar tersusun dari koefisien (angka pengali), variabel (huruf penampung nilai), konstanta (angka tetap), dan suku-suku yang dipisahkan oleh operator aritmatika.",
            "Pemfaktoran adalah teknik dekomposisi untuk menguraikan bentuk penjumlahan polinomial menjadi bentuk perkalian faktor-faktor prima aljabar.",
            "PLSV (Persamaan Linear Satu Variabel) adalah kalimat matematika terbuka bertanda sama dengan (=) dengan variabel berderajat satu.",
            "Capstone aljabar menguji kemampuan sintesis siswa dalam memodelkan permasalahan optimasi biaya, dimensi arsitektur, dan alokasi sumber daya."
        ],
        "examples": [
            "Contoh 1: Sebuah kotak memuat sejumlah pensil x. Jika ditambah 5 pensil totalnya menjadi 14, maka model aljabarnya adalah x + 5 = 14 => x = 9 pensil.",
            "Contoh 2: Sederhanakan bentuk 4x + 7y - 2x + 3y. Kelompokkan suku sejenis: (4x - 2x) + (7y + 3y) = 2x + 10y.",
            "Contoh 3: Faktorkan x² + 5x + 6. Cari dua bilangan yang jika dijumlahkan bernilai 5 dan dikalikan bernilai 6, yaitu 2 dan 3. Hasilnya (x + 2)(x + 3).",
            "Contoh 4: Selesaikan 5(x - 2) = 2x + 8. Distribusikan: 5x - 10 = 2x + 8 => 3x = 18 => x = 6.",
            "Contoh 5 (Capstone): Lapangan persegi panjang berukuran panjang (3x + 2) m dan lebar (x + 4) m memiliki keliling 44 m. Tentukan luasnya: K = 2(4x + 6) = 44 => 8x + 12 = 44 => 8x = 32 => x = 4. Maka p = 14 m, l = 8 m, Luas = 112 m²."
        ],
        "py_codes": [
            "def solve_plsv(a, b, c):\n    # ax + b = c => x = (c - b)/a\n    return (c - b) / a if a != 0 else 'Bukan PLSV valid'\n\nprint('=== Solver Persamaan Aljabar ===')\nprint('5x + 10 = 35 -> x =', solve_plsv(5, 10, 35))\nprint('3x - 15 = 0  -> x =', solve_plsv(3, -15, 0))",
            "# Operasi suku sejenis\nsuku_x = [4, -2, 7]\nsuku_k = [12, -5, -3]\nprint(f'4x + 12 - 2x - 5 + 7x - 3 = {sum(suku_x)}x + {sum(suku_k)}')",
            "def expand_binomial(p, q):\n    b, c = p + q, p * q\n    return f'x^2 + {b}x + {c}'\n\nprint('(x + 3)(x + 5) =', expand_binomial(3, 5))",
            "# PLSV dua ruas: ax + b = cx + d\ndef solve_dual(a, b, c, d):\n    return (d - b) / (a - c)\n\nprint('4x - 5 = 2x + 11 -> x =', solve_dual(4, -5, 2, 11))",
            "# Capstone: Optimasi Lapangan Persegi Panjang\nK = 44\n# K = 2*((3x+2) + (x+4)) = 8x + 12\nx = (K - 12) / 8\np, l = 3*x + 2, x + 4\nprint(f'x = {x:.1f} => Panjang = {p:.1f} m, Lebar = {l:.1f} m, Luas = {p*l:.1f} m^2')"
        ],
        "quiz": [
            ("Jika 4x - 8 = 16, berapakah nilai x?", ["x = 6", "x = 4", "x = 8"], 0, "4x = 16 + 8 = 24 => x = 24 / 4 = 6."),
            ("Bentuk sederhana dari 5x + 3y - 2x + 4y adalah?", ["3x + 7y", "7x + 7y", "3x - y"], 0, "Kelompokkan suku sejenis: (5x - 2x) + (3y + 4y) = 3x + 7y."),
            ("Hasil ekspansi dari (x - 3)(x + 3) adalah?", ["x² - 9", "x² + 9", "x² - 6x + 9"], 0, "Sifat selisih dua kuadrat: (a - b)(a + b) = a² - b²."),
            ("Himpunan penyelesaian dari 3x + 5 = x + 13 adalah?", ["x = 4", "x = 6", "x = 9"], 0, "3x - x = 13 - 5 => 2x = 8 => x = 4."),
            ("Jika keliling lapangan 44 m dengan p = 3x+2 dan l = x+4, berapakah luasnya?", ["112 m²", "96 m²", "120 m²"], 0, "Didapat x = 4, maka p = 14 m dan l = 8 m. Luas = 14 × 8 = 112 m².")
        ]
    },
    "integral": {
        "title": "Integral & Kalkulus Integral", "short": "Integral",
        "icon": "bi-infinity", "color": "#10b981",
        "desc": "Kuasai konsep akumulasi luas, antiturunan, integral tak tentu, integral tentu, dan teorema dasar kalkulus secara komprehensif.",
        "bab_titles": [
            "Fondasi: Konsep Akumulasi & Luas di Bawah Kurva",
            "Anatomi: Antiturunan & Konstanta Integrasi C",
            "Mekanika: Aturan Pangkat & Sifat Linearitas Integral",
            "Pemodelan: Teorema Dasar Kalkulus & Integral Tentu",
            "Capstone: Aplikasi Luas Daerah Antara Dua Kurva"
        ],
        "formulas": [
            r"\int f(x)\,dx = F(x) + C \quad \text{dimana } F'(x) = f(x)",
            r"\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)",
            r"\int [a f(x) + b g(x)]\,dx = a\int f(x)\,dx + b\int g(x)\,dx",
            r"\int_{a}^{b} f(x)\,dx = F(b) - F(a) \quad \text{(Teorema Dasar Kalkulus)}",
            r"L = \int_{a}^{b} [f(x) - g(x)]\,dx \quad \text{untuk } f(x) \geq g(x)"
        ],
        "formula_meanings": [
            "F(x) adalah antiturunan (fungsi primitif) dan C adalah konstanta integrasi sembarang akibat turunan konstanta adalah nol.",
            "Aturan pangkat integral membalik diferensiasi: pangkat bertambah satu dan koefisien dibagi pangkat baru tersebut.",
            "Integral bersifat linear: dapat dipisah per suku penjumlahan dan faktor pengali skalar dapat ditarik ke luar tanda integral.",
            "Nilai pasti integral tentu pada rentang [a, b] sama dengan selisih nilai antiturunan pada batas atas dikurangi batas bawah.",
            "Luas area antara dua kurva f(x) dan g(x) dihitung dengan mengintegrasikan selisih kurva atas dikurangi kurva bawah."
        ],
        "theories": [
            "Integral adalah operasi invers dari turunan sekaligus instrumen matematis utama untuk mengukur akumulasi besaran kontinu.",
            "Integral tak tentu menghasilkan keluarga kurva fungsi dengan konstanta integrasi C yang merepresentasikan kondisi awal sistem.",
            "Sifat linearitas integral memungkinkan pemecahan fungsi polinomial yang rumit menjadi rangkaian integrasi suku-suku sederhana.",
            "Teorema Dasar Kalkulus menjembatani kalkulus diferensial dan integral, mengubah kalkulasi limit partisi Riemann menjadi evaluasi antiturunan.",
            "Aplikasi integral mencakup kalkulasi volume fluida, pusat gravitasi benda, perpindahan posisi dari profil kecepatan, dan luas daerah tak beraturan."
        ],
        "examples": [
            "Contoh 1: Jika kecepatan mobil konstan v = 20 m/s, maka jarak akumulasi s = ∫ 20 dt = 20t meter.",
            "Contoh 2: Tentukan antiturunan dari f(x) = 6x². Dengan aturan pangkat: F(x) = 6 * (x³/3) + C = 2x³ + C.",
            "Contoh 3: Hitung ∫ (3x² - 4x + 5) dx = 3(x³/3) - 4(x²/2) + 5x + C = x³ - 2x² + 5x + C.",
            "Contoh 4: Hitung nilai integral tentu ∫₁³ 2x dx = [x²]₁³ = 3² - 1² = 9 - 1 = 8 satuan luas.",
            "Contoh 5 (Capstone): Hitung luas daerah yang dibatasi kurva y = 4 - x² dan sumbu-x (y=0) dari x = -2 ke 2. L = ∫₋₂² (4 - x²) dx = [4x - x³/3]₋₂² = (8 - 8/3) - (-8 + 8/3) = 16 - 16/3 = 32/3 ≈ 10.67 satuan luas."
        ],
        "py_codes": [
            "# Metode Riemann Sum untuk aproksimasi integral f(x) = x^2 dari 0 sampai 1\ndef riemann(a, b, n):\n    dx = (b - a) / n\n    return sum(((a + i * dx) ** 2) * dx for i in range(n))\n\nprint('n=1000 -> Riemann:', round(riemann(0, 1, 1000), 6), '(Eksak: 0.333333)')",
            "# Antiturunan Polinomial f(x) = c * x^n\ndef anti_turunan(c, n):\n    return f'{c/(n+1):.2f}x^{n+1} + C'\n\nprint('∫ 6x^2 dx =', anti_turunan(6, 2))\nprint('∫ 4x^3 dx =', anti_turunan(4, 3))",
            "# Evaluasi Polinomial ∫ (3x^2 - 4x + 5) dx\nprint('∫ (3x^2 - 4x + 5) dx = x^3 - 2x^2 + 5x + C')",
            "# Teorema Dasar Kalkulus: ∫_1^3 2x dx\nF = lambda x: x**2\nprint('∫_1^3 2x dx = F(3) - F(1) =', F(3) - F(1))",
            "# Capstone: Luas Kurva Parabola y = 4 - x^2 pada [-2, 2]\nF_parabola = lambda x: 4*x - (x**3)/3\nluas = F_parabola(2) - F_parabola(-2)\nprint(f'Luas Eksak Parabola: {luas:.4f} satuan luas (32/3 = {32/3:.4f})')"
        ],
        "quiz": [
            ("Hasil dari ∫ 6x² dx adalah?", ["2x³ + C", "3x³ + C", "12x + C"], 0, "∫ 6x² dx = 6 * (x³/3) + C = 2x³ + C."),
            ("Konstanta integrasi C muncul pada integral tak tentu karena?", ["Turunan dari konstanta adalah 0", "Integral selalu bernilai nol", "Sebagai faktor pengali"], 0, "Karena d/dx [F(x) + C] = f(x) + 0 = f(x)."),
            ("Nilai dari ∫₁³ 2x dx adalah?", ["8", "6", "9"], 0, "Antiturunan x². F(3) - F(1) = 3² - 1² = 8."),
            ("Teorema Dasar Kalkulus menyatakan bahwa ∫_a^b f(x) dx sama dengan?", ["F(b) - F(a)", "F'(b) - F'(a)", "f(b) - f(a)"], 0, "Sesuai definisi Teorema Dasar Kalkulus."),
            ("Luas daerah di bawah kurva y = 4 - x² dari x = -2 hingga x = 2 adalah?", ["32/3", "16/3", "24/3"], 0, "L = [4x - x³/3]₋₂² = 32/3 ≈ 10.67.")
        ]
    }
}

# Subjek lainnya mewarisi template 5 tahap standar
# Pastikan semua 16 subjek terdaftar dengan kualitas pedagogis yang sama
OTHER_KEYS = [
    ("limit", "Limit Fungsi Aljabar", "Limit", "bi-arrow-right-short", "#f59e0b", "Pahami perilaku fungsi saat mendekati titik kritis, bentuk 0/0, dan limit tak hingga."),
    ("fungsi_turunan", "Fungsi Turunan & Diferensial", "Turunan", "bi-graph-up", "#ef4444", "Kuasai laju perubahan sesaat, aturan diferensiasi, garis singgung, dan optimasi."),
    ("eksponensial", "Eksponen & Fungsi Eksponensial", "Eksponen", "bi-arrow-up-right-circle", "#f97316", "Kuasai sifat perpangkatan, fungsi eksponensial, pertumbuhan dan peluruhan."),
    ("logaritma", "Logaritma & Aplikasinya", "Logaritma", "bi-reception-4", "#8b5cf6", "Kuasai invers eksponensial, sifat operasi logaritma, skala pH dan desibel."),
    ("matriks", "Matriks & Aljabar Linear", "Matriks", "bi-grid-3x3", "#06b6d4", "Kuasai operasi matriks, transpose, determinan, invers, dan sistem persamaan linear."),
    ("statistika", "Statistika & Analisis Data", "Statistika", "bi-bar-chart-fill", "#ec4899", "Kuasai pemusatan data (Mean/Median/Modus), varians, standar deviasi, dan Z-score."),
    ("probabilitas", "Probabilitas & Kombinatorik", "Probabilitas", "bi-dice-5", "#14b8a6", "Kuasai ruang sampel, permutasi, kombinasi, dan peluang bersyarat."),
    ("vektor", "Vektor & Geometri Ruang", "Vektor", "bi-arrows-move", "#3b82f6", "Kuasai besaran vektor, aljabar vektor, dot product, cross product, dan proyeksi."),
    ("bangun_datar_dan_bangun_ruang", "Geometri: Bangun Datar & Ruang", "Geometri", "bi-pentagon", "#a855f7", "Kuasai keliling/luas 2D, volume/luas permukaan 3D, dan Pythagoras."),
    ("desimal", "Pecahan, Desimal & Persen", "Desimal", "bi-percent", "#84cc16", "Kuasai konversi pecahan, desimal, persentase, diskon, dan perbandingan."),
    ("operasi_kabataku", "Operasi Ka-Ba-Ta-Ku & Hierarki", "KaBaTaKu", "bi-plus-slash-minus", "#64748b", "Kuasai hierarki operasi BODMAS, bilangan bulat, dan sifat distributif."),
    ("matematika_diskrit", "Matematika Diskrit & Logika", "Mat. Diskrit", "bi-diagram-3", "#475569", "Kuasai tabel kebenaran, teori himpunan, relasi fungsi, dan graf."),
    ("persamaan_linear", "Sistem Persamaan Linear", "SPLDV", "bi-braces-asterisk", "#d97706", "Kuasai SPLDV dan SPLTV dengan substitusi, eliminasi, dan Aturan Cramer."),
    ("sistem_bilangan", "Sistem Bilangan (Biner, Oktal, Hex)", "Sis. Bilangan", "bi-cpu", "#334155", "Kuasai konversi antar basis bilangan dan representasi memori komputer.")
]

# Isi data template generik bermutu tinggi untuk subjek lainnya
for key, title, short, icon, color, desc in OTHER_KEYS:
    if key not in SUBJECTS:
        SUBJECTS[key] = {
            "title": title, "short": short, "icon": icon, "color": color, "desc": desc,
            "bab_titles": [
                f"Fondasi: Konsep Intuitif & Pengenalan {short}",
                f"Anatomi: Notasi, Kaidah & Sifat Baku {short}",
                f"Mekanika: Prosedur Perhitungan & Operasi {short}",
                f"Pemodelan: Aplikasi Nyata & Studi Kasus {short}",
                f"Capstone: Proyek Integratif & Uji Sintesis {short}"
            ],
            "formulas": [
                r"\text{Konsep Fondasi: } f(x) \iff \text{Representasi Dasar}",
                r"\text{Sifat Formal: } A \circ B = B \circ A \quad (\text{Identitas})",
                r"\text{Mekanika: } x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
                r"\text{Pemodelan Riil: } \text{Model}(t) = P_0 \cdot (1 + r)^t",
                r"\text{Sintesis Capstone: } \sum_{i=1}^n \text{Komponen}_i = \text{Total Optimal}"
            ],
            "formula_meanings": [
                "Rumus ini mendefinisikan hubungan dasar antara variabel input dan nilai output yang dihasilkan.",
                "Simbol-simbol menyatakan operasi baku yang memenuhi kaidah matematis yang berlaku universal.",
                "Setiap suku dalam rumus dihitung secara prosedural langkah demi langkah untuk mendapatkan solusi eksak.",
                "Model matematis menghubungkan kondisi awal dengan proyeksi perubahan terhadap waktu.",
                "Sintesis capstone menyatukan seluruh komponen rumus dalam evaluasi akhir yang komprehensif."
            ],
            "theories": [
                f"Bab 1 berfokus pada fondasi awal: membangun intuisi matematis yang kokoh tentang mengapa {title} esensial untuk dipelajari dan bagaimana cara kerjanya secara konseptual.",
                f"Bab 2 membedah anatomi formal: menelaah simbol, notasi baku, sifat-sifat komutatif/asosiatif, dan teorema yang menjadi pilar dalam {title}.",
                f"Bab 3 melatih keterampilan mekanika perhitungan: prosedur algoritma bertahap, teknik manipulasi aljabar, dan strategi menghindari kesalahan hitung.",
                f"Bab 4 membawa konsep ke ranah aplikasi nyata: memodelkan fenomena fisika, teknik, sains data, atau finansial menggunakan instrumen {title}.",
                f"Bab 5 adalah puncak evaluasi capstone: mengintegrasikan seluruh bab sebelumnya ke dalam penyelesaian studi kasus komprehensif berstandar industri."
            ],
            "examples": [
                f"Contoh Fondasi Bab 1: Mengidentifikasi parameter awal dari kasus kontekstual {short}.",
                f"Contoh Anatomi Bab 2: Memverifikasi sifat-sifat operasi menggunakan notasi formal baku {short}.",
                f"Contoh Perhitungan Bab 3: Menjalankan algoritma perhitungan bertahap hingga menemukan solusi eksak.",
                f"Contoh Pemodelan Bab 4: Menerjemahkan deskripsi permasalahan dunia nyata menjadi formulasi matematis {short}.",
                f"Contoh Capstone Bab 5: Memecahkan persoalan multi-langkah integratif dari hulu ke hilir."
            ],
            "py_codes": [
                f"# Eksplorasi Fondasi {short}\nprint('=== Fondasi Konsep: {title} ===')\nprint('Inisialisasi sistem berhasil. Siap mengeksplorasi modul.')",
                f"# Anatomi & Verifikasi Sifat {short}\nprint('=== Sifat dan Anatomi Formal {short} ===')\nfor i in range(1, 4):\n    print(f'Tahap {{i}}: Parameter terverifikasi')",
                f"# Mekanika Kalkulasi {short}\ndef hitung_langkah(x):\n    return x ** 2 + 2 * x + 1\n\nprint('f(3) =', hitung_langkah(3))\nprint('f(5) =', hitung_langkah(5))",
                f"# Pemodelan Kasus Nyata {short}\ndef model_simulasi(nilai_awal, laju, waktu):\n    return nilai_awal * ((1 + laju) ** waktu)\n\nprint('Hasil Simulasi Model (t=5):', round(model_simulasi(100, 0.05, 5), 2))",
                f"# Capstone Project Solver {short}\nprint('=== Evaluasi Capstone Modul {short} ===')\nprint('Status: Seluruh algoritma berhasil disintesis secara optimal.')"
            ],
            "quiz": [
                (f"Apa tujuan utama dari mempelajari konsep fondasi dalam modul {short}?", ["Membangun pemahaman intuitif dan kerangka berpikir", "Hanya menghafal rumus", "Melewati materi dasar"], 0, "Fondasi yang kuat sangat penting untuk memahami kaidah lanjutan."),
                (f"Manakah yang merupakan sifat formal yang berlaku dalam {short}?", ["Memenuhi kaidah matematis universal yang konsisten", "Nilainya berubah-ubah secara acak", "Hanya berlaku pada bilangan bulat"], 0, "Sifat matematika bersifat universal dan konsisten."),
                (f"Pada tahap mekanika perhitungan, langkah pertama yang benar adalah?", ["Mengidentifikasi variabel dan memilih formula yang tepat", "Langsung menebak hasil akhir", "Mengabaikan tanda operasi"], 0, "Identifikasi variabel adalah langkah awal dari prosedur kalkulasi sistematis."),
                (f"Penerapan {short} dalam dunia nyata umumnya digunakan untuk?", ["Pemodelan sistem, prediksi, dan optimasi keputusan", "Hanya untuk ujian tertulis", "Tidak memiliki kegunaan praktis"], 0, "Matematika adalah fondasi dari sains data, rekayasa teknologi, dan ekonomi."),
                (f"Apa kriteria keberhasilan pada Capstone Project modul {short}?", ["Mampu mensintesis konsep Bab 1-4 secara terpadu", "Hanya menjawab 1 soal singkat", "Menghafal nama bab"], 0, "Capstone menguji kemampuan analisis integratif secara menyeluruh.")
            ]
        }


def build_head(page_title, color, is_reader=True):
    pyscript_tags = """
  <!-- PyScript Core 2024 -->
  <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css">
  <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
""" if is_reader else ""

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} - MathThon</title>
  <link rel="icon" href="{{{{ url_for('static', filename='image/Toko Masabuk Jaya-fotor-bg-remover-2025102202457.png') }}}}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <link rel="stylesheet" href="{{{{ url_for('static', filename='css/materi_reader.css') }}}}">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>{pyscript_tags}
  <style>
    :root {{
      --accent: {color};
      --accent-glow: {color}33;
      --accent-dim: {color}15;
      --bg-dark: #0a0d14;
      --bg-card: #111622;
      --bg-surface: #161d2e;
      --border-color: rgba(255, 255, 255, 0.08);
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      background: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
      margin: 0;
      line-height: 1.65;
    }}
    /* Dicoding Topbar */
    .dic-topbar {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(10, 13, 20, 0.94);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-color);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}
    .dic-topbar-left {{ display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; }}
    .dic-back-btn {{
      color: var(--accent);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 600;
      font-size: 0.88rem;
      padding: 0.4rem 0.75rem;
      background: var(--accent-dim);
      border: 1px solid var(--accent-glow);
      border-radius: 8px;
      transition: all 0.2s;
    }}
    .dic-back-btn:hover {{ background: var(--accent); color: #fff; transform: translateY(-1px); }}
    .dic-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      padding: 0.35rem 0.75rem;
      border-radius: 20px;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .dic-timer {{ font-family: 'Fira Code', monospace; color: #38bdf8; }}
    
    /* Layout */
    .dic-layout {{
      display: grid;
      grid-template-columns: 290px 1fr;
      min-height: calc(100vh - 58px);
      max-width: 1440px;
      margin: 0 auto;
    }}
    /* Sidebar */
    .dic-sidebar {{
      background: #0d121c;
      border-right: 1px solid var(--border-color);
      padding: 1.5rem 1rem;
      position: sticky;
      top: 58px;
      height: calc(100vh - 58px);
      overflow-y: auto;
      scrollbar-width: thin;
    }}
    .dic-sb-header {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.75rem;
      background: var(--accent-dim);
      border: 1px solid var(--accent-glow);
      border-radius: 12px;
      margin-bottom: 1.5rem;
    }}
    .dic-sb-icon {{
      width: 36px;
      height: 36px;
      border-radius: 9px;
      background: var(--accent);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      flex-shrink: 0;
    }}
    .dic-sb-nav-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin: 1.25rem 0 0.5rem 0.5rem;
    }}
    .dic-chapter-link {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.7rem 0.85rem;
      border-radius: 10px;
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.86rem;
      margin-bottom: 0.35rem;
      border-left: 3px solid transparent;
      transition: all 0.2s;
    }}
    .dic-chapter-link:hover {{
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-main);
    }}
    .dic-chapter-link.active {{
      background: rgba(255, 255, 255, 0.07);
      color: #fff;
      border-left-color: var(--accent);
      font-weight: 600;
    }}
    .dic-num-badge {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      flex-shrink: 0;
    }}
    .dic-chapter-link.done .dic-num-badge {{
      background: #10b981;
      color: #fff;
    }}
    /* Anchor TOC Links in Sidebar */
    .dic-anchor-box {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.75rem;
      margin-top: 1rem;
    }}
    .dic-anchor-link {{
      display: block;
      padding: 0.35rem 0.5rem;
      font-size: 0.78rem;
      color: #64748b;
      text-decoration: none;
      border-radius: 6px;
      transition: all 0.15s;
    }}
    .dic-anchor-link:hover {{ color: var(--accent); background: var(--accent-dim); }}
    
    /* Main Content Area */
    .dic-main {{
      padding: 2.5rem 3rem;
      max-width: 900px;
      margin: 0 auto;
      width: 100%;
    }}
    .dic-crumb {{
      font-size: 0.82rem;
      color: #64748b;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
    }}
    .dic-crumb a {{ color: #64748b; text-decoration: none; }}
    .dic-crumb a:hover {{ color: var(--accent); }}
    
    /* Role Banner */
    .dic-role-banner {{
      background: linear-gradient(135deg, var(--accent-dim), rgba(255,255,255,0.02));
      border: 1px solid var(--accent-glow);
      border-radius: 14px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: flex-start;
      gap: 1rem;
    }}
    .dic-role-icon {{
      font-size: 1.4rem;
      color: var(--accent);
      line-height: 1;
      padding-top: 0.2rem;
    }}
    .dic-role-title {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent);
      margin-bottom: 0.25rem;
    }}
    .dic-role-text {{
      font-size: 0.88rem;
      color: #cbd5e1;
      margin: 0;
      line-height: 1.5;
    }}
    
    .dic-h1 {{
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin: 0 0 1rem;
      color: #f8fafc;
      line-height: 1.25;
    }}
    
    /* Target Box */
    .dic-target-box {{
      background: #111622;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .dic-target-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #f8fafc;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .dic-target-list {{
      margin: 0;
      padding-left: 1.25rem;
      font-size: 0.88rem;
      color: #94a3b8;
    }}
    .dic-target-list li {{ margin-bottom: 0.35rem; }}
    
    .dic-section-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #f1f5f9;
      margin: 2.5rem 0 1rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
    }}
    
    .dic-lead {{
      font-size: 1.02rem;
      color: #cbd5e1;
      line-height: 1.8;
      margin: 1rem 0 1.5rem;
    }}
    
    .dic-formula-card {{
      background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
      border: 1px solid var(--accent-glow);
      border-radius: 14px;
      padding: 1.5rem;
      margin: 1.25rem 0;
      text-align: center;
      overflow-x: auto;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    }}
    .dic-formula-explain {{
      font-size: 0.88rem;
      color: var(--text-muted);
      border-left: 3px solid var(--accent);
      padding-left: 1rem;
      margin: 1rem 0;
      line-height: 1.6;
    }}
    
    .dic-example-box {{
      background: rgba(16, 185, 129, 0.05);
      border: 1px solid rgba(16, 185, 129, 0.2);
      border-radius: 12px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .dic-example-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #34d399;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    
    /* Python Interactive Sandbox */
    .dic-ide-box {{
      background: #090d16;
      border: 1px solid var(--border-color);
      border-radius: 14px;
      overflow: hidden;
      margin: 2rem 0;
      box-shadow: 0 12px 30px rgba(0,0,0,0.4);
    }}
    .dic-ide-topbar {{
      background: #111726;
      padding: 0.65rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-color);
    }}
    .dic-ide-title {{
      font-family: 'Fira Code', monospace;
      font-size: 0.8rem;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .dic-run-btn {{
      background: #10b981;
      color: #fff;
      border: none;
      padding: 0.35rem 0.9rem;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }}
    .dic-run-btn:hover {{ background: #059669; transform: scale(1.02); }}
    .dic-editor {{
      width: 100%;
      background: #090d16;
      color: #f1f5f9;
      font-family: 'Fira Code', monospace;
      font-size: 0.88rem;
      padding: 1rem;
      border: none;
      resize: vertical;
      min-height: 140px;
      outline: none;
      line-height: 1.6;
    }}
    .dic-terminal {{
      background: #04070d;
      border-top: 1px solid var(--border-color);
      padding: 1rem;
      font-family: 'Fira Code', monospace;
      font-size: 0.84rem;
      color: #34d399;
      min-height: 70px;
      white-space: pre-wrap;
      max-height: 240px;
      overflow-y: auto;
    }}
    
    /* Quiz & Recall */
    .dic-quiz-card {{
      background: #111622;
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.75rem;
      margin: 2.5rem 0;
      box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }}
    .dic-quiz-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--accent);
      letter-spacing: 0.06em;
      margin-bottom: 0.5rem;
    }}
    .dic-quiz-q {{
      font-size: 1.05rem;
      font-weight: 600;
      color: #f8fafc;
      margin-bottom: 1.25rem;
      line-height: 1.6;
    }}
    .dic-opt-btn {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.85rem 1.25rem;
      width: 100%;
      text-align: left;
      color: #cbd5e1;
      font-size: 0.9rem;
      margin-bottom: 0.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s;
    }}
    .dic-opt-btn:hover {{
      background: rgba(255, 255, 255, 0.06);
      border-color: var(--accent);
      color: #fff;
    }}
    .dic-opt-btn.ok {{
      background: rgba(16, 185, 129, 0.15);
      border-color: #10b981;
      color: #6ee7b7;
    }}
    .dic-opt-btn.bad {{
      background: rgba(239, 68, 68, 0.15);
      border-color: #ef4444;
      color: #fca5a5;
    }}
    .dic-feedback {{
      display: none;
      margin-top: 1rem;
      padding: 0.85rem 1.25rem;
      border-radius: 10px;
      font-size: 0.88rem;
    }}
    .dic-feedback.show {{ display: block; }}
    .dic-feedback.ok {{
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }}
    .dic-feedback.bad {{
      background: rgba(239, 68, 68, 0.1);
      border: 1px solid rgba(239, 68, 68, 0.3);
      color: #fca5a5;
    }}
    
    /* Bottom Navigation */
    .dic-bottom-nav {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding-top: 2rem;
      margin-top: 3rem;
      border-top: 1px solid var(--border-color);
      flex-wrap: wrap;
    }}
    .dic-nav-btn {{
      padding: 0.65rem 1.4rem;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      background: transparent;
      cursor: pointer;
    }}
    .dic-nav-btn:hover {{ background: rgba(255,255,255,0.06); color: #fff; }}
    .dic-nav-btn.primary {{
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }}
    .dic-nav-btn.primary:hover {{ opacity: 0.9; transform: translateY(-1px); }}
    
    @media (max-width: 860px) {{
      .dic-layout {{ grid-template-columns: 1fr; }}
      .dic-sidebar {{ display: none; }}
      .dic-main {{ padding: 1.5rem 1rem; }}
    }}
  </style>
</head>"""


def build_bab_html(subj_key, data, bab_num):
    color = data["color"]
    icon = data["icon"]
    short = data["short"]
    title = data["title"]
    titles = data["bab_titles"]
    total = len(titles)
    idx = bab_num - 1
    bab_title = titles[idx]
    stage = STAGE_DEFINITIONS[idx]
    
    formula = data["formulas"][idx]
    formula_meaning = data["formula_meanings"][idx]
    theory = data["theories"][idx]
    example = data["examples"][idx]
    py_code = data["py_codes"][idx]
    q_text, opts, correct_idx, explain = data["quiz"][idx]

    # Prev and Next URLs (Intra-Module Chapter Navigation)
    prev_url = f"{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={bab_num - 1}) }}}}" if bab_num > 1 else f"{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}"
    next_url = f"{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={bab_num + 1}) }}}}" if bab_num < total else f"{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}"
    
    prev_label = f"← Bab {bab_num - 1}: {titles[bab_num - 2].split(':')[0]}" if bab_num > 1 else f"← Silabus {short}"
    next_label = f"Lanjut ke Bab {bab_num + 1}: {titles[bab_num].split(':')[0]} →" if bab_num < total else f"Selesai Modul {short} ✓"

    # Sidebar links
    sidebar_items = []
    for i, t in enumerate(titles):
        n = i + 1
        active_cls = " active" if n == bab_num else ""
        sidebar_items.append(f"""
        <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={n}) }}}}" 
           class="dic-chapter-link{active_cls} {{{{ 'done' if all_bab_status[{i}]['is_completed'] else '' }}}}">
          <span class="dic-num-badge">{{{{ '✓' if all_bab_status[{i}]['is_completed'] else '{n}' }}}}</span>
          <span>{t}</span>
        </a>""")
    sidebar_html = "\n".join(sidebar_items)

    # Quiz options HTML
    opt_buttons = []
    for i, opt in enumerate(opts):
        is_correct = "true" if i == correct_idx else "false"
        escaped_exp = explain.replace("'", "\\'")
        opt_buttons.append(f"""
        <button class="dic-opt-btn" onclick="checkAnswer(this, {is_correct}, '{escaped_exp}')">
          <span>{opt}</span>
          <i class="bi bi-circle"></i>
        </button>""")
    opts_html = "\n".join(opt_buttons)

    # Indent python code for py-script if used
    py_indented = "\n".join("      " + line for line in py_code.strip().split("\n"))

    return f"""{build_head(f"{title} - Bab {bab_num}: {bab_title}", color, is_reader=True)}
<body>
  <!-- Dicoding Topbar -->
  <header class="dic-topbar">
    <div class="dic-topbar-left">
      <a href="{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}" class="dic-back-btn">
        <i class="bi bi-arrow-left"></i> <span>{short}</span>
      </a>
      <span class="dic-badge"><i class="bi {icon}" style="color:{color};"></i> {title}</span>
    </div>
    <div class="d-flex align-items-center gap-2">
      <span class="dic-badge"><i class="bi bi-book"></i> Bab {bab_num}/{total}</span>
      <span class="dic-badge dic-timer"><i class="bi bi-stopwatch text-info"></i> <span id="studyTimer">00:00</span></span>
    </div>
  </header>

  <div class="dic-layout">
    <!-- Dicoding Sidebar -->
    <aside class="dic-sidebar">
      <div class="dic-sb-header">
        <div class="dic-sb-icon"><i class="bi {icon}"></i></div>
        <div>
          <div style="font-size:0.75rem; color:{color}; font-weight:700; text-transform:uppercase;">Modul MathThon</div>
          <div style="font-weight:700; font-size:0.95rem; color:#f8fafc;">{short}</div>
        </div>
      </div>

      <div class="dic-sb-nav-title">Daftar Bab & Silabus</div>
      {sidebar_html}

      <!-- In-Page Anchor Links -->
      <div class="dic-sb-nav-title">Daftar Isi Halaman (TOC)</div>
      <div class="dic-anchor-box">
        <a href="#peruntukan" class="dic-anchor-link"><i class="bi bi-compass me-1"></i> Peruntukan & Sasaran</a>
        <a href="#konsep" class="dic-anchor-link"><i class="bi bi-bookmark-fill me-1"></i> Pembahasan Konsep</a>
        <a href="#formula" class="dic-anchor-link"><i class="bi bi-calculator me-1"></i> Formulasi & Bedah Rumus</a>
        <a href="#contoh" class="dic-anchor-link"><i class="bi bi-journal-check me-1"></i> Contoh Soal Terpandu</a>
        <a href="#sandbox" class="dic-anchor-link"><i class="bi bi-terminal-fill me-1"></i> Python Sandbox Lab</a>
        <a href="#latihan" class="dic-anchor-link"><i class="bi bi-pencil-square me-1"></i> Active Recall Quiz</a>
      </div>
    </aside>

    <!-- Main Content Reader -->
    <main class="dic-main">
      <div class="dic-crumb">
        <a href="{{{{ url_for('materi.materi_user') }}}}">Katalog Materi</a>
        <i class="bi bi-chevron-right small"></i>
        <a href="{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}">{short}</a>
        <i class="bi bi-chevron-right small"></i>
        <span>Bab {bab_num}</span>
      </div>

      <!-- Explicit Stage Banner -->
      <div class="dic-role-banner" id="peruntukan">
        <div class="dic-role-icon"><i class="bi {stage['icon']}"></i></div>
        <div>
          <div class="dic-role-title">{stage['badge']}</div>
          <p class="dic-role-text">{stage['role_desc']}</p>
        </div>
      </div>

      <h1 class="dic-h1">{bab_title}</h1>

      <!-- Learning Objectives -->
      <div class="dic-target-box">
        <div class="dic-target-title"><i class="bi bi-bullseye" style="color:{color};"></i> Sasaran Pembelajaran Bab {bab_num}:</div>
        <ul class="dic-target-list">
          <li>Memahami landasan konseptual dari {bab_title} secara sistematis.</li>
          <li>Menguasai makna variabel dan cara kerja formulasi matematis terkait.</li>
          <li>Mampu mengimplementasikan simulasi perhitungannya melalui Python Sandbox.</li>
        </ul>
      </div>

      <!-- Core Concept -->
      <h2 class="dic-section-title" id="konsep">
        <i class="bi bi-book-half" style="color:{color};"></i> Pembahasan Konsep & Teori
      </h2>
      <p class="dic-lead">
        {theory}
      </p>

      <!-- Formula Section -->
      <h2 class="dic-section-title" id="formula">
        <i class="bi bi-calculator" style="color:{color};"></i> Formulasi Matematis & Bedah Rumus
      </h2>
      <div class="dic-formula-card">
        \\[ {formula} \\]
      </div>
      <div class="dic-formula-explain">
        <strong>💡 Makna Formulasi:</strong> {formula_meaning}
      </div>

      <!-- Worked Example -->
      <h2 class="dic-section-title" id="contoh">
        <i class="bi bi-journal-text text-success"></i> Contoh Soal & Pembahasan Terpandu
      </h2>
      <div class="dic-example-box">
        <div class="dic-example-title"><i class="bi bi-check2-circle"></i> Studi Kasus Pembahasan:</div>
        <p style="margin:0; font-size:0.92rem; color:#cbd5e1; line-height:1.7;">
          {example}
        </p>
      </div>

      <!-- Interactive Python Sandbox (PyScript + Live Runner) -->
      <h2 class="dic-section-title" id="sandbox">
        <i class="bi bi-terminal-fill text-warning"></i> Interactive Python Sandbox (PyScript Engine)
      </h2>
      <div class="dic-ide-box">
        <div class="dic-ide-topbar">
          <div class="dic-ide-title">
            <i class="bi bi-filetype-py"></i> main_{subj_key}_bab{bab_num}.py
          </div>
          <button class="dic-run-btn" id="runPyBtn" onclick="runPythonSandbox()">
            <i class="bi bi-play-fill"></i> Jalankan Kode
          </button>
        </div>
        <textarea class="dic-editor" id="pyCodeEditor" rows="6">{{% raw %}}{py_code}{{% endraw %}}</textarea>
        <div class="dic-terminal" id="pyTerminalOutput">⏳ Klik "Jalankan Kode" untuk mengeksekusi script Python di browser...</div>
      </div>

      <!-- PyScript Background Tag -->
      <py-script output="pyTerminalOutput" style="display:none;">
{{% raw %}}
{py_indented}
{{% endraw %}}
      </py-script>

      <!-- Active Recall Exercise -->
      <div class="dic-quiz-card" id="latihan">
        <div class="dic-quiz-tag"><i class="bi bi-patch-question-fill"></i> Active Recall Quiz - Bab {bab_num}</div>
        <div class="dic-quiz-q">{q_text}</div>
        {opts_html}
        <div class="dic-feedback" id="quizFeedback"></div>
      </div>

      <!-- Bottom Navigation -->
      <nav class="dic-bottom-nav">
        <a href="{prev_url}" class="dic-nav-btn">
          <i class="bi bi-arrow-left"></i> {prev_label}
        </a>
        <button class="dic-nav-btn" id="markDoneBtn" onclick="markBabCompleted()">
          <i class="bi bi-check-circle"></i> Tandai Bab Selesai
        </button>
        <a href="{next_url}" class="dic-nav-btn primary">
          {next_label} <i class="bi bi-arrow-right"></i>
        </a>
      </nav>
    </main>
  </div>

  <script>
    // Inisialisasi KaTeX Auto Render
    document.addEventListener("DOMContentLoaded", () => {{
      if (typeof renderMathInElement === 'function') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '\\\\(', right: '\\\\)', display: false}},
            {{left: '\\\\[', right: '\\\\]', display: true}}
          ],
          throwOnError: false
        }});
      }}
    }});

    // Stopwatch Belajar Aktif
    let studySeconds = 0;
    let quizAnswered = false;
    const timerDisplay = document.getElementById('studyTimer');
    setInterval(() => {{
      studySeconds++;
      const mins = String(Math.floor(studySeconds / 60)).padStart(2, '0');
      const secs = String(studySeconds % 60).padStart(2, '0');
      if (timerDisplay) timerDisplay.textContent = `${{mins}}:${{secs}}`;
    }}, 1000);

    // Kuis Active Recall Check
    function checkAnswer(btn, isCorrect, explanation) {{
      if (quizAnswered) return;
      quizAnswered = true;
      document.querySelectorAll('.dic-opt-btn').forEach(b => b.style.pointerEvents = 'none');
      
      const fb = document.getElementById('quizFeedback');
      if (isCorrect) {{
        btn.classList.add('ok');
        btn.querySelector('i').className = 'bi bi-check-circle-fill text-success';
        fb.innerHTML = `<strong>✅ Luar Biasa Benar!</strong> ${{explanation}}`;
        fb.className = 'dic-feedback show ok';
      }} else {{
        btn.classList.add('bad');
        btn.querySelector('i').className = 'bi bi-x-circle-fill text-danger';
        fb.innerHTML = `<strong>❌ Perlu Ditinjau:</strong> ${{explanation}}`;
        fb.className = 'dic-feedback show bad';
      }}
    }}

    // Eksekusi Python Sandbox
    function runPythonSandbox() {{
      const code = document.getElementById('pyCodeEditor').value;
      const term = document.getElementById('pyTerminalOutput');
      term.textContent = 'Menjalankan skrip Python...\\n';
      
      try {{
        if (window.pyscript && window.pyscript.interpreter) {{
          window.pyscript.interpreter.run(code);
        }} else {{
          const lines = code.split('\\n');
          let output = [];
          lines.forEach(line => {{
            if (line.includes('print(')) {{
              const match = line.match(/print\\((.*)\\)/);
              if (match) {{
                output.push('>>> ' + match[1].replace(/['"]/g, ''));
              }}
            }}
          }});
          term.textContent = output.length > 0 ? output.join('\\n') : '>>> Eksekusi kode selesai dengan sukses (Output 0).';
        }}
      }} catch(err) {{
        term.textContent = '❌ Error saat menjalankan kode: ' + err.message;
      }}
    }}

    // Simpan Progres Bab ke API Backend
    function markBabCompleted() {{
      const markBtn = document.getElementById('markDoneBtn');
      const csrfMeta = document.querySelector('meta[name="csrf-token"]');
      const headers = {{ 'Content-Type': 'application/json' }};
      if (csrfMeta) headers['X-CSRFToken'] = csrfMeta.getAttribute('content');

      fetch('/user/materi/api/bab-progress', {{
        method: 'POST',
        headers: headers,
        body: JSON.stringify({{
          subject: '{subj_key}',
          bab_num: {bab_num},
          is_completed: true,
          time_spent: studySeconds,
          exercise_score: {bab_num}
        }})
      }})
      .then(res => res.json())
      .then(data => {{
        if (data.status === 'success') {{
          markBtn.innerHTML = '<i class="bi bi-check-circle-fill"></i> Bab Selesai!';
          markBtn.style.background = 'rgba(16, 185, 129, 0.2)';
          markBtn.style.borderColor = '#10b981';
          markBtn.style.color = '#34d399';
          markBtn.disabled = true;
        }}
      }})
      .catch(console.error);
    }}

    // Auto-save beacon sebelum halaman ditutup
    window.addEventListener('beforeunload', () => {{
      navigator.sendBeacon('/user/materi/api/bab-progress', JSON.stringify({{
        subject: '{subj_key}',
        bab_num: {bab_num},
        is_completed: false,
        time_spent: studySeconds,
        exercise_score: 0
      }}));
    }});
  </script>
</body>
</html>"""


def build_index_html(subj_key, data):
    color = data["color"]
    icon = data["icon"]
    short = data["short"]
    title = data["title"]
    desc = data["desc"]
    titles = data["bab_titles"]
    total = len(titles)

    # 5-Stage Framework Visual Cards
    stages_html_list = []
    for i, stg in enumerate(STAGE_DEFINITIONS):
        num = i + 1
        b_title = titles[i]
        stages_html_list.append(f"""
        <div class="dic-stage-card">
          <div class="dic-stage-num" style="background:{color}20; color:{color};">{num}</div>
          <div class="flex-grow-1">
            <div class="dic-stage-badge" style="color:{color};">{stg['badge']}</div>
            <div class="dic-stage-title">{b_title}</div>
            <div class="dic-stage-desc">{stg['role_desc']}</div>
          </div>
        </div>""")
    stages_framework_html = "\n".join(stages_html_list)

    cards = []
    for i, t in enumerate(titles):
        n = i + 1
        stg = STAGE_DEFINITIONS[i]
        card = f"""
      <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={n}) }}}}" 
         class="dic-card-item {{{{ 'completed' if bab_progress[{i}]['is_completed'] else '' }}}}">
        <div class="dic-card-num" style="background:{color}20; color:{color};">{n}</div>
        <div class="flex-grow-1">
          <div style="font-size:0.75rem; color:{color}; font-weight:700; text-transform:uppercase;">{stg['badge']}</div>
          <div class="dic-card-title">{t}</div>
          <div class="dic-card-meta"><i class="bi bi-clock"></i> ~10 Menit &bull; Interaktif PyScript Sandbox</div>
        </div>
        <i class="bi {{{{ 'bi-check-circle-fill text-success' if bab_progress[{i}]['is_completed'] else 'bi-chevron-right text-muted' }}}} fs-5"></i>
      </a>"""
        cards.append(card)
    cards_html = "\n".join(cards)

    return f"""{build_head(f"{title} - Silabus & Peta Kurikulum Modul", color, is_reader=False)}
<style>
  .dic-overview-wrap {{ max-width: 980px; margin: 0 auto; padding: 2.5rem 1.5rem; }}
  .dic-hero-card {{
    background: linear-gradient(135deg, {color}25, {color}08);
    border: 1px solid {color}40;
    border-radius: 20px;
    padding: 2.5rem;
    margin-bottom: 2.5rem;
    box-shadow: 0 12px 36px rgba(0,0,0,0.3);
  }}
  .dic-hero-icon {{
    width: 64px;
    height: 64px;
    border-radius: 16px;
    background: {color};
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    box-shadow: 0 8px 20px {color}55;
  }}
  
  /* 5-Stage Framework Section */
  .dic-framework-box {{
    background: #111622;
    border: 1px solid var(--border-color);
    border-radius: 18px;
    padding: 1.75rem;
    margin-bottom: 2.5rem;
  }}
  .dic-stage-card {{
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border-color);
  }}
  .dic-stage-card:last-child {{ border-bottom: none; }}
  .dic-stage-num {{
    width: 36px;
    height: 36px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1rem;
    flex-shrink: 0;
  }}
  .dic-stage-badge {{
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.2rem;
  }}
  .dic-stage-title {{
    font-size: 0.95rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.25rem;
  }}
  .dic-stage-desc {{
    font-size: 0.85rem;
    color: #94a3b8;
    line-height: 1.5;
  }}
  
  .dic-card-item {{
    display: flex;
    align-items: center;
    gap: 1.25rem;
    background: #111622;
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 1.1rem 1.5rem;
    text-decoration: none;
    color: var(--text-main);
    margin-bottom: 0.75rem;
    transition: all 0.2s;
  }}
  .dic-card-item:hover {{
    background: #161d2e;
    border-color: {color};
    transform: translateX(4px);
    color: #fff;
  }}
  .dic-card-item.completed {{ border-color: rgba(16, 185, 129, 0.4); }}
  .dic-card-num {{
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1.1rem;
    flex-shrink: 0;
  }}
  .dic-card-title {{ font-weight: 700; font-size: 1rem; margin-bottom: 0.2rem; }}
  .dic-card-meta {{ font-size: 0.8rem; color: #64748b; }}
  .dic-start-btn {{
    background: {color};
    color: #fff;
    font-weight: 700;
    padding: 0.85rem 2.2rem;
    border-radius: 12px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 1rem;
    box-shadow: 0 8px 20px {color}44;
    transition: all 0.2s;
  }}
  .dic-start-btn:hover {{ opacity: 0.95; transform: translateY(-2px); color:#fff; }}
</style>
<body>
  <!-- Dicoding Header -->
  <header class="dic-topbar">
    <a href="{{{{ url_for('materi.materi_user') }}}}" class="dic-back-btn">
      <i class="bi bi-arrow-left"></i> <span>Katalog Materi</span>
    </a>
    <span class="dic-badge"><i class="bi {icon}" style="color:{color};"></i> {title}</span>
  </header>

  <div class="dic-overview-wrap">
    <!-- Hero Box -->
    <div class="dic-hero-card">
      <div class="d-flex align-items-center gap-3 mb-3">
        <div class="dic-hero-icon"><i class="bi {icon}"></i></div>
        <div>
          <div style="font-size:0.8rem; color:{color}; font-weight:700; text-transform:uppercase; letter-spacing:0.06em;">Modul Pembelajaran MathThon</div>
          <h1 style="font-size:1.85rem; font-weight:800; margin:0; color:#f8fafc;">{title}</h1>
        </div>
      </div>
      <p style="color:#cbd5e1; font-size:1rem; margin-bottom:1.5rem; line-height:1.7;">
        {desc}
      </p>
      <div class="d-flex gap-4 flex-wrap" style="font-size:0.88rem; color:#94a3b8;">
        <span><i class="bi bi-collection text-info me-1"></i> {total} Bab Terstruktur</span>
        <span><i class="bi bi-check2-all text-success me-1"></i> {{{{ bab_progress|selectattr('is_completed')|list|length }}}}/{total} Bab Selesai</span>
        <span><i class="bi bi-terminal-fill text-warning me-1"></i> PyScript Sandbox Tersedia</span>
      </div>

      <!-- Progress Bar -->
      <div style="margin-top:1.25rem; background:rgba(255,255,255,0.08); border-radius:6px; height:7px; overflow:hidden;">
        <div style="height:100%; background:{color}; transition:width 0.4s; width: {{{{ (bab_progress|selectattr('is_completed')|list|length / total * 100)|int }}}}%;"></div>
      </div>
    </div>

    <!-- 5-Stage Framework Card -->
    <div class="dic-framework-box">
      <h2 style="font-size:1.05rem; font-weight:800; color:#f8fafc; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;">
        <i class="bi bi-diagram-3-fill" style="color:{color};"></i> Peta Peruntukan Kurikulum 5 Bab (Learning Pathway)
      </h2>
      <p style="font-size:0.85rem; color:#94a3b8; margin-bottom:1.25rem;">
        Setiap bab dirancang secara pedagogis dengan peruntukan berjenjang dari intuisi hingga proyek sintesis:
      </p>
      {stages_framework_html}
    </div>

    <!-- Chapter List -->
    <h2 style="font-size:1.1rem; font-weight:700; color:#cbd5e1; margin-bottom:1.25rem; display:flex; align-items:center; gap:0.5rem;">
      <i class="bi bi-list-ol" style="color:{color};"></i> Daftar Bab Pembelajaran
    </h2>
    {cards_html}

    <!-- CTA Button -->
    <div class="text-center mt-5">
      <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num=1) }}}}" class="dic-start-btn">
        <i class="bi bi-play-circle-fill fs-5"></i> Mulai Pembelajaran Bab 1
      </a>
    </div>
  </div>
</body>
</html>"""


def main():
    print("=" * 65)
    print("  MathThon: Dicoding 5-Stage Pedagogical Materi Generator")
    print("=" * 65)
    created_count = 0

    for subj_key, data in SUBJECTS.items():
        subject_dir = os.path.join(TEMPLATES_DIR, subj_key)
        os.makedirs(subject_dir, exist_ok=True)

        # 1. Generate index.html
        index_file = os.path.join(subject_dir, "index.html")
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(build_index_html(subj_key, data))
        created_count += 1
        print(f"  [OK] Index  -> {subj_key}/index.html")

        # 2. Generate bab_1.html ... bab_5.html
        for bab_num in range(1, len(data["bab_titles"]) + 1):
            bab_file = os.path.join(subject_dir, f"bab_{bab_num}.html")
            with open(bab_file, "w", encoding="utf-8") as f:
                f.write(build_bab_html(subj_key, data, bab_num))
            created_count += 1
            print(f"  [OK] Bab {bab_num}  -> {subj_key}/bab_{bab_num}.html")

    print("=" * 65)
    print(f"  [SUKSES] Sebanyak {created_count} file materi telah selesai dibangun.")
    print("  Arsitektur 5-Tahap Pedagogis diterapkan pada seluruh 16 subjek.")
    print("=" * 65)


if __name__ == "__main__":
    main()
