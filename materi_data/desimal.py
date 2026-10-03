# -*- coding: utf-8 -*-
DATA = {
    "title": "Pecahan, Desimal & Persen",
    "short": "Desimal",
    "icon": "bi-percent",
    "color": "#84cc16",
    "desc": "Kuasai konversi pecahan biasa, desimal persepuluhan, persentase diskon bertingkat (30% + 10%), rasio proporsi, margin laba, dan perhitungan bunga simpanan.",
    "babs": [
        {
            "title": "Fondasi: Tiga Wajah Kuantitas Bagian dari Keseluruhan",
            "objectives": [
                "Memahami keterkaitan antara Pecahan Biasa (a/b), Pecahan Desimal (0.xx), dan Persentase (xx%).",
                "Melakukan konversi dua arah antar ketiga bentuk representasi dengan lancar.",
                "Memahami nilai tempat di belakang tanda koma (persepuluhan, perseratusan, perseribuan)."
            ],
            "hook": "Jika sebuah toko mengumumkan diskon 1/4 harga, toko kedua menawarkan potongan 0.25, dan toko ketiga memasang banner diskon 25%—manakah toko yang memberikan diskon paling besar? Jawabannya: KETIGANYA PERSIS SAMA! Pecahan, Desimal, dan Persen hanyalah tiga baju berbeda dari satu sosok kuantitas yang identik. Menguasai ketiga representasi ini adalah keterampilan literasi finansial paling fundamental dalam hidup!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrow-repeat text-primary\"></i> 1. Segitiga Emas Konversi</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Pecahan ke Desimal:</strong> Bagi pembilang dengan penyebut ($a \\div b$). Contoh: $\\frac{3}{4} = 3 \\div 4 = 0.75$.</li>\n                <li><strong>Desimal ke Persen:</strong> Kalikan dengan $100\\%$. Contoh: $0.75 \\times 100\\% = 75\\%$.</li>\n                <li><strong>Persen ke Pecahan:</strong> Jadikan berpenyebut 100 lalu sederhanakan. Contoh: $75\\% = \\frac{75}{100} = \\frac{3}{4}$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Hafalkan pasangan pecahan desimal populer: 1/2 = 0.5 (50%), 1/4 = 0.25 (25%), 3/4 = 0.75 (75%), 1/5 = 0.2 (20%), 1/8 = 0.125 (12.5%)!",
            "pitfall": "Jangan keliru meletakkan angka nol: $5\\% = 0.05$, BUKAN $0.5$ ($0.5$ adalah $50\\%$)!",
            "fun_fact": "Kata 'Persen' berasal dari bahasa Latin 'Per Centum' yang berarti 'per seratus', digunakan oleh pedagang Romawi kuno untuk memungut pajak perdagangan lelang.",
            "formula": "\\frac{a}{b} \\xrightarrow{\\div} \\text{Desimal } (0.x) \\xrightarrow{\\times 100\\%} \\text{Persen } (P\\%)",
            "formula_params": [
                [
                    "a/b",
                    "Format pecahan biasa murni."
                ],
                [
                    "0.x",
                    "Format notasi desimal."
                ],
                [
                    "P%",
                    "Format persentil perseratus."
                ]
            ],
            "formula_intuition": "Menyajikan perbandingan proporsi dalam skala satuan 1 atau skala perseratus 100.",
            "example": {
                "question": "Ubahlah pecahan $3/8$ menjadi: (a) Bentuk desimal, dan (b) Bentuk persen!",
                "known": "Pecahan biasa 3/8.",
                "asked": "Desimal dan persentase.",
                "steps": [
                    [
                        "Langkah 1: Bagi 3 dengan 8 untuk Bentuk Desimal",
                        "$3 \\div 8 = 0.375$."
                    ],
                    [
                        "Langkah 2: Kalikan dengan 100% untuk Bentuk Persen",
                        "$0.375 \\times 100\\% = 37.5\\%$ (atau $37\\frac{1}{2}\\%$)."
                    ]
                ],
                "conclusion": "Pecahan 3/8 setara dengan desimal 0.375 dan persentase 37.5%."
            },
            "takeaways": [
                "Pecahan, desimal, dan persen adalah tiga bentuk berbeda untuk menyatakan kuantitas rasional.",
                "Mengubah desimal ke persen cukup menggeser tanda koma dua langkah ke kanan.",
                "Persen selalu mengacu pada basis pembanding perseratus (per centum)."
            ],
            "quiz": [
                "Berapakah bentuk persen dari pecahan 4/5?",
                [
                    "80%",
                    "75%",
                    "85%"
                ],
                0,
                "(4/5) * 100% = 400 / 5 = 80%."
            ]
        },
        {
            "title": "Anatomi: Nilai Tempat Desimal & Operasi Aritmetika Koma",
            "objectives": [
                "Memahami nilai tempat desimal: Persepuluhan (0.1), Perseratusan (0.01), Perseribuan (0.001).",
                "Melakukan penjumlahan dan pengurangan desimal dengan meluruskan tanda koma vertikal.",
                "Melakukan perkalian dan pembagian desimal dengan menghitung total akumulasi digit di belakang koma."
            ],
            "hook": "Mengapa dalam perkalian desimal 0.2 * 0.3 hasilnya bukan 0.6 melainkan 0.06? Karena kita sedang mengalikan 2 persepuluh dengan 3 persepuluh: (2/10) * (3/10) = 6/100 = 0.06 (enam perseratus)! Kecerobohan penempatan tanda koma desimal adalah kesalahan paling fatal yang sering memicu kerugian jutaan dolar di bursa saham!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-dot text-primary\"></i> Aturan Operasi Desimal</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Penjumlahan & Pengurangan:</strong> Tanda koma desimal <strong>WAJIB DILURUSKAN SECARA VERTIKAL</strong> sejajar ke bawah.</li>\n                <li><strong>Perkalian Desimal:</strong> Kalikan angka seperti bilangan bulat biasa tanpa memedulikan koma, lalu letakkan tanda koma di akhir dengan jumlah digit desimal = <strong>total jumlah digit desimal kedua bilangan</strong>.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk pembagian desimal seperti $12 \\div 0.04$: Geser koma pembagi ke kanan 2 kali agar menjadi bilangan bulat 4, dan lakukan pergeseran yang sama pada angka 12 menjadi 1200. $1200 \\div 4 = 300$. Sangat mudah!",
            "pitfall": "Jangan meluruskan ujung angka saat menjumlahkan desimal! Luruskan TANDA KOMA, bukan digit paling kanannya!",
            "fun_fact": "Penggunaan titik dan koma desimal berbeda di tiap negara: Indonesia dan sebagian besar Eropa menggunakan koma (3,14), sedangkan Amerika dan Inggris menggunakan titik (3.14).",
            "formula": "(0.a) \\times (0.b) = \\frac{a \\times b}{100} = 0.0(ab)",
            "formula_params": [
                [
                    "0.a",
                    "Bilangan 1 digit desimal."
                ],
                [
                    "0.b",
                    "Bilangan 1 digit desimal."
                ],
                [
                    "100",
                    "Penyebut akumulasi 2 digit desimal."
                ]
            ],
            "formula_intuition": "Mengakumulasikan jumlah posisi nilai tempat pembagi perpangkatan sepuluh.",
            "example": {
                "question": "Hitunglah hasil dari: (a) $14.5 + 3.25 - 0.725$, dan (b) $0.4 \\times 0.25$!",
                "known": "Operasi penjumlahan, pengurangan, dan perkalian desimal.",
                "asked": "Hasil perhitungan tepat.",
                "steps": [
                    [
                        "Langkah 1: Penjumlahan dengan Meluruskan Koma",
                        "$14.500 + 3.250 = 17.750$."
                    ],
                    [
                        "Langkah 2: Pengurangan Sejajar",
                        "$17.750 - 0.725 = 17.025$."
                    ],
                    [
                        "Langkah 3: Perkalian Desimal",
                        "Kalikan angka murni: $4 \\times 25 = 100$.<br>Hitung jumlah digit di belakang koma: 0.4 (1 digit) dan 0.25 (2 digit) = total 3 digit desimal.<br>Maka geser koma 3 langkah dari 100: $0.100 = 0.10$."
                    ]
                ],
                "conclusion": "Hasil berturut-turut: (a) 17.025 dan (b) 0.10."
            },
            "takeaways": [
                "Penjumlahan desimal mensyaratkan tanda koma vertikal harus lurus sejajar.",
                "Perkalian desimal mengakumulasikan total jumlah digit di belakang koma.",
                "Pembagian desimal disederhanakan dengan mengalikan kelipatan 10 pada pembilang dan penyebut."
            ],
            "quiz": [
                "Berapakah hasil dari 0.03 * 0.2?",
                [
                    "0.006",
                    "0.06",
                    "0.6"
                ],
                0,
                "3 * 2 = 6. Total digit di belakang koma adalah 2 + 1 = 3 digit. Maka hasilnya 0.006."
            ]
        },
        {
            "title": "Mekanika: Jebakan Logika Diskon Bertingkat (30% + 10%)",
            "objectives": [
                "Membongkar miskonsepsi diskon bertingkat: mengapa diskon 30% + 10% BUKAN sama dengan diskon 40%.",
                "Menghitung faktor pengali bayar sekuensial: (1 - d1) * (1 - d2).",
                "Menghitung diskon efektif riil yang diterima konsumen."
            ],
            "hook": "Sebuah department store memajang spanduk raksasa promo akhir tahun: 'DISKON 50% + 20%!'. Pelanggan yang naif bersorak gembira mengira mereka mendapatkan diskon 70% dan hanya perlu membayar 30% harga barang. Betapa terkejutnya mereka di kasir saat harus membayar 40% dari harga barang! Mengapa bisa demikian? Ke mana hilangnya 10% diskon tersebut? Inilah rahasia matematika di balik strategi diskon bertingkat dunia ritel!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-tag-fill text-primary\"></i> 1. Anatomi Perhitungan Diskon Bertingkat</h3>\n              <p>Diskon bertingkat $d_1 + d_2$ diaplikasikan <strong>SECARA BERURUTAN</strong>, bukan dijumlahkan:</p>\n              <ol class=\"dic-list\">\n                <li>Diskon pertama $d_1$ memotong dari <strong>100% Harga Awal Pokok</strong>. Sisa yang harus dibayar adalah $(1 - d_1) \\times \\text{Harga Awal}$.</li>\n                <li>Diskon kedua $d_2$ HANYA MEMOTONG dari <strong>Sisa Harga Setelah Diskon Pertama</strong>, BUKAN dari harga awal!</li>\n              </ol>\n              \\[ \\text{Faktor Bayar Bersih} = (1 - d_1) \\times (1 - d_2) \\]\n              \\[ \\text{Diskon Efektif Riil} = 1 - [(1 - d_1) \\times (1 - d_2)] \\]\n            </div>\n            ",
            "pro_tip": "Jalan pintas menghitung diskon 30% + 10%: Bayar = 70% * 90% = 63% dari harga label! Maka diskon riilnya adalah 100% - 63% = 37% (bukan 40%)!",
            "pitfall": "Jangan pernah menjumlahkan angka persentase diskon bertingkat secara langsung! Promo 50% + 50% BUKAN berarti barangnya gratis 100%, melainkan kamu tetap harus membayar $0.50 \\times 0.50 = 25\\%$ dari harga label!",
            "fun_fact": "Strategi diskon bertingkat diciptakan oleh psikolog perilaku konsumen karena otak manusia secara intuitif tergiur melihat dua angka besar berjejer meskipun potongan harga aslinya lebih sedikit daripada diskon tunggal setara.",
            "formula": "\\text{Harga Bayar} = P \\times (1 - d_1) \\times (1 - d_2) \\quad ; \\quad d_{\\text{efektif}} = d_1 + d_2 - (d_1 \\times d_2)",
            "formula_params": [
                [
                    "P",
                    "Harga label barang sebelum diskon."
                ],
                [
                    "d_1, d_2",
                    "Persentase diskon pertama dan kedua (desimal)."
                ],
                [
                    "d_{\\text{efektif}}",
                    "Diskon riil sesungguhnya."
                ]
            ],
            "formula_intuition": "Mengalikan sisa persentase pembayaran secara bertahap.",
            "example": {
                "question": "Sebuah jaket musim dingin berlabel harga Rp 200.000 mendapatkan promo diskon bertingkat 30% + 10%. Hitunglah: (a) Berapa rupiah uang yang harus dibayar di kasir, dan (b) Berapakah persentase diskon efektif sesungguhnya!",
                "known": "$P = 200.000$, $d_1 = 30\\% = 0.30$, $d_2 = 10\\% = 0.10$.",
                "asked": "Harga bayar dan diskon efektif.",
                "steps": [
                    [
                        "Langkah 1: Hitung Sisa Harga Setelah Diskon Pertama 30%",
                        "Sisa 1 = $200.000 \\times (1 - 0.30) = 200.000 \\times 0.70 = 140.000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 2: Terapkan Diskon Kedua 10% pada Sisa Rp 140.000",
                        "Potongan diskon 2 = $10\\% \\times 140.000 = 14.000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 3: Hitung Harga Bayar Akhir Kasir",
                        "Harga bayar = $140.000 - 14.000 = 126.000\\text{ rupiah}$.<br>Atau dengan rumus cepat: $200.000 \\times 0.70 \\times 0.90 = 126.000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 4: Hitung Persentase Diskon Efektif",
                        "Total potongan = $200.000 - 126.000 = 74.000\\text{ rupiah}$.<br>$\\text{Diskon Efektif} = \\frac{74.000}{200.000} \\times 100\\% = 37\\%$ (Bukan 40%!)."
                    ]
                ],
                "conclusion": "Konsumen harus membayar Rp 126.000 di kasir, dan diskon efektif riil yang dinikmati adalah 37%."
            },
            "takeaways": [
                "Diskon bertingkat tidak dapat dijumlahkan secara langsung.",
                "Diskon kedua hanya memotong dari sisa harga setelah diskon pertama.",
                "Promo 30% + 10% setara dengan diskon tunggal 37%."
            ],
            "quiz": [
                "Sebuah barang seharga Rp 100.000 mendapat promo diskon 50% + 50%. Berapakah yang harus dibayar pembeli di kasir?",
                [
                    "Rp 25.000",
                    "Rp 0 (Gratis)",
                    "Rp 50.000"
                ],
                0,
                "Bayar = 100.000 * 0.50 * 0.50 = Rp 25.000 (diskon efektif 75%, bukan 100% gratis)."
            ]
        },
        {
            "title": "Pemodelan: Margin Keuntungan Finansial & Mark-up Penjualan",
            "objectives": [
                "Membedakan Margin Laba (Profit Margin berbasis Harga Jual) dan Mark-up (berbasis Harga Modal Beli).",
                "Menghitung harga jual yang tepat untuk mencapai target margin keuntungan persentil tertentu.",
                "Menganalisis dampak diskon promosi terhadap margin keuntungan bersih bisnis."
            ],
            "hook": "Banyak pengusaha pemula bangkrut karena kesalahan fatal membedakan antara 'Mark-up' dan 'Margin Laba'. Jika kamu membeli barang modal Rp 100.000 dan menaikkan harga sebesar 25% menjadi Rp 125.000, apakah margin keuntunganmu 25%? SALAH! Keuntunganmu adalah Rp 25.000 dari harga jual Rp 125.000, yang artinya margin labamu HANYA 20%! Memahami persentase modal vs harga jual adalah pondasi kelangsungan bisnis UMKM dan startup modern.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-cash-coin text-primary\"></i> Mark-up vs Margin Laba</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Mark-up (%):</strong> Persentase kenaikan harga yang ditambahkan ke Harga Pokok Penjualan (HPP):\n                  \\[ \\text{Mark-up} = \\frac{\\text{Laba}}{\\text{Modal HPP}} \\times 100\\% \\]\n                </li>\n                <li><strong>Profit Margin (%):</strong> Persentase keuntungan bersih dari total omset Harga Jual:\n                  \\[ \\text{Margin} = \\frac{\\text{Laba}}{\\text{Harga Jual}} \\times 100\\% \\]\n                </li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk menentukan harga jual dengan target margin laba m%: Gunakan rumus $P_{\\text{jual}} = \\frac{\\text{HPP}}{1 - m}$, jangan mengalikan HPP dengan (1 + m)!",
            "pitfall": "Nilai Margin Laba tidak pernah bisa mencapai 100% (karena HPP selalu lebih besar dari 0), sedangkan nilai Mark-up bisa mencapai ratusan persen!",
            "fun_fact": "Restoran cepat saji dan bioskop memiliki mark-up minuman soda dan popcorn hingga lebih dari 1.000% (modal Rp 2.000 dijual Rp 25.000) untuk menutupi biaya operasional sewa gedung mall.",
            "formula": "\\text{Harga Jual} = \\frac{\\text{HPP}}{1 - \\text{Margin}} \\quad ; \\quad \\text{Margin} = \\frac{P_{\\text{jual}} - \\text{HPP}}{P_{\\text{jual}}} \\times 100\\%",
            "formula_params": [
                [
                    "HPP",
                    "Harga Pokok Penjualan / modal dasar produksi."
                ],
                [
                    "P_{\\text{jual}}",
                    "Harga banderol jual konsumen."
                ],
                [
                    "Margin",
                    "Rasio laba terhadap harga jual (desimal)."
                ]
            ],
            "formula_intuition": "Menghitung proporsi keuntungan dari setiap satu rupiah uang yang dibayarkan konsumen.",
            "example": {
                "question": "Seorang pemilik kedai kopi memiliki modal biaya produksi HPP satu gelas kopi sebesar Rp 15.000. Jika ia menargetkan Margin Laba bersih sebesar 25% (0.25), berapakah harga jual per gelas kopi yang harus dipasang di daftar menu?",
                "known": "$\\text{HPP} = 15.000$, target $\\text{Margin} = 25\\% = 0.25$.",
                "asked": "Harga Jual $P_{\\text{jual}}$.",
                "steps": [
                    [
                        "Langkah 1: Gunakan Rumus Penetapan Harga Jual Berbasis Margin",
                        "$P_{\\text{jual}} = \\frac{\\text{HPP}}{1 - \\text{Margin}} = \\frac{15000}{1 - 0.25}$."
                    ],
                    [
                        "Langkah 2: Hitung Penyebut",
                        "$1 - 0.25 = 0.75$."
                    ],
                    [
                        "Langkah 3: Bagi Modal dengan 0.75",
                        "$P_{\\text{jual}} = \\frac{15000}{0.75} = \\frac{15000}{\\frac{3}{4}} = 15000 \\times \\frac{4}{3} = 20.000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 4: Verifikasi Margin",
                        "Laba = $20.000 - 15.000 = 5.000$.<br>Margin = $\\frac{5000}{20000} \\times 100\\% = 25\\%$ (Tepat dan Akurat!)."
                    ]
                ],
                "conclusion": "Harga jual kopi yang harus dipasang di menu adalah Rp 20.000 per gelas."
            },
            "takeaways": [
                "Mark-up dihitung berbasis modal HPP, sedangkan Margin laba dihitung berbasis harga jual akhir.",
                "Rumus penetapan harga target margin adalah $\\text{HPP} / (1 - \\text{margin})$.",
                "Ketepatan kalkulasi persentase melindungi pelaku usaha dari kerugian tersembunyi."
            ],
            "quiz": [
                "Sebuah barang dibeli dengan modal Rp 80.000 dan dijual seharga Rp 100.000. Berapakah Margin Laba penjualan barang tersebut?",
                [
                    "20%",
                    "25%",
                    "15%"
                ],
                0,
                "Laba = 100.000 - 80.000 = 20.000. Margin = 20.000 / 100.000 * 100% = 20%."
            ]
        },
        {
            "title": "Capstone: Laporan Rekonsiliasi Neraca Finansial Bisnis E-Commerce",
            "objectives": [
                "Mengintegrasikan desimal, persentase diskon bertingkat, komisi platform, dan pajak PPN dalam laporan keuangan e-commerce.",
                "Menghitung pendapatan bersih (Net Payout) penjual online setelah dipotong biaya promosi dan biaya layanan.",
                "Mengevaluasi profitabilitas operasional toko digital secara komprehensif."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Financial Officer (CFO) sebuah brand pakaian yang berjualan di marketplace e-commerce. Dalam kampanye festival belanja 11.11, toko mencatatkan total omset kotor Rp 500.000.000. Namun marketplace mengenakan potongan komisi layanan 4%, promo voucher subsidi toko 5%, dan biaya pemrosesan pembayaran 1.5%. Menggunakan kalkulasi presisi pecahan desimal dan persen, susunlah rekonsiliasi keuangan bersih yang benar-benar masuk ke rekening kas perusahaan!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Rekonsiliasi Keuangan Marketplace</h3>\n              <p>Struktur pembagian omset e-commerce:</p>\n              \\[ \\text{Net Payout} = \\text{Omset Kotor} \\times (1 - \\text{Biaya Layanan} - \\text{Subsidi Voucher} - \\text{Biaya Payment}) \\]\n            </div>\n            ",
            "pro_tip": "Dalam akuntansi e-commerce skala besar, selalu hitung desimal hingga 4 angka di belakang koma untuk menghindari selisih pembulatan sen uang!",
            "pitfall": "Pastikan biaya persentase marketplace dihitung dari omset kotor ataukah dari nilai setelah subsidi voucher sesuai ketentuan kontrak penjual!",
            "fun_fact": "Sistem kliring perbankan global (seperti SWIFT dan Bank Indonesia) menggunakan pembulatan Banker's Rounding (Round to Even) untuk mencegah bias inflasi akumulasi desimal pecahan sen.",
            "formula": "\\text{Dana Bersih} = \\text{Omset} \\times \\left(1 - \\sum \\text{Fee}_{\\%} \\right)",
            "formula_params": [
                [
                    "Omset",
                    "Total nilai transaksi bruto penjualan."
                ],
                [
                    "\\sum \\text{Fee}_{\\%}",
                    "Akumulasi seluruh persentase potongan layanan."
                ]
            ],
            "formula_intuition": "Mengurangkan potongan komisi secara serentak dari total pendapatan kotor.",
            "example": {
                "question": "Sebuah toko online membukukan omset kotor Rp 100.000.000. Potongan marketplace meliputi: Komisi Layanan 4% (0.04), Voucher Diskon Toko 5% (0.05), dan Biaya Gateway Pembayaran 1.5% (0.015). Hitunglah: (a) Total persentase potongan biaya, (b) Jumlah nominal rupiah seluruh potongan, dan (c) Dana bersih yang diterima penjual!",
                "known": "Omset = Rp 100.000.000. Potongan: 4%, 5%, 1.5%.",
                "asked": "Total % fee, total potongan nominal, dan dana bersih.",
                "steps": [
                    [
                        "Langkah 1: Akumulasikan Persentase Seluruh Biaya Potongan",
                        "Total fee = $4\\% + 5\\% + 1.5\\% = 10.5\\% = 0.105$."
                    ],
                    [
                        "Langkah 2: Hitung Total Nominal Rupiah Potongan",
                        "Potongan = $100.000.000 \\times 0.105 = 10.500.000\\text{ rupiah}$."
                    ],
                    [
                        "Langkah 3: Hitung Dana Bersih (Net Payout)",
                        "Dana bersih = $100.000.000 - 10.500.000 = 89.500.000\\text{ rupiah}$.<br>Atau: $100.000.000 \\times (1 - 0.105) = 100.000.000 \\times 0.895 = 89.500.000$ rupiah."
                    ]
                ],
                "conclusion": "Total potongan biaya adalah 10.5% (Rp 10.500.000) dan dana bersih yang berhasil dicairkan ke rekening penjual adalah Rp 89.500.000."
            },
            "takeaways": [
                "Persentase komisi dan diskon diakumulasikan untuk menghitung potongan netto akhir.",
                "Ketelitian konversi desimal menjamin keakuratan laporan keuangan bisnis digital.",
                "Selamat! Kamu telah menyelesaikan seluruh kurikulum Pecahan, Desimal & Persen dengan pemahaman praktis kelas satu!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE DESIMAL: Jika total akumulasi fee potongan marketplace adalah 10.5%, berapa persenkah dana bersih yang diterima penjual dari total omsetnya?",
                [
                    "89.5%",
                    "90.5%",
                    "88.5%"
                ],
                0,
                "Dana bersih = 100% - 10.5% = 89.5%."
            ]
        }
    ]
}
