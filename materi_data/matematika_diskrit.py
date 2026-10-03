# -*- coding: utf-8 -*-
DATA = {
    "title": "Matematika Diskrit & Logika",
    "short": "Mat. Diskrit",
    "icon": "bi-diagram-3",
    "color": "#475569",
    "desc": "Kuasai logika proposisional, tabel kebenaran, hukum De Morgan, teori himpunan, diagram Venn, prinsip inklusi-eksklusi, dan struktur dasar teori graf ilmu komputer.",
    "babs": [
        {
            "title": "Fondasi: Dunia Kontinu vs Dunia Diskrit Komputer",
            "objectives": [
                "Memahami perbedaan mendasar antara matematika kontinu (kalkulus analog) dan matematika diskrit (struktur digital terpisah berhingga).",
                "Memahami mengapa matematika diskrit adalah bahasa ibu dari seluruh algoritma ilmu komputer dan rekayasa perangkat lunak.",
                "Mengenal struktur data diskrit dasar: himpunan, relasi biner, dan graf jaringan."
            ],
            "hook": "Jam dinding jarum analog bergerak mengalir mulus tanpa henti (kontinu). Namun jam digital melompat dari detik 01 ke detik 02 secara diskrit (terpisah tegas). Komputer digital kita tidak bekerja dengan kurva mulus tak terhingga; prosesor komputer memproses angka diskrit 0 dan 1 yang terputus-putus! Matematika Diskrit adalah fondasi logika arsitektur seluruh sistem operasi, struktur database SQL, enkripsi internet, dan kecerdasan buatan.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-cpu-fill text-primary\"></i> 1. Hakikat Matematika Diskrit</h3>\n              <p>Matematika diskrit mengkaji struktur objek matematika yang terpisah satu sama lain dan dapat dicacah (countable), berbeda dengan kalkulus yang mengkaji perubahan mulus tak hingga.</p>\n              <ul class=\"dic-list\">\n                <li><strong>Kontinu:</strong> Bilangan riil di antara 0 dan 1 (ada tak hingga banyaknya angka pecahan desimal kontinu).</li>\n                <li><strong>Diskrit:</strong> Bilangan bulat $\\{\\dots, -2, -1, 0, 1, 2, \\dots\\}$, piksel layar monitor, simpul jaringan internet, dan status sakelar biner ON/OFF.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Jika suatu masalah berkaitan dengan 'langkah-langkah algoritma langkah demi langkah', 'rute tercepat di peta GPS', atau 'hubungan relasi pertemanan media sosial', kamu sedang berada di ranah Matematika Diskrit!",
            "pitfall": "Jangan gunakan konsep turunan atau integral kalkulus kontinu pada himpunan diskrit! Pada matematika diskrit, kita menggunakan teknik rekurensi, kombinatorika, dan pembuktian induksi matematika.",
            "fun_fact": "Pelopor komputer modern Alan Turing menggunakan konsep logika matematika diskrit mesin pita keadaan (Turing Machine) untuk mendefinisikan apa yang bisa dan tidak bisa dihitung oleh komputer.",
            "formula": "S_{\\text{diskrit}} = \\{x_1, x_2, \\dots, x_n\\} \\quad ; \\quad |S| = n \\quad (\\text{Kardinalitas Himpunan})",
            "formula_params": [
                [
                    "S",
                    "Himpunan berhingga yang elemennya dapat dicacah."
                ],
                [
                    "|S|",
                    "Kardinalitas (jumlah anggota elemen di dalam himpunan)."
                ]
            ],
            "formula_intuition": "Mengelompokkan entitas terpisah ke dalam wadah koleksi terdefinisi tegas.",
            "example": {
                "question": "Diberikan himpunan karakter sandi $A = \\{a, b, c, d\\}$. Tentukan kardinalitas himpunan A, dan hitung banyaknya seluruh kemungkinan himpunan bagian (Himpunan Kuasa / Power Set) yang dapat dibentuk dari A!",
                "known": "Himpunan A berisikan elemen a, b, c, d.",
                "asked": "Kardinalitas $|A|$ dan banyak himpunan bagian $|P(A)|$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Kardinalitas Elemen A",
                        "Elemen A adalah a, b, c, d (ada 4 elemen unik). Maka $|A| = 4$."
                    ],
                    [
                        "Langkah 2: Terapkan Rumus Banyak Himpunan Kuasa",
                        "Setiap elemen memiliki 2 opsi (masuk atau tidak masuk ke himpunan bagian):<br>$|P(A)| = 2^{|A|} = 2^4$."
                    ],
                    [
                        "Langkah 3: Evaluasi Nilai Perpangkatan",
                        "$2^4 = 16\\text{ himpunan bagian}$ (termasuk himpunan kosong $\\emptyset$ dan himpunan A itu sendiri)."
                    ]
                ],
                "conclusion": "Kardinalitas himpunan adalah 4 dan total himpunan bagian yang dapat dibentuk adalah 16 himpunan."
            },
            "takeaways": [
                "Matematika diskrit mengkaji struktur yang terpisah dan terhitung, menjadi landasan ilmu komputer.",
                "Kardinalitas $|S|$ menyatakan jumlah anggota di dalam suatu himpunan.",
                "Himpunan dengan $n$ anggota memiliki $2^n$ kemungkinan himpunan bagian."
            ],
            "quiz": [
                "Sebuah himpunan memiliki 3 elemen: {1, 2, 3}. Berapakah jumlah seluruh himpunan bagian yang mungkin dibuat dari himpunan tersebut?",
                [
                    "8",
                    "6",
                    "9"
                ],
                0,
                "Jumlah himpunan bagian = 2^n = 2^3 = 8."
            ]
        },
        {
            "title": "Anatomi: Logika Proposisional, Tabel Kebenaran & Hukum De Morgan",
            "objectives": [
                "Memahami proposisi deklaratif (bernilai Benar atau Salah, tetapi tidak keduanya).",
                "Menyusun tabel kebenaran untuk operasi logika dasar: Negasi (¬), Konjungsi (∧), Disjungsi (∨), dan Implikasi (⇒).",
                "Menerapkan Hukum De Morgan untuk menyederhanakan negasi logika majemuk."
            ],
            "hook": "Ketika kamu menulis kode program: `if (umur >= 17 and punyaKTP == true)`, program komputermu sedang mengevaluasi Logika Proposisional! Logika matematika adalah sirkuit gerbang sakelar transistor di dalam prosesor: listrik mengalir (1 = Benar) atau terputus (0 = Salah). Menguasai tabel kebenaran memampukanmu merancang algoritma logika perangkat lunak yang kokoh tanpa bug percabangan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-diagram-3-fill text-primary\"></i> 1. Empat Operator Logika Baku</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Konjungsi ($p \\land q$ / 'DAN'):</strong> Bernilai BENAR <strong>hanya jika kedua</strong> $p$ dan $q$ bernilai Benar.</li>\n                <li><strong>Disjungsi ($p \\lor q$ / 'ATAU'):</strong> Bernilai BENAR jika <strong>salah satu atau kedua</strong> proposisi bernilai Benar.</li>\n                <li><strong>Implikasi ($p \\implies q$ / 'JIKA p MAKA q'):</strong> Bernilai SALAH <strong>hanya jika</strong> anteseden $p$ Benar tetapi konsekuen $q$ Salah! Ekuivalensi penting: $p \\implies q \\equiv \\neg p \\lor q$.</li>\n                <li><strong>Hukum De Morgan (Pembalikan Logika):</strong>\n                  \\[ \\neg(p \\land q) \\equiv \\neg p \\lor \\neg q \\quad ; \\quad \\neg(p \\lor q) \\equiv \\neg p \\land \\neg q \\]\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Hukum De Morgan dalam bahasa manusia: Negasi dari 'Hari hujan DAN jalan basah' adalah 'Hari TIDAK hujan ATAU jalan TIDAK basah'. Kata 'DAN' otomatis berbalik menjadi 'ATAU' saat dinegasikan!",
            "pitfall": "Hati-hati dengan Implikasi $p \\implies q$: Jika premis awal $p$ sudah Salah, maka seluruh implikasi otomatis dianggap BENAR secara logika formal (Vacuous Truth)!",
            "fun_fact": "Matematikawan Inggris George Boole menerbitkan aljabar logika biner (Aljabar Boolean) pada tahun 1854 tanpa tahu bahwa 80 tahun kemudian penemuannya akan menjadi arsitektur seluruh sirkuit komputer digital oleh Claude Shannon.",
            "formula": "\\neg(p \\land q) \\equiv \\neg p \\lor \\neg q \\quad ; \\quad \\neg(p \\lor q) \\equiv \\neg p \\land \\neg q \\quad ; \\quad (p \\implies q) \\equiv (\\neg p \\lor q)",
            "formula_params": [
                [
                    "p, q",
                    "Proposisi logika pembentuk kalimat."
                ],
                [
                    "\\land, \\lor",
                    "Operator konjungsi (AND) dan disjungsi (OR)."
                ],
                [
                    "\\neg",
                    "Operator negasi ingkaran (NOT)."
                ]
            ],
            "formula_intuition": "Menegasikan seluruh kondisi mendistribusikan negasi ke masing-masing syarat dan membalik kata hubungnya.",
            "example": {
                "question": "Diberikan pernyataan logika: 'Siswa lulus ujian DAN siswa rajin belajar'. Tentukan negasi logika dari pernyataan tersebut menggunakan Hukum De Morgan!",
                "known": "Proposisi $p$ = 'Siswa lulus ujian', $q$ = 'Siswa rajin belajar'. Pernyataan adalah $(p \\land q)$.",
                "asked": "Bentuk negasi $\\neg(p \\land q)$.",
                "steps": [
                    [
                        "Langkah 1: Terapkan Hukum De Morgan",
                        "$\\neg(p \\land q) \\equiv \\neg p \\lor \\neg q$."
                    ],
                    [
                        "Langkah 2: Tentukan Negasi Masing-Masing Proposisi",
                        "$\\neg p$ = 'Siswa TIDAK lulus ujian'.<br>$\\neg q$ = 'Siswa TIDAK rajin belajar'."
                    ],
                    [
                        "Langkah 3: Hubungkan dengan Operator Disjungsi (ATAU)",
                        "'Siswa tidak lulus ujian ATAU siswa tidak rajin belajar'."
                    ]
                ],
                "conclusion": "Negasi yang sah secara logika adalah: 'Siswa tidak lulus ujian ATAU siswa tidak rajin belajar'."
            },
            "takeaways": [
                "Logika proposisional mengevaluasi nilai kebenaran biner mutlak (True atau False).",
                "Konjungsi mensyaratkan kedua syarat benar, sedangkan disjungsi cukup salah satu benar.",
                "Hukum De Morgan membalik kata penghubung DAN menjadi ATAU saat mendistribusikan ingkaran."
            ],
            "quiz": [
                "Pernyataan implikasi 'p => q' bernilai SALAH hanya pada kondisi?",
                [
                    "p Benar dan q Salah",
                    "p Salah dan q Benar",
                    "Kedua p dan q bernilai Salah"
                ],
                0,
                "Sebuah janji 'Jika p maka q' hanya dianggap ingkar janji (salah) jika syarat p dipenuhi tetapi realisasi q tidak ditepati."
            ]
        },
        {
            "title": "Mekanika: Teori Himpunan & Diagram Venn Prinsip Inklusi-Eksklusi",
            "objectives": [
                "Memahami operasi himpunan: Irisan (Interseksi), Gabungan (Union), Selisih (Difference), dan Komplemen.",
                "Memvisualisasikan data multi-kelompok menggunakan Diagram Venn.",
                "Menerapkan Prinsip Inklusi-Eksklusi untuk menghitung kardinalitas gabungan n(A u B)."
            ],
            "hook": "Dalam sebuah survei terhadap 100 orang: 60 orang menyukai kopi dan 50 orang menyukai teh. Mengapa jika dijumlahkan hasilnya 60 + 50 = 110 orang, padahal total responden hanya 100 orang? Ke mana 10 orang itu berasal? Mereka tidak datang dari planet lain! Ada orang-orang yang menyukai KEDUA-DUANYA (kopi dan teh) sehingga terhitung dua kali. Prinsip Inklusi-Eksklusi adalah algoritma presisi untuk mengeliminasi duplikasi data pada sistem database relasional SQL (INNER JOIN & UNION)!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-intersect text-primary\"></i> 1. Operasi Himpunan Baku</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Irisan ($A \\cap B$ / Interseksi):</strong> Himpunan anggota yang dimiliki bersama oleh A DAN B.</li>\n                <li><strong>Gabungan ($A \\cup B$ / Union):</strong> Himpunan seluruh anggota yang menjadi anggota A ATAU anggota B.</li>\n                <li><strong>Selisih ($A - B$):</strong> Anggota yang berada di A tetapi BUKAN anggota B.</li>\n                <li><strong>Prinsip Inklusi-Eksklusi Dua Himpunan:</strong>\n                  \\[ n(A \\cup B) = n(A) + n(B) - n(A \\cap B) \\]\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mengisi Diagram Venn soal cerita: Selalu isi bagian IRISAN PALING DALAM $n(A \\cap B)$ terlebih dahulu, lalu kurangkan angka tersebut dari masing-masing kelompok!",
            "pitfall": "Jangan menjumlahkan $n(A) + n(B)$ begitu saja tanpa mengurangkan irisannya! Duplikasi data adalah musuh utama integritas database.",
            "fun_fact": "Diagram Venn dirancang oleh matematikawan Inggris John Venn pada tahun 1880 untuk memvisualisasikan proposisi logika silogisme George Boole.",
            "formula": "n(A \\cup B) = n(A) + n(B) - n(A \\cap B) \\quad ; \\quad n(S) = n(A \\cup B) + n((A \\cup B)^c)",
            "formula_params": [
                [
                    "n(A \\cup B)",
                    "Banyaknya anggota gabungan A atau B."
                ],
                [
                    "n(A \\cap B)",
                    "Banyaknya anggota irisan persekutuan A dan B."
                ],
                [
                    "n(S)",
                    "Total semesta data."
                ]
            ],
            "formula_intuition": "Menjumlahkan kedua kelompok lalu mengurangkan satu kali irisan yang terhitung ganda.",
            "example": {
                "question": "Dari survei terhadap 100 mahasiswa teknik: 60 mahasiswa menyukai mata kuliah Pemrograman, 50 mahasiswa menyukai Kalkulus, dan 25 mahasiswa menyukai keduanya. Berapakah jumlah mahasiswa yang TIDAK menyukai Pemrograman maupun Kalkulus?",
                "known": "$n(S) = 100$, $n(P) = 60$, $n(K) = 50$, $n(P \\cap K) = 25$.",
                "asked": "Banyak mahasiswa di luar kedua kelompok $n((P \\cup K)^c)$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Gabungan Mahasiswa yang Menyukai Minimal Salah Satu",
                        "$n(P \\cup K) = n(P) + n(K) - n(P \\cap K)$."
                    ],
                    [
                        "Langkah 2: Evaluasi Angka Inklusi-Eksklusi",
                        "$n(P \\cup K) = 60 + 50 - 25 = 110 - 25 = 85\\text{ mahasiswa}$."
                    ],
                    [
                        "Langkah 3: Kurangkan dari Total Mahasiswa Semesta",
                        "Mahasiswa yang tidak suka keduanya = $n(S) - n(P \\cup K) = 100 - 85 = 15\\text{ mahasiswa}$."
                    ]
                ],
                "conclusion": "Ada 15 mahasiswa yang tidak menyukai Pemrograman maupun Kalkulus."
            },
            "takeaways": [
                "Prinsip inklusi-eksklusi mengeliminasi pencatatan ganda pada irisan persekutuan himpunan.",
                "Diagram Venn memvisualisasikan pembagian wilayah saling lepas, irisan, dan semesta.",
                "Konsep himpunan adalah fondasi query database relasional SQL (JOIN, UNION, EXCEPT)."
            ],
            "quiz": [
                "Diketahui n(A) = 30, n(B) = 25, dan n(A ∩ B) = 10. Berapakah nilai n(A ∪ B)?",
                [
                    "45",
                    "55",
                    "35"
                ],
                0,
                "n(A ∪ B) = n(A) + n(B) - n(A ∩ B) = 30 + 25 - 10 = 45."
            ]
        },
        {
            "title": "Pemodelan: Pengantar Teori Graf & Rute Terpendek Jaringan",
            "objectives": [
                "Memahami komponen dasar graf: Simpul (Vertex / Node) dan Sisi Penghubung (Edge).",
                "Membedakan graf berarah (Directed Graph) dan graf berbobot (Weighted Graph).",
                "Memodelkan masalah rute logistik terpendek (Algoritma Dijkstra) dan jejaring sosial."
            ],
            "hook": "Bagaimana Google Maps atau aplikasi ojek online dapat menemukan rute perjalanan tercepat dari rumahmu ke stasiun kereta dalam waktu kurang dari 0.1 detik di antara jutaan ruas jalan raya? Peta jalanan dimodelkan sebagai GRAF MATEMATIKA: persimpangan jalan adalah simpul (Node), ruas jalan adalah sisi (Edge), dan jarak tempuh adalah bobot (Weight). Teori Graf adalah bahasa matematika yang menggerakkan sistem navigasi GPS dan jejaring sosial dunia!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-diagram-3 text-primary\"></i> 1. Anatomi Teori Graf $G = (V, E)$</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Simpul (Vertex / Node $V$):</strong> Titik representasi entitas (kota, pengguna media sosial, router jaringan).</li>\n                <li><strong>Sisi (Edge $E$):</strong> Garis penghubung yang menghubungkan sepasang simpul (ruas jalan raya, hubungan pertemanan, kabel fiber optik).</li>\n                <li><strong>Graf Berbobot (Weighted Graph):</strong> Setiap sisi memiliki nilai numerik (bobot jarak km, biaya tol, atau latensi waktu).</li>\n                <li><strong>Derajat Simpul (Degree):</strong> Banyaknya sisi yang terhubung ke satu simpul.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Teorema Jabat Tangan (Handshaking Lemma): Jumlah derajat seluruh simpul pada graf selalu tepat DUA KALI jumlah total sisinya: $\\sum \\text{deg}(v) = 2|E|$!",
            "pitfall": "Jangan tertukar antara lintasan (Path) dan siklus (Cycle)! Siklus adalah lintasan yang titik awal dan titik akhirnya kembali ke simpul yang sama.",
            "fun_fact": "Teori Graf lahir pada tahun 1736 ketika Leonhard Euler memecahkan teka-teki 'Tujuh Jembatan Königsberg', membuktikan bahwa mustahil berjalan melewati ketujuh jembatan kota itu tepat satu kali tanpa menyeberangi jembatan yang sama dua kali.",
            "formula": "G = (V, E) \\quad ; \\quad \\sum_{v \\in V} \\text{deg}(v) = 2|E| \\quad (\\text{Handshaking Lemma})",
            "formula_params": [
                [
                    "V",
                    "Himpunan simpul vertex."
                ],
                [
                    "E",
                    "Himpunan sisi edge."
                ],
                [
                    "\\text{deg}(v)",
                    "Derajat keterhubungan simpul v."
                ]
            ],
            "formula_intuition": "Setiap satu garis sisi selalu memiliki dua ujung titik simpul penopang.",
            "example": {
                "question": "Sebuah jaringan telekomunikasi terdiri dari 5 router (simpul). Masing-masing router terhubung dengan tepat 4 kabel jaringan ke router lainnya (graf reguler derajat 4). Berapakah jumlah total kabel jaringan (sisi) yang dibutuhkan di dalam jaringan tersebut?",
                "known": "Banyak simpul $|V| = 5$. Setiap simpul berderajat $\\text{deg}(v) = 4$.",
                "asked": "Jumlah total sisi $|E|$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Jumlah Derajat Seluruh Simpul",
                        "Total derajat = $5 \\times 4 = 20$."
                    ],
                    [
                        "Langkah 2: Terapkan Teorema Jabat Tangan (Handshaking Lemma)",
                        "$\\sum \\text{deg}(v) = 2|E| \\implies 20 = 2|E|$."
                    ],
                    [
                        "Langkah 3: Selesaikan Jumlah Sisi |E|",
                        "$|E| = \\frac{20}{2} = 10\\text{ kabel sisi}$ (merupakan Graf Lengkap $K_5$)."
                    ]
                ],
                "conclusion": "Total kabel jaringan penghubung yang dibutuhkan adalah 10 kabel."
            },
            "takeaways": [
                "Graf $G = (V, E)$ memodelkan relasi jaringan antar-entitas di dunia nyata.",
                "Handshaking Lemma membuktikan jumlah derajat simpul selalu sama dengan dua kali banyak sisi.",
                "Teori graf adalah inti algoritma rute navigasi terpendek dan analisis jejaring sosial."
            ],
            "quiz": [
                "Sebuah graf memiliki 6 sisi edge. Berapakah jumlah total derajat seluruh simpulnya?",
                [
                    "12",
                    "6",
                    "18"
                ],
                0,
                "Berdasarkan Handshaking Lemma: Total derajat = 2 * |E| = 2 * 6 = 12."
            ]
        },
        {
            "title": "Capstone: Perancangan Sirkuit Gerbang Logika Digital Keamanan Multi-Sensor",
            "objectives": [
                "Mengintegrasikan Aljabar Boolean, tabel kebenaran, dan gerbang logika digital (AND, OR, NOT).",
                "Merancang sirkuit sistem alarm kebakaran dan kebocoran gas otomatis multi-sensor.",
                "Menyederhanakan ekspresi logika Boolean untuk menghemat biaya komponen chip sirkuit terpadu (IC)."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Hardware Security Architect untuk gedung reaktor nuklir. Gedung dipasangi 3 sensor keselamatan: Sensor Panas Api (A), Sensor Asap Gas (B), dan Sakelar Darurat Manual (C). Sistem alarm peringatan (Y) harus berbunyi nyaring (Y = 1) jika: Sakelar manual diaktifkan (C = 1), ATAU jika Sensor Panas Api dan Sensor Asap terpicu bersamaan (A = 1 dan B = 1). Rancanglah tabel kebenaran, ekspresi Aljabar Boolean, dan diagram gerbang logika sirkuit sistem ini!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-shield-shaded text-warning\"></i> Skenario Sirkuit Gerbang Logika Digital</h3>\n              <p>Representasi fungsi logika alarm pengaman gedung:</p>\n              \\[ Y = (A \\land B) \\lor C \\]\n              <ul class=\"dic-list\">\n                <li>Gerbang <strong>AND</strong>: Mengalikan sinyal $A \\cdot B$.</li>\n                <li>Gerbang <strong>OR</strong>: Menjumlahkan sinyal $(A \\cdot B) + C$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Dalam perancangan sirkuit digital, minimasi Aljabar Boolean menggunakan Peta Karnaugh (K-Map) dapat memangkas jumlah transistor hingga 50% untuk menekan konsumsi daya baterai!",
            "pitfall": "Jangan tertukar simbol gerbang logika: Gerbang AND berbentuk busur lurus dengan ujung setengah lingkaran, sedangkan gerbang OR memiliki sisi input melengkung ke dalam dengan ujung runcing.",
            "fun_fact": "Miliaran transistor di dalam chip prosesor smartphone tercanggih hari ini (Apple M-Series / Qualcomm Snapdragon) dibangun semata-mata dari jutaan gerbang logika dasar NAND dan NOR yang dieksekusi dalam skala nanometer!",
            "formula": "Y = (A \\cdot B) + C \\quad ; \\quad \\text{Gerbang AND } (\\cdot) \\ ; \\ \\text{Gerbang OR } (+)",
            "formula_params": [
                [
                    "A",
                    "Sensor Panas Api (1 = Api terdeteksi, 0 = Normal)."
                ],
                [
                    "B",
                    "Sensor Asap Gas (1 = Asap terdeteksi, 0 = Normal)."
                ],
                [
                    "C",
                    "Sakelar Manual Tombol Darurat."
                ],
                [
                    "Y",
                    "Status Alarm Sirine (1 = Berbunyi, 0 = Diam)."
                ]
            ],
            "formula_intuition": "Menggabungkan syarat deteksi ganda otomatis dengan override tombol manual darurat.",
            "example": {
                "question": "Berdasarkan formula sistem alarm $Y = (A \\cdot B) + C$, tentukan status alarm (berbunyi 1 atau diam 0) pada kondisi berikut: (a) Api terdeteksi ($A=1$), asap tidak ada ($B=0$), tombol tidak ditekan ($C=0$), dan (b) Tombol darurat manual ditekan ($C=1$) meskipun tidak ada api ($A=0$) dan tidak ada asap ($B=0$)!",
                "known": "Fungsi sirkuit $Y = (A \\cdot B) + C$.",
                "asked": "Status output alarm Y pada kedua skenario.",
                "steps": [
                    [
                        "Langkah 1: Uji Skenario (a)",
                        "$Y = (1 \\cdot 0) + 0 = 0 + 0 = 0$ (Alarm Diam / Tidak Berbunyi karena asap tidak terdeteksi untuk konfirmasi api)."
                    ],
                    [
                        "Langkah 2: Uji Skenario (b)",
                        "$Y = (0 \\cdot 0) + 1 = 0 + 1 = 1$ (Alarm BERBUNYI NYARING karena tombol darurat manual diaktifkan)!"
                    ]
                ],
                "conclusion": "Pada kondisi (a) alarm tetap diam ($Y=0$), sedangkan pada kondisi (b) alarm berbunyi aktif ($Y=1$)."
            },
            "takeaways": [
                "Aljabar Boolean mentranslasikan aturan logika manusia menjadi sirkuit kelistrikan digital.",
                "Gerbang AND, OR, dan NOT adalah batu bata pembangun seluruh prosesor komputer modern.",
                "Selamat! Kamu telah menuntaskan seluruh kurikulum Matematika Diskrit & Logika dengan standar kompetensi gemilang!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE MATEMATIKA DISKRIT: Berapakah nilai output Y dari ekspresi logika Y = (A AND B) OR C jika A = 1, B = 1, dan C = 0?",
                [
                    "Y = 1 (Aktif)",
                    "Y = 0 (Nonaktif)",
                    "Tidak terdefinisi"
                ],
                0,
                "(1 AND 1) = 1. Lalu 1 OR 0 = 1. Maka alarm Y aktif berbunyi."
            ]
        }
    ]
}
