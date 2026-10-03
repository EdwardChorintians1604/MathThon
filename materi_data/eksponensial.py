# -*- coding: utf-8 -*-
DATA = {
    "title": "Eksponen & Fungsi Eksponensial",
    "short": "Eksponen",
    "icon": "bi-arrow-up-right-circle",
    "color": "#f97316",
    "desc": "Kuasai sifat-sifat perpangkatan, eksponen pecahan dan negatif, grafik fungsi eksponensial, persamaan eksponen, serta pemodelan pertumbuhan dan peluruhan radioaktif.",
    "babs": [
        {
            "title": "Fondasi: Dari Penjumlahan Berulang Menuju Ledakan Eksponensial",
            "objectives": [
                "Memahami eksponen sebagai operasi perkalian berulang dari bilangan pokok basis.",
                "Memahami fenomena pertumbuhan eksponensial vs pertumbuhan linier.",
                "Menguasai definisi formal bilangan berpangkat nol (a^0 = 1) dan pangkat negatif (a^-n = 1/a^n)."
            ],
            "hook": "Jika kamu melipat selembar kertas biasa menjadi dua, lalu melipatnya lagi, dan lagi... jika kamu mampu melipat kertas itu sebanyak 42 kali, setebal apakah kertas tersebut? Kebanyakan orang mengira setinggi meja atau gedung. Padahal jawabannya mengejutkan dunia: Kertas itu akan mencapai BULAN! (Lebih dari 400.000 kilometer). Mengapa? Karena ketebalannya berlipat ganda secara eksponensial: $2^{42}$ lapis! Inilah kedahsyatan ledakan pertumbuhan eksponensial.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-graph-up-arrow text-primary\"></i> 1. Definisi & Notasi Eksponen</h3>\n              <p>Untuk setiap bilangan riil $a$ (basis) dan bilangan bulat positif $n$ (eksponen):</p>\n              \\[ a^n = \\underbrace{a \\times a \\times a \\times \\dots \\times a}_{n \\text{ faktor}} \\]\n              <ul class=\"dic-list\">\n                <li><strong>Basis Bilangan Pokok ($a$):</strong> Bilangan yang dikalikan berulang kali.</li>\n                <li><strong>Eksponen Pangkat ($n$):</strong> Banyaknya faktor pengali perkalian.</li>\n                <li><strong>Pangkat Nol ($a^0 = 1$):</strong> Setiap bilangan bukan nol dipangkatkan 0 selalu bernilai 1. Bukti: $\\frac{a^n}{a^n} = a^{n-n} = a^0 = 1$.</li>\n                <li><strong>Pangkat Negatif ($a^{-n} = \\frac{1}{a^n}$):</strong> Pangkat negatif merepresentasikan kebalikan perkalian (pecahan desimal).</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk memindahkan suku berpangkat dari pembilang ke penyebut (atau sebaliknya), cukup balikkan tanda pangkatnya! Contoh: $\\frac{1}{x^{-3}} = x^3$ dan $x^{-5} = \\frac{1}{x^5}$.",
            "pitfall": "Hati-hati dengan tanda negatif pada basis! $(-3)^2 = (-3) \\times (-3) = +9$, TETAPI $-3^2 = -(3 \\times 3) = -9$. Tanda kurung memegang peranan krusial!",
            "fun_fact": "Dalam legenda kuno India, penemu catur meminta hadiah kepada Raja berupa 1 butir beras di kotak catur pertama, 2 butir di kotak kedua, 4 di kotak ketiga, 8 di kotak keempat ($2^{n-1}$). Raja menyetujuinya tanpa sadar bahwa kotak ke-64 membutuhkan lebih dari 18 triliun butir beras—lebih banyak dari seluruh hasil panen bumi selama berabad-abad!",
            "formula": "a^0 = 1 \\quad (a \\neq 0) \\quad ; \\quad a^{-n} = \\frac{1}{a^n} \\quad ; \\quad a^{\\frac{m}{n}} = \\sqrt[n]{a^m}",
            "formula_params": [
                [
                    "a",
                    "Bilangan pokok (basis)."
                ],
                [
                    "n",
                    "Eksponen pangkat bulat."
                ],
                [
                    "m/n",
                    "Eksponen pecahan pembentuk bentuk akar."
                ]
            ],
            "formula_intuition": "Pangkat positif mengalikan maju, pangkat nol adalah titik netral 1, dan pangkat negatif membagi mundur.",
            "example": {
                "question": "Hitunglah nilai numerik dari: (a) $2^{-3}$, (b) $16^{3/4}$, dan (c) $(-5)^0 + (-2)^3$!",
                "known": "Operasi pangkat negatif, pecahan, dan nol.",
                "asked": "Nilai numerik eksak.",
                "steps": [
                    [
                        "Langkah 1: Hitung $2^{-3}$",
                        "$2^{-3} = \\frac{1}{2^3} = \\frac{1}{8} = 0.125$."
                    ],
                    [
                        "Langkah 2: Hitung $16^{3/4}$ Menggunakan Bentuk Akar",
                        "$16^{3/4} = (\\sqrt[4]{16})^3$. Karena $2^4 = 16$, maka $\\sqrt[4]{16} = 2$. Hasilnya adalah $2^3 = 8$."
                    ],
                    [
                        "Langkah 3: Hitung $(-5)^0 + (-2)^3$",
                        "$(-5)^0 = 1$.<br>$(-2)^3 = (-2) \\times (-2) \\times (-2) = -8$.<br>Hasil akhir: $1 + (-8) = -7$."
                    ]
                ],
                "conclusion": "Hasil berturut-turut: (a) 1/8, (b) 8, dan (c) -7."
            },
            "takeaways": [
                "Eksponen adalah perkalian berulang yang menghasilkan pertumbuhan cepat.",
                "Setiap bilangan bukan nol berpangkat nol bernilai 1 ($a^0 = 1$).",
                "Pangkat pecahan $a^{m/n}$ ekuivalen dengan bentuk akar ke-n dari $a^m$."
            ],
            "quiz": [
                "Berapakah nilai dari 27^(2/3)?",
                [
                    "9",
                    "3",
                    "18"
                ],
                0,
                "27^(2/3) = (akar pangkat 3 dari 27)^2 = 3^2 = 9."
            ]
        },
        {
            "title": "Anatomi: 7 Hukum Operasi Aljabar Pangkat Baku",
            "objectives": [
                "Menguasai sifat perkalian basis sama: a^m * a^n = a^(m+n).",
                "Menguasai sifat pembagian basis sama: a^m / a^n = a^(m-n).",
                "Menguasai sifat pemangkatan berpangkat: (a^m)^n = a^(m*n) dan distributif pangkat."
            ],
            "hook": "Berapakah hasil dari $(2^{100} \\times 2^{50}) / 2^{140}$? Menghitung angka raksasa ini secara manual akan memakan waktu ribuan tahun. Namun dengan 7 Hukum Eksponen Baku, kita cukup menjumlahkan dan mengurangkan angka pangkatnya: 100 + 50 - 140 = 10, sehingga jawabannya sekejap mata adalah $2^{10} = 1024$! Aturan aljabar ini menyederhanakan perhitungan raksasa menjadi penjumlahan tingkat dasar.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-list-check text-primary\"></i> 7 Sifat Emas Eksponen</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Perkalian Basis Sama:</strong> $a^m \\cdot a^n = a^{m + n}$ (Pangkat dijumlahkan).</li>\n                <li><strong>Pembagian Basis Sama:</strong> $\\frac{a^m}{a^n} = a^{m - n}$ (Pangkat dikurangkan).</li>\n                <li><strong>Pangkat Dipangkatkan:</strong> $(a^m)^n = a^{m \\cdot n}$ (Pangkat dikalikan).</li>\n                <li><strong>Distributif Perkalian:</strong> $(a \\cdot b)^n = a^n \\cdot b^n$.</li>\n                <li><strong>Distributif Pecahan:</strong> $\\left(\\frac{a}{b}\\right)^n = \\frac{a^n}{b^n}$.</li>\n                <li><strong>Pangkat Pecahan:</strong> $a^{m/n} = \\sqrt[n]{a^m}$.</li>\n                <li><strong>Pangkat Negatif:</strong> $a^{-n} = \\frac{1}{a^n}$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Sifat $a^m \\cdot a^n = a^{m+n}$ HANYA BERLAKU jika BASISNYA SAMA PERSIS ($a = a$). Jangan mencoba menjumlahkan pangkat pada $2^3 \\times 3^4$ karena basisnya berbeda (2 dan 3)!",
            "pitfall": "Jangan mengalikan basis saat menjumlahkan pangkat! $2^3 \\cdot 2^4 = 2^{3+4} = 2^7$, BUKAN $4^7$!",
            "fun_fact": "Hukum Moore (Moore's Law) dalam industri mikroprosesor komputer menyatakan bahwa jumlah transistor pada chip prosesor berlipat ganda setiap dua tahun secara eksponensial, mendorong evolusi superkomputer modern.",
            "formula": "a^m \\cdot a^n = a^{m+n} \\quad ; \\quad \\frac{a^m}{a^n} = a^{m-n} \\quad ; \\quad (a^m)^n = a^{mn}",
            "formula_params": [
                [
                    "a",
                    "Basis bilangan pokok ($a > 0$)."
                ],
                [
                    "m, n",
                    "Eksponen pangkat riil."
                ]
            ],
            "formula_intuition": "Mengubah operasi perkalian multiplikatif menjadi operasi penjumlahan aditif pada skala logaritmik eksponen.",
            "example": {
                "question": "Sederhanakan bentuk aljabar berikut ke dalam bentuk pangkat positif paling ringkas: $\\frac{(2x^3 y^{-2})^3}{4x^4 y^2}$!",
                "known": "Pecahan aljabar dengan variabel x dan y berpangkat.",
                "asked": "Bentuk pangkat positif paling sederhana.",
                "steps": [
                    [
                        "Langkah 1: Uraikan Pangkat Pembilang",
                        "$(2x^3 y^{-2})^3 = 2^3 \\cdot (x^3)^3 \\cdot (y^{-2})^3 = 8 x^9 y^{-6}$."
                    ],
                    [
                        "Langkah 2: Tuliskan Pecahan Lengkap",
                        "$\\frac{8 x^9 y^{-6}}{4 x^4 y^2}$."
                    ],
                    [
                        "Langkah 3: Bagi Koefisien Angka dan Kurangkan Pangkat Variabel",
                        "Angka: $8 / 4 = 2$.<br>Variabel x: $x^{9 - 4} = x^5$.<br>Variabel y: $y^{-6 - 2} = y^{-8}$."
                    ],
                    [
                        "Langkah 4: Ubah ke Pangkat Positif",
                        "$2 x^5 \\cdot \\frac{1}{y^8} = \\frac{2x^5}{y^8}$."
                    ]
                ],
                "conclusion": "Bentuk sederhananya adalah $\\frac{2x^5}{y^8}$."
            },
            "takeaways": [
                "Perkalian basis sama menjumlahkan pangkat, sedangkan pembagian mengurangkan pangkat.",
                "Pangkat dipangkatkan mengalikan pangkatnya: $(a^m)^n = a^{mn}$.",
                "Pangkat negatif berpindah posisi antara pembilang dan penyebut."
            ],
            "quiz": [
                "Bentuk sederhana dari (x² y³)⁴ / (x⁵ y²) adalah?",
                [
                    "x³ y¹⁰",
                    "x³ y¹⁴",
                    "x¹³ y¹⁰"
                ],
                0,
                "(x^8 y^12) / (x^5 y^2) = x^(8-5) y^(12-2) = x^3 y^10."
            ]
        },
        {
            "title": "Mekanika: Prosedur Menyelesaikan Persamaan Eksponen",
            "objectives": [
                "Menyelesaikan persamaan eksponen bentuk a^f(x) = a^p dengan menyamakan basis.",
                "Menyelesaikan persamaan eksponen bentuk a^f(x) = b^f(x) (pangkat sama, basis berbeda).",
                "Menyelesaikan persamaan eksponen tipe kuadrat tersamar menggunakan pemisalan u."
            ],
            "hook": "Jika kamu menginvestasikan uang dan tabunganmu bertumbuh mengikuti persamaan 2^(2x - 1) = 32, bagaimana cara mencari nilai waktu x? Dalam persamaan eksponen, variabel yang kita cari berada 'di atas langit' sebagai pangkat! Kunci pembuka solusinya adalah: 'Samakan Rumah Basisnya'. Ketika basis kiri dan kanan sama-sama bernilai 2, maka pangkatnya otomatis harus sama!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-key-fill text-primary\"></i> 1. Tiga Tipe Utama Persamaan Eksponen</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Tipe 1 (Basis Sama):</strong> $a^{f(x)} = a^p \\implies f(x) = p$. Cukup samakan pangkatnya!</li>\n                <li><strong>Tipe 2 (Basis Berbeda, Pangkat Sama):</strong> $a^{f(x)} = b^{f(x)}$ dengan $a \\neq b$. Karena basis berbeda, persamaan hanya bernilai sama jika pangkatnya bernilai NOL: $f(x) = 0$ (karena $a^0 = b^0 = 1$).</li>\n                <li><strong>Tipe 3 (Bentuk Kuadrat Tersamar):</strong> $A(a^x)^2 + B(a^x) + C = 0$. Diselesaikan dengan pemisalan $u = a^x$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Ketahui pohon faktor kelipatan basis populer: $32 = 2^5$, $64 = 2^6 = 4^3$, $81 = 3^4 = 9^2$, $125 = 5^3$. Mengenali bilangan-bilangan ini mempermudah penyamaan basis!",
            "pitfall": "Jangan lupa bahwa nilai pemisalan eksponensial $u = a^x$ SELALU BERNILAI POSITIF ($u > 0$). Jika pemfaktoran kuadrat menghasilkan nilai $u$ negatif (misal $u = -3$), nilai tersebut tidak memiliki solusi riil!",
            "fun_fact": "Persamaan eksponen adalah model matematis utama di balik perhitungan waktu paruh peluruhan isotop Karbon-14 yang digunakan para arkeolog untuk menentukan usia fosil purbakala dinosaurus dan mumi Mesir Kuno.",
            "formula": "a^{f(x)} = a^g(x) \\iff f(x) = g(x) \\quad (a > 0, a \\neq 1) \\quad ; \\quad a^{f(x)} = b^{f(x)} \\implies f(x) = 0",
            "formula_params": [
                [
                    "a",
                    "Basis bilangan positif bukan satu."
                ],
                [
                    "f(x), g(x)",
                    "Fungsi aljabar pada pangkat."
                ]
            ],
            "formula_intuition": "Fungsi eksponensial bersifat monoton satu-satu (injektif), sehingga output yang sama menjamin input pangkat yang identik.",
            "example": {
                "question": "Tentukan himpunan penyelesaian dari persamaan eksponen: $3^{2x - 1} = \\frac{1}{27}$!",
                "known": "$3^{2x - 1} = \\frac{1}{27}$.",
                "asked": "Nilai x penyelesaian.",
                "steps": [
                    [
                        "Langkah 1: Ubah Ruas Kanan Menjadi Basis 3",
                        "$27 = 3^3 \\implies \\frac{1}{27} = 3^{-3}$."
                    ],
                    [
                        "Langkah 2: Samakan Persamaan dengan Basis yang Sama",
                        "$3^{2x - 1} = 3^{-3}$."
                    ],
                    [
                        "Langkah 3: Samakan Pangkat Eksponen",
                        "$2x - 1 = -3$."
                    ],
                    [
                        "Langkah 4: Selesaikan Persamaan Linear",
                        "$2x = -3 + 1 \\implies 2x = -2 \\implies x = -1$."
                    ]
                ],
                "conclusion": "Nilai x yang memenuhi persamaan eksponen tersebut adalah x = -1."
            },
            "takeaways": [
                "Persamaan eksponen diselesaikan dengan menyamakan basis bilangan pokok di kedua ruas.",
                "Jika basis berbeda dan pangkat sama, maka pangkat harus sama dengan nol ($f(x) = 0$).",
                "Bentuk kuadrat eksponen diselesaikan melalui substitusi pemisalan $u = a^x$."
            ],
            "quiz": [
                "Jika 4^(x + 1) = 64, berapakah nilai x?",
                [
                    "x = 2",
                    "x = 3",
                    "x = 1"
                ],
                0,
                "4^(x + 1) = 4^3 => x + 1 = 3 => x = 2."
            ]
        },
        {
            "title": "Pemodelan: Pertumbuhan Populasi & Peluruhan Radioaktif Waktu Paruh",
            "objectives": [
                "Memodelkan pertumbuhan populasi organisme biologi secara eksponensial (N(t) = N0 * a^(t/T)).",
                "Memodelkan hukum peluruhan zat radioaktif berbasis waktu paruh (Half-Life).",
                "Menghitung proyeksi jumlah zat sisa setelah periode waktu tertentu."
            ],
            "hook": "Bakteri E. coli membelah diri menjadi dua setiap 20 menit sekali. Jika mula-mula hanya ada 1 butir bakteri di atas makanan yang dibiarkan terbuka, dalam waktu 8 jam saja jumlah bakteri tersebut telah meledak menjadi lebih dari 16 juta bakteri! Di sisi lain, limbah radioaktif nuklir meluruh separuh demi separuh selama ribuan tahun. Inilah dua sisi mata uang model eksponensial: Pertumbuhan dan Peluruhan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-activity text-primary\"></i> 1. Model Pertumbuhan & Peluruhan Eksponensial</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Model Pertumbuhan (Pembelahan):</strong>\n                  \\[ N(t) = N_0 \\cdot r^{\\frac{t}{T}} \\]\n                  di mana $N_0$ adalah jumlah mula-mula, $r$ adalah faktor penggandaan (misal 2 untuk membelah dua), $T$ adalah periode waktu pembelahan.\n                </li>\n                <li><strong>Model Peluruhan Radioaktif (Waktu Paruh $T_{1/2}$):</strong>\n                  \\[ N(t) = N_0 \\cdot \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}} \\]\n                  di mana $T_{1/2}$ adalah waktu yang dibutuhkan zat untuk meluruh menjadi tepat separuh dari massa awalnya.\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk menghitung berapa kali pembelahan atau peluruhan terjadi: cukup bagi waktu total pengamatan $t$ dengan periode siklusnya $T$ ($n = t / T$)!",
            "pitfall": "Pastikan satuan waktu t dan periode T sama persis! Jika waktu t dalam jam dan periode T dalam menit, ubah jam menjadi menit terlebih dahulu.",
            "fun_fact": "Unsur radioaktif Uranium-235 yang digunakan dalam reaktor nuklir memiliki waktu paruh sekitar 700 juta tahun, menjadikannya 'jam geologis' alami untuk mengukur usia formasi bebatuan bumi.",
            "formula": "N(t) = N_0 \\cdot 2^{\\frac{t}{T}} \\quad (\\text{Pertumbuhan}) \\quad ; \\quad N(t) = N_0 \\cdot \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}} \\quad (\\text{Peluruhan})",
            "formula_params": [
                [
                    "N_0",
                    "Kuantitas mula-mula pada t = 0."
                ],
                [
                    "N(t)",
                    "Kuantitas pada saat waktu t."
                ],
                [
                    "T_{1/2}",
                    "Waktu paruh (half-life)."
                ]
            ],
            "formula_intuition": "Melipatgandakan atau membagi separuh kuantitas secara berulang pada setiap kelipatan interval periode.",
            "example": {
                "question": "Sebuah sampel zat radioaktif memiliki massa mula-mula 80 gram dengan waktu paruh 4 jam. Berapakah sisa massa zat radioaktif tersebut setelah disimpan selama 12 jam?",
                "known": "Massa awal $N_0 = 80\\text{ gram}$, waktu paruh $T_{1/2} = 4\\text{ jam}$, waktu peluruhan $t = 12\\text{ jam}$.",
                "asked": "Massa sisa $N(12)$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Banyaknya Siklus Peluruhan yang Terjadi",
                        "$n = \\frac{t}{T_{1/2}} = \\frac{12}{4} = 3\\text{ siklus}$."
                    ],
                    [
                        "Langkah 2: Masukkan ke Rumus Peluruhan Eksponensial",
                        "$N(12) = 80 \\cdot \\left(\\frac{1}{2}\\right)^3$."
                    ],
                    [
                        "Langkah 3: Hitung Nilai Pangkat",
                        "$\\left(\\frac{1}{2}\\right)^3 = \\frac{1}{8}$."
                    ],
                    [
                        "Langkah 4: Kalikan dengan Massa Awal",
                        "$N(12) = 80 \\times \\frac{1}{8} = 10\\text{ gram}$."
                    ]
                ],
                "conclusion": "Setelah 12 jam, massa zat radioaktif yang tersisa adalah 10 gram."
            },
            "takeaways": [
                "Pertumbuhan eksponensial melipatgandakan jumlah, sedangkan peluruhan memotong separuh jumlah secara berkala.",
                "Pangkat eksponen menyatakan banyaknya siklus waktu yang telah berlalu ($t / T$).",
                "Model eksponen krusial dalam mikrobiologi, kedokteran nuklir, dan analisis pandemi."
            ],
            "quiz": [
                "Sebuah koloni bakteri berjumlah 100 membelah diri menjadi dua setiap 15 menit. Berapakah jumlah bakteri setelah 1 jam (60 menit)?",
                [
                    "1.600 bakteri",
                    "800 bakteri",
                    "3.200 bakteri"
                ],
                0,
                "n = 60 / 15 = 4 siklus. N = 100 * 2^4 = 100 * 16 = 1.600 bakteri."
            ]
        },
        {
            "title": "Capstone: Model Bunga Majemuk Finansial & Aturan Penggandaan Investasi",
            "objectives": [
                "Mengintegrasikan model eksponensial dalam kalkulasi pertumbuhan investasi bunga majemuk (Compound Interest).",
                "Memahami mengapa Albert Einstein menyebut bunga majemuk sebagai 'Keajaiban Dunia Kedelapan'.",
                "Mengevaluasi keputusan finansial tabungan masa depan menggunakan Aturan 72 (Rule of 72)."
            ],
            "hook": "Selamat datang di Tahap Capstone! Albert Einstein pernah berkata: 'Bunga majemuk adalah keajaiban dunia kedelapan. Siapa yang memahaminya, menghasilkannya; siapa yang tidak, membayarnya!'. Jika kamu menginvestasikan modal Rp 10.000.000 dengan imbal hasil majemuk 10% per tahun, uangmu tidak bertambah secara linier melainkan bertumbuh secara eksponensial bunga berbunga! Sebagai financial analyst, tugasmu adalah memodelkan akumulasi kekayaan ini untuk 20 tahun ke depan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Formula Bunga Majemuk (Compound Interest)</h3>\n              <p>Pada bunga majemuk, bunga yang diperoleh di akhir periode ditambahkan ke modal pokok untuk menghasilkan bunga baru pada periode berikutnya:</p>\n              \\[ A(t) = P \\left(1 + \\frac{r}{n}\\right)^{nt} \\]\n              <ul class=\"dic-list\">\n                <li>$P$: Modal pokok awal (Principal).</li>\n                <li>$r$: Suku bunga tahunan (desimal).</li>\n                <li>$n$: Frekuensi pemajemukan per tahun ($n=1$ tahunan, $n=12$ bulanan).</li>\n                <li>$t$: Jangka waktu investasi (tahun).</li>\n              </ul>\n              <h4 class=\"fw-bold text-info mt-3\"><i class=\"bi bi-clock-history\"></i> Aturan Penggandaan Aset (Rule of 72):</h4>\n              <p>Waktu yang dibutuhkan agar uangmu berlipat ganda 2x lipat dapat diaproksimasi dengan cepat: $t_{\\text{ganda}} \\approx \\frac{72}{\\text{Suku Bunga (\\%)}}$. Contoh: bunga 10% akan menggandakan uang setiap $72/10 \\approx 7.2$ tahun!</p>\n            </div>\n            ",
            "pro_tip": "Waktu adalah faktor terkuat dalam fungsi eksponensial! Memulai investasi 5 tahun lebih awal memberikan hasil akhir yang jauh lebih besar daripada menyetor modal dua kali lipat lebih banyak di kemudian hari!",
            "pitfall": "Jangan lupa mengubah persentase bunga menjadi angka desimal: $8\\% = 0.08$, bukan $0.8$!",
            "fun_fact": "Investor legendaris Warren Buffett mengumpulkan lebih dari 99% kekayaan totalnya setelah ia berusia 50 tahun semata-mata karena efek kurva eksponensial bunga majemuk jangka panjang!",
            "formula": "A(t) = P(1 + r)^t \\quad (\\text{Tahunan}) \\quad ; \\quad t_{\\text{double}} \\approx \\frac{72}{r_{\\%}}",
            "formula_params": [
                [
                    "P",
                    "Modal awal simpanan."
                ],
                [
                    "r",
                    "Suku bunga majemuk tahunan."
                ],
                [
                    "t",
                    "Waktu tahun simpanan."
                ]
            ],
            "formula_intuition": "Mengalikan faktor pertumbuhan $(1 + r)$ secara kumulatif sebanyak t periode tahun.",
            "example": {
                "question": "Seseorang menabung modal awal Rp 10.000.000 pada instrumen reksa dana dengan bunga majemuk tahunan 10% per tahun ($r = 0.10$). Hitung total saldo tabungan setelah 3 tahun!",
                "known": "$P = 10.000.000$, $r = 0.10$, $t = 3\\text{ tahun}$.",
                "asked": "Saldo akhir A(3).",
                "steps": [
                    [
                        "Langkah 1: Tentukan Faktor Pertumbuhan",
                        "$1 + r = 1 + 0.10 = 1.10$."
                    ],
                    [
                        "Langkah 2: Hitung Pangkat Faktor Waktu $(1.10)^3$",
                        "$1.10 \\times 1.10 \\times 1.10 = 1.21 \\times 1.10 = 1.331$."
                    ],
                    [
                        "Langkah 3: Kalikan dengan Modal Pokok Awal P",
                        "$A(3) = 10.000.000 \\times 1.331 = 13.310.000\\text{ rupiah}$."
                    ]
                ],
                "conclusion": "Total saldo akhir tabungan setelah 3 tahun bertumbuh menjadi Rp 13.310.000 (menghasilkan keuntungan bunga Rp 3.310.000)."
            },
            "takeaways": [
                "Bunga majemuk adalah contoh penerapan eksponensial terkuat dalam dunia finansial dan perbankan.",
                "Eksponen waktu $t$ memicu kurva pertumbuhan tajam setelah melewati periode kritis.",
                "Selamat! Kamu telah menguasai seluruh kurikulum Eksponen & Fungsi Eksponensial dengan hasil istimewa!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE EKSPONEN: Menggunakan Aturan 72, kira-kira berapa tahun yang dibutuhkan tabungan untuk berlipat ganda 2x lipat jika suku bunga majemuk adalah 9% per tahun?",
                [
                    "8 tahun",
                    "9 tahun",
                    "7.2 tahun"
                ],
                0,
                "t = 72 / 9 = 8 tahun."
            ]
        }
    ]
}
