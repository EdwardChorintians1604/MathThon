# -*- coding: utf-8 -*-
DATA = {
    "title": "Sistem Persamaan Linear",
    "short": "SPLDV",
    "icon": "bi-braces-asterisk",
    "color": "#d97706",
    "desc": "Kuasai SPLDV dan SPLTV, metode eliminasi, substitusi murni, metode grafik, determinan Cramer, serta aplikasinya dalam pemodelan bisnis dan riset operasional.",
    "babs": [
        {
            "title": "Fondasi: Garis Lurus & Makna Perpotongan Dua Hubungan Linier",
            "objectives": [
                "Memahami persamaan linear dua variabel sebagai garis lurus tak berhingga di bidang Cartesius.",
                "Memahami solusi SPLDV sebagai titik potong persekutuan koordinat (x, y) yang memuaskan kedua garis.",
                "Mengenali tiga kemungkinan geometri solusi: Tepat Satu Solusi, Tak Hingga Solusi, atau Tidak Ada Solusi."
            ],
            "hook": "Dua buah drone diterbangkan di langit malam. Drone pertama terbang mengikuti lintasan garis y = 2x + 1, sedangkan drone kedua terbang mengikuti garis y = -x + 7. Akankah kedua drone tersebut bertabrakan di udara? Jika ya, di titik koordinat manakah tabrakan itu akan terjadi? Menjawab pertanyaan ini adalah esensi dari Sistem Persamaan Linear: mencari satu titik koordinat persekutuan yang memenuhi kedua persamaan secara simultan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-graph-up text-primary\"></i> 1. Tiga Kemungkinan Geometris Solusi SPLDV</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Garis Berpotongan (Tepat Satu Solusi Unik):</strong> Gradien kedua garis berbeda ($m_1 \\neq m_2$). Menghasilkan satu pasangan nilai $(x, y)$.</li>\n                <li><strong>Garis Sejajar (Tidak Ada Solusi / Nol Solusi):</strong> Gradien sama tetapi konstanta berbeda ($m_1 = m_2, c_1 \\neq c_2$). Kedua garis tidak pernah bertemu sampai kiamat!</li>\n                <li><strong>Garis Berimpit (Tak Hingga Banyak Solusi):</strong> Kedua persamaan berkelipatan identik dan membentuk garis yang sama persis.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk menguji apakah SPLDV memiliki solusi unik tanpa harus menghitung sampai akhir: Periksa rasio koefisiennya! Jika $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$, sistem dijamin pasti memiliki tepat satu solusi!",
            "pitfall": "Jangan terkecoh dengan dua persamaan yang sejajar! Jika suatu sistem tidak memiliki solusi, himpunan penyelesaiannya adalah Himpunan Kosong ($\\emptyset$), bukan angka nol!",
            "fun_fact": "Sistem Persamaan Linear dengan ribuan variabel diselesaikan setiap hari oleh Google PageRank untuk mengurutkan miliaran halaman website di mesin pencarian internet.",
            "formula": "\\begin{cases} a_1 x + b_1 y = c_1 \\\\ a_2 x + b_2 y = c_2 \\end{cases} \\implies (x^*, y^*) = \\text{Titik Potong Garis}",
            "formula_params": [
                [
                    "a_1, a_2",
                    "Koefisien variabel x."
                ],
                [
                    "b_1, b_2",
                    "Koefisien variabel y."
                ],
                [
                    "c_1, c_2",
                    "Konstanta ruas kanan."
                ]
            ],
            "formula_intuition": "Mencari titik pertemuan persekutuan dari dua garis lurus yang berpotongan.",
            "example": {
                "question": "Tentukan titik potong persekutuan dari dua persamaan linear: $x + y = 10$ dan $x - y = 4$ secara analitis!",
                "known": "$x + y = 10$ dan $x - y = 4$.",
                "asked": "Pasangan titik potong (x, y).",
                "steps": [
                    [
                        "Langkah 1: Jumlahkan Kedua Persamaan untuk Mengeliminasi y",
                        "$(x + y) + (x - y) = 10 + 4 \\implies 2x = 14$."
                    ],
                    [
                        "Langkah 2: Dapatkan Nilai x",
                        "$x = \\frac{14}{2} = 7$."
                    ],
                    [
                        "Langkah 3: Substitusikan x = 7 ke Persamaan Pertama",
                        "$7 + y = 10 \\implies y = 10 - 7 = 3$."
                    ]
                ],
                "conclusion": "Kedua garis berpotongan di titik koordinat tunggal (7, 3)."
            },
            "takeaways": [
                "Solusi SPLDV secara geometris adalah koordinat titik potong dari kedua garis di bidang Cartesius.",
                "Dua garis yang sejajar tidak memiliki solusi persekutuan.",
                "Dua garis yang berimpit memiliki tak terhingga banyaknya solusi."
            ],
            "quiz": [
                "Jika dua garis dalam SPLDV memiliki gradien yang sama persis namun konstanta pergeseran berbeda, maka sistem tersebut memiliki?",
                [
                    "Tidak ada solusi sama sekali",
                    "Tepat satu solusi",
                    "Tak hingga banyak solusi"
                ],
                0,
                "Garis dengan gradien sama bersikap sejajar dan tidak akan pernah berpotongan, sehingga tidak memiliki solusi."
            ]
        },
        {
            "title": "Anatomi: Struktur Baku SPLDV & Tiga Metode Penyelesaian",
            "objectives": [
                "Menguasai Metode Substitusi murni (mengganti variabel dari satu persamaan ke persamaan lain).",
                "Menguasai Metode Eliminasi murni (menyamakan koefisien lalu mengurangkan).",
                "Menguasai Metode Campuran (Eliminasi-Substitusi) sebagai metode paling efisien."
            ],
            "hook": "Di antara Metode Grafik, Substitusi, dan Eliminasi—manakah yang paling disukai para juara olimpiade dan programer? Metode Campuran (Gabungan)! Kita menggunakan eliminasi satu kali untuk melenyapkan satu variabel pengganggu, lalu menyelesaikannya dengan substitusi instan. Kombinasi ini memangkas langkah pengerjaan hingga separuh waktu!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-gear-fill text-primary\"></i> 1. Metode Gabungan (Eliminasi - Substitusi)</h3>\n              <ol class=\"dic-list\">\n                <li><strong>Langkah 1 (Eliminasi):</strong> Samakan koefisien salah satu variabel (misal x) dengan mengalikan kedua persamaan dengan faktor konstanta yang sesuai.</li>\n                <li><strong>Langkah 2:</strong> Kurangkan atau jumlahkan kedua persamaan untuk mengeliminasi variabel tersebut sehingga didapat nilai variabel lainnya (misal y).</li>\n                <li><strong>Langkah 3 (Substitusi):</strong> Masukkan nilai variabel yang telah didapat (y) ke salah satu persamaan awal untuk memperoleh nilai variabel pasangannya (x).</li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Pilihlah untuk mengeliminasi variabel yang koefisiennya paling mudah disamakan atau yang sudah memiliki koefisien 1!",
            "pitfall": "Hati-hati dengan tanda negatif saat mengurangkan dua persamaan: $(3x - (-2x)) = 3x + 2x = 5x$, jangan sampai keliru menjadi $1x$!",
            "fun_fact": "Metode eliminasi sistem persamaan linear tercatat pertama kali dalam naskah matematika kuno Tiongkok 'Jiuzhang Suanshu' (Sembilan Bab tentang Seni Matematika) dari Dinasti Han sekitar abad ke-2 SM, berabad-abad sebelum Carl Friedrich Gauss memformalkannya di Eropa (Eliminasi Gauss).",
            "formula": "\\begin{cases} a_1 x + b_1 y = c_1 \\ (\\times a_2) \\\\ a_2 x + b_2 y = c_2 \\ (\\times a_1) \\end{cases} \\implies (a_1 b_2 - a_2 b_1)y = a_1 c_2 - a_2 c_1",
            "formula_params": [
                [
                    "x, y",
                    "Dua variabel yang dicari penyelesaiannya simultan."
                ]
            ],
            "formula_intuition": "Menyamakan magnitudo koefisien agar variabel target dapat dilenyapkan secara bersih melalui pengurangan.",
            "example": {
                "question": "Selesaikan SPLDV berikut menggunakan metode gabungan eliminasi-substitusi: $2x + 3y = 12$ dan $3x + 2y = 13$!",
                "known": "Persamaan 1: $2x + 3y = 12$, Persamaan 2: $3x + 2y = 13$.",
                "asked": "Nilai himpunan penyelesaian x dan y.",
                "steps": [
                    [
                        "Langkah 1: Samakan Koefisien x",
                        "Kalikan Persamaan 1 dengan 3: $6x + 9y = 36$.<br>Kalikan Persamaan 2 dengan 2: $6x + 4y = 26$."
                    ],
                    [
                        "Langkah 2: Kurangkan Kedua Persamaan",
                        "$(6x - 6x) + (9y - 4y) = 36 - 26 \\implies 5y = 10 \\implies y = 2$."
                    ],
                    [
                        "Langkah 3: Substitusikan y = 2 ke Persamaan 1",
                        "$2x + 3(2) = 12 \\implies 2x + 6 = 12 \\implies 2x = 6 \\implies x = 3$."
                    ]
                ],
                "conclusion": "Himpunan penyelesaiannya adalah {(3, 2)} dengan x = 3 dan y = 2."
            },
            "takeaways": [
                "Metode gabungan eliminasi-substitusi adalah teknik paling praktis dan minim risiko salah hitung.",
                "Penyamaan koefisien dilakukan menggunakan prinsip Kelipatan Persekutuan Terkecil (KPK).",
                "Solusi akhir dapat diverifikasi dengan memasukkan nilai x dan y ke kedua persamaan awal."
            ],
            "quiz": [
                "Jika x + y = 8 dan x - y = 2, berapakah nilai dari x dan y?",
                [
                    "x = 5 dan y = 3",
                    "x = 6 dan y = 2",
                    "x = 4 dan y = 4"
                ],
                0,
                "Jumlahkan: 2x = 10 => x = 5. Masukkan ke pers 1: 5 + y = 8 => y = 3."
            ]
        },
        {
            "title": "Mekanika: Aturan Determinan Cramer & SPLTV 3 Variabel",
            "objectives": [
                "Menyelesaikan SPLDV menggunakan Aturan Determinan Cramer (D, Dx, Dy).",
                "Memperluas sistem persamaan linear menjadi 3 variabel (SPLTV x, y, z).",
                "Menyelesaikan SPLTV dengan metode eliminasi berjenjang bertahap."
            ],
            "hook": "Bagaimana jika kita harus menyelesaikan sistem dengan 3 variabel: x (kecepatan), y (waktu), dan z (konsumsi bahan bakar)? Metode aljabar biasa bisa sangat panjang dan membingungkan. Aturan Cramer hadir sebagai formula determinan matriks yang elegan: kita cukup menghitung determinan D, Dx, Dy, Dz, dan solusinya langsung keluar dalam sekejap!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-grid-1x2 text-primary\"></i> 1. Aturan Determinan Cramer untuk SPLDV</h3>\n              <p>Untuk sistem persamaan:</p>\n              \\[ \\begin{cases} a_1 x + b_1 y = c_1 \\\\ a_2 x + b_2 y = c_2 \\end{cases} \\]\n              <ul class=\"dic-list\">\n                <li>$D = \\det \\begin{pmatrix} a_1 & b_1 \\\\ a_2 & b_2 \\end{pmatrix} = a_1 b_2 - a_2 b_1$.</li>\n                <li>$D_x = \\det \\begin{pmatrix} c_1 & b_1 \\\\ c_2 & b_2 \\end{pmatrix} = c_1 b_2 - c_2 b_1$ (Ganti kolom x dengan konstanta c).</li>\n                <li>$D_y = \\det \\begin{pmatrix} a_1 & c_1 \\\\ a_2 & c_2 \\end{pmatrix} = a_1 c_2 - a_2 c_1$ (Ganti kolom y dengan konstanta c).</li>\n              </ul>\n              \\[ x = \\frac{D_x}{D} \\quad \\text{dan} \\quad y = \\frac{D_y}{D} \\quad (D \\neq 0) \\]\n            </div>\n            ",
            "pro_tip": "Aturan Cramer sangat mudah diprogram dalam bahasa Python atau JavaScript karena hanya memerlukan fungsi determinan sederhana!",
            "pitfall": "Jika nilai determinan utama D = 0, Aturan Cramer tidak dapat digunakan (pembagian dengan nol)!",
            "fun_fact": "Aturan Cramer dipublikasikan oleh matematikawan Swiss Gabriel Cramer pada tahun 1750 dalam risalahnya tentang kurva aljabar.",
            "formula": "x = \\frac{D_x}{D} \\quad ; \\quad y = \\frac{D_y}{D} \\quad ; \\quad z = \\frac{D_z}{D} \\quad (D \\neq 0)",
            "formula_params": [
                [
                    "D",
                    "Determinan matriks koefisien utama."
                ],
                [
                    "D_x, D_y, D_z",
                    "Determinan minor dengan kolom variabel digantikan kolom konstanta."
                ]
            ],
            "formula_intuition": "Menghitung rasio volume ruang transformasi yang diskalakan oleh masing-masing variabel.",
            "example": {
                "question": "Selesaikan sistem $3x + 2y = 16$ dan $x - 2y = -8$ menggunakan Aturan Cramer!",
                "known": "$a_1=3, b_1=2, c_1=16$ dan $a_2=1, b_2=-2, c_2=-8$.",
                "asked": "Nilai x dan y via determinan.",
                "steps": [
                    [
                        "Langkah 1: Hitung Determinan Utama D",
                        "$D = (3)(-2) - (2)(1) = -6 - 2 = -8$."
                    ],
                    [
                        "Langkah 2: Hitung Determinan Dx",
                        "$D_x = (16)(-2) - (2)(-8) = -32 - (-16) = -32 + 16 = -16$."
                    ],
                    [
                        "Langkah 3: Hitung Determinan Dy",
                        "$D_y = (3)(-8) - (16)(1) = -24 - 16 = -40$."
                    ],
                    [
                        "Langkah 4: Hitung Nilai Solusi x dan y",
                        "$x = \\frac{D_x}{D} = \\frac{-16}{-8} = 2$.<br>$y = \\frac{D_y}{D} = \\frac{-40}{-8} = 5$."
                    ]
                ],
                "conclusion": "Solusi sistem adalah x = 2 dan y = 5."
            },
            "takeaways": [
                "Aturan Cramer menghitung solusi SPLDV murni dari perbandingan nilai determinan.",
                "Kolom variabel yang dicari digantikan oleh kolom konstanta ruas kanan.",
                "Syarat mutlak aturan Cramer adalah determinan utama D tidak boleh sama dengan nol."
            ],
            "quiz": [
                "Pada aturan Cramer, jika determinan utama D = 5 dan Dx = 20, berapakah nilai variabel x?",
                [
                    "x = 4",
                    "x = 1/4",
                    "x = 100"
                ],
                0,
                "x = Dx / D = 20 / 5 = 4."
            ]
        },
        {
            "title": "Pemodelan: Aplikasi Nyata Sistem Persamaan Linear",
            "objectives": [
                "Menerjemahkan masalah cerita transaksi bisnis, tarif tiket, dan sistem parkir menjadi model SPLDV formal.",
                "Menyelesaikan masalah campuran larutan kimia dan persentase paduan logam.",
                "Menginterpretasikan makna nilai variabel dalam konteks keuangan dan ekonomi."
            ],
            "hook": "Seorang petugas kasir festival konser musik mencatat bahwa penjualan 3 tiket VIP dan 5 tiket Festival menghasilkan Rp 4.100.000, sedangkan penjualan 2 tiket VIP dan 3 tiket Festival menghasilkan Rp 2.600.000. Petugas lupa mencatat harga satuan masing-masing tiket! Bagaimana cara mengetahui harga pasti 1 tiket VIP dan 1 tiket Festival tanpa menebak-nebak? Pemodelan SPLDV memecahkannya dengan kepastian matematis mutlak!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-lightbulb-fill text-primary\"></i> Tiga Langkah Pemodelan Masalah Nyata</h3>\n              <ol class=\"dic-list\">\n                <li><strong>Identifikasi Variabel:</strong> Berikan nama simbol variabel pada besaran yang belum diketahui nilainya (misal $x$ dan $y$).</li>\n                <li><strong>Susun Dua Persamaan Bebas:</strong> Terjemahkan dua kalimat kondisi fakta pada soal cerita menjadi dua persamaan matematika linier.</li>\n                <li><strong>Selesaikan dengan Metode Aljabar & Tuliskan Kesimpulan Nyata Lengkap dengan Satuan.</strong></li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Pastikan satuan besaran di seluruh persamaan konsisten! Jika harga tiket dinyatakan dalam ribuan rupiah, nyatakan semuanya dalam ribuan rupiah.",
            "pitfall": "Jangan berhenti setelah menemukan angka x dan y! Selalu baca kembali apa yang ditanyakan di akhir soal (apakah mencari nilai $x$, nilai $y$, ataukah harga kombinasi $2x + 3y$!).",
            "fun_fact": "Dalam riset operasional logistik maskapai penerbangan, algoritma pencocokan awak kabin dan pesawat menggunakan sistem persamaan linear ribuan variabel (Simplex Algorithm) untuk menghemat biaya operasional miliaran rupiah setiap penerbangan.",
            "formula": "\\text{Model: } \\begin{cases} a_1 x + b_1 y = \\text{Kondisi 1} \\\\ a_2 x + b_2 y = \\text{Kondisi 2} \\end{cases}",
            "formula_params": [
                [
                    "x",
                    "Harga / kuantitas barang pertama."
                ],
                [
                    "y",
                    "Harga / kuantitas barang kedua."
                ]
            ],
            "formula_intuition": "Menghubungkan dua kendala faktual independen untuk mengunci satu titik temu solusi.",
            "example": {
                "question": "Di area parkir terdapat 50 kendaraan yang terdiri dari sepeda motor (roda 2) dan mobil (roda 4). Petugas parkir menghitung jumlah seluruh roda kendaraan tersebut adalah 140 buah roda. Berapakah jumlah mobil dan jumlah motor di tempat parkir tersebut?",
                "known": "Total kendaraan = 50. Total roda = 140. Motor = 2 roda, Mobil = 4 roda.",
                "asked": "Banyak motor (x) dan banyak mobil (y).",
                "steps": [
                    [
                        "Langkah 1: Susun Sistem Persamaan",
                        "Persamaan Jumlah Kendaraan: $x + y = 50$.<br>Persamaan Jumlah Roda: $2x + 4y = 140$."
                    ],
                    [
                        "Langkah 2: Sederhanakan Persamaan Roda",
                        "Bagi persamaan roda dengan 2: $x + 2y = 70$."
                    ],
                    [
                        "Langkah 3: Kurangkan Kedua Persamaan",
                        "$(x + 2y) - (x + y) = 70 - 50 \\implies y = 20\\text{ mobil}$."
                    ],
                    [
                        "Langkah 4: Cari Banyak Motor x",
                        "$x + 20 = 50 \\implies x = 50 - 20 = 30\\text{ motor}$."
                    ]
                ],
                "conclusion": "Di area parkir terdapat 30 unit sepeda motor dan 20 unit mobil (Cek: 30(2) + 20(4) = 60 + 80 = 140 roda, Valid!)."
            },
            "takeaways": [
                "Soal cerita diselesaikan dengan menetapkan variabel, menyusun sistem, dan mengeliminasi.",
                "Verifikasi selalu hasil akhir terhadap fakta kondisi soal.",
                "SPLDV diaplikasikan luas dalam manajemen inventaris dan transaksi ritel."
            ],
            "quiz": [
                "Harga 2 buku dan 3 pensil Rp 17.000, sedangkan harga 1 buku dan 2 pensil Rp 10.000. Berapakah harga 1 buah buku?",
                [
                    "Rp 4.000",
                    "Rp 3.000",
                    "Rp 5.000"
                ],
                0,
                "Model: 2b + 3p = 17.000 dan b + 2p = 10.000 (kalikan 2: 2b + 4p = 20.000). Kurangkan: p = 3.000 (pensil). Maka b = 10.000 - 2(3.000) = Rp 4.000."
            ]
        },
        {
            "title": "Capstone: Optimasi Anggaran Logistik Rantai Pasok Multi-Gudang",
            "objectives": [
                "Mengintegrasikan penyelesaian SPLTV 3 variabel untuk memecahkan alokasi armada transportasi distribusi pangan nasional.",
                "Menyusun model kendala kapasitas muatan, batas anggaran bahan bakar, dan kuota volume pengiriman.",
                "Mengevaluasi keputusan manajerial logistik berdasarkan solusi matematis formal."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Director of Supply Chain Logistics BUMN Pangan. Sebuah pusat distribusi harus mengirimkan 90 ton bantuan beras menggunakan tiga jenis armada: Truk Kecil (x) bermuatan 2 ton, Truk Sedang (y) bermuatan 3 ton, dan Truk Tronton (z) bermuatan 5 ton. Total armada yang dikerahkan tepat 30 kendaraan. Biaya operasional total dipatok Rp 41 juta dengan rincian biaya: Truk Kecil Rp 1 juta, Truk Sedang Rp 1.5 juta, dan Truk Tronton Rp 2 juta per unit. Tentukan jumlah masing-masing armada yang harus diberangkatkan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario SPLTV Logistik Pangan 3 Variabel</h3>\n              <p>Sistem dimodelkan oleh tiga persamaan simultan berderajat satu:</p>\n              \\[ \\begin{cases} x + y + z = 30 & (\\text{Total Kendaraan}) \\\\ 2x + 3y + 5z = 90 & (\\text{Kapasitas Tonase}) \\\\ x + 1.5y + 2z = 41 & (\\text{Anggaran Biaya Juta Rp}) \\end{cases} \\]\n            </div>\n            ",
            "pro_tip": "Untuk menyelesaikan SPLTV 3 variabel dengan cepat: Eliminasi variabel yang sama (misal x) dari dua pasang persamaan berbeda untuk menghasilkan SPLDV 2 variabel (y dan z) yang jauh lebih sederhana!",
            "pitfall": "Jangan menggabungkan kembali persamaan yang baru saja dihasilkan dengan persamaan asal tanpa eliminasi, karena akan menghasilkan identitas lingkaran kosong (tautologi)!",
            "fun_fact": "Metode penyelesaian sistem persamaan linear multi-variabel adalah fondasi dari algoritma optimasi rute armada pengiriman logistik raksasa dunia seperti FedEx, UPS, dan Amazon Prime.",
            "formula": "\\begin{cases} x + y + z = N \\\\ a x + b y + c z = T \\\\ d x + e y + f z = B \\end{cases} \\implies \\text{Eliminasi Berjenjang menuju SPLDV}",
            "formula_params": [
                [
                    "x, y, z",
                    "Alokasi armada truk kecil, sedang, dan tronton."
                ],
                [
                    "N, T, B",
                    "Kendala total kendaraan, tonase muatan, dan anggaran."
                ]
            ],
            "formula_intuition": "Menemukan titik potong persekutuan dari tiga bidang datar di ruang 3 dimensi (x, y, z).",
            "example": {
                "question": "Selesaikan sistem logistik di atas untuk menentukan berapa banyak Truk Kecil (x), Truk Sedang (y), dan Truk Tronton (z) yang harus dikerahkan!",
                "known": "(1) $x + y + z = 30$, (2) $2x + 3y + 5z = 90$, (3) $x + 1.5y + 2z = 41$.",
                "asked": "Nilai x, y, dan z.",
                "steps": [
                    [
                        "Langkah 1: Kalikan Persamaan (3) dengan 2 agar Bilangan Bulat",
                        "$2x + 3y + 4z = 82$ (Sebut sebagai Persamaan 4)."
                    ],
                    [
                        "Langkah 2: Kurangkan Persamaan (2) dengan Persamaan (4)",
                        "$(2x + 3y + 5z) - (2x + 3y + 4z) = 90 - 82 \\implies z = 8\\text{ unit tronton}$!"
                    ],
                    [
                        "Langkah 3: Substitusikan z = 8 ke Persamaan (1) dan (2)",
                        "Dari Pers (1): $x + y + 8 = 30 \\implies x + y = 22$.<br>Dari Pers (2): $2x + 3y + 5(8) = 90 \\implies 2x + 3y + 40 = 90 \\implies 2x + 3y = 50$."
                    ],
                    [
                        "Langkah 4: Selesaikan SPLDV x dan y",
                        "Kalikan $x + y = 22$ dengan 2: $2x + 2y = 44$.<br>Kurangkan: $(2x + 3y) - (2x + 2y) = 50 - 44 \\implies y = 6\\text{ unit truk sedang}$."
                    ],
                    [
                        "Langkah 5: Cari Nilai x",
                        "$x = 22 - 6 = 16\\text{ unit truk kecil}$."
                    ]
                ],
                "conclusion": "Armada optimal yang diberangkatkan adalah 16 unit Truk Kecil, 6 unit Truk Sedang, dan 8 unit Truk Tronton (Total = 16 + 6 + 8 = 30 kendaraan)."
            },
            "takeaways": [
                "SPLTV memodelkan masalah multi-kendala di dunia nyata menjadi solusi numerik unik.",
                "Eliminasi berjenjang menyederhanakan 3 variabel menjadi 2 variabel hingga diperoleh solusi.",
                "Selamat! Kamu telah menguasai seluruh kurikulum Sistem Persamaan Linear dengan standar pemecahan masalah tingkat tinggi!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE SPLTV: Berdasarkan hasil perhitungan alokasi armada di atas, berapakah banyak Truk Tronton (z) yang diberangkatkan?",
                [
                    "8 unit",
                    "6 unit",
                    "16 unit"
                ],
                0,
                "Dari eliminasi (2x + 3y + 5z = 90) - (2x + 3y + 4z = 82) diperoleh langsung z = 8 unit."
            ]
        }
    ]
}
