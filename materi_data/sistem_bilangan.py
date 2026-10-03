# -*- coding: utf-8 -*-
DATA = {
    "title": "Sistem Bilangan (Biner, Oktal, Hex)",
    "short": "Sis. Bilangan",
    "icon": "bi-cpu",
    "color": "#334155",
    "desc": "Kuasai arsitektur nilai tempat polinomial basis numerik, konversi Biner (Basis 2), Oktal (Basis 8), Desimal (Basis 10), Heksadesimal (Basis 16), kode warna CSS RGB, dan memori komputer.",
    "babs": [
        {
            "title": "Fondasi: Konsep Nilai Tempat Berbobot Polinomial",
            "objectives": [
                "Memahami konsep basis bilangan (Radix) dan sistem nilai tempat bertingkat (Positional Number System).",
                "Memahami mengapa manusia menggunakan Desimal (Basis 10) dan komputer menggunakan Biner (Basis 2).",
                "Menguraikan nilai suatu bilangan ke dalam representasi polinomial berpangkat basis."
            ],
            "hook": "Mengapa manusia di seluruh dunia menghitung menggunakan sistem Desimal (Basis 10)? Bukan karena angka 10 memiliki keajaiban mistis, melainkan murni karena anatomi tubuh: nenek moyang manusia memiliki 10 jari tangan! Jika kita terlahir memiliki 8 jari seperti kartun The Simpsons, kita semua hari ini pasti menggunakan sistem Oktal (Basis 8). Komputer hanya memiliki 'dua jari': tegangan listrik tinggi (1) dan tegangan rendah (0), sehingga komputer berpikir dalam sistem BINER (Basis 2)!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-hash text-primary\"></i> 1. Teorema Ekspansi Polinomial Basis $b$</h3>\n              <p>Setiap bilangan pada basis apa pun dapat diuraikan sebagai penjumlahan digit dikalikan bobot perpangkatan basisnya:</p>\n              \\[ N_b = \\sum_{i=0}^{n} d_i \\cdot b^i = d_n b^n + \\dots + d_2 b^2 + d_1 b^1 + d_0 b^0 \\]\n              <ul class=\"dic-list\">\n                <li>Contoh Desimal Basis 10: $253_{10} = (2 \\times 10^2) + (5 \\times 10^1) + (3 \\times 10^0) = 200 + 50 + 3$.</li>\n                <li>Contoh Biner Basis 2: $1101_2 = (1 \\times 2^3) + (1 \\times 2^2) + (0 \\times 2^1) + (1 \\times 2^0) = 8 + 4 + 0 + 1 = 13_{10}$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Hafalkan deret bobot pangkat dua: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024! Menghafal deret ini membuat konversi biner ke desimal berlangsung secepat kilat tanpa perlu kalkulator.",
            "pitfall": "Angka terbesar pada basis $b$ selalu bernilai $b - 1$! Pada basis 10, digit terbesar adalah 9. Pada basis 2 (biner), digit terbesar adalah 1 (angka 2 tidak pernah ada di sistem biner!).",
            "fun_fact": "Bangsa Maya kuno di Amerika Tengah menggunakan sistem Vigesimal (Basis 20) karena mereka menghitung menggunakan 10 jari tangan ditambah 10 jari kaki, sedangkan bangsa Sumeria kuno menggunakan Basis 60 (Seksagesimal) yang menjadi asal mula mengapa 1 jam = 60 menit dan 1 lingkaran = 360 derajat!",
            "formula": "N_{10} = \\sum_{i=0}^n d_i \\cdot b^i = d_n b^n + \\dots + d_1 b^1 + d_0 b^0",
            "formula_params": [
                [
                    "b",
                    "Basis bilangan pokok (2, 8, 10, atau 16)."
                ],
                [
                    "d_i",
                    "Digit angka pada posisi ke-i."
                ],
                [
                    "b^i",
                    "Bobot nilai tempat posisi ke-i."
                ]
            ],
            "formula_intuition": "Mengalikan setiap simbol angka dengan bobot nilai kelipatan basisnya.",
            "example": {
                "question": "Konversikan bilangan biner $10110_2$ ke dalam sistem bilangan desimal biasa (basis 10)!",
                "known": "Bilangan biner 5 digit: 1, 0, 1, 1, 0.",
                "asked": "Nilai desimal ekuivalen.",
                "steps": [
                    [
                        "Langkah 1: Tuliskan Bobot Pangkat Dua dari Kanan ke Kiri",
                        "Digit ke-0 (paling kanan) = $2^0 = 1$.<br>Digit ke-1 = $2^1 = 2$.<br>Digit ke-2 = $2^2 = 4$.<br>Digit ke-3 = $2^3 = 8$.<br>Digit ke-4 = $2^4 = 16$."
                    ],
                    [
                        "Langkah 2: Kalikan Masing-Masing Digit dengan Bobotnya",
                        "($1 \\times 16$) + ($0 \\times 8$) + ($1 \\times 4$) + ($1 \\times 2$) + ($0 \\times 1$)."
                    ],
                    [
                        "Langkah 3: Jumlahkan Seluruh Hasil Kali",
                        "$16 + 0 + 4 + 2 + 0 = 22_{10}$."
                    ]
                ],
                "conclusion": "Bilangan biner $10110_2$ tepat sama dengan bilangan desimal 22."
            },
            "takeaways": [
                "Sistem bilangan beroperasi di atas prinsip nilai tempat polinomial berbobot basis.",
                "Biner adalah bahasa internal perangkat keras komputer yang tersusun dari digit 0 dan 1.",
                "Konversi ke desimal dilakukan dengan menjumlahkan perkalian digit terhadap pangkat basisnya."
            ],
            "quiz": [
                "Berapakah nilai desimal dari bilangan biner 1111₂?",
                [
                    "15",
                    "16",
                    "14"
                ],
                0,
                "1*8 + 1*4 + 1*2 + 1*1 = 8 + 4 + 2 + 1 = 15."
            ]
        },
        {
            "title": "Anatomi: Empat Sistem Bilangan Baku Komputer (Biner, Oktal, Desimal, Heksa)",
            "objectives": [
                "Mengenali 4 sistem bilangan baku komputasi: Biner (2), Oktal (8), Desimal (10), dan Heksadesimal (16).",
                "Memahami simbol huruf heksadesimal A s.d. F yang merepresentasikan nilai 10 s.d. 15.",
                "Memahami hubungan alami antara Biner, Oktal (kelompok 3 bit), dan Heksadesimal (kelompok 4 bit)."
            ],
            "hook": "Bagi manusia, membaca untaian biner 32-bit seperti `11111111000000001010101001010101` sangat memusingkan kepala. Di sinilah Heksadesimal (Basis 16) hadir sebagai penyelamat programmer! Setiap 4 digit biner (nibble) tepat diringkas menjadi 1 karakter heksadesimal saja. Untaian panjang di atas cukup ditulis ringkas sebagai `FF00AA55`! Heksadesimal adalah jembatan komunikasi antara pikiran manusia dan memori mesin komputer.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-cpu text-primary\"></i> Karakteristik Empat Basis Komputer</h3>\n              <div class=\"table-responsive\">\n                <table class=\"table table-dark table-bordered small\">\n                  <thead><tr><th>Sistem Bilangan</th><th>Basis Radix</th><th>Digit Simbol yang Sah</th><th>Contoh Penulisan</th></tr></thead>\n                  <tbody>\n                    <tr><td><strong>Biner</strong></td><td>Basis 2</td><td>0, 1</td><td>$1010_2$</td></tr>\n                    <tr><td><strong>Oktal</strong></td><td>Basis 8</td><td>0, 1, 2, 3, 4, 5, 6, 7</td><td>$75_8$</td></tr>\n                    <tr><td><strong>Desimal</strong></td><td>Basis 10</td><td>0, 1, 2, 3, 4, 5, 6, 7, 8, 9</td><td>$255_{10}$</td></tr>\n                    <tr><td><strong>Heksadesimal</strong></td><td>Basis 16</td><td>0 s.d. 9, dan A=10, B=11, C=12, D=13, E=14, F=15</td><td>$\\text{FF}_{16}$</td></tr>\n                  </tbody>\n                </table>\n              </div>\n            </div>\n            ",
            "pro_tip": "Tabel konversi instan huruf Heksadesimal yang wajib hafal: A = 10, B = 11, C = 12, D = 13, E = 14, F = 15!",
            "pitfall": "Angka 10 pada heksadesimal ($10_{16}$) BUKAN bernilai sepuluh, melainkan bernilai 16 desimal ($1 \\times 16^1 + 0 = 16$)!",
            "fun_fact": "Dalam rekayasa sistem operasi Linux dan Unix, izin akses file (file permissions) ditulis dalam sistem Oktal: `chmod 777` bermakna 7 (Baca+Tulis+Eksekusi) untuk Pemilik, Grup, dan Publik.",
            "formula": "\\text{Heksa: } A=10, \\ B=11, \\ C=12, \\ D=13, \\ E=14, \\ F=15 \\quad ; \\quad 1 \\text{ Hex Digit} = 4 \\text{ Bits}",
            "formula_params": [
                [
                    "A - F",
                    "Simbol alfabet untuk digit di atas 9."
                ],
                [
                    "Nibble",
                    "Kelompok 4 digit biner yang setara tepat 1 digit heksa."
                ]
            ],
            "formula_intuition": "Basis 16 adalah $2^4$, sehingga pemetaan 4-bit biner ke 1 karakter heksadesimal bersifat sempurna tanpa sisa.",
            "example": {
                "question": "Konversikan bilangan heksadesimal $2\\text{F}_{16}$ ke dalam sistem bilangan desimal biasa!",
                "known": "$2\\text{F}_{16}$ dengan digit 2 dan digit F (F = 15).",
                "asked": "Nilai desimal.",
                "steps": [
                    [
                        "Langkah 1: Identifikasi Nilai Simbol",
                        "Digit 2 = 2. Digit F = 15."
                    ],
                    [
                        "Langkah 2: Kalikan Masing-Masing Digit dengan Bobot Pangkat 16",
                        "Digit ke-1: $2 \\times 16^1 = 32$.<br>Digit ke-0: $15 \\times 16^0 = 15 \\times 1 = 15$."
                    ],
                    [
                        "Langkah 3: Jumlahkan Seluruh Hasil",
                        "$32 + 15 = 47_{10}$."
                    ]
                ],
                "conclusion": "Bilangan heksadesimal 2F setara dengan bilangan desimal 47."
            },
            "takeaways": [
                "Heksadesimal menggunakan 16 simbol: 0-9 dan huruf A-F.",
                "Satu digit heksadesimal meringkas tepat 4 digit biner (1 nibble).",
                "Dua digit heksadesimal membentuk tepat 1 Byte data (8 bit) dari 00 s.d. FF (0 s.d. 255)."
            ],
            "quiz": [
                "Simbol huruf apakah yang mewakili nilai angka desimal 13 pada sistem heksadesimal?",
                [
                    "D",
                    "C",
                    "E"
                ],
                0,
                "A=10, B=11, C=12, D=13, E=14, F=15."
            ]
        },
        {
            "title": "Mekanika: Algoritma Konversi Desimal ke Basis Lain (Metode Modulo Sisa)",
            "objectives": [
                "Menguasai algoritma pembagian berulang modulo untuk mengubah Desimal ke Biner, Oktal, dan Heksa.",
                "Menyusun urutan digit hasil dari sisa pembagian terakhir menuju sisa pertama (Bottom-Up).",
                "Menguasai teknik konversi langsung Biner ke Heksadesimal menggunakan pengelompokan 4-bit."
            ],
            "hook": "Bagaimana sebuah chip prosesor komputer mengubah angka desimal yang kamu ketik di keyboard (misal angka 25) menjadi sinyal biner mesin? Komputer menjalankan Algoritma Modulo Sisa Pembagian: bagi angka berulang-ulang dengan 2, catat sisa pembagiannya (0 atau 1), lalu baca dari bawah ke atas! Prosedur mekanis ini adalah algoritma konversi tertua yang paling andal dalam sejarah ilmu komputasi.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrow-down-up text-primary\"></i> 1. Algoritma Pembagian Berulang Modulo</h3>\n              <p>Untuk mengubah bilangan desimal ke basis $b$ (misal $b = 2$ atau $b = 16$):</p>\n              <ol class=\"dic-list\">\n                <li>Bagi bilangan tersebut dengan basis $b$, catat hasil bagi bulat dan sisa pembagiannya (modulo).</li>\n                <li>Bagi kembali hasil bagi tersebut dengan $b$ terus-menerus sampai hasil baginya menjadi 0.</li>\n                <li><strong>Baca Hasil dari Bawah ke Atas (Bottom-Up):</strong> Sisa pembagian paling terakhir menjadi digit paling kiri (Most Significant Bit / MSB), dan sisa pertama menjadi digit paling kanan (Least Significant Bit / LSB).</li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Jalan pintas tercepat mengonversi Biner ke Heksadesimal: Kelompokkan digit biner per 4 bit dari kanan ke kiri, lalu konversi tiap 4 bit tersebut menjadi 1 digit heksa! Contoh: `1101 1010` -> `1101` adalah 13 (D) dan `1010` adalah 10 (A) -> Hasilnya langsung `DA`!",
            "pitfall": "Jangan membaca sisa pembagian dari atas ke bawah! Pembacaan HARUS DARI BAWAH KE ATAS (sisa pembagian paling akhir ditulis pertama)!",
            "fun_fact": "Algoritma pembagian modulo sisa ini dinamakan Algoritma Horner Invers yang telah diterapkan sejak era Dinasti Song di Tiongkok abad ke-13 untuk menghitung kalender gerhana bulan.",
            "formula": "N \\div b = Q_1 \\text{ sisa } R_0 \\ ; \\ Q_1 \\div b = Q_2 \\text{ sisa } R_1 \\dots \\implies \\text{Digit: } R_n \\dots R_1 R_0",
            "formula_params": [
                [
                    "N",
                    "Bilangan desimal mula-mula."
                ],
                [
                    "b",
                    "Basis tujuan pembagi (2 untuk biner, 16 untuk heksa)."
                ],
                [
                    "R_i",
                    "Sisa bagi modulo yang menjadi digit bilangan."
                ]
            ],
            "formula_intuition": "Mengekstrak koefisien polinomial basis satu per satu mulai dari pangkat terendah.",
            "example": {
                "question": "Konversikan bilangan desimal $29_{10}$ ke dalam bentuk bilangan biner (basis 2) menggunakan metode pembagian berulang modulo!",
                "known": "Bilangan desimal 29.",
                "asked": "Bentuk biner basis 2.",
                "steps": [
                    [
                        "Langkah 1: Bagi 29 dengan 2",
                        "$29 \\div 2 = 14$ dengan sisa $1$."
                    ],
                    [
                        "Langkah 2: Bagi 14 dengan 2",
                        "$14 \\div 2 = 7$ dengan sisa $0$."
                    ],
                    [
                        "Langkah 3: Bagi 7 dengan 2",
                        "$7 \\div 2 = 3$ dengan sisa $1$."
                    ],
                    [
                        "Langkah 4: Bagi 3 dengan 2",
                        "$3 \\div 2 = 1$ dengan sisa $1$."
                    ],
                    [
                        "Langkah 5: Bagi 1 dengan 2",
                        "$1 \\div 2 = 0$ dengan sisa $1$ (Berhenti karena hasil bagi sudah 0)."
                    ],
                    [
                        "Langkah 6: Baca Sisa Pembagian dari Bawah ke Atas",
                        "Sisa dari bawah ke atas: $1, 1, 1, 0, 1$."
                    ]
                ],
                "conclusion": "Bilangan desimal $29_{10}$ setara dengan bilangan biner $11101_2$."
            },
            "takeaways": [
                "Konversi desimal ke basis lain dilakukan dengan pembagian berulang basis sasaran.",
                "Sisa pembagian modulo dicatat dan dibaca dari bawah ke atas (Bottom-Up).",
                "Pengelompokan 4-bit biner mempercepat konversi biner ke heksadesimal secara instan."
            ],
            "quiz": [
                "Berapakah representasi biner dari bilangan desimal 19?",
                [
                    "10011₂",
                    "10101₂",
                    "11001₂"
                ],
                0,
                "19 = 16 + 2 + 1 = 1*16 + 0*8 + 0*4 + 1*2 + 1*1 = 10011₂."
            ]
        },
        {
            "title": "Pemodelan: Kode Warna Hex CSS Web (#FF5733) & Memori RAM",
            "objectives": [
                "Memahami pemodelan warna digital RGB 24-bit TrueColor menggunakan notasi kode Hex CSS (#RRGGBB).",
                "Mengonversi intensitas komponen warna merah (R), hijau (G), dan biru (B) dari heksadesimal ke skala desimal 0 s.d. 255.",
                "Memahami pemodelan pengalamatan memori komputer (Hex Memory Address) pada kartu grafis dan RAM."
            ],
            "hook": "Pernahkah kamu melihat kode warna seperti `#FF0000` di CSS website atau software Photoshop? Mengapa ada tanda pagar dan huruf FF? Kode tersebut adalah representasi HEKADESIMAL dari intensitas cahaya warna Red, Green, Blue (RGB)! Sepasang digit heksa pertama `FF` mewakili Merah maksimal (255), sepasang kedua `00` mewakili Hijau nol, dan sepasang ketiga `00` mewakili Biru nol. Kode `#FF0000` adalah warna Merah Murni! Heksadesimal adalah bahasa visual perancang web di seluruh dunia.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-palette-fill text-primary\"></i> 1. Struktur Kode Warna Hex CSS (#RRGGBB)</h3>\n              <p>Format warna digital 24-bit True Color membagi warna ke dalam 3 saluran intensitas cahaya masing-masing berukuran 1 Byte (8 bit = 00 s.d. FF = 0 s.d. 255):</p>\n              \\[ \\#\\underbrace{\\text{RR}}_{\\text{Merah}} \\ \\underbrace{\\text{GG}}_{\\text{Hijau}} \\ \\underbrace{\\text{BB}}_{\\text{Biru}} \\]\n              <ul class=\"dic-list\">\n                <li>$\\#000000$: Hitam Total (seluruh lampu RGB mati).</li>\n                <li>$\\#FFFFFF$: Putih Murni Maksimal ($255, 255, 255$).</li>\n                <li>Setiap pasang digit heksa dikonversi ke desimal melalui: $\\text{Nilai} = (d_1 \\times 16) + d_0$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mencerahkan warna di CSS web: Naikkan nilai angka/huruf heksadesimalnya mendekati FF! Untuk menggelapkan warna: Turunkan nilainya mendekati 00.",
            "pitfall": "Ingat bahwa nilai maksimum 1 Byte adalah 255 (FF), BUKAN 256! Rentang nilai intensitas adalah 0 hingga 255 (total 256 kombinasi).",
            "fun_fact": "Dengan format RGB 24-bit ($256 \\times 256 \\times 256$), layar smartphonemu mampu menampilkan lebih dari 16.7 juta variasi warna yang melampaui kemampuan mata manusia untuk membedakannya.",
            "formula": "\\#RRGGBB \\implies \\text{Intensitas} = (d_1 \\times 16) + d_0 \\quad (0 \\le \\text{Nilai} \\le 255)",
            "formula_params": [
                [
                    "RR",
                    "Intensitas warna Red (Merah) heksa."
                ],
                [
                    "GG",
                    "Intensitas warna Green (Hijau) heksa."
                ],
                [
                    "BB",
                    "Intensitas warna Blue (Biru) heksa."
                ]
            ],
            "formula_intuition": "Menggabungkan tiga channel intensitas cahaya 8-bit menjadi warna komposit aditif.",
            "example": {
                "question": "Sebuah warna pada website memiliki kode CSS Hex: `#2F80ED`. Hitunglah nilai intensitas desimal dari komponen warna Merah (Red) dan komponen warna Hijau (Green) dari kode warna tersebut!",
                "known": "Kode warna `#2F80ED`. Komponen Merah = `2F`, Komponen Hijau = `80`.",
                "asked": "Nilai desimal intensitas Red dan Green (skala 0 s.d. 255).",
                "steps": [
                    [
                        "Langkah 1: Konversi Komponen Merah (2F)",
                        "Digit 1 = 2, Digit 0 = F = 15.<br>$\\text{Red} = (2 \\times 16) + 15 = 32 + 15 = 47$."
                    ],
                    [
                        "Langkah 2: Konversi Komponen Hijau (80)",
                        "Digit 1 = 8, Digit 0 = 0.<br>$\\text{Green} = (8 \\times 16) + 0 = 128 + 0 = 128$."
                    ]
                ],
                "conclusion": "Intensitas warna Merah adalah 47 dan intensitas warna Hijau adalah 128 (Format CSS setara dengan rgb(47, 128, 237))."
            },
            "takeaways": [
                "Kode warna Hex CSS (#RRGGBB) adalah representasi heksadesimal dari intensitas warna 8-bit.",
                "Setiap pasang digit heksa mengodekan intensitas cahaya dari 0 hingga 255.",
                "Format heksadesimal menjadi standar tampilan alamat memori komputer dan grafika web."
            ],
            "quiz": [
                "Berapakah nilai desimal dari komponen warna heksa FF?",
                [
                    "255",
                    "256",
                    "100"
                ],
                0,
                "FF = (15 * 16) + 15 = 240 + 15 = 255."
            ]
        },
        {
            "title": "Capstone: Decoder Paket Jaringan Komputer & Ekstraksi Header IP",
            "objectives": [
                "Menerapkan konversi sistem bilangan untuk mendekode (mengekstrak) header paket jaringan internet (TCP/IP).",
                "Menerjemahkan byte data heksadesimal mentah menjadi alamat IP dan port jaringan desimal.",
                "Mengevaluasi integritas transmisi data digital menggunakan aljabar sistem bilangan."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Network Cybersecurity Analyst. Sebuah serangan siber terdeteksi pada server perusahaan. Perangkat lunak sniffer (Wireshark) menangkap potongan byte mentah heksadesimal dari header paket jaringan yang mencurigakan: `7F 00 00 01` dan port tujuan `1F 90`. Menggunakan keahlian konversi sistem bilanganmu, terjemahkan paket byte tersebut ke dalam format Alamat IP desimal bertitik (Dotted-Decimal IP) dan nomor port tujuan desimal!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-ethernet text-warning\"></i> Skenario Decoding Alamat IP IPv4</h3>\n              <p>Alamat IPv4 terdiri dari 4 Byte (32 bit) yang dipisahkan oleh tanda titik. Setiap Byte heksadesimal dikonversikan menjadi angka desimal 0 s.d. 255:</p>\n              \\[ \\text{Hex: } H_1 \\ H_2 \\ H_3 \\ H_4 \\implies D_1.D_2.D_3.D_4 \\]\n              <p>Port jaringan terdiri dari 2 Byte (16 bit) yang dihitung dengan: $\\text{Port} = (B_{\\text{high}} \\times 256) + B_{\\text{low}}$.</p>\n            </div>\n            ",
            "pro_tip": "Alamat IP `7F.00.00.01` dalam heksadesimal adalah alamat localhost legendaris `127.0.0.1` (Home loopback address komputer lokal)!",
            "pitfall": "Pada port 16-bit (2 Byte), Byte pertama dikalikan 256 ($16^2$), bukan dikalikan 16!",
            "fun_fact": "Setiap detik, seluruh infrastruktur internet dunia memproses lebih dari 100 triliun konversi biner-ke-heksadesimal ini untuk mengirimkan video YouTube, pesan WhatsApp, dan transaksi perbankan tanpa henti.",
            "formula": "\\text{IPv4: } (H_1)_{10} \\ . \\ (H_2)_{10} \\ . \\ (H_3)_{10} \\ . \\ (H_4)_{10} \\quad ; \\quad \\text{Port} = (d_3 \\cdot 16^3) + (d_2 \\cdot 16^2) + (d_1 \\cdot 16^1) + d_0",
            "formula_params": [
                [
                    "H_1 - H_4",
                    "Empat oktet byte heksadesimal alamat IP."
                ],
                [
                    "Port",
                    "Nomor port layanan jaringan 16-bit."
                ]
            ],
            "formula_intuition": "Merekonsiliasi stream data biner mesin menjadi alamat jaringan yang dapat diatur oleh administrator sistem.",
            "example": {
                "question": "Diberikan byte mentah header jaringan: Alamat IP = `7F 00 00 01` dan Port = `1F 90`. Dekodekan paket tersebut menjadi Alamat IP desimal bertitik dan nomor Port desimal!",
                "known": "IP Hex = 7F 00 00 01, Port Hex = 1F90.",
                "asked": "Alamat IP desimal dan Nomor Port desimal.",
                "steps": [
                    [
                        "Langkah 1: Dekode Byte IP Pertama (7F)",
                        "$7\\text{F}_{16} = (7 \\times 16) + 15 = 112 + 15 = 127$."
                    ],
                    [
                        "Langkah 2: Dekode Byte IP Sisa (00, 00, 01)",
                        "$00_{16} = 0$, $00_{16} = 0$, $01_{16} = 1$.<br>Maka Alamat IP adalah $127.0.0.1$."
                    ],
                    [
                        "Langkah 3: Dekode Port 16-bit (1F90)",
                        "$1\\text{F}90_{16} = (1 \\times 16^3) + (15 \\times 16^2) + (9 \\times 16^1) + (0 \\times 16^0)$."
                    ],
                    [
                        "Langkah 4: Hitung Masing-Masing Perpangkatan Port",
                        "$1 \\times 4096 = 4096$.<br>$15 \\times 256 = 3840$.<br>$9 \\times 16 = 144$.<br>$0 \\times 1 = 0$."
                    ],
                    [
                        "Langkah 5: Jumlahkan Seluruh Nilai Port",
                        "$4096 + 3840 + 144 + 0 = 8080$."
                    ]
                ],
                "conclusion": "Paket data berhasil didekode: Alamat IP adalah 127.0.0.1 (Localhost) dan Port tujuan adalah 8080 (Web Server Port)."
            },
            "takeaways": [
                "Sistem bilangan adalah tulang punggung seluruh protokol komunikasi data internet dan telekomunikasi.",
                "Konversi heksadesimal memungkinkan analisis forensik jaringan komputer skala rendah (low-level).",
                "Selamat! Kamu telah menguasai seluruh kurikulum Sistem Bilangan dari logika biner hingga decoding paket jaringan modern!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE SISTEM BILANGAN: Berapakah nilai desimal dari byte heksadesimal 7F pada alamat IP di atas?",
                [
                    "127",
                    "112",
                    "128"
                ],
                0,
                "7F = (7 * 16) + 15 = 112 + 15 = 127."
            ]
        }
    ]
}
