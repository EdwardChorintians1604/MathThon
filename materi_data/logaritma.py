# -*- coding: utf-8 -*-
DATA = {
    "title": "Logaritma & Aplikasinya",
    "short": "Logaritma",
    "icon": "bi-reception-4",
    "color": "#8b5cf6",
    "desc": "Kuasai operasi invers eksponensial, sifat rantai logaritma, skala pH kimia, skala Richter gempa bumi, intensitas bunyi desibel, dan peluruhan pendinginan Newton.",
    "babs": [
        {
            "title": "Fondasi: Mengapa Kita Butuh Operasi Invers Eksponen?",
            "objectives": [
                "Memahami logaritma sebagai operasi inversi (kebalikan) dari perpangkatan eksponensial.",
                "Menuliskan bentuk ekivalensi antara persamaan eksponen dan persamaan logaritma (^a\\log b = c <=> a^c = b).",
                "Memahami syarat basis a > 0, a != 1 dan numerus b > 0."
            ],
            "hook": "Jika $2^3 = 8$, itu adalah eksponen: mencari hasil perkalian 2 sebanyak 3 kali. Tetapi bagaimana jika pertanyaannya dibalik: '2 harus dipangkatkan berapa agar hasilnya menjadi 8?'. Pertanyaan kebalikan inilah yang dijawab oleh LOGARITMA: $^2\\log 8 = 3$! Logaritma diciptakan oleh bangsawan Skotlandia John Napier pada tahun 1614 untuk menyelamatkan para astronom dari kelelahan menghitung perkalian orbit planet yang memuat puluhan angka di belakang koma.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrow-left-right text-primary\"></i> 1. Definisi & Notasi Logaritma</h3>\n              <p>Logaritma adalah operasi matematika untuk mencari eksponen pangkat dari suatu basis bilangan pokok:</p>\n              \\[ ^a\\log b = c \\iff a^c = b \\]\n              <ul class=\"dic-list\">\n                <li><strong>Basis Bilangan Pokok ($a$):</strong> Syarat: $a > 0$ dan $a \\neq 1$.</li>\n                <li><strong>Numerus ($b$):</strong> Bilangan yang dicarikan logaritmanya. Syarat mutlak: <strong>$b > 0$ (harus selalu positif)</strong>!</li>\n                <li><strong>Hasil Logaritma ($c$):</strong> Nilai eksponen pangkat.</li>\n                <li><strong>Logaritma Umum (Briggsian):</strong> Logaritma berbasis 10 sering ditulis tanpa angka basis: $\\log x$ bermakna $^{10}\\log x$.</li>\n                <li><strong>Logaritma Natural (Napierian):</strong> Logaritma berbasis bilangan Euler $e \\approx 2.71828$ dinotasikan sebagai $\\ln x = ^e\\log x$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Cara membaca cepat bentuk logaritma: '$^a\\log b = c$' bacalah sebagai: '$a$ pangkat berapa yang sama dengan $b$?', jawabannya adalah $c$!",
            "pitfall": "Numerus TIDAK BOLEH bernilai negatif atau nol! $\\log(-5)$ dan $\\log(0)$ tidak terdefinisi dalam bilangan riil karena tidak ada bilangan positif dipangkatkan angka berapa pun yang menghasilkan angka negatif atau nol!",
            "fun_fact": "Astronom legendaris Pierre-Simon Laplace menyatakan bahwa penemuan logaritma 'telah menggandakan usia hidup para astronom' karena berhasil memangkas kerja hitung berbulan-bulan menjadi hanya beberapa hari saja.",
            "formula": "^a\\log b = c \\iff a^c = b \\quad (a > 0, \\ a \\neq 1, \\ b > 0) \\quad ; \\quad ^a\\log 1 = 0 \\quad ; \\quad ^a\\log a = 1",
            "formula_params": [
                [
                    "a",
                    "Basis bilangan pokok logaritma."
                ],
                [
                    "b",
                    "Numerus (bilangan positif di dalam logaritma)."
                ],
                [
                    "c",
                    "Pangkat eksponen solusi."
                ]
            ],
            "formula_intuition": "Mengekstrak eksponen pangkat yang tersembunyi menjadi angka skalar linier biasa.",
            "example": {
                "question": "Ubahlah bentuk eksponen berikut menjadi bentuk logaritma: (a) $5^3 = 125$, (b) $2^{-4} = \\frac{1}{16}$, lalu hitung nilai dari (c) $^3\\log 81$!",
                "known": "Persamaan eksponen $5^3=125$, $2^{-4}=1/16$, dan nilai $^3\\log 81$.",
                "asked": "Bentuk logaritma dan nilai evaluasi numerik.",
                "steps": [
                    [
                        "Langkah 1: Konversi $5^3 = 125$",
                        "Basis $a = 5$, hasil $b = 125$, pangkat $c = 3$. Bentuk logaritmanya: $^5\\log 125 = 3$."
                    ],
                    [
                        "Langkah 2: Konversi $2^{-4} = 1/16$",
                        "Basis $a = 2$, hasil $b = 1/16$, pangkat $c = -4$. Bentuk logaritmanya: $^2\\log\\left(\\frac{1}{16}\\right) = -4$."
                    ],
                    [
                        "Langkah 3: Hitung $^3\\log 81$",
                        "Tanya: 3 pangkat berapa sama dengan 81? Karena $3^4 = 81$, maka $^3\\log 81 = 4$."
                    ]
                ],
                "conclusion": "Hasil berturut-turut: (a) $^5\\log 125 = 3$, (b) $^2\\log(1/16) = -4$, dan (c) $^3\\log 81 = 4$."
            },
            "takeaways": [
                "Logaritma adalah invers fungsi eksponensial: mencari pangkat dari suatu bilangan basis.",
                "Numerus logaritma wajib selalu bernilai positif riil ($b > 0$).",
                "$^a\\log 1 = 0$ untuk setiap basis apa pun karena $a^0 = 1$."
            ],
            "quiz": [
                "Berapakah nilai dari ^2\\log 64?",
                [
                    "6",
                    "5",
                    "8"
                ],
                0,
                "Karena 2^6 = 64, maka ^2\\log 64 = 6."
            ]
        },
        {
            "title": "Anatomi: 7 Sifat Emas Operasi Aljabar Logaritma",
            "objectives": [
                "Menguasai sifat perkalian numerus: ^a\\log(b * c) = ^a\\log b + ^a\\log c.",
                "Menguasai sifat pembagian numerus: ^a\\log(b / c) = ^a\\log b - ^a\\log c.",
                "Menguasai sifat pangkat numerus dan sifat rantai perubahan basis: ^a\\log b * ^b\\log c = ^a\\log c."
            ],
            "hook": "Tahukah kamu apa rahasia terbesar mengapa logaritma sangat dipuja ilmuwan selama ratusan tahun? Karena logaritma memiliki kekuatan sihir untuk MENGUBAH PERKALIAN MENJADI PENJUMLAHAN: $\\log(A \\times B) = \\log A + \\log B$! Di era sebelum ada kalkulator saku, para insinyur mengalikan angka-angka raksasa hanya dengan menjumlahkan nilai logaritmanya di buku tabel!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-gem text-primary\"></i> 7 Sifat Emas Logaritma</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Sifat Penjumlahan (Perkalian Numerus):</strong> $^a\\log(b \\cdot c) = ^a\\log b + ^a\\log c$.</li>\n                <li><strong>Sifat Pengurangan (Pembagian Numerus):</strong> $^a\\log\\left(\\frac{b}{c}\\right) = ^a\\log b - ^a\\log c$.</li>\n                <li><strong>Sifat Pangkat Numerus:</strong> $^a\\log(b^n) = n \\cdot ^a\\log b$.</li>\n                <li><strong>Sifat Pangkat Basis & Numerus:</strong> $^{a^m}\\log(b^n) = \\frac{n}{m} \\cdot ^a\\log b$.</li>\n                <li><strong>Sifat Perubahan Basis:</strong> $^a\\log b = \\frac{^p\\log b}{^p\\log a} = \\frac{1}{^b\\log a}$.</li>\n                <li><strong>Sifat Rantai Berantai:</strong> $^a\\log b \\cdot ^b\\log c \\cdot ^c\\log d = ^a\\log d$.</li>\n                <li><strong>Sifat Eksponen Logaritma:</strong> $a^{^a\\log b} = b$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk menerapkan sifat penjumlahan $^a\\log b + ^a\\log c = ^a\\log(bc)$, pastikan ANGKA BASISNYA IDENTIK SAMA! Jika basis berbeda, gunakan sifat perubahan basis terlebih dahulu.",
            "pitfall": "Jangan keliru: $\\log(b + c) \\neq \\log b + \\log c$! Logaritma penjumlahan TIDAK DAPAT dipecah. Yang bisa dipecah adalah logaritma dari perkalian!",
            "fun_fact": "Mistar geser (Slide Rule)—alat kalkulator mekanis analog berbasis skala logaritma geser—digunakan oleh para insinyur NASA untuk merancang roket misi Apollo 11 yang sukses mendaratkan manusia pertama di bulan tahun 1969!",
            "formula": "^a\\log(b \\cdot c) = ^a\\log b + ^a\\log c \\quad ; \\quad ^a\\log b^n = n \\cdot ^a\\log b \\quad ; \\quad ^a\\log b \\cdot ^b\\log c = ^a\\log c",
            "formula_params": [
                [
                    "a",
                    "Basis bilangan pokok bersama."
                ],
                [
                    "b, c",
                    "Faktor-faktor perkalian numerus."
                ],
                [
                    "n",
                    "Pangkat pada numerus yang dapat ditarik ke depan."
                ]
            ],
            "formula_intuition": "Memetakan perkalian perkalian multiplikatif menjadi penjumlahan penambahan aditif sederhana.",
            "example": {
                "question": "Hitunglah nilai sederhana dari: $^3\\log 18 - ^3\\log 2 + ^2\\log 3 \\cdot ^3\\log 8$!",
                "known": "Operasi logaritma berbasis 3 dan sifat rantai berbasis 2.",
                "asked": "Nilai numerik sederhana.",
                "steps": [
                    [
                        "Langkah 1: Sederhanakan Bagian Pertama Menggunakan Sifat Pengurangan",
                        "$^3\\log 18 - ^3\\log 2 = ^3\\log\\left(\\frac{18}{2}\\right) = ^3\\log 9$."
                    ],
                    [
                        "Langkah 2: Evaluasi Nilai $^3\\log 9$",
                        "$^3\\log 9 = ^3\\log(3^2) = 2$."
                    ],
                    [
                        "Langkah 3: Sederhanakan Bagian Kedua Menggunakan Sifat Rantai",
                        "$^2\\log 3 \\cdot ^3\\log 8 = ^2\\log 8$."
                    ],
                    [
                        "Langkah 4: Evaluasi Nilai $^2\\log 8$",
                        "$^2\\log 8 = ^2\\log(2^3) = 3$."
                    ],
                    [
                        "Langkah 5: Jumlahkan Seluruh Hasil",
                        "$2 + 3 = 5$."
                    ]
                ],
                "conclusion": "Nilai akhir dari ekspresi logaritma tersebut adalah 5."
            },
            "takeaways": [
                "Pengurangan logaritma basis sama membagi nilai numerusnya.",
                "Sifat rantai melenyapkan basis dan numerus perantara yang sama: $^a\\log b \\cdot ^b\\log c = ^a\\log c$.",
                "Pangkat pada numerus dapat dikeluarkan ke depan sebagai faktor pengali skalar."
            ],
            "quiz": [
                "Berapakah nilai dari ^2\\log 12 + ^2\\log 4 - ^2\\log 6?",
                [
                    "3",
                    "4",
                    "2"
                ],
                0,
                "^2\\log((12 * 4) / 6) = ^2\\log(48 / 6) = ^2\\log 8 = 3."
            ]
        },
        {
            "title": "Mekanika: Prosedur Menyelesaikan Persamaan & Pertidaksamaan Logaritma",
            "objectives": [
                "Menyelesaikan persamaan logaritma bentuk ^a\\log f(x) = ^a\\log g(x).",
                "Menguji syarat mutlak numerus f(x) > 0 dan g(x) > 0 (Uji Ekstraneous Solution).",
                "Menyelesaikan pertidaksamaan logaritma dengan memperhatikan nilai basis (0 < a < 1 membalik tanda pertidaksamaan)."
            ],
            "hook": "Banyak siswa mengira bahwa setelah mencoret simbol logaritma dan mendapatkan nilai x, pekerjaan mereka selesai. Padahal di dunia nyata matematika, ada jebakan mematikan yang disebut 'Solusi Palsu' (Extraneous Solution)! Jika nilai x yang kamu dapatkan membuat numerus di dalam kurung bernilai negatif, nilai x tersebut HARUS DIBUANG ke tempat sampah karena logaritma bilangan negatif tidak nyata!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-shield-exclamation text-primary\"></i> Aturan Mutlak Syarat Numerus</h3>\n              <p>Untuk menyelesaikan persamaan $^a\\log f(x) = ^a\\log g(x)$:</p>\n              <ol class=\"dic-list\">\n                <li>Samakan bentuk logaritma di kedua ruas dengan basis yang identik.</li>\n                <li>Samakan kedua fungsi numerus: $f(x) = g(x)$.</li>\n                <li><strong>Wajib Uji Syarat Numerus:</strong> Periksa apakah solusi $x$ memenuhi $f(x) > 0$ dan $g(x) > 0$. Nilai yang membuat numerus $\\le 0$ harus digugurkan!</li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Pada pertidaksamaan logaritma: Jika basis $a > 1$, tanda pertidaksamaan TETAP ($\\le$ tetap $\\le$). Tetapi jika basis pecahan $0 < a < 1$, tanda pertidaksamaan WAJIB DIBALIK ($<$ menjadi $>$), karena kurva fungsinya menurun monoton!",
            "pitfall": "Jangan pernah lupa menguji syarat numerus di akhir pengerjaan! Melewatkan langkah ini adalah penyebab 80% kesalahan siswa dalam ujian logaritma.",
            "fun_fact": "Dalam rekayasa audio akustik, telinga manusia mendengar tingkat kekerasan bunyi secara logaritmik, sehingga peningkatan 10 kali lipat energi suara hanya terdengar seperti kenaikan 2 kali lipat oleh gendang telinga kita.",
            "formula": "^a\\log f(x) = ^a\\log g(x) \\iff f(x) = g(x) \\quad \\text{dengan syarat } f(x) > 0 \\text{ dan } g(x) > 0",
            "formula_params": [
                [
                    "f(x), g(x)",
                    "Fungsi aljabar numerus yang wajib bernilai positif."
                ]
            ],
            "formula_intuition": "Menyamakan input numerus setelah memastikan kedua ekspresi berada dalam domain valid.",
            "example": {
                "question": "Tentukan himpunan penyelesaian dari persamaan logaritma: $^2\\log(x^2 - 3) = ^2\\log(2x)$!",
                "known": "$^2\\log(x^2 - 3) = ^2\\log(2x)$ dengan basis sama $a = 2$.",
                "asked": "Nilai x yang memenuhi beserta verifikasi syarat numerus.",
                "steps": [
                    [
                        "Langkah 1: Samakan Kedua Numerus",
                        "$x^2 - 3 = 2x \\implies x^2 - 2x - 3 = 0$."
                    ],
                    [
                        "Langkah 2: Faktorkan Persamaan Kuadrat",
                        "$(x - 3)(x + 1) = 0 \\implies x_1 = 3$ atau $x_2 = -1$."
                    ],
                    [
                        "Langkah 3: Uji Syarat Numerus untuk $x_2 = -1$",
                        "Masukkan $x = -1$ ke numerus $2x$: $2(-1) = -2 < 0$ (TIDAK MEMENUHI / DITOLAK!)."
                    ],
                    [
                        "Langkah 4: Uji Syarat Numerus untuk $x_1 = 3$",
                        "Numerus 1: $3^2 - 3 = 9 - 3 = 6 > 0$ (Positif, Valid!).<br>Numerus 2: $2(3) = 6 > 0$ (Positif, Valid!)."
                    ]
                ],
                "conclusion": "Himpunan penyelesaian satu-satunya yang sah adalah x = 3 (nilai x = -1 gugur karena melanggar syarat numerus positif)."
            },
            "takeaways": [
                "Persamaan logaritma basis sama diselesaikan dengan menyamakan numerus: $f(x) = g(x)$.",
                "Syarat numerus positif ($f(x) > 0$) adalah saringan wajib untuk mengeliminasi solusi palsu.",
                "Pada basis pecahan $0 < a < 1$, tanda pertidaksamaan harus berbalik arah."
            ],
            "quiz": [
                "Jika ^3\\log(2x - 1) = 2, berapakah nilai x?",
                [
                    "x = 5",
                    "x = 4",
                    "x = 7"
                ],
                0,
                "^3\\log(2x - 1) = 2 <=> 2x - 1 = 3^2 <=> 2x - 1 = 9 <=> 2x = 10 <=> x = 5. Syarat: 2(5) - 1 = 9 > 0 (Valid)."
            ]
        },
        {
            "title": "Pemodelan: Skala Logaritmik Kompresi Rentang Ekstrem (pH, Richter & Desibel)",
            "objectives": [
                "Memahami skala logaritmik sebagai teknik mengompresi rentang angka ekstrem triliunan menjadi skala linier praktis.",
                "Menghitung derajat keasaman kimiawi (pH = -log[H+]).",
                "Menghitung perbandingan energi gempa bumi Skala Richter dan intensitas kebisingan Desibel (dB)."
            ],
            "hook": "Berapakah perbandingan kekuatan gempa magnitudo 7 Skala Richter dibandingkan gempa magnitudo 5? Orang awam mengira selisihnya hanya sedikit (7 - 5 = 2). Mereka salah besar! Karena Skala Richter adalah skala logaritmik basis 10, kenaikan 2 poin berarti getaran tanah 10^2 = 100 kali lebih kuat, dan pelepasan energi guncangannya melesat 1000 kali lebih dahsyat! Skala logaritmik adalah pengompres angka raksasa agar mudah dipahami akal manusia.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-compress text-primary\"></i> Tiga Skala Logaritmik Terkenal di Dunia</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Skala Keasaman Kimia (pH):</strong> Mengukur konsentrasi ion hidrogen $[H^+]$ dalam larutan:\n                  \\[ \\text{pH} = -\\log[H^+] \\]\n                  Larutan netral memiliki $\\text{pH} = 7$, asam memiliki $\\text{pH} < 7$, dan basa memiliki $\\text{pH} > 7$.\n                </li>\n                <li><strong>Intensitas Kebisingan Bunyi (Desibel - dB):</strong>\n                  \\[ \\beta = 10 \\log\\left(\\frac{I}{I_0}\\right) \\]\n                  di mana $I_0 = 10^{-12}\\text{ W/m}^2$ adalah ambang batas pendengaran manusia.\n                </li>\n                <li><strong>Skala Richter Gempa Bumi:</strong> Setiap kenaikan 1 skala logaritmik melipatgandakan energi gempa sekitar 31.6 kali lipat ($10^{1.5}$).</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Setiap penurunan 1 poin skala pH (misal dari pH 6 ke pH 5) berarti konsentrasi keasaman ion hidrogen melonjak TEPAT 10 KALI LIPAT lebih pekat!",
            "pitfall": "Tanda minus pada rumus pH ($-\\log[H^+]$) sangat penting karena konsentrasi $[H^+]$ biasanya sangat kecil ($10^{-3}, 10^{-7}$). Tanda minus membalik nilai negatif menjadi bilangan positif yang mudah dibaca kasir laboratorium.",
            "fun_fact": "Suara peluncuran roket Saturn V ke bulan mencapai 204 desibel (dB)—suara yang begitu dahsyat energinya hingga mampu menghancurkan struktur beton jika air peredam suara tidak disemprotkan ke landasan luncur.",
            "formula": "\\text{pH} = -\\log[H^+] \\iff [H^+] = 10^{-\\text{pH}} \\quad ; \\quad \\beta = 10\\log\\left(\\frac{I}{I_0}\\right) \\text{ dB}",
            "formula_params": [
                [
                    "[H^+]",
                    "Konsentrasi ion hidrogen (Molaritas M = mol/L)."
                ],
                [
                    "I",
                    "Intensitas gelombang bunyi (Watt/m²)."
                ],
                [
                    "I_0",
                    "Ambang batas pendengaran terlemah (10^-12 Watt/m²)."
                ]
            ],
            "formula_intuition": "Mengompresi skala nano $10^{-14}$ hingga $10^0$ menjadi rentang angka bulat praktis 0 s.d. 14.",
            "example": {
                "question": "Sebuah sampel minuman soda diuji di laboratorium kimia dan ditemukan memiliki konsentrasi ion hidrogen $[H^+] = 2 \\times 10^{-3}\\text{ M}$. Jika diketahui $\\log 2 \\approx 0.301$, hitunglah derajat keasaman (pH) dari minuman soda tersebut!",
                "known": "$[H^+] = 2 \\times 10^{-3}\\text{ M}$ dan $\\log 2 \\approx 0.301$.",
                "asked": "Nilai derajat keasaman pH.",
                "steps": [
                    [
                        "Langkah 1: Masukkan ke Rumus Definisi pH",
                        "$\\text{pH} = -\\log(2 \\times 10^{-3})$."
                    ],
                    [
                        "Langkah 2: Uraikan Menggunakan Sifat Penjumlahan Logaritma",
                        "$\\text{pH} = -[\\log 2 + \\log(10^{-3})]$."
                    ],
                    [
                        "Langkah 3: Evaluasi $\\log(10^{-3})$",
                        "$\\log(10^{-3}) = -3$."
                    ],
                    [
                        "Langkah 4: Hitung Nilai Akhir",
                        "$\\text{pH} = -[0.301 + (-3)] = -[-2.699] = 2.699 \\approx 2.7$."
                    ]
                ],
                "conclusion": "Derajat keasaman minuman soda tersebut adalah pH 2.7 (bersifat asam kuat)."
            },
            "takeaways": [
                "Skala logaritmik mengompresi angka rentang dinamis raksasa menjadi representasi angka yang mudah dibaca.",
                "Derajat keasaman pH dirumuskan dengan invers logaritma basis 10: $\\text{pH} = -\\log[H^+]$.",
                "Perubahan kecil pada skala logaritmik mencerminkan pelipatgandaan eksponensial pada kondisi fisik riil."
            ],
            "quiz": [
                "Berapakah pH dari larutan asam lambung jika konsentrasi ion hidrogennya adalah [H+] = 10^-2 M?",
                [
                    "pH = 2",
                    "pH = -2",
                    "pH = 12"
                ],
                0,
                "pH = -log(10^-2) = -(-2) = 2 (Asam kuat)."
            ]
        },
        {
            "title": "Capstone: Analisis Forensik Waktu Kematian (Hukum Pendinginan Newton)",
            "objectives": [
                "Mengintegrasikan fungsi eksponensial dan logaritma natural (ln) untuk memecahkan misteri investigasi kriminal forensik.",
                "Memodelkan peluruhan temperatur jenazah menggunakan Hukum Pendinginan Newton.",
                "Menentukan estimasi waktu jam kematian (Time of Death) secara presisi menggunakan aljabar logaritma."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Lead Forensic Detective di Tempat Kejadian Perkara (TKP). Sesosok jenazah ditemukan di dalam kamar berpendingin AC bersuhu konstan 20°C. Pada pukul 14.00, suhu tubuh jenazah diukur 30°C. Satu jam kemudian pada pukul 15.00, suhunya turun menjadi 28°C. Suhu normal manusia saat hidup adalah 37°C. Kapan tepatnya korban meninggal dunia? Kunci pemecahan kasus ini ada pada persamaan Logaritma Natural Hukum Pendinginan Newton!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-thermometer-snow text-warning\"></i> Skenario Hukum Pendinginan Newton (Newton's Law of Cooling)</h3>\n              <p>Laju pendinginan suhu tubuh terhadap suhu lingkungan $T_s$ dimodelkan oleh persamaan:</p>\n              \\[ T(t) = T_s + (T_0 - T_s) e^{-kt} \\]\n              <p>Untuk mencari waktu $t$ yang tersembunyi pada pangkat eksponen, kedua ruas diisolasi lalu diterapkan operasi <strong>Logaritma Natural ($\\ln$)</strong>:</p>\n              \\[ -kt = \\ln\\left( \\frac{T(t) - T_s}{T_0 - T_s} \\right) \\implies t = -\\frac{1}{k} \\ln\\left( \\frac{T(t) - T_s}{T_0 - T_s} \\right) \\]\n            </div>\n            ",
            "pro_tip": "Untuk melenyapkan bilangan basis Euler e pada persamaan eksponen: terapkan fungsi ln (logaritma natural) pada kedua ruas karena $\\ln(e^x) = x$!",
            "pitfall": "Jangan lupakan suhu ruangan lingkungan ($T_s$)! Suhu benda yang mendingin tidak pernah turun menuju nol mutlak, melainkan meluruh mendekati suhu ruangan sekitarnya.",
            "fun_fact": "Hukum Pendinginan Newton dan persamaan diferensial logaritmik ini digunakan secara resmi oleh institusi forensik dunia seperti FBI dan Interpol untuk menetapkan alibi tersangka dalam sidang pengadilan pembunuhan.",
            "formula": "T(t) = T_s + (T_0 - T_s)e^{-kt} \\iff t = -\\frac{1}{k}\\ln\\left(\\frac{T(t) - T_s}{T_0 - T_s}\\right)",
            "formula_params": [
                [
                    "T(t)",
                    "Temperatur tubuh pada saat waktu t (°C)."
                ],
                [
                    "T_s",
                    "Temperatur lingkungan sekitar / suhu AC ruangan (20°C)."
                ],
                [
                    "T_0",
                    "Temperatur mula-mula saat korban hidup normal (37°C)."
                ],
                [
                    "k",
                    "Konstanta laju konduksi pendinginan termal spesifik."
                ]
            ],
            "formula_intuition": "Menggunakan logaritma natural untuk mengekstrak variabel waktu t dari peluruhan eksponensial termal.",
            "example": {
                "question": "Suhu tubuh korban diukur saat ditemukan adalah $30^\\circ\\text{C}$ pada ruangan $T_s = 20^\\circ\\text{C}$. Satu jam kemudian suhunya menjadi $28^\\circ\\text{C}$. Didapatkan konstanta laju pendinginan $k = \\ln(10/8) \\approx 0.223\\text{ per jam}$. Jika suhu saat hidup adalah $T_0 = 37^\\circ\\text{C}$, berapa jam sebelum penemuan jenazah kematian terjadi?",
                "known": "$T_s = 20^\\circ\\text{C}$, $T_0 = 37^\\circ\\text{C}$, suhu saat ditemukan $T = 30^\\circ\\text{C}$, konstanta $k = 0.223$.",
                "asked": "Lama waktu kematian $t$.",
                "steps": [
                    [
                        "Langkah 1: Masukkan Angka ke Persamaan Peluruhan",
                        "$30 = 20 + (37 - 20) e^{-0.223 t}$."
                    ],
                    [
                        "Langkah 2: Kurangkan dengan Suhu Ruangan 20",
                        "$30 - 20 = 17 e^{-0.223 t} \\implies 10 = 17 e^{-0.223 t}$."
                    ],
                    [
                        "Langkah 3: Bagi Kedua Ruas dengan 17",
                        "$e^{-0.223 t} = \\frac{10}{17} \\approx 0.5882$."
                    ],
                    [
                        "Langkah 4: Terapkan Logaritma Natural (ln) di Kedua Ruas",
                        "$-0.223 t = \\ln(0.5882) \\approx -0.5306$."
                    ],
                    [
                        "Langkah 5: Hitung Nilai Waktu t",
                        "$t = \\frac{-0.5306}{-0.223} \\approx 2.38\\text{ jam}$ (sekitar 2 jam 23 menit sebelum pukul 14.00)."
                    ]
                ],
                "conclusion": "Waktu kematian korban diperkirakan terjadi pada pukul 11.37 siang (2 jam 23 menit sebelum jenazah ditemukan)."
            },
            "takeaways": [
                "Logaritma natural (ln) adalah kunci pemecah variabel pangkat eksponensial kontinu.",
                "Hukum pendinginan termal menghubungkan penurunan suhu biologis dengan jeda waktu forensik.",
                "Selamat! Kamu telah menguasai seluruh kurikulum Logaritma & Aplikasinya dengan tingkat pemahaman komprehensif!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE LOGARITMA: Mengapa operasi logaritma natural (ln) digunakan untuk memecahkan persamaan e^(kt) = C?",
                [
                    "Karena ln adalah invers dari fungsi eksponensial e^x sehingga ln(e^x) = x",
                    "Karena logaritma natural selalu bernilai 1",
                    "Karena bilangan Euler tidak bisa dibagi biasa"
                ],
                0,
                "Logaritma natural ln berbasis bilangan e, sehingga operasi ln(e^u) langsung mengekstrak pangkat u."
            ]
        }
    ]
}
