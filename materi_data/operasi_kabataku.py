# -*- coding: utf-8 -*-
DATA = {
    "title": "Operasi Ka-Ba-Ta-Ku & Hierarki",
    "short": "KaBaTaKu",
    "icon": "bi-slash-circle",
    "color": "#64748b",
    "desc": "Kuasai hierarki urutan operasi matematika KaBaTaKu / PEMDAS, evaluasi tanda kurung, operasi bilangan negatif, pohon sintaks, dan eliminasi ambiguitas kalkulasi.",
    "babs": [
        {
            "title": "Fondasi: Mengapa Hierarki Urutan Operasi Diperlukan?",
            "objectives": [
                "Memahami mengapa ekspresi matematika membutuhkan konvensi urutan operasi universal.",
                "Mengenali ambiguitas yang terjadi jika kalkulasi dilakukan dari kiri ke kanan secara membabi buta.",
                "Memahami hakikat perkalian sebagai penjumlahan berulang yang mengikat lebih kuat."
            ],
            "hook": "Berapakah hasil dari 2 + 3 * 4? Jika kamu menghitungnya dari kiri ke kanan (2 + 3 = 5, lalu 5 * 4 = 20), kamu SALAH BESAR! Hasil yang benar adalah 14! Mengapa? Karena perkalian adalah bentuk ringkas dari penjumlahan berulang: 3 * 4 bermakna (4 + 4 + 4). Maka 2 + 3 * 4 bermakna 2 + (4 + 4 + 4) = 14. Tanpa aturan hierarki KaBaTaKu, seluruh kalkulator, kode program perbankan, dan roket antariksa akan mengalami kekacauan kalkulasi numerik!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-shield-check text-primary\"></i> 1. Menghilangkan Ambiguitas Matematika</h3>\n              <p>Bahasa matematika adalah bahasa universal yang tidak boleh memiliki makna ganda (ambigu). Konvensi hierarki operasi menetapkan urutan kasta prioritas eksekusi operator agar siapa pun di seluruh belahan dunia selalu memperoleh hasil akhir yang identik.</p>\n            </div>\n            ",
            "pro_tip": "Di Indonesia aturan ini disingkat Ka-Ba-Ta-Ku (Kali, Bagi, Tambah, Kurang). Di standar internasional disingkat PEMDAS: Parentheses (Kurung), Exponents (Pangkat), Multiplication & Division (Kali/Bagi), Addition & Subtraction (Tambah/Kurang)!",
            "pitfall": "Jangan mengira perkalian SELALU didahulukan dibanding pembagian! Perkalian dan Pembagian memiliki KASTA KEKUATAN YANG SETARA: jika keduanya muncul bersamaan, selesaikan secara berurutan dari KIRI KE KANAN!",
            "fun_fact": "Kalkulator pertama di dunia yang diciptakan Blaise Pascal tahun 1642 (Pascaline) hanya bisa melakukan penjumlahan dan pengurangan mekanis roda gerigi. Konvensi urutan operasi KaBaTaKu baru diformalkan secara global di awal abad ke-20 seiring lahirnya industri komputer modern.",
            "formula": "\\text{Hierarki: } \\text{Tanda Kurung } () \\ > \\ \\text{Pangkat/Akar } x^n \\ > \\ \\text{Kali/Bagi } (\\times, \\div) \\ > \\ \\text{Tambah/Kurang } (+, -)",
            "formula_params": [
                [
                    "()",
                    "Kasta Tertinggi: Tanda kurung memaksa eksekusi terlebih dahulu."
                ],
                [
                    "\\times, \\div",
                    "Kasta Menengah: Perkalian dan pembagian setara dari kiri ke kanan."
                ],
                [
                    "+ , -",
                    "Kasta Dasar: Penjumlahan dan pengurangan dieksekusi terakhir."
                ]
            ],
            "formula_intuition": "Operator dengan ikatan multiplikatif dihitung terlebih dahulu sebelum operator penambahan linier.",
            "example": {
                "question": "Hitunglah hasil yang benar dari ekspresi aritmetika berikut: $15 + 5 \\times 4 - 18 \\div 3$!",
                "known": "Ekspresi memuat operasi tambah, kali, kurang, dan bagi.",
                "asked": "Hasil evaluasi sesuai hierarki KaBaTaKu.",
                "steps": [
                    [
                        "Langkah 1: Identifikasi dan Dahulukan Perkalian dan Pembagian",
                        "$5 \\times 4 = 20$.<br>$18 \\div 3 = 6$."
                    ],
                    [
                        "Langkah 2: Tuliskan Ulang Ekspresi dengan Hasil Kali/Bagi",
                        "$15 + 20 - 6$."
                    ],
                    [
                        "Langkah 3: Selesaikan Penjumlahan dan Pengurangan dari Kiri ke Kanan",
                        "$15 + 20 = 35$.<br>$35 - 6 = 29$."
                    ]
                ],
                "conclusion": "Hasil yang benar dari ekspresi tersebut adalah 29."
            },
            "takeaways": [
                "Hierarki KaBaTaKu menghilangkan ambiguitas penafsiran ekspresi matematika.",
                "Perkalian dan pembagian selalu didahulukan dibanding penjumlahan dan pengurangan.",
                "Operator yang setara dievaluasi berurutan dari arah kiri ke kanan."
            ],
            "quiz": [
                "Berapakah hasil dari 10 + 2 * 6?",
                [
                    "22",
                    "72",
                    "32"
                ],
                0,
                "Dahulukan perkalian: 2 * 6 = 12. Lalu jumlahkan: 10 + 12 = 22."
            ]
        },
        {
            "title": "Anatomi: Kuasa Tanda Kurung & Pohon Sintaks Evaluasi",
            "objectives": [
                "Menguasai fungsi tanda kurung (Parentheses) sebagai 'Kasta Tertinggi' yang mengesampingkan hierarki dasar.",
                "Mengevaluasi tanda kurung bersarang (Nested Brackets): Kurung Biasa (), Kurung Kurawal {}, dan Kurung Siku [].",
                "Memahami pohon sintaks ekspresi (Expression Tree) yang digunakan oleh compiler komputer."
            ],
            "hook": "Jika perkalian lebih kuat daripada penjumlahan, bagaimana jika seorang apoteker ingin meracik obat di mana dosis (A + B) wajib dicampurkan dulu sebelum dikalikan dengan faktor berat pasien? Di sinilah tanda kurung bertindak sebagai PENGUASA MUTLAK: tanda kurung memiliki hak veto untuk memaksa operasi apa pun di dalamnya dieksekusi nomor satu mengalahkan operator apa pun di luar!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-parentheses text-primary\"></i> 1. Hak Veto Tanda Kurung</h3>\n              <p>Tanda kurung memaksa urutan evaluasi lokal terlebih dahulu. Bandingkan:</p>\n              \\[ 10 + 4 \\times 2 = 10 + 8 = 18 \\quad \\text{vs} \\quad (10 + 4) \\times 2 = 14 \\times 2 = 28 \\]\n              <h4 class=\"fw-bold text-info mt-3\"><i class=\"bi bi-diagram-3\"></i> Aturan Kurung Bersarang (Nested):</h4>\n              <p>Selesaikan dari <strong>Tanda Kurung Paling Dalam</strong> bergerak keluar secara bertahap:</p>\n              \\[ [ \\ \\{ \\ ( \\ \\dots \\ ) \\ \\} \\ ] \\]\n            </div>\n            ",
            "pro_tip": "Saat menyusun rumus di Microsoft Excel atau Google Sheets, selalu pasang tanda kurung secara eksplisit jika kamu ingin penjumlahan didahulukan sebelum perkalian, contoh: `=(A1 + B1) * C1`!",
            "pitfall": "Pastikan setiap kurung buka `(` selalu memiliki pasangan kurung tutup `)` yang sesuai! Kurung yang tidak seimbang (Unbalanced Parentheses) adalah penyebab paling sering terjadinya error program di seluruh dunia.",
            "fun_fact": "Bahasa pemrograman legendaris LISP (salah satu bahasa pemrograman kecerdasan buatan tertua tahun 1958) dibangun hampir seluruhnya menggunakan ribuan tanda kurung bersarang, sehingga programmer sering bercanda bahwa LISP adalah singkatan dari 'Lost In Stupid Parentheses'.",
            "formula": "(A + B) \\times C \\neq A + (B \\times C) \\quad ; \\quad \\text{Prioritas: } [ \\ \\{ \\ ( \\ \\text{Terdalam} \\ ) \\ \\} \\ ]",
            "formula_params": [
                [
                    "()",
                    "Kurung biasa (level 1)."
                ],
                [
                    "{}",
                    "Kurung kurawal (level 2)."
                ],
                [
                    "[]",
                    "Kurung siku (level 3)."
                ]
            ],
            "formula_intuition": "Mengisolasi blok operasi menjadi satu paket nilai mandiri sebelum berinteraksi dengan luar.",
            "example": {
                "question": "Hitunglah nilai dari ekspresi bertingkat dengan kurung bersarang berikut: $50 - 2 \\times [ 14 - (3 + 5) ]$!",
                "known": "Terdapat kurung siku luar dan kurung biasa di bagian dalam.",
                "asked": "Hasil evaluasi numerik.",
                "steps": [
                    [
                        "Langkah 1: Selesaikan Kurung Paling Dalam $(3 + 5)$",
                        "$3 + 5 = 8$."
                    ],
                    [
                        "Langkah 2: Selesaikan Isi Kurung Siku $[14 - 8]$",
                        "$14 - 8 = 6$."
                    ],
                    [
                        "Langkah 3: Tuliskan Ekspresi yang Tersisa",
                        "$50 - 2 \\times 6$."
                    ],
                    [
                        "Langkah 4: Dahulukan Perkalian dibanding Pengurangan",
                        "$2 \\times 6 = 12$."
                    ],
                    [
                        "Langkah 5: Kurangkan",
                        "$50 - 12 = 38$."
                    ]
                ],
                "conclusion": "Hasil akhir ekspresi bertingkat tersebut adalah 38."
            },
            "takeaways": [
                "Tanda kurung adalah prioritas kasta tertinggi yang membatalkan urutan operasi biasa.",
                "Kurung bersarang diselesaikan secara bertahap dari kurung terdalam menuju keluar.",
                "Tanda kurung menjamin logika komputasi tereksekusi tanpa kesalahan interpretasi."
            ],
            "quiz": [
                "Berapakah hasil dari (12 - 4) * (2 + 3)?",
                [
                    "40",
                    "22",
                    "60"
                ],
                0,
                "(12 - 4) = 8, dan (2 + 3) = 5. Maka 8 * 5 = 40."
            ]
        },
        {
            "title": "Mekanika: Aritmetika Bilangan Negatif & Distribusi Tanda",
            "objectives": [
                "Menguasai perkalian dan pembagian tanda: (+) * (+) = (+), (-) * (-) = (+), dan beda tanda menghasilkan (-).",
                "Memahami pengurangan bilangan negatif sebagai operasi penjumlahan berlawanan (a - (-b) = a + b).",
                "Menerapkan sifat distributif tanda negatif terhadap isi tanda kurung: -(a - b) = -a + b."
            ],
            "hook": "Mengapa dalam matematika 'Minus dikali Minus hasilnya adalah Plus'? Mengapa utang dikurangi utang justru membuat kita bertambah kaya? Secara filosofis dan logika formal: 'Menghapuskan (Minus) sebuah Kesalahan/Utang (Minus) adalah sebuah Kebaikan (Plus)'. Memahami mekanika tanda negatif melatih ketelitian aljabar tingkat tinggi yang bebas dari kecerobohan.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-plus-slash-minus text-primary\"></i> 1. Hukum Perkalian & Pembagian Tanda</h3>\n              <ul class=\"dic-list\">\n                <li>$(+) \\times (+) = (+)$ dan $(-) \\times (-) = (+)$ (Tanda sama selalu menghasilkan <strong>POSITIF</strong>).</li>\n                <li>$(+) \\times (-) = (-)$ dan $(-) \\times (+) = (-)$ (Tanda berbeda selalu menghasilkan <strong>NEGATIF</strong>).</li>\n                <li>Aturan yang sama berlaku persis pada operasi pembagian: $\\frac{-a}{-b} = +\\frac{a}{b}$.</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-distribute-vertical text-primary\"></i> 2. Pengurangan Tanda Negatif</h3>\n              <p>Mengurangkan bilangan negatif ekuivalen dengan menjumlahkan lawannya:</p>\n              \\[ a - (-b) = a + b \\]\n            </div>\n            ",
            "pro_tip": "Untuk menghitung rentang suhu (misal dari -5°C ke 25°C): Selalu gunakan rumus Selisih = Suhu Akhir - Suhu Awal = 25 - (-5) = 25 + 5 = 30°C kenaikan!",
            "pitfall": "Jangan lupakan distributif tanda minus ke seluruh anggota kurung! $-(3x - 5)$ menjadi $-3x + 5$, BUKAN $-3x - 5$!",
            "fun_fact": "Konsep bilangan negatif pertama kali diperlakukan secara terhormat oleh matematikawan India Brahmagupta pada abad ke-7 Masehi, yang menyebut bilangan negatif sebagai 'utang' (debt) dan bilangan positif sebagai 'kekayaan' (fortune).",
            "formula": "(-a) \\times (-b) = +ab \\quad ; \\quad a - (-b) = a + b \\quad ; \\quad -(a - b) = -a + b",
            "formula_params": [
                [
                    "a, b",
                    "Bilangan riil."
                ]
            ],
            "formula_intuition": "Dua pembalikan arah 180° menghasilkan kembalinya arah ke orientasi semula 360° (positif).",
            "example": {
                "question": "Hitunglah hasil dari operasi: $-12 + (-4) \\times (-3) - (-15) \\div 5$!",
                "known": "Operasi memuat bilangan negatif, perkalian, dan pembagian.",
                "asked": "Hasil akhir evaluasi numerik.",
                "steps": [
                    [
                        "Langkah 1: Selesaikan Perkalian Tanda Negatif",
                        "$(-4) \\times (-3) = +12$ (karena minus dikali minus = plus)."
                    ],
                    [
                        "Langkah 2: Selesaikan Pembagian",
                        "$(-15) \\div 5 = -3$."
                    ],
                    [
                        "Langkah 3: Tuliskan Ulang Ekspresi",
                        "$-12 + 12 - (-3)$."
                    ],
                    [
                        "Langkah 4: Evaluasi dari Kiri ke Kanan",
                        "$-12 + 12 = 0$.<br>$0 - (-3) = 0 + 3 = 3$."
                    ]
                ],
                "conclusion": "Hasil akhir dari operasi tersebut adalah 3."
            },
            "takeaways": [
                "Perkalian dan pembagian dua bilangan bertanda sama selalu menghasilkan bilangan positif.",
                "Mengurangkan bilangan negatif berubah menjadi penjumlahan positif: $a - (-b) = a + b$.",
                "Tanda negatif di depan kurung mendistribusikan pembalikan tanda ke semua suku di dalamnya."
            ],
            "quiz": [
                "Berapakah hasil dari -8 - (-10)?",
                [
                    "+2",
                    "-18",
                    "-2"
                ],
                0,
                "-8 - (-10) = -8 + 10 = +2."
            ]
        },
        {
            "title": "Pemodelan: Menyusun Ekspresi Tunggal Transaksi Finansial",
            "objectives": [
                "Menerjemahkan narasi transaksi keuangan belanja sehari-hari menjadi satu kalimat matematika KaBaTaKu tunggal.",
                "Menggunakan tanda kurung secara tepat untuk memodelkan diskon dan potongan harga.",
                "Menghitung kembalian uang kasir tanpa kesalahan aritmetika."
            ],
            "hook": "Ibu pergi ke supermarket membeli 3 kotak susu seharga Rp 15.000 per kotak, 2 bungkus biskuit seharga Rp 8.000 per bungkus dengan potongan kupon diskon Rp 3.000 untuk total belanja. Ibu membayar dengan selembar uang Rp 100.000. Berapakah uang kembalian yang diterima Ibu? Kasir modern tidak menghitung manual di kertas; mesin barcode menyusunnya menjadi satu ekspresi aritmetika tunggal: 100000 - (3 * 15000 + 2 * 8000 - 3000)!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-cart-check text-primary\"></i> Konstruksi Model Transaksi Finansial</h3>\n              <p>Struktur baku perhitungan kembalian kasir:</p>\n              \\[ \\text{Kembalian} = \\text{Uang Tunai Bayar} - \\left( \\sum (\\text{Banyak Barang} \\times \\text{Harga Satuan}) - \\text{Diskon} \\right) \\]\n            </div>\n            ",
            "pro_tip": "Gunakan tanda kurung besar untuk membungkus seluruh total belanjaan sebelum dikurangkan dari uang pembayaran agar terhindar dari salah hitung kasir!",
            "pitfall": "Jangan mengurangkan diskon dari uang tunai bayar di awal! Diskon selalu mengurangi total nilai belanja barang.",
            "fun_fact": "Bahasa pemrosesan perbankan kuno COBOL (yang masih memproses 95% transaksi geser kartu ATM dunia hari ini) mengandalkan hierarki aritmetika ketat untuk mencegah salah hitung pembagian sen dolar.",
            "formula": "\\text{Sisa} = \\text{Bayar} - \\left[ \\sum (n_i \\cdot p_i) - D \\right]",
            "formula_params": [
                [
                    "Bayar",
                    "Uang tunai yang diserahkan konsumen."
                ],
                [
                    "n_i, p_i",
                    "Jumlah dan harga masing-masing jenis barang."
                ],
                [
                    "D",
                    "Potongan voucher diskon belanja."
                ]
            ],
            "formula_intuition": "Mengurangkan uang tunai dengan total belanja bersih setelah dikurangi potongan promosi.",
            "example": {
                "question": "Budi membeli 4 buku tulis seharga Rp 5.000/buku dan 3 pulpen seharga Rp 3.000/pulpen. Toko memberikan potongan diskon Rp 4.000. Jika Budi membayar dengan selembar uang Rp 50.000, tuliskan model ekspresi tunggalnya dan hitung uang kembalian yang diterima Budi!",
                "known": "4 buku @ Rp 5.000, 3 pulpen @ Rp 3.000, diskon Rp 4.000, uang bayar Rp 50.000.",
                "asked": "Model ekspresi tunggal dan uang kembalian.",
                "steps": [
                    [
                        "Langkah 1: Susun Ekspresi KaBaTaKu Tunggal",
                        "$\\text{Kembalian} = 50000 - [ (4 \\times 5000) + (3 \\times 3000) - 4000 ]$."
                    ],
                    [
                        "Langkah 2: Hitung Perkalian di Dalam Kurung",
                        "$4 \\times 5000 = 20000$.<br>$3 \\times 3000 = 9000$."
                    ],
                    [
                        "Langkah 3: Hitung Total Belanja Bersih",
                        "$20000 + 9000 - 4000 = 29000 - 4000 = 25000$."
                    ],
                    [
                        "Langkah 4: Kurangkan dari Uang Tunai Pembayaran",
                        "$50000 - 25000 = 25000\\text{ rupiah}$."
                    ]
                ],
                "conclusion": "Uang kembalian yang diterima Budi adalah Rp 25.000."
            },
            "takeaways": [
                "Soal cerita belanja dirangkum dalam satu ekspresi tunggal menggunakan tanda kurung pelindung.",
                "Perkalian kuantitas dan harga satuan didahulukan secara otomatis oleh aturan KaBaTaKu.",
                "Total belanja bersih adalah jumlah belanja bruto dikurangi nilai voucher promosi."
            ],
            "quiz": [
                "Ekspresi manakah yang benar untuk 'Uang Rp 50.000 dikurangi belanja 2 baju seharga Rp 20.000 per potong'?",
                [
                    "50000 - (2 * 20000)",
                    "(50000 - 2) * 20000",
                    "50000 - 2 + 20000"
                ],
                0,
                "Belanja 2 baju seharga 20.000 dimodelkan dengan (2 * 20000), lalu dikurangkan dari 50.000."
            ]
        },
        {
            "title": "Capstone: Audit Logika Algoritma Kasir Ritel POS (Point of Sale)",
            "objectives": [
                "Mengintegrasikan seluruh aturan KaBaTaKu, kurung bersarang, diskon bertingkat, dan pajak pertambahan nilai (PPN 11%).",
                "Mendeteksi kesalahan logika (bug aritmetika) pada kode program software kasir Point of Sale (POS).",
                "Membuat algoritma penagihan invoice kasir yang akurat dan terverifikasi secara matematis."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Lead Software Quality Assurance (QA) pada sistem kasir jaringan supermarket waralaba terbesar nasional. Seorang programmer magang menulis rumus total tagihan invoice sebagai: Total = Subtotal - DiskonMember * Subtotal + PajakPPN. Akibat ketiadaan tanda kurung dan pelanggaran aturan KaBaTaKu, sistem menghasilkan tagihan minus miliaran rupiah saat diuji coba! Tugasmu adalah mengaudit, memperbaiki, dan menyusun formula KaBaTaKu standar industri yang anti-bocor!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-receipt-cutoff text-warning\"></i> Skenario Audit Invoice Kasir POS</h3>\n              <p>Struktur hierarki perhitungan invoice ritel berstandar akuntansi:</p>\n              <ol class=\"dic-list\">\n                <li><strong>Subtotal Belanja Bruto:</strong> $S = \\sum (\\text{qty}_i \\times \\text{harga}_i)$.</li>\n                <li><strong>Total Belanja Setelah Diskon Member ($D = 10\\%$):</strong>\n                  \\[ B = S \\times (1 - d) \\]\n                </li>\n                <li><strong>Total Tagihan Akhir Setelah Ditambah PPN 11%:</strong>\n                  \\[ \\text{Tagihan} = B \\times (1 + \\text{PPN}) = [ S \\times (1 - d) ] \\times 1.11 \\]\n                </li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Dalam rekayasa perangkat lunak, selalu gunakan tanda kurung tegas untuk mengontrol urutan operasi finansial daripada mengandalkan asumsi compiler!",
            "pitfall": "Jangan menjumlahkan diskon dan pajak secara langsung! Pajak PPN 11% dikenakan pada nilai barang SETELAH DISKON (nilai kena pajak), bukan pada harga awal kotor.",
            "fun_fact": "Pada tahun 1962, roket antariksa Mariner 1 NASA meledak 293 detik setelah peluncuran hanya karena seorang programmer melewatkan satu simbol tanda hubung (hyphen) pada rumus panduan terbang!",
            "formula": "\\text{Invoice} = \\left[ \\left( \\sum n_i p_i \\right) \\times (1 - d) \\right] \\times (1 + \\text{PPN})",
            "formula_params": [
                [
                    "n_i, p_i",
                    "Item barang dan harga satuan."
                ],
                [
                    "d",
                    "Diskon member (desimal)."
                ],
                [
                    "PPN",
                    "Pajak Pertambahan Nilai (11% = 0.11)."
                ]
            ],
            "formula_intuition": "Mengaplikasikan faktor diskon pemotong terlebih dahulu, baru kemudian mengalikan faktor pengali pajak.",
            "example": {
                "question": "Seorang pelanggan membeli 2 kemeja @ Rp 150.000 dan 1 celana @ Rp 200.000. Pelanggan mendapat diskon member 10% ($d = 0.10$). Transaksi dikenakan pajak PPN 11% ($0.11$). Hitunglah total tagihan akhir kasir yang benar!",
                "known": "Kemeja: $2 \\times 150.000 = 300.000$. Celana: $1 \\times 200.000 = 200.000$. Diskon member = 10%. PPN = 11%.",
                "asked": "Total tagihan invoice kasir yang sah.",
                "steps": [
                    [
                        "Langkah 1: Hitung Subtotal Belanja Kotor",
                        "$S = (2 \\times 150000) + (1 \\times 200000) = 300000 + 200000 = 500000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 2: Terapkan Diskon Member 10%",
                        "Faktor bayar = $1 - 0.10 = 0.90$.<br>Nilai setelah diskon: $B = 500000 \\times 0.90 = 450000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 3: Terapkan Pajak PPN 11% ke Nilai Setelah Diskon",
                        "Faktor pajak = $1 + 0.11 = 1.11$.<br>Total akhir: $450000 \\times 1.11 = 499500\\text{ rupiah}$."
                    ]
                ],
                "conclusion": "Total tagihan kasir akhir yang benar dan sah adalah Rp 499.500."
            },
            "takeaways": [
                "Hierarki tanda kurung mengamankan algoritma finansial dari celah kesalahan komputasi.",
                "Pajak PPN dihitung dari dasar pengenaan pajak (nilai setelah diskon).",
                "Selamat! Kamu telah menguasai seluruh kurikulum Operasi Ka-Ba-Ta-Ku & Hierarki Aritmatika secara sempurna!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE KABATAKU: Mengapa rumus Subtotal * (1 - 0.10) * 1.11 benar, sedangkan rumus Subtotal - 0.10 + 0.11 salah besar?",
                [
                    "Karena diskon dan pajak adalah pengali persentase proporsional, bukan konstanta aditif rupiah",
                    "Karena angka 0.10 tidak bisa dikurangkan",
                    "Karena komputer tidak mengenal pengurangan"
                ],
                0,
                "Diskon 10% dan PPN 11% adalah faktor skala proporsional terhadap nilai transaksi, bukan angka nominal 10 rupiah atau 10 sen."
            ]
        }
    ]
}
