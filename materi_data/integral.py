# -*- coding: utf-8 -*-
DATA = {
    "title": "Integral & Kalkulus Integral",
    "short": "Integral",
    "icon": "bi-infinity",
    "color": "#10b981",
    "desc": "Kuasai konsep akumulasi kontinu, antiturunan, integral tak tentu (+ C), integral tentu luas daerah Riemann, teknik substitusi, dan aplikasinya dalam fisika dan teknik.",
    "babs": [
        {
            "title": "Fondasi: Paradoks Menghitung Luas Kurva Melengkung",
            "objectives": [
                "Memahami limit partisi jumlah Riemann persegi panjang menuju luas eksak kontinu.",
                "Memahami Teorema Dasar Kalkulus yang menghubungkan turunan dan integral sebagai proses inversi.",
                "Membedakan konsep Integral Tak Tentu (fungsi antiturunan) dan Integral Tentu (nilai skalar luas batas)."
            ],
            "hook": "Bagaimana kamu menghitung luas persegi panjang? Cukup panjang kali lebar. Bagaimana dengan segitiga? Setengah alas kali tinggi. Tetapi bagaimana jika lantaimu memiliki batas melengkung seperti kurva parabola atau danau berliuk? Rumus geometri klasik menyerah! Kalkulus Integral hadir sebagai mukjizat intelektual: memecah bidang melengkung menjadi miliaran persegi panjang ultra-ramping lalu menjumlahkannya hingga menghasilkan luas eksak tanpa ada celah sedikit pun!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-bounding-box-circles text-primary\"></i> 1. Partisi Jumlah Riemann Menuju Integral</h3>\n              <p>Luas daerah di bawah kurva $y = f(x)$ dari $x = a$ hingga $x = b$ diaproksimasi dengan membagi interval menjadi $n$ persegi panjang berlebar $\\Delta x$:</p>\n              \\[ L \\approx \\sum_{i=1}^n f(x_i) \\Delta x \\]\n              <p>Ketika jumlah partisi ditarik menuju tak terhingga ($n \\to \\infty$), lebar $\\Delta x$ menyusut menjadi diferensial infinitesimal $dx$, dan simbol sigma $\\sum$ bermutasi menjadi simbol integral memanjang $\\int$ (dari huruf S Latin, <em>Summa</em>):</p>\n              \\[ \\int_a^b f(x) dx = \\lim_{n \\to \\infty} \\sum_{i=1}^n f(x_i) \\Delta x \\]\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrow-repeat text-primary\"></i> 2. Teorema Dasar Kalkulus (The Fundamental Theorem)</h3>\n              <p>Integral dan Turunan adalah dua sisi mata uang yang saling membatalkan (proses invers). Jika $F'(x) = f(x)$, maka:</p>\n              \\[ \\int f(x) dx = F(x) + C \\quad \\text{dan} \\quad \\int_a^b f(x) dx = F(b) - F(a) \\]\n            </div>\n            ",
            "pro_tip": "Jangan pernah lupa menuliskan konstanta integrasi $+ C$ pada Integral Tak Tentu! Huruf C mewakili keluarga fungsi tak berhingga banyaknya yang memiliki kemiringan turunan yang sama.",
            "pitfall": "Pada Integral Tentu dengan batas $[a, b]$, konstanta $+ C$ tidak perlu ditulis lagi karena akan saling mengurangkan: $[F(b) + C] - [F(a) + C] = F(b) - F(a)$.",
            "fun_fact": "Simbol integral yang elegan $\\int$ dirancang oleh matematikawan Jerman Gottfried Wilhelm Leibniz pada tahun 1675. Huruf 'S' panjang tersebut melambangkan kata 'Summa' (penjumlahan tak terhingga).",
            "formula": "\\int x^n dx = \\frac{1}{n + 1} x^{n + 1} + C \\quad (n \\neq -1) \\quad ; \\quad \\int_a^b f(x) dx = [F(x)]_a^b = F(b) - F(a)",
            "formula_params": [
                [
                    "\\int",
                    "Simbol integral (operator akumulasi kontinu)."
                ],
                [
                    "f(x)",
                    "Integran (fungsi yang diintegrasikan)."
                ],
                [
                    "dx",
                    "Diferensial variabel integrasi."
                ],
                [
                    "C",
                    "Konstanta integrasi sembarang."
                ],
                [
                    "F(b) - F(a)",
                    "Evaluasi batas atas dikurangi batas bawah."
                ]
            ],
            "formula_intuition": "Menambah pangkat variabel sebesar 1 dan membaginya dengan pangkat baru tersebut (kebalikan dari aturan pangkat turunan).",
            "example": {
                "question": "Hitunglah: (a) Integral tak tentu $\\int (3x^2 + 4x - 5) dx$, dan (b) Nilai integral tentu $\\int_1^3 2x dx$!",
                "known": "Fungsi integran polinomial aljabar.",
                "asked": "Hasil integrasi tak tentu dan tentu.",
                "steps": [
                    [
                        "Langkah 1: Integrasikan Suku per Suku untuk Soal (a)",
                        "$\\int 3x^2 dx = 3 \\cdot \\frac{x^3}{3} = x^3$.<br>$\\int 4x dx = 4 \\cdot \\frac{x^2}{2} = 2x^2$.<br>$\\int -5 dx = -5x$."
                    ],
                    [
                        "Langkah 2: Tambahkan Konstanta C",
                        "$x^3 + 2x^2 - 5x + C$."
                    ],
                    [
                        "Langkah 3: Hitung Antiturunan untuk Soal (b)",
                        "$\\int 2x dx = x^2$."
                    ],
                    [
                        "Langkah 4: Masukkan Batas Atas x = 3 dan Batas Bawah x = 1",
                        "$[x^2]_1^3 = (3^2) - (1^2) = 9 - 1 = 8$."
                    ]
                ],
                "conclusion": "(a) Hasil integral tak tentu adalah $x^3 + 2x^2 - 5x + C$. (b) Nilai luas integral tentu adalah 8 satuan luas."
            },
            "takeaways": [
                "Integral adalah antiturunan (kebalikan dari diferensial) dan operator akumulasi luas.",
                "Rumus dasar pangkat integral: $\\int x^n dx = \\frac{1}{n+1} x^{n+1} + C$.",
                "Integral tentu menghitung akumulasi netto pada interval batas $[a, b]$ melalui $F(b) - F(a)$."
            ],
            "quiz": [
                "Berapakah hasil dari integral tak tentu $\\int 6x^2 dx$?",
                [
                    "2x³ + C",
                    "3x³ + C",
                    "12x + C"
                ],
                0,
                "\\int 6x^2 dx = 6 * (x^3 / 3) + C = 2x^3 + C."
            ]
        },
        {
            "title": "Anatomi: Kaidah Integral Aljabar Baku & Sifat Kelinearan",
            "objectives": [
                "Menguasai sifat kelinearan integral terhadap perkalian skalar dan penjumlahan.",
                "Mengintegrasikan bentuk pecahan pangkat aljabar dan bentuk akar x^(p/q).",
                "Memahami kasus khusus pangkat n = -1 yang menghasilkan logaritma natural (integral 1/x dx = ln|x| + C)."
            ],
            "hook": "Perhatikan rumus pangkat integral $\\frac{x^{n+1}}{n+1}$. Apa yang terjadi jika nilai n = -1? Penyebutnya akan menjadi nol (-1 + 1 = 0), yang terlarang dalam matematika! Ke mana arah rumus ini pergi? Ternyata untuk kasus $n = -1$, integral melahirkan fungsi istimewa baru: Logaritma Natural $\\ln|x|$! Fakta anatomis ini menghubungkan aljabar dan fungsi transenden secara menakjubkan.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-journal-code text-primary\"></i> 1. Sifat Kelinearan Integral</h3>\n              <ul class=\"dic-list\">\n                <li>$\\int k \\cdot f(x) dx = k \\int f(x) dx$ (Konstanta pengali dapat dikeluarkan ke depan integral).</li>\n                <li>$\\int [f(x) \\pm g(x)] dx = \\int f(x) dx \\pm \\int g(x) dx$ (Integral penjumlahan dapat dipecah menjadi masing-masing suku).</li>\n                <li><strong>Kasus Pangkat $n = -1$:</strong>\n                  \\[ \\int \\frac{1}{x} dx = \\ln|x| + C \\]\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Jika menemui bentuk pecahan aljabar dengan penyebut suku tunggal, pecah menjadi beberapa pecahan terpisah sebelum diintegrasikan! Contoh: $\\frac{x^2 + 1}{x} = x + \\frac{1}{x}$.",
            "pitfall": "Integral dari perkalian BUKAN perkalian dari integral! $\\int f(x)g(x) dx \\neq \\int f(x)dx \\cdot \\int g(x)dx$. Kamu harus mengekspansinya terlebih dahulu!",
            "fun_fact": "Fungsi logaritma natural $\\ln x$ sebenarnya secara historis didefinisikan secara murni sebagai luas area di bawah kurva hiperbola $y = 1/t$ dari $1$ hingga $x$.",
            "formula": "\\int \\left(a x^n + \\frac{b}{x}\\right) dx = \\frac{a}{n+1}x^{n+1} + b\\ln|x| + C \\quad (n \\neq -1)",
            "formula_params": [
                [
                    "n \\neq -1",
                    "Syarat berlakunya aturan pangkat aljabar biasa."
                ],
                [
                    "\\ln|x|",
                    "Logaritma natural berbasis bilangan Euler e (2.71828...)."
                ]
            ],
            "formula_intuition": "Mengintegrasikan fungsi hiperbolik yang mengisi kekosongan hukum pangkat kalkulus.",
            "example": {
                "question": "Selesaikan integral berikut: $\\int \\left( 5x^4 + \\frac{3}{x} - \\frac{2}{x^2} \\right) dx$!",
                "known": "Ekspresi penjumlahan tiga jenis suku pangkat.",
                "asked": "Hasil integrasi antiturunan.",
                "steps": [
                    [
                        "Langkah 1: Ubah Suku Pecahan ke Bentuk Pangkat Negatif",
                        "$-2/x^2 = -2x^{-2}$."
                    ],
                    [
                        "Langkah 2: Integrasikan Suku Pertama $5x^4$",
                        "$5 \\cdot \\frac{x^5}{5} = x^5$."
                    ],
                    [
                        "Langkah 3: Integrasikan Suku Kedua $3/x$",
                        "$3\\ln|x|$."
                    ],
                    [
                        "Langkah 4: Integrasikan Suku Ketiga $-2x^{-2}$",
                        "$-2 \\cdot \\frac{x^{-2 + 1}}{-2 + 1} = -2 \\cdot \\frac{x^{-1}}{-1} = 2x^{-1} = \\frac{2}{x}$."
                    ],
                    [
                        "Langkah 5: Gabungkan Seluruh Suku dengan $+ C$",
                        "$x^5 + 3\\ln|x| + \\frac{2}{x} + C$."
                    ]
                ],
                "conclusion": "Hasil integralnya adalah $x^5 + 3\\ln|x| + \\frac{2}{x} + C$."
            },
            "takeaways": [
                "Integral bersifat linear: dapat dipisahkan per suku dan konstanta dapat ditarik ke depan.",
                "Pangkat pecahan dan pangkat negatif wajib diintegrasikan dengan hati-hati pada tanda aritmatika.",
                "Khusus suku $\\frac{1}{x}$, antiturunannya menghasilkan $\\ln|x| + C$."
            ],
            "quiz": [
                "Berapakah hasil dari $\\int \\left(4x^3 + \\frac{1}{x}\\right) dx$?",
                [
                    "x⁴ + ln|x| + C",
                    "12x² - 1/x² + C",
                    "x⁴ + 1 + C"
                ],
                0,
                "\\int 4x^3 dx = x^4, dan \\int (1/x) dx = \\ln|x|. Jadi hasilnya x^4 + \\ln|x| + C."
            ]
        },
        {
            "title": "Mekanika: Teknik Integrasi Substitusi Aljabar (Metode Pemisalan u)",
            "objectives": [
                "Mengenali bentuk integral yang dapat diselesaikan dengan metode substitusi u (pola f(g(x)) * g'(x)).",
                "Melakukan transformasi variabel dari x menjadi variabel baru u dan du.",
                "Mengubah batas integrasi pada integral tentu saat melakukan substitusi variabel."
            ],
            "hook": "Bagaimana kamu menyelesaikan integral yang rumit seperti $\\int 2x (x^2 + 5)^7 dx$? Jika kamu harus mengekspansikan pangkat 7 secara manual, kamu butuh waktu seharian! Tetapi perhatikan trik ini: turunan dari $(x^2 + 5)$ adalah $2x$ yang tepat berada di sampingnya! Metode Substitusi adalah teknik penyamaran variabel yang menyederhanakan monster aljabar rumit menjadi bentuk dasar $\\int u^7 du$ yang sangat ramah anak!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-magic text-primary\"></i> 1. Prinsip Metode Substitusi u</h3>\n              <p>Metode substitusi adalah kebalikan dari Aturan Rantai (Chain Rule) pada turunan. Langkah proseduralnya:</p>\n              <ol class=\"dic-list\">\n                <li><strong>Pilih Pemisalan $u$:</strong> Pilih fungsi yang berada di dalam kurung atau pangkat yang turunannya muncul sebagai pengali di bagian lain integral.</li>\n                <li><strong>Hitung Turunan $du$:</strong> $u = g(x) \\implies du = g'(x) dx \\implies dx = \\frac{du}{g'(x)}$.</li>\n                <li><strong>Substitusikan ke Soal:</strong> Gantikan seluruh ekspresi $x$ menjadi variabel tunggal $u$. Semua variabel $x$ HARUS LENYAP!</li>\n                <li><strong>Integrasikan terhadap $u$:</strong> $\\int u^n du = \\frac{1}{n+1} u^{n+1} + C$.</li>\n                <li><strong>Kembalikan ke Variabel Asal $x$.</strong></li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Pedoman memilih u: Biasanya u adalah bagian fungsi yang memiliki pangkat lebih tinggi satu derajat dibandingkan fungsi pengalinya di luar!",
            "pitfall": "Jangan biarkan ada variabel x yang tersisa saat mengintegrasikan u! Jika masih ada variabel x yang tidak bisa dicoret, kemungkinan pemisalan u kamu salah atau memerlukan manipulasi aljabar lanjutan.",
            "fun_fact": "Metode substitusi adalah bentuk paling sederhana dari Teorema Perubahan Variabel (Change of Variables) yang digunakan dalam fisika kuantum untuk mengubah koordinat Cartesius menjadi koordinat bola ruang Hilbert.",
            "formula": "\\int f(g(x)) g'(x) dx = \\int f(u) du \\quad \\text{dengan } u = g(x), \\ du = g'(x)dx",
            "formula_params": [
                [
                    "u = g(x)",
                    "Fungsi dalam yang dimisalkan."
                ],
                [
                    "du = g'(x)dx",
                    "Diferensial turunan pengait."
                ]
            ],
            "formula_intuition": "Menyederhanakan struktur ekspresi dengan memadatkan fungsi komposisi menjadi variabel tunggal.",
            "example": {
                "question": "Hitunglah hasil integral: $\\int 2x (x^2 + 3)^5 dx$!",
                "known": "Integran memuat fungsi $(x^2 + 3)^5$ dan faktor pengali $2x$.",
                "asked": "Hasil integrasi metode substitusi.",
                "steps": [
                    [
                        "Langkah 1: Tentukan Pemisalan u",
                        "Misalkan $u = x^2 + 3$."
                    ],
                    [
                        "Langkah 2: Cari Diferensial du",
                        "$\\frac{du}{dx} = 2x \\implies du = 2x dx \\implies dx = \\frac{du}{2x}$."
                    ],
                    [
                        "Langkah 3: Substitusikan ke Integral Awal",
                        "$\\int 2x \\cdot u^5 \\cdot \\left(\\frac{du}{2x}\\right) = \\int u^5 du$ (Variabel $2x$ saling mencoret!)."
                    ],
                    [
                        "Langkah 4: Integrasikan terhadap u",
                        "$\\frac{1}{5 + 1} u^6 + C = \\frac{1}{6} u^6 + C$."
                    ],
                    [
                        "Langkah 5: Kembalikan Nilai u Asal",
                        "$\\frac{1}{6} (x^2 + 3)^6 + C$."
                    ]
                ],
                "conclusion": "Hasil integral adalah $\\frac{1}{6} (x^2 + 3)^6 + C$."
            },
            "takeaways": [
                "Metode substitusi digunakan ketika ada fungsi komposisi beserta turunannya di dalam integral.",
                "Seluruh komponen variabel x harus berhasil ditransformasikan sepenuhnya menjadi variabel u.",
                "Hasil integrasi u selalu dikembalikan ke fungsi variabel x asli di akhir perhitungan."
            ],
            "quiz": [
                "Hasil dari $\\int 3x^2 (x^3 + 1)^4 dx$ adalah?",
                [
                    "⅕ (x³ + 1)⁵ + C",
                    "(x³ + 1)⁵ + C",
                    "¼ (x³ + 1)⁴ + C"
                ],
                0,
                "Misal u = x^3 + 1, maka du = 3x^2 dx. Integral menjadi \\int u^4 du = (1/5)u^5 + C = (1/5)(x^3 + 1)^5 + C."
            ]
        },
        {
            "title": "Pemodelan: Menghitung Luas Daerah Antara Dua Kurva",
            "objectives": [
                "Memodelkan luas daerah di bawah kurva tunggal terhadap sumbu X.",
                "Menentukan titik potong dua kurva sebagai batas bawah a dan batas atas b.",
                "Menghitung luas daerah tertutup di antara dua kurva: Integral (Kurva Atas - Kurva Bawah) dx."
            ],
            "hook": "Berapakah luas sebidang tanah perkebunan yang dibatasi oleh aliran sungai yang melengkung parabolik dan garis batas jalan raya yang lurus? Mengukur langsung dengan meteran tanah mustahil menghasilkan angka presisi. Menggunakan formula kalkulus Integral Kurva Atas dikurangi Kurva Bawah, surveyor dan arsitek lanskap dapat menentukan luas tanah hingga sentimeter persegi secara presisi!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-intersect text-primary\"></i> 1. Formula Luas Daerah Antara Dua Kurva</h3>\n              <p>Jika kurva $y_1 = f(x)$ berada di atas kurva $y_2 = g(x)$ pada interval $[a, b]$, maka luas daerah tertutup yang dibentuk di antara keduanya dirumuskan sebagai:</p>\n              \\[ L = \\int_a^b [y_{\\text{atas}} - y_{\\text{bawah}}] dx = \\int_a^b [f(x) - g(x)] dx \\]\n              <ul class=\"dic-list\">\n                <li>Batas integrasi $a$ dan $b$ diperoleh dari <strong>titik potong kedua kurva</strong> ($f(x) = g(x)$).</li>\n                <li>Luas daerah <strong>SELALU BERNILAI POSITIF</strong> ($L > 0$).</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mengetahui kurva mana yang berada di 'atas' dan 'bawah' tanpa menggambar grafik secara detail: Ambil satu angka uji sebarang di antara batas $a$ dan $b$, lalu masukkan ke kedua fungsi. Fungsi yang menghasilkan nilai y lebih besar adalah kurva ATAS!",
            "pitfall": "Jangan sampai terbalik mengurangkan kurva! Jika kamu menghitung Kurva Bawah dikurangi Kurva Atas, hasil integralmu akan bertanda negatif ($-L$). Luas fisik tidak pernah bernilai negatif!",
            "fun_fact": "Dalam ilmu ekonomi, konsep luas antara dua kurva ini dinamakan Surplus Konsumen dan Surplus Produsen pada perpotongan kurva permintaan dan penawaran pasar bebas.",
            "formula": "Luas = \\int_a^b [f(x) - g(x)] dx \\quad \\text{dengan } f(x) \\ge g(x) \\text{ pada } [a, b]",
            "formula_params": [
                [
                    "f(x)",
                    "Fungsi kurva batas atas."
                ],
                [
                    "g(x)",
                    "Fungsi kurva batas bawah."
                ],
                [
                    "a, b",
                    "Koordinat titik potong persekutuan."
                ]
            ],
            "formula_intuition": "Mengurangkan tinggi balok elemen atas dengan tinggi balok elemen bawah untuk mendapatkan luas partisi murni.",
            "example": {
                "question": "Hitunglah luas daerah yang dibatasi oleh kurva parabola $y = 4 - x^2$ dan garis lurus $y = 0$ (sumbu X)!",
                "known": "Kurva atas $y = 4 - x^2$ dan kurva bawah $y = 0$.",
                "asked": "Batas integrasi dan luas daerah.",
                "steps": [
                    [
                        "Langkah 1: Tentukan Titik Potong (Batas a dan b)",
                        "$4 - x^2 = 0 \\implies x^2 = 4 \\implies x = -2$ dan $x = 2$.<br>Maka batas bawah $a = -2$ dan batas atas $b = 2$."
                    ],
                    [
                        "Langkah 2: Susun Integral Luas",
                        "$L = \\int_{-2}^2 (4 - x^2) dx$."
                    ],
                    [
                        "Langkah 3: Cari Antiturunan",
                        "$\\left[ 4x - \\frac{x^3}{3} \\right]_{-2}^2$."
                    ],
                    [
                        "Langkah 4: Masukkan Batas Atas x = 2",
                        "$\\left( 4(2) - \\frac{2^3}{3} \\right) = 8 - \\frac{8}{3} = \\frac{16}{3}$."
                    ],
                    [
                        "Langkah 5: Masukkan Batas Bawah x = -2",
                        "$\\left( 4(-2) - \\frac{(-2)^3}{3} \\right) = -8 + \\frac{8}{3} = -\\frac{16}{3}$."
                    ],
                    [
                        "Langkah 6: Kurangkan Batas Atas dengan Batas Bawah",
                        "$L = \\frac{16}{3} - \\left(-\\frac{16}{3}\\right) = \\frac{32}{3} = 10\\frac{2}{3}$ satuan luas."
                    ]
                ],
                "conclusion": "Luas daerah tertutup tersebut adalah 32/3 (atau sekitar 10.67) satuan luas."
            },
            "takeaways": [
                "Luas antara dua kurva selalu dirumuskan sebagai $\\int (y_{\\text{atas}} - y_{\\text{bawah}}) dx$.",
                "Batas integrasi diperoleh dari absis x titik potong kedua kurva.",
                "Nilai luas area fisik harus selalu positif."
            ],
            "quiz": [
                "Berapakah luas daerah yang dibatasi oleh garis y = 2x, sumbu X, dan garis x = 3?",
                [
                    "9 satuan luas",
                    "6 satuan luas",
                    "18 satuan luas"
                ],
                0,
                "L = \\int_0^3 2x dx = [x^2]_0^3 = 3^2 - 0 = 9 satuan luas."
            ]
        },
        {
            "title": "Capstone: Estimasi Total Akumulasi Cadangan Energi Air Waduk PLTA",
            "objectives": [
                "Mengintegrasikan laju aliran fluida debit air Q(t) terhadap waktu untuk menghitung akumulasi volume air total.",
                "Menghitung potensi energi gravitasi listrik yang dibangkitkan turbin PLTA menggunakan kalkulus integral.",
                "Mengevaluasi keputusan manajemen pelepasan pintu air bendungan saat curah hujan ekstrem."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Hydrological Engineer pada Pembangkit Listrik Tenaga Air (PLTA) Waduk Cirata. Menjelang musim badai, debit air sungai yang mengalir masuk ke waduk berubah dinamis terhadap waktu mengikuti fungsi laju alir: Q(t) = 300 + 40t - 3t^2 (dalam meter kubik per jam) selama interval badai 10 jam (0 <= t <= 10). Tugasmu adalah menghitung: (1) Total volume air yang terakumulasi di dalam waduk, dan (2) Berapa Megawatt-hour estimasi cadangan energi listrik yang dapat dihasilkan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-droplet-fill text-warning\"></i> Pemodelan Akumulasi Debit Fluida</h3>\n              <p>Debit aliran fluida adalah laju perubahan volume terhadap waktu ($Q = \\frac{dV}{dt}$). Maka total volume air akumulasi $V_{\\text{total}}$ yang tertampung selama selang waktu $t = 0$ hingga $t = T$ diperoleh dari integral tentu debit:</p>\n              \\[ V_{\\text{total}} = \\int_0^T Q(t) dt \\]\n            </div>\n            ",
            "pro_tip": "Ingat prinsip fundamental fisika kalkulus: Integral dari 'Laju Perubahan' (kecepatan, debit, daya listrik) terhadap waktu SELALU menghasilkan 'Total Akumulasi Akumulatif' (jarak, volume, energi)!",
            "pitfall": "Perhatikan satuan waktu! Jika debit dinyatakan per jam, maka batas integrasi t juga harus dinyatakan dalam satuan jam yang selaras.",
            "fun_fact": "Simulasi hidrodinamika bendungan terbesar dunia, Three Gorges Dam di Tiongkok, menggunakan model integrasi volume elemen hingga kontinu untuk mengendalikan banjir Sungai Yangtze dan menghasilkan listrik lebih dari 100 miliar kilowatt-jam per tahun.",
            "formula": "V_{\\text{total}} = \\int_0^T Q(t) dt \\quad ; \\quad E_{\\text{listrik}} = \\eta \\cdot \\rho \\cdot g \\cdot h \\cdot V_{\\text{total}}",
            "formula_params": [
                [
                    "Q(t)",
                    "Laju debit air masuk waduk (m³/jam)."
                ],
                [
                    "T",
                    "Durasi periode pengamatan badai (jam)."
                ],
                [
                    "V_{\\text{total}}",
                    "Volume total air tertampung (m³)."
                ]
            ],
            "formula_intuition": "Mengakumulasikan laju aliran sesaat sepanjang selang waktu pemantauan.",
            "example": {
                "question": "Debit air masuk waduk dimodelkan oleh $Q(t) = 300 + 40t - 3t^2\\text{ m}^3/\\text{jam}$ selama periode badai 10 jam ($0 \\le t \\le 10$). Hitung total volume air yang tertampung di dalam waduk!",
                "known": "$Q(t) = 300 + 40t - 3t^2$ dan selang waktu $0 \\le t \\le 10\\text{ jam}$.",
                "asked": "Volume total $V_{\\text{total}}$.",
                "steps": [
                    [
                        "Langkah 1: Susun Rumus Integral Akumulasi",
                        "$V_{\\text{total}} = \\int_0^{10} (300 + 40t - 3t^2) dt$."
                    ],
                    [
                        "Langkah 2: Cari Antiturunan Aljabar",
                        "$\\left[ 300t + \\frac{40t^2}{2} - \\frac{3t^3}{3} \\right]_0^{10} = [300t + 20t^2 - t^3]_0^{10}$."
                    ],
                    [
                        "Langkah 3: Masukkan Batas Atas t = 10",
                        "$300(10) + 20(10^2) - (10^3) = 3000 + 20(100) - 1000 = 3000 + 2000 - 1000 = 4000\\text{ m}^3$."
                    ],
                    [
                        "Langkah 4: Masukkan Batas Bawah t = 0",
                        "$0 + 0 - 0 = 0$."
                    ],
                    [
                        "Langkah 5: Kurangkan Batas Atas dengan Batas Bawah",
                        "$V_{\\text{total}} = 4000 - 0 = 4000\\text{ meter kubik}$ (atau 4 juta liter)."
                    ]
                ],
                "conclusion": "Total volume air badai yang terakumulasi di dalam waduk adalah 4.000 meter kubik."
            },
            "takeaways": [
                "Kalkulus integral adalah alat utama pemodelan akumulasi fluida dan energi dalam sains rekayasa.",
                "Integral dari fungsi laju perubahan menghasilkan besaran kuantitas total yang terkumpul.",
                "Selamat! Kamu telah menuntaskan seluruh modul Integral & Kalkulus dengan pencapaian yang mengagumkan!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE INTEGRAL: Berapakah nilai volume yang terakumulasi jika debit konstan Q = 50 m³/jam mengalir selama 10 jam (dihitung via integral $\\int_0^{10} 50 dt$)?",
                [
                    "500 m³",
                    "250 m³",
                    "50 m³"
                ],
                0,
                "[50t] dari 0 sampai 10 = 50(10) - 0 = 500 m³."
            ]
        }
    ]
}
