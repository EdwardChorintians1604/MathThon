# -*- coding: utf-8 -*-
DATA = {
    "title": "Limit Fungsi Aljabar",
    "short": "Limit",
    "icon": "bi-speedometer2",
    "color": "#0ea5e9",
    "desc": "Kuasai konsep pendekatan nilai tak hingga, kontinuitas fungsi, teknik eliminasi bentuk tak tentu 0/0, perkalian sekawan, dan aplikasinya dalam laju perubahan sesaat.",
    "babs": [
        {
            "title": "Fondasi: Intuisi Mendekati Tak Terhingga & Lubang Kontinuitas",
            "objectives": [
                "Memahami konsep limit sebagai nilai pendekatan x mendekati c (x -> c), bukan nilai x = c.",
                "Memahami mengapa bentuk 0/0 disebut sebagai 'bentuk tak tentu' dalam kalkulus.",
                "Menginterpretasikan limit kiri dan limit kanan untuk menguji keberadaan limit fungsi."
            ],
            "hook": "Bayangkan kamu sedang mengemudi mobil menuju bibir jurang. Konsep nilai fungsi $f(c)$ menanyakan: 'Apa yang terjadi jika mobil kamu melompat tepat ke dalam jurang?'. Jawabannya adalah hancur (tidak terdefinisi). Namun konsep LIMIT menanyakan pertanyaan yang jauh lebih cerdas: 'Ke arah mana ketinggian jalan yang kamu tuju saat mobilmu semakin mendekati 1 milimeter sebelum jurang?'. Limit adalah mikroskop matematika untuk meneliti fenomena di ambang batas!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-search text-primary\"></i> 1. Hakikat Nilai Limit: Pendekatan, Bukan Substitusi</h3>\n              <p>Notasi $\\lim_{x \\to c} f(x) = L$ dibaca: <em>'Limit dari $f(x)$ untuk $x$ mendekati $c$ adalah sama dengan $L$'</em>.</p>\n              <p>Artinya: Ketika nilai $x$ bergerak semakin dekat mendekati $c$ (tetapi $x \\neq c$), maka nilai output fungsi $f(x)$ akan bergerak semakin dekat menuju nilai tunggal $L$.</p>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrow-left-right text-primary\"></i> 2. Syarat Keberadaan Limit (Dua Arah)</h3>\n              <p>Limit fungsi $\\lim_{x \\to c} f(x)$ <strong>ADA</strong> jika dan hanya jika:</p>\n              \\[ \\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = L \\]\n              <p>Limit dari arah kiri ($x \\to c^-$) harus menghasilkan angka yang sama persis dengan limit dari arah kanan ($x \\to c^+$).</p>\n            </div>\n            ",
            "pro_tip": "Langkah pertama saat menghadapi soal limit: Selalu lakukan substitusi langsung nilai $x = c$. Jika hasilnya angka riil (seperti 5, 0, atau -2), itulah jawaban akhirnya! Kamu hanya perlu menggunakan teknik aljabar jika hasilnya berbentuk $0/0$.",
            "pitfall": "Jangan menyamakan $0/0$ dengan angka 1 atau 0! Bentuk $0/0$ disebut Bentuk Tak Tentu (Indeterminate Form) karena nilainya bisa berapa saja tergantung fungsi pembentuknya.",
            "fun_fact": "Konsep limit yang presisi secara matematis baru berhasil dirumuskan oleh matematikawan Prancis Augustin-Louis Cauchy pada tahun 1821 menggunakan definisi formal $\\epsilon - \\delta$ (Epsilon-Delta), lebih dari 150 tahun setelah kalkulus diciptakan oleh Newton dan Leibniz!",
            "formula": "\\lim_{x \\to c} f(x) = L \\iff \\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = L",
            "formula_params": [
                [
                    "c",
                    "Titik nilai yang didekati oleh variabel x."
                ],
                [
                    "L",
                    "Nilai target limit fungsi."
                ],
                [
                    "c^-",
                    "Pendekatan dari arah kiri (nilai lebih kecil dari c)."
                ],
                [
                    "c^+",
                    "Pendekatan dari arah kanan (nilai lebih besar dari c)."
                ]
            ],
            "formula_intuition": "Limit meneliti konsistensi kecenderungan nilai fungsi dari kedua arah mata angin.",
            "example": {
                "question": "Diberikan fungsi $f(x) = \\frac{x^2 - 4}{x - 2}$. Mengapa substitusi langsung $x = 2$ menghasilkan bentuk tak tentu, dan berapakah nilai limit sejati fungsi tersebut saat $x \\to 2$?",
                "known": "$f(x) = \\frac{x^2 - 4}{x - 2}$ pada saat $x \\to 2$.",
                "asked": "Analisis bentuk tak tentu dan nilai $\\lim_{x \\to 2} f(x)$.",
                "steps": [
                    [
                        "Langkah 1: Coba Substitusi Langsung",
                        "$f(2) = \\frac{2^2 - 4}{2 - 2} = \\frac{0}{0}$ (Bentuk Tak Tentu / Lubang Pembagian Nol)."
                    ],
                    [
                        "Langkah 2: Faktorkan Pembilang Menggunakan Selisih Kuadrat",
                        "$x^2 - 4 = (x - 2)(x + 2)$."
                    ],
                    [
                        "Langkah 3: Sederhanakan Pecahan (Karena $x \\neq 2$, faktor $(x - 2)$ boleh dicoret)",
                        "$\\lim_{x \\to 2} \\frac{(x - 2)(x + 2)}{x - 2} = \\lim_{x \\to 2} (x + 2)$."
                    ],
                    [
                        "Langkah 4: Masukkan Nilai $x = 2$",
                        "$2 + 2 = 4$."
                    ]
                ],
                "conclusion": "Meskipun fungsi tidak terdefinisi di titik x = 2, nilai limitnya ada dan konvergen tepat ke angka 4."
            },
            "takeaways": [
                "Limit adalah nilai pendekatan di sekitar titik sasaran, bukan nilai pada titik itu sendiri.",
                "Bentuk $0/0$ adalah sinyal bahwa ada faktor pembuat nol yang harus dihilangkan.",
                "Limit ada jika limit kiri dan limit kanan bernilai sama."
            ],
            "quiz": [
                "Berapakah nilai dari $\\lim_{x \\to 3} (2x^2 - 5)$?",
                [
                    "13",
                    "7",
                    "31"
                ],
                0,
                "Karena bukan bentuk 0/0, substitusikan langsung: 2(3^2) - 5 = 2(9) - 5 = 18 - 5 = 13."
            ]
        },
        {
            "title": "Anatomi: Teorema & Sifat Operasi Baku Limit",
            "objectives": [
                "Menguasai sifat-sifat dasar operasi limit aljabar (penjumlahan, pengurangan, perkalian, pembagian, perpangkatan, dan akar).",
                "Mengevaluasi limit polinomial berderajat tinggi dengan substitusi terurai.",
                "Menghindari operasi ilegal pada pembagian limit saat penyebut bernilai nol."
            ],
            "hook": "Sama seperti hukum fisika yang mengatur pergerakan benda di alam semesta, limit memiliki 'Konstitusi Hukum Limit' (Limit Laws) yang menjamin bahwa kalkulasi limit dapat dipecah menjadi bagian-bagian kecil yang sangat mudah diselesaikan satu per satu!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-shield-check text-primary\"></i> 1. Sifat-Sifat Aljabar Teorema Limit</h3>\n              <p>Jika $\\lim_{x \\to c} f(x) = L$ dan $\\lim_{x \\to c} g(x) = M$, maka berlaku sifat baku:</p>\n              <ul class=\"dic-list\">\n                <li><strong>Penjumlahan/Pengurangan:</strong> $\\lim [f(x) \\pm g(x)] = L \\pm M$.</li>\n                <li><strong>Perkalian Skalar:</strong> $\\lim [k \\cdot f(x)] = k \\cdot L$.</li>\n                <li><strong>Perkalian:</strong> $\\lim [f(x) \\cdot g(x)] = L \\cdot M$.</li>\n                <li><strong>Pembagian:</strong> $\\lim \\frac{f(x)}{g(x)} = \\frac{L}{M}$, dengan syarat $M \\neq 0$.</li>\n                <li><strong>Akar:</strong> $\\lim \\sqrt[n]{f(x)} = \\sqrt[n]{L}$, dengan syarat $L > 0$ jika $n$ genap.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Sifat-sifat limit memungkinkan kita memindahkan tanda limit masuk ke dalam tanda kurung, ke dalam akar, atau ke dalam fungsi pangkat!",
            "pitfall": "Hati-hati dengan sifat pembagian: Sifat $\\lim (f/g) = L/M$ GAGAL jika limit penyebut bernilai $M = 0$!",
            "fun_fact": "Teorema Limit adalah jembatan logis yang mengubah matematika diskrit statis menjadi kalkulus kontinu dinamis yang memungkinkan manusia menghitung laju percepatan roket menuju bulan.",
            "formula": "\\lim_{x \\to c} [f(x) \\pm g(x)] = L \\pm M \\quad ; \\quad \\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\frac{L}{M} \\quad (M \\neq 0)",
            "formula_params": [
                [
                    "L, M",
                    "Nilai limit dari masing-masing komponen fungsi."
                ],
                [
                    "c",
                    "Titik pendekatan koordinat."
                ]
            ],
            "formula_intuition": "Operator limit bersifat linier terhadap penjumlahan dan perkalian skalar.",
            "example": {
                "question": "Jika diketahui $\\lim_{x \\to 2} f(x) = 5$ dan $\\lim_{x \\to 2} g(x) = 3$, hitunglah nilai dari $\\lim_{x \\to 2} \\sqrt{f(x)^2 + g(x)^2 + 2}$!",
                "known": "$L = 5$ dan $M = 3$ saat $x \\to 2$.",
                "asked": "Nilai limit ekspresi akar kuadrat.",
                "steps": [
                    [
                        "Langkah 1: Masukkan Sifat Limit ke Dalam Bentuk Akar",
                        "$\\sqrt{\\lim f(x)^2 + \\lim g(x)^2 + 2}$."
                    ],
                    [
                        "Langkah 2: Evaluasi Nilai Limit Komponen",
                        "$\\lim f(x)^2 = 5^2 = 25$ dan $\\lim g(x)^2 = 3^2 = 9$."
                    ],
                    [
                        "Langkah 3: Hitung Nilai di Dalam Akar",
                        "$\\sqrt{25 + 9 + 2} = \\sqrt{36} = 6$."
                    ]
                ],
                "conclusion": "Nilai limit fungsi tersebut adalah 6."
            },
            "takeaways": [
                "Sifat-sifat limit memungkinkan pemecahan limit ekspresi rumit menjadi limit-limit sederhana.",
                "Limit akar sama dengan akar dari nilai limitnya.",
                "Pembagian limit mensyaratkan nilai limit penyebut tidak boleh sama dengan nol."
            ],
            "quiz": [
                "Jika $\\lim_{x \\to 1} f(x) = 4$, berapakah nilai dari $\\lim_{x \\to 1} [3f(x) - 2]$?",
                [
                    "10",
                    "14",
                    "12"
                ],
                0,
                "Gunakan sifat linear: 3(4) - 2 = 12 - 2 = 10."
            ]
        },
        {
            "title": "Mekanika: Teknik Eliminasi Bentuk Tak Tentu 0/0 (Faktorisasi & Sekawan)",
            "objectives": [
                "Menguasai teknik faktorisasi aljabar untuk mengeliminasi pembuat nol pada limit rasional.",
                "Menguasai teknik perkalian sekawan (merasionalkan bentuk akar) untuk limit yang memuat tanda akar.",
                "Memahami pengantar aturan L'Hôpital sebagai alternatif turunan untuk bentuk 0/0."
            ],
            "hook": "Ketika kamu memasukkan nilai x dan hasilnya memunculkan angka terkutuk '0/0', jangan panik! Itu bukan berarti jawabannya tidak ada, melainkan jawabannya sedang terkunci di balik selubung aljabar. Dalam bab ini, kamu akan mempelajari dua kunci pembuka kunci tersebut: Teknik Faktorisasi Polinomial dan Teknik Pedang Perkalian Sekawan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-tools text-primary\"></i> 1. Strategi 1: Metode Pemfaktoran Aljabar</h3>\n              <p>Gunakan metode ini jika pembilang dan penyebut berupa fungsi polinomial aljabar:</p>\n              <ol class=\"dic-list\">\n                <li>Faktorkan pembilang dan penyebut secara penuh.</li>\n                <li>Coret (eliminasi) faktor persekutuan pembuat nol $(x - c)$.</li>\n                <li>Substitusikan kembali nilai $x = c$.</li>\n              </ol>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-link-45deg text-primary\"></i> 2. Strategi 2: Perkalian Bentuk Sekawan (Konjugat)</h3>\n              <p>Gunakan metode ini jika bentuk limit memuat tanda akar $\\sqrt{A} - B$:</p>\n              <ul class=\"dic-list\">\n                <li>Bentuk sekawan dari $(\\sqrt{A} - B)$ adalah $(\\sqrt{A} + B)$.</li>\n                <li>Kalikan pembilang dan penyebut dengan bentuk sekawannya menggunakan identitas selisih dua kuadrat:\n                  \\[ (\\sqrt{A} - B)(\\sqrt{A} + B) = A - B^2 \\]\n                </li>\n                <li>Tanda akar akan lenyap dan faktor pembuat nol dapat dicoret!</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Jika $x \\to 3$, maka faktor pembuat nol penyebab 0/0 pasti berbentuk $(x - 3)$. Carilah faktor $(x - 3)$ pada pembilang dan penyebut untuk dieliminasi!",
            "pitfall": "Saat mengalikan bentuk sekawan pada pecahan, pastikan mengalikan pembilang DAN penyebut secara adil agar nilainya tidak berubah (mengalikan dengan bentuk bernilai 1)!",
            "fun_fact": "Aturan L'Hôpital (turunan pembilang dibagi turunan penyebut) sebenarnya ditemukan oleh matematikawan brilian Swiss Johann Bernoulli, tetapi dibeli hak publikasinya oleh bangsawan Prancis Guillaume de l'Hôpital pada tahun 1696!",
            "formula": "\\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\lim_{x \\to c} \\frac{(x - c)P(x)}{(x - c)Q(x)} = \\frac{P(c)}{Q(c)} \\quad ; \\quad (\\sqrt{u} - v)(\\sqrt{u} + v) = u - v^2",
            "formula_params": [
                [
                    "(x - c)",
                    "Faktor pembuat nol penyebab terjadinya 0/0."
                ],
                [
                    "P(x), Q(x)",
                    "Polinomial sisa setelah penyederhanaan."
                ]
            ],
            "formula_intuition": "Mencoret pembagi nol yang bernilai sama untuk memunculkan nilai kontinuitas sejati kurva.",
            "example": {
                "question": "Hitunglah nilai limit berikut: $\\lim_{x \\to 4} \\frac{x - 4}{\\sqrt{x} - 2}$!",
                "known": "Substitusi langsung menghasilkan $\\frac{4 - 4}{\\sqrt{4} - 2} = \\frac{0}{0}$ (Bentuk Tak Tentu).",
                "asked": "Nilai limit dengan teknik perkalian sekawan.",
                "steps": [
                    [
                        "Langkah 1: Tentukan Bentuk Sekawan Penyebut",
                        "Bentuk sekawan dari $(\\sqrt{x} - 2)$ adalah $(\\sqrt{x} + 2)$."
                    ],
                    [
                        "Langkah 2: Kalikan Pembilang dan Penyebut dengan Sekawannya",
                        "$\\lim_{x \\to 4} \\frac{(x - 4)(\\sqrt{x} + 2)}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)}$."
                    ],
                    [
                        "Langkah 3: Uraikan Penyebut",
                        "Penyebut menjadi $(\\sqrt{x})^2 - 2^2 = x - 4$."
                    ],
                    [
                        "Langkah 4: Coret Faktor Pembuat Nol $(x - 4)$",
                        "$\\lim_{x \\to 4} \\frac{(x - 4)(\\sqrt{x} + 2)}{x - 4} = \\lim_{x \\to 4} (\\sqrt{x} + 2)$."
                    ],
                    [
                        "Langkah 5: Masukkan Nilai $x = 4$",
                        "$\\sqrt{4} + 2 = 2 + 2 = 4$."
                    ]
                ],
                "conclusion": "Nilai limit dari fungsi tersebut adalah 4."
            },
            "takeaways": [
                "Bentuk tak tentu 0/0 pada polinomial diselesaikan dengan faktorisasi pembilang dan penyebut.",
                "Bentuk tak tentu yang melibatkan akar diselesaikan dengan perkalian sekawan.",
                "Setelah faktor pembuat nol dicoret, substitusi langsung dapat dilakukan dengan aman."
            ],
            "quiz": [
                "Berapakah nilai dari $\\lim_{x \\to 3} \\frac{x^2 - 9}{x - 3}$?",
                [
                    "6",
                    "0",
                    "Tak hingga"
                ],
                0,
                "(x^2 - 9)/(x - 3) = (x - 3)(x + 3)/(x - 3) = x + 3. Pada x = 3, nilainya adalah 3 + 3 = 6."
            ]
        },
        {
            "title": "Pemodelan: Limit Tak Hingga & Laju Pertumbuhan Populasi",
            "objectives": [
                "Menyelesaikan limit menuju tak hingga (x -> tak hingga) pada fungsi rasional.",
                "Menguasai aturan derajat pangkat tertinggi pembilang vs penyebut.",
                "Memodelkan fenomena kapasitas lingkungan (carrying capacity) pada model pertumbuhan populasi logistik."
            ],
            "hook": "Jika populasi ikan di sebuah danau bertambah setiap tahun, apakah jumlah ikannya akan bertambah terus hingga miliaran ikan memenuhi danau sampai tumpah ke daratan? Tentu tidak! Sumber makanan dan luas danau memiliki batas maksimum alami yang disebut Carrying Capacity (Kapasitas Daya Tampung). Model limit tak hingga ($t \\to \\infty$) adalah alat matematika yang digunakan ahli biologi untuk memprediksi populasi stabil jangka panjang tersebut!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-infinity text-primary\"></i> 1. Kaidah Derajat Pangkat Tertinggi ($x \\to \\infty$)</h3>\n              <p>Untuk limit pecahan polinomial $\\lim_{x \\to \\infty} \\frac{a x^m + \\dots}{b x^n + \\dots}$:</p>\n              <ul class=\"dic-list\">\n                <li><strong>Jika derajat sama ($m = n$):</strong> Hasilnya adalah rasio koefisien tertinggi: $\\frac{a}{b}$.</li>\n                <li><strong>Jika derajat pembilang lebih kecil ($m < n$):</strong> Hasilnya adalah $0$.</li>\n                <li><strong>Jika derajat pembilang lebih besar ($m > n$):</strong> Hasilnya adalah $\\infty$ atau $-\\infty$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Jalan pintas limit tak hingga pecahan: abaikan semua suku berderajat rendah! Cukup perhatikan suku dengan pangkat tertinggi pada pembilang dan penyebut!",
            "pitfall": "Jangan membagi dengan nol! Ingat bahwa $\\frac{k}{\\infty} \\to 0$, tetapi $\\frac{k}{0} \\to \\infty$.",
            "fun_fact": "Konsep limit tak hingga digunakan dalam fisika kosmologi untuk menghitung Kecepatan Lepas (Escape Velocity) yang dibutuhkan roket untuk melepaskan diri dari tarikan gravitasi bumi secara permanen menuju ruang hampa udara.",
            "formula": "\\lim_{x \\to \\infty} \\frac{a x^n + \\dots}{b x^n + \\dots} = \\frac{a}{b} \\quad ; \\quad \\lim_{x \\to \\infty} \\frac{1}{x^k} = 0 \\quad (k > 0)",
            "formula_params": [
                [
                    "a, b",
                    "Koefisien dari pangkat tertinggi."
                ],
                [
                    "n",
                    "Derajat pangkat tertinggi polinomial."
                ],
                [
                    "\\infty",
                    "Simbol kuantitas tak berhingga."
                ]
            ],
            "formula_intuition": "Saat x menjadi sangat besar (jutaan atau miliaran), suku-suku berderajat rendah menjadi tidak berarti dan didominasi sepenuhnya oleh suku berpangkat tertinggi.",
            "example": {
                "question": "Jumlah populasi rusa (dalam ratusan ekor) di suaka margasatwa setelah t tahun dimodelkan oleh fungsi: $P(t) = \\frac{50t + 20}{2t + 5}$. Berapakah estimasi populasi rusa dalam jangka panjang ketika waktu mendekati tak terhingga ($t \\to \\infty$)?",
                "known": "$P(t) = \\frac{50t + 20}{2t + 5}$ saat $t \\to \\infty$.",
                "asked": "Nilai limit $\\lim_{t \\to \\infty} P(t)$.",
                "steps": [
                    [
                        "Langkah 1: Identifikasi Pangkat Tertinggi",
                        "Pangkat tertinggi pada pembilang dan penyebut adalah $t^1$ (derajat sama, $m = n = 1$)."
                    ],
                    [
                        "Langkah 2: Bagi Pembilang dan Penyebut dengan t",
                        "$\\lim_{t \\to \\infty} \\frac{50 + \\frac{20}{t}}{2 + \\frac{5}{t}}$."
                    ],
                    [
                        "Langkah 3: Evaluasi Nilai Limit $\\frac{1}{t} \\to 0$",
                        "$\\frac{50 + 0}{2 + 0} = \\frac{50}{2} = 25$."
                    ],
                    [
                        "Langkah 4: Kalikan dengan Satuan",
                        "25 ratusan ekor = $25 \\times 100 = 2.500\\text{ ekor}$."
                    ]
                ],
                "conclusion": "Dalam jangka panjang, populasi rusa akan stabil mendekati batas daya tampung 2.500 ekor."
            },
            "takeaways": [
                "Limit tak hingga pada fungsi rasional ditentukan oleh rasio pangkat tertingginya.",
                "Suku pembagi berpangkat tinggi mendekati nol saat x menuju tak hingga: $1/x^k \\to 0$.",
                "Model limit memprediksi batas kestabilan ekologis dan ekonomi jangka panjang."
            ],
            "quiz": [
                "Berapakah nilai dari $\\lim_{x \\to \\infty} \\frac{6x^3 + 4x - 1}{2x^3 - 5x^2}$?",
                [
                    "3",
                    "0",
                    "Tak hingga"
                ],
                0,
                "Karena derajat tertinggi sama-sama x^3, ambil rasio koefisiennya: 6 / 2 = 3."
            ]
        },
        {
            "title": "Capstone: Analisis Kontinuitas Jalur Transmisi Sinyal Jaringan",
            "objectives": [
                "Menguji syarat formal kontinuitas fungsi di suatu titik (f(c) terdefinisi, limit ada, dan keduanya sama).",
                "Menganalisis fungsi piecewise (sepotong-sepotong) pada sistem switching sinyal telekomunikasi.",
                "Menentukan parameter konstanta agar transmisi data berjalan mulus tanpa lompatan sinyal (diskontinuitas)."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Telecommunication Signal Engineer. Sinyal transmisi serat optik berpindah dari stasiun pemancar ke kabel bawah laut menggunakan protokol sinyal piecewise: untuk waktu t < 3 detik sinyal mengikuti kurva parabola f(t) = t^2 + k, dan untuk t >= 3 detik sinyal mengikuti garis f(t) = 4t - 1. Jika terdapat lonjakan mendadak pada t = 3, paket data akan rusak (data packet loss)! Tugasmu adalah mencari nilai konstanta k agar sinyal kontinu sempurna tanpa terputus!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Syarat Formal Tiga Pilar Kontinuitas</h3>\n              <p>Suatu fungsi $f(x)$ dikatakan <strong>kontinu di titik $x = c$</strong> jika memenuhi TIGA SYARAT MUTLAK:</p>\n              <ol class=\"dic-list\">\n                <li>$f(c)$ terdefinisi (ada nilainya secara riil).</li>\n                <li>$\\lim_{x \\to c} f(x)$ ada (artinya limit kiri = limit kanan).</li>\n                <li>Nilai limit sama persis dengan nilai fungsinya:\n                  \\[ \\lim_{x \\to c} f(x) = f(c) \\]\n                </li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Untuk menyambungkan dua kurva fungsi piecewise agar kontinu di titik perbatasan c, cukup samakan nilai limit kiri dan limit kanan di titik tersebut!",
            "pitfall": "Fungsi yang memiliki limit belum tentu kontinu jika titik pada fungsinya berlubang atau berada di tempat lain!",
            "fun_fact": "Dalam animasi film 3D (seperti film animasi Pixar), kurva spline Bézier dirancang dengan kontinuitas turunan tingkat tinggi ($C^1$ dan $C^2$ continuity) agar permukaan animasi karakter terlihat halus sempurna tanpa patahan.",
            "formula": "\\text{Kontinu di } x = c \\iff \\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = f(c)",
            "formula_params": [
                [
                    "c",
                    "Titik sambungan perbatasan fungsi."
                ],
                [
                    "f(c)",
                    "Nilai fungsi pada titik c."
                ]
            ],
            "formula_intuition": "Memastikan tidak ada celah, lompatan vertikal mendadak, atau lubang pada kurva lintasan.",
            "example": {
                "question": "Diberikan fungsi piecewise sinyal: $f(t) = \\begin{cases} t^2 + k, & t < 3 \\\\ 4t - 1, & t \\ge 3 \\end{cases}$. Tentukan nilai konstanta k agar fungsi sinyal tersebut kontinu di titik $t = 3$!",
                "known": "Fungsi cabang kiri $t^2 + k$ dan cabang kanan $4t - 1$ di titik batas $t = 3$.",
                "asked": "Nilai k agar kontinu.",
                "steps": [
                    [
                        "Langkah 1: Hitung Limit Kiri ($t \\to 3^-$)",
                        "$\\lim_{t \\to 3^-} (t^2 + k) = 3^2 + k = 9 + k$."
                    ],
                    [
                        "Langkah 2: Hitung Limit Kanan & Nilai $f(3)$ ($t \\to 3^+$)",
                        "$\\lim_{t \\to 3^+} (4t - 1) = 4(3) - 1 = 12 - 1 = 11$."
                    ],
                    [
                        "Langkah 3: Samakan Limit Kiri dan Kanan untuk Menjamin Kontinuitas",
                        "$9 + k = 11 \\implies k = 11 - 9 = 2$."
                    ]
                ],
                "conclusion": "Nilai konstanta k harus tepat bernilai 2 agar jalur sinyal kontinu tanpa kehilangan paket data."
            },
            "takeaways": [
                "Kontinuitas mensyaratkan grafik tidak terputus, tidak berlubang, dan tidak melompat.",
                "Penyambungan kurva piecewise diselesaikan dengan menyamakan limit kiri dan limit kanan.",
                "Selamat! Kamu telah menuntaskan seluruh materi Limit Fungsi Aljabar dengan standar masteri!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE LIMIT: Agar fungsi $g(x) = \\begin{cases} ax + 3, & x < 2 \\\\ 7, & x \\ge 2 \\end{cases}$ kontinu di x = 2, berapakah nilai a?",
                [
                    "a = 2",
                    "a = 4",
                    "a = 5"
                ],
                0,
                "Limit kiri = 2a + 3. Limit kanan = 7. Maka 2a + 3 = 7 => 2a = 4 => a = 2."
            ]
        }
    ]
}
