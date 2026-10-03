# -*- coding: utf-8 -*-
DATA = {
    "title": "Geometri: Bangun Datar & Ruang",
    "short": "Geometri",
    "icon": "bi-pentagon",
    "color": "#a855f7",
    "desc": "Kuasai dimensi ruang 2D dan 3D, Teorema Pythagoras, keliling dan luas bangun datar, volume dan luas permukaan bangun ruang, serta hukum skala spasial.",
    "babs": [
        {
            "title": "Fondasi: Dimensi Geometri Spasial & Teorema Pythagoras",
            "objectives": [
                "Memahami perbedaan dimensi spasial: Titik (0D), Garis Panjang (1D), Luas Penampang (2D), dan Volume Ruang (3D).",
                "Membuktikan Teorema Pythagoras secara geometris pada segitiga siku-siku (c^2 = a^2 + b^2).",
                "Menghitung diagonal ruang balok dan kubus menggunakan generalisasi Pythagoras 3D."
            ],
            "hook": "Tahukah kamu mengapa raksasa setinggi 20 meter seperti di film fiksi tidak mungkin bisa hidup di dunia nyata? Jika tinggi tubuh raksasa membesar 10 kali lipat, luas tulang penopang kakinya hanya membesar 100 kali (10^2), tetapi bobot massa tubuhnya melonjak 1.000 kali lipat (10^3)! Tulang kakinya akan patah seketika di bawah berat badannya sendiri. Geometri bukan sekadar hafalan rumus; geometri adalah aturan hukum fisika ruang yang membatasi bentuk seluruh makhluk hidup dan konstruksi gedung di alam semesta!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-bounding-box text-primary\"></i> 1. Hierarki Dimensi Ruang</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Dimensi 0 (Titik):</strong> Tidak memiliki panjang, luas, maupun volume. Hanya menyatakan posisi koordinat.</li>\n                <li><strong>Dimensi 1 (Garis / Panjang $L$):</strong> Memiliki satuan meter (m). Contoh: keliling, sisi, radius.</li>\n                <li><strong>Dimensi 2 (Bidang Datar / Luas $A$):</strong> Memiliki satuan meter persegi ($m^2$). Skala area bertumbuh kuadratik ($k^2$).</li>\n                <li><strong>Dimensi 3 (Ruang / Volume $V$):</strong> Memiliki satuan meter kubik ($m^3$). Skala kapasitas bertumbuh kubik ($k^3$).</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-triangle-fill text-primary\"></i> 2. Teorema Pythagoras: Jembatan Antar-Dimensi</h3>\n              <p>Pada segitiga siku-siku dengan sisi siku-siku $a$ dan $b$ serta sisi miring (hipotenusa) $c$:</p>\n              \\[ c^2 = a^2 + b^2 \\iff c = \\sqrt{a^2 + b^2} \\]\n              <p>Perluasan Pythagoras pada Diagonal Ruang Balok 3D:</p>\n              \\[ d_{\\text{ruang}} = \\sqrt{p^2 + l^2 + t^2} \\]\n            </div>\n            ",
            "pro_tip": "Kuasai angka Triple Pythagoras populer: (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17) beserta kelipatannya. Menghafal angka ini menghemat 90% waktu pengerjaan soal ujian!",
            "pitfall": "Teorema Pythagoras HANYA BERLAKU pada segitiga siku-siku (sudut tepat 90°)! Untuk segitiga sembarang lancip atau tumpul, kamu harus menggunakan Aturan Cosinus.",
            "fun_fact": "Meskipun dinamai menurut filsuf Yunani Pythagoras dari Samos (sekitar 500 SM), tablet tanah liat Babilonia kuno Plimpton 322 membuktikan bahwa bangsa Mesopotamia telah menggunakan angka Triple Pythagoras lebih dari 1.000 tahun sebelum Pythagoras lahir!",
            "formula": "c = \\sqrt{a^2 + b^2} \\quad ; \\quad d_{\\text{ruang}} = \\sqrt{p^2 + l^2 + t^2}",
            "formula_params": [
                [
                    "a, b",
                    "Panjang sisi-sisi tegak siku-siku."
                ],
                [
                    "c",
                    "Sisi miring hipotenusa terpanjang."
                ],
                [
                    "d_{\\text{ruang}}",
                    "Panjang diagonal ruang balok 3D."
                ]
            ],
            "formula_intuition": "Luas bujur sangkar pada sisi miring sama persis dengan penjumlahan luas bujur sangkar pada kedua sisi siku-sikunya.",
            "example": {
                "question": "Sebuah kamar tidur berukuran panjang 4 meter, lebar 3 meter, dan tinggi 12 meter. Berapakah panjang jarak garis lurus terjauh dari sudut lantai bawah ke sudut plafon langit-langit atas yang berseberangan (diagonal ruang)?",
                "known": "$p = 4\\text{ m}, l = 3\\text{ m}, t = 12\\text{ m}$.",
                "asked": "Diagonal ruang kamar $d_{\\text{ruang}}$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Kuadrat Masing-Masing Dimensi",
                        "$p^2 = 4^2 = 16$.<br>$l^2 = 3^2 = 9$.<br>$t^2 = 12^2 = 144$."
                    ],
                    [
                        "Langkah 2: Jumlahkan Ketiga Kuadrat Dimensi",
                        "$16 + 9 + 144 = 169$."
                    ],
                    [
                        "Langkah 3: Ambil Akar Kuadrat Total",
                        "$d_{\\text{ruang}} = \\sqrt{169} = 13\\text{ meter}$."
                    ]
                ],
                "conclusion": "Panjang diagonal ruang kamar tidur tersebut adalah tepat 13 meter."
            },
            "takeaways": [
                "Dimensi 1 (panjang), Dimensi 2 (luas), dan Dimensi 3 (volume) bertumbuh dengan faktor skala pangkat berbeda (k, k², k³).",
                "Teorema Pythagoras $c^2 = a^2 + b^2$ adalah dasar pengukuran jarak euklides di seluruh cabang matematika.",
                "Diagonal ruang balok 3D dihitung dengan $\\sqrt{p^2 + l^2 + t^2}$."
            ],
            "quiz": [
                "Sebuah segitiga siku-siku memiliki sisi tegak 6 cm dan 8 cm. Berapakah panjang sisi miringnya?",
                [
                    "10 cm",
                    "14 cm",
                    "12 cm"
                ],
                0,
                "c = √(6² + 8²) = √(36 + 64) = √100 = 10 cm (Kelipatan 2 dari Triple 3-4-5)."
            ]
        },
        {
            "title": "Anatomi: Bangun Datar Baku (Segitiga, Segiempat & Lingkaran)",
            "objectives": [
                "Memahami formulasi keliling dan luas bangun datar baku: Segitiga, Persegi, Persegi Panjang, Trapesium, dan Jajaran Genjang.",
                "Memahami konstanta Pi (\\pi) sebagai rasio keliling terhadap diameter lingkaran.",
                "Menghitung luas daerah gabungan dan luas bangun arsir komposit."
            ],
            "hook": "Berapakah nilai pasti dari bilangan Pi (\\pi)? Apakah 22/7? Bukan, 22/7 hanyalah pecahan hampiran! Pi (3.14159...) adalah bilangan irasional misterius yang muncul secara alami di seluruh lingkaran di alam semesta: jika kamu membagi keliling roda apa pun dengan diameternya, hasilnya SELALU persis sama dengan Pi! Dari cincin planet Saturnus hingga riak tetesan air di cangkir kopimu, geometri lingkaran terikat oleh konstanta kosmis ini.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-circle text-primary\"></i> 1. Anatomi Lingkaran & Konstanta Pi</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Keliling Lingkaran:</strong> $K = 2\\pi r = \\pi d$.</li>\n                <li><strong>Luas Lingkaran:</strong> $L = \\pi r^2 = \\frac{1}{4} \\pi d^2$.</li>\n                <li><strong>Konstanta $\\pi$:</strong> Didefinisikan sebagai rasio $\\frac{\\text{Keliling}}{\\text{Diameter}}$. Gunakan $\\pi \\approx \\frac{22}{7}$ jika jari-jari kelipatan 7, dan gunakan $\\pi \\approx 3.14$ untuk angka lainnya.</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-square text-primary\"></i> 2. Formula Bangun Datar Populer</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Segitiga:</strong> $\\text{Luas} = \\frac{1}{2} \\times a \\times t$.</li>\n                <li><strong>Trapesium:</strong> $\\text{Luas} = \\frac{(a + b) \\times t}{2}$ (Jumlah sisi sejajar kali tinggi bagi dua).</li>\n                <li><strong>Jajaran Genjang:</strong> $\\text{Luas} = a \\times t$.</li>\n                <li><strong>Belah Ketupat / Layang-layang:</strong> $\\text{Luas} = \\frac{d_1 \\times d_2}{2}$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk menghitung luas daerah arsir komposit: Selalu gunakan strategi pengurangan bentuk: Luas Arsir = Luas Bangun Luar Besar dikurangi Luas Bangun Dalam!",
            "pitfall": "Jangan tertukar antara Jari-Jari (r) dan Diameter (d)! Jari-jari adalah setengah dari diameter ($r = d/2$). Memasukkan diameter langsung ke rumus $\\pi r^2$ akan membuat luasnya salah 4 kali lipat!",
            "fun_fact": "Simbol huruf Yunani $\\pi$ pertama kali dipopulerkan oleh matematikawan jenius Swiss Leonhard Euler pada tahun 1737 dan kini digitnya telah dihitung oleh superkomputer hingga lebih dari 100 triliun digit di belakang koma!",
            "formula": "L_{\\text{lingkaran}} = \\pi r^2 \\quad ; \\quad K = 2\\pi r \\quad ; \\quad L_{\\text{trapesium}} = \\frac{(a + b)t}{2}",
            "formula_params": [
                [
                    "r",
                    "Jari-jari lingkaran (setengah diameter)."
                ],
                [
                    "\\pi",
                    "Konstanta rasio lingkaran (22/7 atau 3.14159...)."
                ],
                [
                    "a, b",
                    "Panjang sisi-sisi sejajar trapesium."
                ],
                [
                    "t",
                    "Tinggi tegak lurus bangun datar."
                ]
            ],
            "formula_intuition": "Luas lingkaran didapat dari memotong lingkaran menjadi irisan juring-juring tak berhingga lalu menatanya menjadi persegi panjang seluas $(\\pi r) \\times r = \\pi r^2$.",
            "example": {
                "question": "Sebuah taman kota berbentuk lingkaran memiliki diameter 28 meter. Di sekeliling taman akan dipasangi pagar kawat pembatas dan area dalamnya akan ditanami rumput jepang. Hitunglah: (a) Panjang pagar kawat keliling yang dibutuhkan, dan (b) Luas area rumput taman tersebut!",
                "known": "Diameter $d = 28\\text{ m} \\implies r = 14\\text{ m}$ (kelipatan 7, gunakan $\\pi = 22/7$).",
                "asked": "Keliling K dan Luas L.",
                "steps": [
                    [
                        "Langkah 1: Hitung Keliling K",
                        "$K = 2\\pi r = 2 \\times \\frac{22}{7} \\times 14 = 2 \\times 22 \\times 2 = 88\\text{ meter}$."
                    ],
                    [
                        "Langkah 2: Hitung Luas Area L",
                        "$L = \\pi r^2 = \\frac{22}{7} \\times 14 \\times 14 = 22 \\times 2 \\times 14 = 44 \\times 14 = 616\\text{ meter persegi (m}^2\\text{)}$."
                    ]
                ],
                "conclusion": "Panjang kawat pagar yang dibutuhkan adalah 88 meter, dan luas area penanaman rumput adalah 616 m²."
            },
            "takeaways": [
                "Luas lingkaran bertumbuh kuadratik terhadap jari-jarinya: $L = \\pi r^2$.",
                "Keliling lingkaran berbanding lurus dengan diameter: $K = \\pi d$.",
                "Tinggi pada segitiga dan trapesium wajib diukur tegak lurus terhadap sisi alas."
            ],
            "quiz": [
                "Sebuah lingkaran memiliki jari-jari 7 cm. Berapakah luas area lingkaran tersebut?",
                [
                    "154 cm²",
                    "44 cm²",
                    "308 cm²"
                ],
                0,
                "Luas = (22/7) * 7 * 7 = 22 * 7 = 154 cm²."
            ]
        },
        {
            "title": "Mekanika: Luas Permukaan & Volume Bangun Ruang 3D",
            "objectives": [
                "Menguasai formula volume dan luas permukaan: Kubus, Balok, Tabung (Silinder), Kerucut, dan Bola.",
                "Memahami hubungan antara Prisma-Tabung (Alas x Tinggi) dan Limas-Kerucut (1/3 Alas x Tinggi).",
                "Menghitung kapasitas kubik fluida (liter dan meter kubik) serta kebutuhan bahan pelapis permukaan."
            ],
            "hook": "Berapakah volume es krim yang dapat ditampung di dalam kerucut (cone) dibandingkan dengan tabung silinder yang memiliki alas dan tinggi yang sama persis? Jika kamu mengisi kerucut itu dengan air lalu menuangkannya ke dalam tabung silinder, kamu butuh TEPAT TIGA KALI TUANGAN kerucut untuk mengisi tabung tersebut sampai penuh! Inilah alasan elegan mengapa rumus volume kerucut dan limas selalu memuat faktor pengali 1/3!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-box text-primary\"></i> 1. Hubungan Indah Volume Bangun Ruang</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Keluarga Prisma & Tabung (Dinding Tegak Lurus):</strong>\n                  \\[ \\text{Volume} = \\text{Luas Alas} \\times \\text{Tinggi} \\]\n                  Tabung (Silinder): $V = \\pi r^2 t$, Luas Permukaan: $L_p = 2\\pi r(r + t)$.\n                </li>\n                <li><strong>Keluarga Limas & Kerucut (Meruncing ke Satu Puncak):</strong>\n                  \\[ \\text{Volume} = \\frac{1}{3} \\times \\text{Luas Alas} \\times \\text{Tinggi} \\]\n                  Kerucut: $V = \\frac{1}{3}\\pi r^2 t$, dengan garis pelukis $s = \\sqrt{r^2 + t^2}$.\n                </li>\n                <li><strong>Bola Murni:</strong>\n                  \\[ \\text{Volume} = \\frac{4}{3}\\pi r^3 \\quad ; \\quad \\text{Luas Permukaan} = 4\\pi r^2 \\]\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Konversi volume praktis yang wajib dihafal: $1\\text{ liter} = 1\\text{ dm}^3 = 1.000\\text{ cm}^3$, dan $1\\text{ meter kubik (m}^3\\text{)} = 1.000\\text{ liter}$!",
            "pitfall": "Pada kerucut, jangan tertukar antara Tinggi Tegak (t) dan Garis Pelukis Miring (s)! Rumus volume menggunakan tinggi tegak t, sedangkan luas selimut menggunakan garis pelukis s ($\\pi r s$).",
            "fun_fact": "Filsuf Yunani Archimedes sangat bangga membuktikan bahwa perbandingan volume bola terhadap silinder penampungnya adalah tepat 2 banding 3, sehingga ia meminta agar gambar bola di dalam silinder dipahat di atas batu nisannya.",
            "formula": "V_{\\text{tabung}} = \\pi r^2 t \\quad ; \\quad V_{\\text{kerucut}} = \\frac{1}{3}\\pi r^2 t \\quad ; \\quad V_{\\text{bola}} = \\frac{4}{3}\\pi r^3",
            "formula_params": [
                [
                    "r",
                    "Jari-jari penampang lingkaran."
                ],
                [
                    "t",
                    "Tinggi tegak bangun ruang."
                ],
                [
                    "s",
                    "Garis pelukis kerucut ($s = \\sqrt{r^2 + t^2}$)."
                ]
            ],
            "formula_intuition": "Volume adalah hasil proyeksi luas penampang 2D sepanjang dimensi tinggi ketiga ruang.",
            "example": {
                "question": "Sebuah tangki penampung air berbentuk silinder tabung memiliki jari-jari alas 70 cm dan tinggi 200 cm. Hitunglah volume kapasitas air maksimal tangki tersebut dalam satuan Liter!",
                "known": "$r = 70\\text{ cm} = 7\\text{ dm}$, $t = 200\\text{ cm} = 20\\text{ dm}$ (Gunakan dm agar langsung bernilai liter).",
                "asked": "Volume kapasitas dalam liter.",
                "steps": [
                    [
                        "Langkah 1: Gunakan Satuan Desimeter untuk Liter",
                        "$r = 7\\text{ dm}$ dan $t = 20\\text{ dm}$ (karena $1\\text{ dm}^3 = 1\\text{ Liter}$)."
                    ],
                    [
                        "Langkah 2: Masukkan ke Rumus Volume Silinder Tabung",
                        "$V = \\pi r^2 t = \\frac{22}{7} \\times 7^2 \\times 20$."
                    ],
                    [
                        "Langkah 3: Hitung Perkalian Aljabar",
                        "$V = \\frac{22}{7} \\times 49 \\times 20 = 22 \\times 7 \\times 20 = 154 \\times 20 = 3.080\\text{ dm}^3$."
                    ],
                    [
                        "Langkah 4: Konversikan ke Satuan Liter",
                        "$3.080\\text{ dm}^3 = 3.080\\text{ liter}$."
                    ]
                ],
                "conclusion": "Tangki silinder tersebut mampu menampung air maksimal sebanyak 3.080 Liter."
            },
            "takeaways": [
                "Volume tabung adalah $\\pi r^2 t$, sedangkan volume kerucut adalah sepertiganya: $\\frac{1}{3}\\pi r^2 t$.",
                "Volume bola murni adalah $\\frac{4}{3}\\pi r^3$ dan luas kulit bolanya adalah $4\\pi r^2$.",
                "Satu desimeter kubik ($1\\text{ dm}^3$) tepat setara dengan satu liter air."
            ],
            "quiz": [
                "Sebuah kerucut memiliki jari-jari dan tinggi yang sama persis dengan sebuah tabung silinder. Jika volume tabung adalah 900 cm³, berapakah volume kerucut tersebut?",
                [
                    "300 cm³",
                    "450 cm³",
                    "600 cm³"
                ],
                0,
                "Volume kerucut adalah tepat 1/3 dari volume tabung dengan dimensi sama: (1/3) * 900 = 300 cm³."
            ]
        },
        {
            "title": "Pemodelan: Hukum Skala Spasial Kuadratik vs Kubik",
            "objectives": [
                "Memahami Hukum Penskalaan Geometris (Square-Cube Law): Luas ~ k^2 sedangkan Volume ~ k^3.",
                "Menganalisis mengapa hewan bertubuh besar membutuhkan struktur tulang yang jauh lebih tebal dibanding serangga.",
                "Memodelkan efisiensi termal rasio Luas Permukaan terhadap Volume (L/V) dalam desain industri pendinginan."
            ],
            "hook": "Pernahkah kamu bertanya mengapa gajah memiliki kaki silinder raksasa yang sangat tebal mirip pilar gedung, sedangkan laba-laba atau nyamuk memiliki kaki yang sangat ramping seperti benang tipis? Mengapa tidak ada serangga berukuran sebesar helikopter? Jawabannya ada pada Hukum Skala Kuadrat-Kubik Galileo Galilei: saat sebuah objek diperbesar k kali lipat, luas penampang tulangnya hanya membesar k² kali, tetapi beban volume massanya meledak k³ kali lipat!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-aspect-ratio text-primary\"></i> 1. Hukum Penskalaan Galileo (Square-Cube Law)</h3>\n              <p>Jika sebuah bangun geometri diskalakan secara proporsional sebesar faktor pengali $k$ di seluruh dimensinya:</p>\n              <ul class=\"dic-list\">\n                <li>Panjang Linier (1D) bertambah sebesar: $k$ kali lipat.</li>\n                <li>Luas Permukaan (2D) bertambah sebesar: $k^2$ kali lipat.</li>\n                <li>Volume & Massa (3D) bertambah sebesar: $k^3$ kali lipat!</li>\n              </ul>\n              <h4 class=\"fw-bold text-info mt-3\"><i class=\"bi bi-cpu\"></i> Rasio Luas terhadap Volume (L/V):</h4>\n              <p>Rasio $L/V$ berbanding terbalik dengan ukuran ($\\sim 1/r$). Benda kecil memiliki rasio permukaan terhadap volume yang sangat besar, sehingga cepat kehilangan panas; sedangkan benda raksasa memiliki rasio L/V kecil sehingga menahan panas jauh lebih lama.</p>\n            </div>\n            ",
            "pro_tip": "Dalam teknik mesin komputer, prosesor bertenaga tinggi (CPU/GPU) menggunakan pendingin heatsink dengan sirip-sirip tipis yang banyak untuk MEMPERBESAR luas permukaan 2D tanpa menambah volume total!",
            "pitfall": "Jangan berasumsi jika dimensi panjang kotak diperbesar 2 kali lipat, berat bebannya hanya bertambah 2 kali lipat! Berat bebannya melonjak $2^3 = 8$ KALI LIPAT!",
            "fun_fact": "Ilmuwan biologi J.B.S. Haldane menerbitkan esai sains terkenal tahun 1926 berjudul 'On Being the Right Size', yang membuktikan bahwa gravitasi mendikte bentuk anatomi seluruh makhluk hidup berdasarkan hukum geometri luas-volume.",
            "formula": "\\frac{A_2}{A_1} = k^2 \\quad ; \\quad \\frac{V_2}{V_1} = k^3 \\quad ; \\quad \\text{Rasio } \\frac{\\text{Luas}}{\\text{Volume}} \\propto \\frac{1}{r}",
            "formula_params": [
                [
                    "k",
                    "Faktor skala kelipatan pembesaran linier."
                ],
                [
                    "A_2 / A_1",
                    "Rasio pertambahan luas permukaan (kuadratik)."
                ],
                [
                    "V_2 / V_1",
                    "Rasio pertambahan kapasitas volume (kubik)."
                ]
            ],
            "formula_intuition": "Pertumbuhan kubik dimensi volume 3D selalu mendominasi dan mengalahkan pertumbuhan kuadratik permukaan 2D.",
            "example": {
                "question": "Sebuah model prototipe patung miniatur logam padat memiliki tinggi 10 cm dengan berat 0.5 kg. Jika patung tersebut akan dibuat ukuran aslinya dengan tinggi 100 cm (skala k = 10) menggunakan bahan logam padat yang sama persis, berapakah berat total patung ukuran aslinya?",
                "known": "Tinggi miniatur = 10 cm, Tinggi asli = 100 cm (Faktor skala $k = 100 / 10 = 10$). Berat awal = 0.5 kg.",
                "asked": "Berat patung asli (Volume berskala kubik).",
                "steps": [
                    [
                        "Langkah 1: Tentukan Faktor Skala Linier k",
                        "$k = \\frac{100\\text{ cm}}{10\\text{ cm}} = 10$."
                    ],
                    [
                        "Langkah 2: Terapkan Hukum Skala Kubik untuk Volume & Massa",
                        "Karena bahan logam identik (massa jenis $\\rho$ sama), rasio massa sebanding dengan rasio volume: $\\frac{M_{\\text{asli}}}{M_{\\text{miniatur}}} = k^3$."
                    ],
                    [
                        "Langkah 3: Hitung $k^3$",
                        "$k^3 = 10^3 = 1.000\\text{ kali lipat}$!"
                    ],
                    [
                        "Langkah 4: Kalikan dengan Berat Miniatur Mula-Mula",
                        "$M_{\\text{asli}} = 0.5\\text{ kg} \\times 1.000 = 500\\text{ kg}$ (setengah ton!)."
                    ]
                ],
                "conclusion": "Meskipun tingginya hanya bertambah 10 kali lipat, berat patung melonjak 1.000 kali lipat menjadi 500 kg."
            },
            "takeaways": [
                "Hukum skala kuadrat-kubik membuktikan bahwa volume bertumbuh secara kubik ($k^3$) jauh lebih cepat daripada luas penampang ($k^2$).",
                "Kapasitas muatan dan berat benda terikat pada volume, sedangkan kekuatan penopang terikat pada luas penampang.",
                "Prinsip ini menjadi dasar rekayasa arsitektur gedung pencakar langit dan biomekanika tubuh hewan."
            ],
            "quiz": [
                "Jika panjang sisi sebuah kubus dilipatgandakan menjadi 3 kali lipat semula, berapa kali lipat pertambahan volume kubus tersebut?",
                [
                    "27 kali lipat",
                    "9 kali lipat",
                    "3 kali lipat"
                ],
                0,
                "Volume bertumbuh secara kubik: k^3 = 3^3 = 27 kali lipat."
            ]
        },
        {
            "title": "Capstone: Desain Tangki Penyimpanan Industri dengan Efisiensi Material",
            "objectives": [
                "Mengintegrasikan perhitungan volume silinder dan luas permukaan untuk merancang tangki penyimpanan bahan bakar industri.",
                "Menganalisis rasio dimensi optimal (tinggi terhadap diameter) agar luas bahan plat baja minimum untuk kapasitas volume tertentu.",
                "Mengevaluasi efisiensi biaya rekayasa konstruksi ruang."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Structural Engineer di perusahaan kilang minyak nasional. Kamu diminta membangun sebuah tangki penyimpanan minyak berbentuk silinder tabung tertutup dengan kapasitas volume tepat 1.000 meter kubik (1 juta liter). Harga plat baja dinding dan tutup sangat mahal. Bagaimana kamu menentukan perbandingan diameter dan tinggi tangki agar jumlah plat baja yang dibutuhkan paling sedikit (biaya termurah)? Matematika geometri ruang memberikan solusi optimasi bentuk paling sempurna!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Geometri Optimasi Tangki Minyak</h3>\n              <p>Untuk menampung volume $V$ tertentu dengan luas permukaan plat baja $L_p$ paling minimal:</p>\n              \\[ V = \\pi r^2 t \\quad ; \\quad L_p = 2\\pi r^2 + 2\\pi r t \\]\n              <p>Teorema kalkulus geometri membuktikan bahwa silinder tabung tertutup paling efisien material selalu tercapai ketika <strong>Tinggi Tangki Sama dengan Diameternya ($t = 2r = d$)</strong>!</p>\n            </div>\n            ",
            "pro_tip": "Bentuk geometri 3D yang memiliki luas permukaan terkecil untuk menampung volume tertentu di alam semesta adalah BOLA MURNI! Inilah alasan mengapa gelembung sabun selalu berbentuk bola sempurna (meminimalkan tegangan permukaan)!",
            "pitfall": "Perhatikan apakah tangki berpenutup atau tanpa penutup! Jika tanpa penutup (terbuka atas), luas alas lingkaran hanya dihitung satu kali ($\\pi r^2$, bukan $2\\pi r^2$).",
            "fun_fact": "Tangki gas alam cair (LNG) berbentuk bola raksasa di kapal tanker laut dirancang bulat sempurna untuk meminimalkan luas permukaan serapan panas dari udara luar sekaligus mendistribusikan tekanan fluida secara seragam ke segala arah.",
            "formula": "V = \\pi r^2 t \\quad ; \\quad L_p = 2\\pi r^2 + 2\\pi r t \\quad ; \\quad \\text{Optimal jika } t = 2r = d",
            "formula_params": [
                [
                    "V",
                    "Kapasitas volume fluida (m³)."
                ],
                [
                    "L_p",
                    "Total luas permukaan plat baja penutup (m²)."
                ],
                [
                    "t = 2r",
                    "Rasio dimensi tangki paling hemat biaya material."
                ]
            ],
            "formula_intuition": "Menyeimbangkan proporsi antara tutup lingkaran atas-bawah dan selimut dinding silinder.",
            "example": {
                "question": "Sebuah tangki silinder tertutup dirancang dengan jari-jari $r = 7\\text{ meter}$ dan tinggi optimal $t = 14\\text{ meter}$ ($t = 2r$). Hitunglah: (a) Kapasitas volume minyak yang dapat ditampung, dan (b) Luas total lembaran plat baja yang dibutuhkan untuk membuat tangki tersebut!",
                "known": "$r = 7\\text{ m}$, $t = 14\\text{ m}$ (Gunakan $\\pi = 22/7$).",
                "asked": "Volume V dan Luas Permukaan $L_p$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Kapasitas Volume Minyak",
                        "$V = \\pi r^2 t = \\frac{22}{7} \\times 7^2 \\times 14 = 22 \\times 7 \\times 14 = 154 \\times 14 = 2.156\\text{ meter kubik}$ (atau lebih dari 2.15 juta liter!)."
                    ],
                    [
                        "Langkah 2: Hitung Luas Plat Permukaan Total",
                        "$L_p = 2\\pi r (r + t) = 2 \\times \\frac{22}{7} \\times 7 \\times (7 + 14)$."
                    ],
                    [
                        "Langkah 3: Evaluasi Nilai Luas",
                        "$L_p = 44 \\times 21 = 924\\text{ meter persegi (m}^2\\text{)}$."
                    ]
                ],
                "conclusion": "Tangki mampu menampung 2.156 m³ minyak dengan kebutuhan material plat baja seluas 924 m²."
            },
            "takeaways": [
                "Geometri ruang menghubungkan keterbatasan material 2D dengan efisiensi kapasitas ruang 3D.",
                "Rasio tinggi sama dengan diameter ($t = d$) memberikan efisiensi material paling optimal pada silinder tabung.",
                "Selamat! Kamu telah menguasai seluruh kurikulum Geometri Bangun Datar & Ruang dengan standar rekayasa kelas dunia!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE GEOMETRI: Bentuk bangun ruang manakah yang memiliki luas permukaan paling minimal untuk menampung volume tertentu di alam semesta?",
                [
                    "Bola",
                    "Kubus",
                    "Silinder"
                ],
                0,
                "Bola adalah bentuk geometri paling sempurna di alam semesta yang meminimalkan rasio luas permukaan terhadap volume (alasan gelembung sabun selalu bulat)."
            ]
        }
    ]
}
