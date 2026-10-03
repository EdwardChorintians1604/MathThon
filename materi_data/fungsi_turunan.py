# -*- coding: utf-8 -*-
DATA = {
    "title": "Fungsi Turunan & Diferensial",
    "short": "Turunan",
    "icon": "bi-graph-up",
    "color": "#f59e0b",
    "desc": "Kuasai konsep laju perubahan sesaat, gradien garis singgung kurva, aturan turunan polinomial, perkalian-pembagian, aturan rantai, dan optimasi titik stasioner maksimum/minimum.",
    "babs": [
        {
            "title": "Fondasi: Laju Perubahan Rata-Rata Menuju Kecepatan Sesaat",
            "objectives": [
                "Memahami perbedaan konsep laju perubahan rata-rata (tali busur secant) dan laju perubahan sesaat (garis singgung tangent).",
                "Memahami definisi formal turunan fungsi berbasis limit h mendekati 0.",
                "Menginterpretasikan turunan pertama sebagai kemiringan (gradien) garis singgung kurva pada suatu titik."
            ],
            "hook": "Ketika polisi lalu lintas menembakkan radar 'speed gun' ke arah mobilmu di jalan tol, apakah radar tersebut mengukur kecepatan rata-rata perjalananmu dari Jakarta ke Bandung? Tentu tidak! Radar mengukur 'Kecepatan Sesaat' pada detik mikro saat sinar radar memantul. Turunan (Diferensial) adalah penemuan terhebat Sir Isaac Newton untuk mengukur laju perubahan tepat pada saat satu kedipan mata terjadi!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-speedometer text-primary\"></i> 1. Definisi Formal Turunan Berbasis Limit</h3>\n              <p>Turunan fungsi $f(x)$ di titik $x$, dinotasikan $f'(x)$ atau $\\frac{df}{dx}$, didefinisikan sebagai limit dari gradien tali busur saat jarak $\\Delta x = h$ mengecil mendekati nol:</p>\n              \\[ f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h} \\]\n              <p>Secara geometris, nilai $f'(c)$ adalah <strong>kemiringan (gradien $m$)</strong> dari garis yang menyinggung kurva $y = f(x)$ tepat di titik $(c, f(c))$.</p>\n            </div>\n            ",
            "pro_tip": "Jika $f'(x) > 0$, grafik sedang NAIK. Jika $f'(x) < 0$, grafik sedang TURUN. Jika $f'(x) = 0$, grafik berada pada posisi DATAR / STASIONER (puncak bukit atau lembah)!",
            "pitfall": "Jangan membagi dengan $h = 0$ secara langsung! Kamu harus menguraikan pembilang $[f(x+h) - f(x)]$ terlebih dahulu hingga faktor $h$ dapat dicoret sebelum memasukkan $h = 0$.",
            "fun_fact": "Isaac Newton menciptakan kalkulus diferensial pada tahun 1665 saat mengisolasi diri di pedesaan Woolsthorpe Manor ketika wabah pes melanda Universitas Cambridge—fenomena yang ia sebut 'Tahun Keajaiban' (Annus Mirabilis).",
            "formula": "f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h} \\quad ; \\quad m_{\\text{tan}} = f'(c)",
            "formula_params": [
                [
                    "f'(x)",
                    "Turunan pertama dari fungsi f(x)."
                ],
                [
                    "h",
                    "Pertambahan selisih interval variabel (\\Delta x \\to 0)."
                ],
                [
                    "m_{\\text{tan}}",
                    "Gradien kemiringan garis singgung kurva di titik c."
                ]
            ],
            "formula_intuition": "Mengecilkan selang waktu pengamatan hingga mendekati nol agar diperoleh laju perubahan instan sesaat.",
            "example": {
                "question": "Gunakan definisi formal limit turunan untuk menentukan turunan dari fungsi $f(x) = x^2$, lalu hitung kemiringan garis singgung kurva tersebut di titik $x = 3$!",
                "known": "$f(x) = x^2$ dan titik evaluasi $x = 3$.",
                "asked": "Fungsi turunan $f'(x)$ dan nilai $f'(3)$.",
                "steps": [
                    [
                        "Langkah 1: Masukkan ke Definisi Limit",
                        "$f'(x) = \\lim_{h \\to 0} \\frac{(x + h)^2 - x^2}{h}$."
                    ],
                    [
                        "Langkah 2: Ekspansi Kuadrat Pembilang",
                        "$(x + h)^2 - x^2 = x^2 + 2xh + h^2 - x^2 = 2xh + h^2$."
                    ],
                    [
                        "Langkah 3: Faktorkan dan Coret h",
                        "$\\lim_{h \\to 0} \\frac{h(2x + h)}{h} = \\lim_{h \\to 0} (2x + h)$."
                    ],
                    [
                        "Langkah 4: Masukkan $h = 0$",
                        "$f'(x) = 2x + 0 = 2x$."
                    ],
                    [
                        "Langkah 5: Evaluasi di Titik $x = 3$",
                        "$m = f'(3) = 2(3) = 6$."
                    ]
                ],
                "conclusion": "Fungsi turunan $f'(x) = 2x$ dan gradien kemiringan kurva di titik x = 3 adalah 6."
            },
            "takeaways": [
                "Turunan adalah limit laju perubahan rata-rata saat interval waktu mendekati nol.",
                "Secara grafis, turunan pertama merepresentasikan gradien garis singgung kurva di suatu titik.",
                "Turunan dari fungsi kuadrat $f(x) = x^2$ terbukti adalah fungsi linear $f'(x) = 2x$."
            ],
            "quiz": [
                "Jika fungsi posisi benda adalah $s(t) = t^2$, berapakah kecepatan sesaat benda pada detik ke-5?",
                [
                    "10 m/s",
                    "25 m/s",
                    "5 m/s"
                ],
                0,
                "Kecepatan sesaat adalah turunan posisi: v(t) = s'(t) = 2t. Pada t = 5, v(5) = 2(5) = 10 m/s."
            ]
        },
        {
            "title": "Anatomi: Kaidah Pangkat Baku & Sifat Aljabar Diferensial",
            "objectives": [
                "Menguasai Kaidah Pangkat Baku (Power Rule): d/dx (x^n) = n x^(n-1).",
                "Menerapkan turunan untuk konstanta, koefisien skalar, serta penjumlahan dan pengurangan suku polinomial.",
                "Menangani turunan fungsi berpangkat pecahan dan pangkat negatif."
            ],
            "hook": "Menghitung turunan menggunakan rumus limit panjang memakan waktu berlembar-lembar kertas. Untungnya para matematikawan menemukan pola emas: Power Rule! Cukup kalikan angka pangkat ke depan, lalu kurangi pangkatnya dengan angka 1. Kaidah ajaib ini memangkas perhitungan dari 10 menit menjadi hanya 2 detik saja!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-lightning-charge text-primary\"></i> 1. Kaidah Pangkat Baku (The Power Rule)</h3>\n              <p>Untuk setiap bilangan riil $n$:</p>\n              \\[ \\frac{d}{dx}(x^n) = n x^{n - 1} \\]\n              <ul class=\"dic-list\">\n                <li><strong>Turunan Konstanta:</strong> $\\frac{d}{dx}(c) = 0$ (karena konstanta tidak pernah berubah nilainya).</li>\n                <li><strong>Turunan Linear:</strong> $\\frac{d}{dx}(ax) = a$.</li>\n                <li><strong>Kaidah Pengali Konstanta:</strong> $\\frac{d}{dx}[k \\cdot f(x)] = k \\cdot f'(x)$.</li>\n                <li><strong>Kaidah Penjumlahan:</strong> $\\frac{d}{dx}[f(x) \\pm g(x)] = f'(x) \\pm g'(x)$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Ubah bentuk akar menjadi pangkat pecahan terlebih dahulu sebelum menerapkan power rule! Contoh: $\\sqrt{x} = x^{1/2} \\implies \\frac{1}{2} x^{-1/2} = \\frac{1}{2\\sqrt{x}}$!",
            "pitfall": "Turunan dari konstanta murni selalu NOL! Contoh: jika $f(x) = 5x + 8$, maka $f'(x) = 5 + 0 = 5$, jangan biarkan angka 8 tetap tertulis!",
            "fun_fact": "Dalam deep learning, algoritma Backpropagation menggunakan kaidah turunan rantai diferensial secara terus-menerus untuk memperbarui bobot neural network agar kecerdasan buatan semakin pintar.",
            "formula": "\\frac{d}{dx}(a x^n) = a \\cdot n x^{n-1} \\quad ; \\quad \\frac{d}{dx}(\\sqrt{x}) = \\frac{1}{2\\sqrt{x}} \\quad ; \\quad \\frac{d}{dx}\\left(\\frac{1}{x}\\right) = -\\frac{1}{x^2}",
            "formula_params": [
                [
                    "a",
                    "Koefisien pengali suku."
                ],
                [
                    "n",
                    "Pangkat eksponen bilangan riil."
                ],
                [
                    "n - 1",
                    "Pangkat baru yang berkurang satu satuan."
                ]
            ],
            "formula_intuition": "Menurunkan derajat polinomial satu tingkat untuk mengukur laju pertumbuhannya.",
            "example": {
                "question": "Tentukan turunan pertama dari fungsi polinomial: $f(x) = 4x^3 - 5x^2 + 7x - 9$!",
                "known": "Fungsi polinomial kubik derajat 3.",
                "asked": "Turunan pertama $f'(x)$.",
                "steps": [
                    [
                        "Langkah 1: Turunkan Suku Pertama $4x^3$",
                        "$4 \\cdot (3 x^{3-1}) = 12x^2$."
                    ],
                    [
                        "Langkah 2: Turunkan Suku Kedua $-5x^2$",
                        "$-5 \\cdot (2 x^{2-1}) = -10x$."
                    ],
                    [
                        "Langkah 3: Turunkan Suku Ketiga $7x$",
                        "$7 \\cdot (1 x^0) = 7$."
                    ],
                    [
                        "Langkah 4: Turunkan Suku Konstanta $-9$",
                        "$0$."
                    ],
                    [
                        "Langkah 5: Gabungkan Seluruh Suku",
                        "$f'(x) = 12x^2 - 10x + 7$."
                    ]
                ],
                "conclusion": "Turunan pertama dari fungsi tersebut adalah $f'(x) = 12x^2 - 10x + 7$."
            },
            "takeaways": [
                "Power Rule mengalikan pangkat ke depan lalu memotong pangkat sebesar 1: $n x^{n-1}$.",
                "Turunan konstanta angka tunggal selalu sama dengan nol.",
                "Operator turunan dapat didistribusikan ke setiap suku penjumlahan dan pengurangan."
            ],
            "quiz": [
                "Berapakah turunan pertama dari $f(x) = 3x^4 - 2x + 5$?",
                [
                    "12x³ - 2",
                    "12x³ - 2x",
                    "7x³ - 2"
                ],
                0,
                "d/dx(3x^4) = 12x^3, d/dx(-2x) = -2, d/dx(5) = 0. Maka hasilnya adalah 12x^3 - 2."
            ]
        },
        {
            "title": "Mekanika: Aturan Perkalian (uv), Pembagian (u/v) & Aturan Rantai (Chain Rule)",
            "objectives": [
                "Menerapkan Aturan Perkalian Produk: d/dx (u * v) = u'v + uv'.",
                "Menerapkan Aturan Pembagian Kuosien: d/dx (u / v) = (u'v - uv') / v^2.",
                "Menguasai Aturan Rantai (Chain Rule) untuk fungsi komposisi berlapis: dy/dx = (dy/du) * (du/dx)."
            ],
            "hook": "Apa yang terjadi jika dua fungsi yang berubah saling dikalikan, seperti Volume Balok = Luas Alas(t) * Tinggi(t)? Kita tidak bisa hanya mengalikan turunannya secara sembarangan ($u' \\cdot v'$ adalah SALAH BESAR). Aturan Perkalian Leibniz $u'v + uv'$ adalah kaidah mekanik yang memastikan semua interaksi antar-variabel terhitung secara akurat!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-gear-wide-connected text-primary\"></i> 1. Tiga Kaidah Mekanika Lanjutan</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Aturan Perkalian (Product Rule):</strong>\n                  \\[ (u \\cdot v)' = u'v + uv' \\]\n                </li>\n                <li><strong>Aturan Pembagian (Quotient Rule):</strong>\n                  \\[ \\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2} \\]\n                </li>\n                <li><strong>Aturan Rantai (Chain Rule - Fungsi Komposisi):</strong> Jika $y = f(u)$ dan $u = g(x)$, maka:\n                  \\[ \\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx} \\]\n                  Aturan Praktis Pangkat: $\\frac{d}{dx}[u(x)]^n = n [u(x)]^{n-1} \\cdot u'(x)$.\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mengingat Aturan Rantai fungsi berpangkat $[u(x)]^n$: Ingat aturan 'Turunkan Kulit Luar, lalu Kalikan dengan Turunan Isinya'!",
            "pitfall": "Pada aturan pembagian, urutan tanda pengurangan sangat krusial! Selalu dahulukan $u'v$ dikurangi $uv'$. Jangan sampai terbalik menjadi $uv' - u'v$ karena pengurangan tidak bersifat komutatif!",
            "fun_fact": "Aturan Rantai (Chain Rule) adalah formula matematika paling berharga di era kecerdasan buatan modern karena seluruh algoritma pelatihan model bahasa besar (LLM) seperti GPT-4 berjalan di atas prinsip diferensiasi aturan rantai berlapis.",
            "formula": "(uv)' = u'v + uv' \\quad ; \\quad \\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2} \\quad ; \\quad \\frac{d}{dx}[u(x)]^n = n [u(x)]^{n-1} u'(x)",
            "formula_params": [
                [
                    "u, v",
                    "Fungsi-fungsi variabel x yang dapat diturunkan."
                ],
                [
                    "u', v'",
                    "Turunan pertama masing-masing fungsi."
                ],
                [
                    "v^2",
                    "Kuadrat fungsi penyebut."
                ]
            ],
            "formula_intuition": "Menghitung laju perubahan total saat kedua komponen saling mempengaruhi secara multiplikatif.",
            "example": {
                "question": "Tentukan turunan pertama dari fungsi komposisi berpangkat: $y = (3x^2 - 5)^4$!",
                "known": "Fungsi komposisi luar berpangkat 4 dengan fungsi dalam $u = 3x^2 - 5$.",
                "asked": "Turunan $y'$ menggunakan aturan rantai.",
                "steps": [
                    [
                        "Langkah 1: Identifikasi Fungsi Dalam u dan Turunannya u'",
                        "$u = 3x^2 - 5 \\implies u' = 6x$."
                    ],
                    [
                        "Langkah 2: Terapkan Aturan Pangkat Luar",
                        "Turunkan pangkat 4 ke depan: $4(u)^{4-1} = 4(3x^2 - 5)^3$."
                    ],
                    [
                        "Langkah 3: Kalikan dengan Turunan Dalam u'",
                        "$y' = 4(3x^2 - 5)^3 \\cdot (6x)$."
                    ],
                    [
                        "Langkah 4: Rapikan Perkalian Koefisien Aljabar",
                        "$y' = 24x(3x^2 - 5)^3$."
                    ]
                ],
                "conclusion": "Hasil turunan pertamanya adalah $y' = 24x(3x^2 - 5)^3$."
            },
            "takeaways": [
                "Turunan perkalian dua fungsi adalah $u'v + uv'$, bukan $u'v'$.",
                "Turunan pembagian adalah $\\frac{u'v - uv'}{v^2}$.",
                "Aturan rantai mengalikan turunan fungsi luar dengan turunan fungsi dalam."
            ],
            "quiz": [
                "Berapakah turunan pertama dari $y = (2x + 1)^3$?",
                [
                    "6(2x + 1)²",
                    "3(2x + 1)²",
                    "2(2x + 1)²"
                ],
                0,
                "Gunakan aturan rantai: y' = 3(2x + 1)^2 * d/dx(2x + 1) = 3(2x + 1)^2 * 2 = 6(2x + 1)^2."
            ]
        },
        {
            "title": "Pemodelan: Titik Stasioner & Optimasi Nilai Maksimum/Minimum",
            "objectives": [
                "Menentukan titik stasioner kurva dengan syarat f'(x) = 0.",
                "Menguji jenis titik stasioner (Maksimum Lokal, Minimum Lokal, atau Titik Belok) menggunakan Uji Turunan Kedua f''(x).",
                "Memodelkan masalah optimasi biaya produksi minimum dan laba penjualan maksimum."
            ],
            "hook": "Setiap CEO perusahaan di dunia menginginkan dua hal: MEMAKSIMALKAN keuntungan dan MEMINIMALKAN biaya pengeluaran. Bagaimana cara menemukan angka produksi yang tepat agar laba mencapai titik puncak absolut? Matematika kalkulus menjawabnya dengan syarat stasioner: di puncak tertinggi dan lembah terendah suatu kurva, kemiringan garis singgungnya tepat bernilai NOL ($f'(x) = 0$)!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-graph-up-arrow text-primary\"></i> 1. Kriteria Titik Stasioner</h3>\n              <p>Titik stasioner terjadi pada nilai $x$ yang menyebabkan gradien garis singgung mendatar:</p>\n              \\[ f'(x) = 0 \\]\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-check2-circle text-primary\"></i> 2. Uji Turunan Kedua ($f''(x)$) untuk Menentukan Jenis Titik</h3>\n              <ul class=\"dic-list\">\n                <li>Jika $f''(c) < 0$: Kurva cekung ke bawah $\\cap$, menghasilkan <strong>Titik Maksimum</strong> (Puncak).</li>\n                <li>Jika $f''(c) > 0$: Kurva cekung ke atas $\\cup$, menghasilkan <strong>Titik Minimum</strong> (Lembah).</li>\n                <li>Jika $f''(c) = 0$: Uji gagal, kemungkinan merupakan <strong>Titik Belok</strong> (Inflexion Point).</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mengingat tanda turunan kedua: $f''(x) < 0$ (negatif = sedih/cemberut = kurva melengkung ke bawah seperti bukit = MAKSIMUM). $f''(x) > 0$ (positif = senyum = kurva melengkung ke atas seperti mangkok = MINIMUM)!",
            "pitfall": "Jangan berhenti setelah menemukan nilai x stasioner! Jika soal meminta 'Nilai Maksimum', kamu wajib memasukkan nilai x tersebut kembali ke fungsi ASAL $f(x)$, bukan ke $f'(x)$!",
            "fun_fact": "Algoritma Gradient Descent yang melatih model AI canggih seperti ChatGPT dan mobil otonom Tesla bekerja dengan prinsip turunan ini: bergerak menuruni gradien lereng fungsi kerugian (Loss Function) hingga mencapai titik minimum global!",
            "formula": "f'(x) = 0 \\quad (\\text{Syarat Stasioner}) \\quad ; \\quad f''(x_{\\text{maks}}) < 0 \\quad ; \\quad f''(x_{\\text{min}}) > 0",
            "formula_params": [
                [
                    "f'(x) = 0",
                    "Kondisi garis singgung mendatar sempurna."
                ],
                [
                    "f''(x)",
                    "Turunan kedua yang mengukur kecekungan kurva (kelengkungan)."
                ]
            ],
            "formula_intuition": "Titik ekstrem adalah titik pergantian arah: dari naik menjadi turun (puncak) atau dari turun menjadi naik (lembah).",
            "example": {
                "question": "Sebuah pabrik memproduksi x unit barang dengan total keuntungan yang dimodelkan oleh fungsi: $U(x) = -2x^2 + 80x - 300$ (dalam juta rupiah). Tentukan jumlah unit barang yang harus diproduksi agar keuntungan mencapai titik maksimum, dan berapakah keuntungan maksimum tersebut!",
                "known": "$U(x) = -2x^2 + 80x - 300$.",
                "asked": "Jumlah unit x untuk laba maksimum dan nilai keuntungan maksimum.",
                "steps": [
                    [
                        "Langkah 1: Terapkan Syarat Stasioner $U'(x) = 0$",
                        "$U'(x) = -4x + 80 = 0$."
                    ],
                    [
                        "Langkah 2: Selesaikan Nilai x",
                        "$-4x = -80 \\implies x = \\frac{-80}{-4} = 20\\text{ unit}$."
                    ],
                    [
                        "Langkah 3: Uji Turunan Kedua untuk Kepastian Titik Maksimum",
                        "$U''(x) = -4$. Karena $-4 < 0$ (negatif), titik $x = 20$ terbukti titik MAKSIMUM mutlak."
                    ],
                    [
                        "Langkah 4: Masukkan $x = 20$ ke Fungsi Keuntungan Mula-Mula $U(x)$",
                        "$U(20) = -2(20)^2 + 80(20) - 300 = -2(400) + 1600 - 300 = -800 + 1600 - 300 = 500$ juta rupiah."
                    ]
                ],
                "conclusion": "Pabrik harus memproduksi 20 unit barang untuk memperoleh keuntungan maksimum sebesar Rp 500.000.000."
            },
            "takeaways": [
                "Titik stasioner diperoleh dengan menetapkan turunan pertama sama dengan nol: $f'(x) = 0$.",
                "Turunan kedua negatif ($f'' < 0$) menandakan titik balik maksimum, sedangkan positif ($f'' > 0$) menandakan titik balik minimum.",
                "Optimasi turunan digunakan luas dalam ilmu ekonomi, rekayasa fisika, dan kecerdasan buatan."
            ],
            "quiz": [
                "Sebuah peluru ditembakkan ke atas dengan ketinggian $h(t) = 40t - 5t^2$ meter. Kapan peluru mencapai ketinggian maksimum?",
                [
                    "t = 4 detik",
                    "t = 8 detik",
                    "t = 2 detik"
                ],
                0,
                "Syarat maksimum: h'(t) = 0 => 40 - 10t = 0 => 10t = 40 => t = 4 detik."
            ]
        },
        {
            "title": "Capstone: Desain Profil Sayap Aerodinamis & Optimasi Efisiensi Bahan Bakar",
            "objectives": [
                "Mengintegrasikan kaidah turunan, analisis stasioner, dan pemodelan polinomial untuk mendesain sayap pesawat terbang aerodinamis.",
                "Menentukan titik kelengkungan maksimum untuk menciptakan gaya angkat (Lift) optimal dengan hambatan udara (Drag) minimal.",
                "Mengevaluasi trade-off parameter teknik penerbangan menggunakan kalkulus diferensial."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Aeronautical Engineer pada proyek pesawat tanpa awak supersonik. Profil kelengkungan sayap atas pesawat dimodelkan oleh fungsi polinomial: y = -x^3 + 6x^2 - 9x + 20 pada rentang koordinat chord sayap 0 <= x <= 4. Pilot membutuhkan analisis presisi: di titik koordinat x berapakah ketebalan sayap mencapai puncak maksimum absolut? Dan di mana titik belok aerodinamis terjadi? Tuntaskan misi kalkulus rekayasa aeronautika ini!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Profil Sayap Aerofoil NACA</h3>\n              <p>Kelengkungan sayap atas pesawat menghasilkan perbedaan kecepatan aliran udara Bernoulli yang menciptakan gaya angkat vertikal. Titik puncak kelengkungan sayap adalah titik stasioner lokal dari fungsi kontur aerofoil.</p>\n            </div>\n            ",
            "pro_tip": "Dalam rekayasa aerodinamika, titik belok ($f''(x) = 0$) menandai transisi transisi lapisan batas udara (boundary layer transition) dari aliran laminer mulus menjadi aliran turbulen!",
            "pitfall": "Selalu periksa batas domain fisik ($0 \\le x \\le 4$)! Titik stasioner yang berada di luar domain sayap harus diabaikan.",
            "fun_fact": "Profil sayap aerofoil pesawat komersial modern dirancang menggunakan algoritma optimasi kalkulus Adjoint-State Method yang mengoptimalkan jutaan titik kelengkungan secara otomatis untuk menghemat miliaran liter avtur dunia setiap tahun.",
            "formula": "y'(x) = 0 \\implies \\text{Puncak Aerofoil} \\quad ; \\quad y''(x) = 0 \\implies \\text{Titik Belok Aliran}",
            "formula_params": [
                [
                    "y(x)",
                    "Kontur elevasi ketebalan sayap."
                ],
                [
                    "y'(x)",
                    "Gradien kemiringan permukaan sayap."
                ],
                [
                    "y''(x)",
                    "Laju perubahan kelengkungan (kurvatur)."
                ]
            ],
            "formula_intuition": "Menemukan titik transisi fisik fluida dengan melacak kemiringan garis singgung nol.",
            "example": {
                "question": "Profil sayap atas dimodelkan oleh $y = -x^3 + 6x^2 - 9x + 20$ untuk interval $0 \\le x \\le 4$. Tentukan koordinat x tempat ketebalan sayap mencapai puncak lokal maksimum, dan tentukan letak titik beloknya!",
                "known": "$y = -x^3 + 6x^2 - 9x + 20$ pada $0 \\le x \\le 4$.",
                "asked": "Titik puncak maksimum lokal dan titik belok.",
                "steps": [
                    [
                        "Langkah 1: Cari Turunan Pertama $y'$",
                        "$y' = -3x^2 + 12x - 9$."
                    ],
                    [
                        "Langkah 2: Terapkan Syarat Stasioner $y' = 0$",
                        "$-3x^2 + 12x - 9 = 0$. Bagi dengan -3: $x^2 - 4x + 3 = 0$."
                    ],
                    [
                        "Langkah 3: Faktorkan untuk Mendapatkan Titik Kritis",
                        "$(x - 1)(x - 3) = 0 \\implies x_1 = 1$ atau $x_2 = 3$."
                    ],
                    [
                        "Langkah 4: Uji Turunan Kedua $y'' = -6x + 12$",
                        "Pada $x = 1$: $y''(1) = -6(1) + 12 = +6 > 0$ (Lembah Minimum Lokal).<br>Pada $x = 3$: $y''(3) = -6(3) + 12 = -6 < 0$ (Puncak MAKSIMUM Lokal!)."
                    ],
                    [
                        "Langkah 5: Tentukan Titik Belok dengan Syarat $y'' = 0$",
                        "$-6x + 12 = 0 \\implies 6x = 12 \\implies x = 2$."
                    ]
                ],
                "conclusion": "Puncak ketebalan sayap maksimum lokal tercapai tepat pada x = 3, dan titik belok kurvatur aerofoil berada pada x = 2."
            },
            "takeaways": [
                "Kalkulus diferensial memegang peranan krusial dalam optimasi rekayasa penerbangan dan aerodinamika.",
                "Uji turunan pertama mendeteksi titik stasioner, sedangkan uji turunan kedua memastikan tipe ekstremnya.",
                "Selamat! Kamu telah menguasai konsep Fungsi Turunan & Diferensial dengan tingkat kompetensi luar biasa!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE TURUNAN: Pada fungsi profil sayap $y = -x^3 + 6x^2 - 9x + 20$, berapakah nilai kelengkungan turunan kedua y''(x) di titik belok x = 2?",
                [
                    "0",
                    "-6",
                    "+6"
                ],
                0,
                "Titik belok didefinisikan secara mutlak oleh syarat y''(x) = 0. Pada x = 2: y''(2) = -6(2) + 12 = 0."
            ]
        }
    ]
}
