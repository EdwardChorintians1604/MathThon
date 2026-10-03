# -*- coding: utf-8 -*-
DATA = {
    "title": "Pengenalan Aljabar & PLSV",
    "short": "Aljabar",
    "icon": "bi-calculator",
    "color": "#6366f1",
    "desc": "Kuasai dasar-dasar variabel, ekspresi aljabar, faktorisasi polinomial, persamaan linear satu variabel, dan prinsip kesetaraan neraca matematika.",
    "babs": [
        {
            "title": "Fondasi: Dari Aritmatika Konkret Menuju Abstraksi Variabel",
            "objectives": [
                "Memahami mengapa manusia membutuhkan aljabar dan simbol variabel untuk menyatakan pola umum.",
                "Membedakan antara kuantitas konstan (tetap) dan variabel (penampung nilai yang berubah).",
                "Menerjemahkan kalimat bahasa sehari-hari menjadi kalimat matematika aljabar terbuka."
            ],
            "hook": "Bayangkan seorang pemilik toko grosir ingin menghitung total keuntungan harian. Hari ini ia menjual 15 kantong beras, besok mungkin 40 kantong, lusa 28 kantong. Jika ia harus menulis rumus baru dari awal setiap hari, ia akan kelelahan! Aljabar hadir sebagai mukjizat matematika: alih-alih angka kaku, kita menggunakan huruf penampung seperti x untuk mewakili jumlah kantong yang belum diketahui. Inilah awal mula komputasi dan pemrograman modern!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-box-seam-fill text-primary\"></i> 1. Konsep Variabel: Kotak Misteri Penampung Nilai</h3>\n              <p>Dalam aritmatika dasar SD, kita terbiasa melihat kotak kosong seperti $\\square + 5 = 12$. Dalam aljabar formal, kotak kosong tersebut digantikan oleh simbol huruf kecil (biasanya $x, y, z, a, b$). Huruf ini dinamakan <strong>Variabel (Peubah)</strong>.</p>\n              <ul class=\"dic-list\">\n                <li><strong>Konstanta:</strong> Nilai bilangan tetap yang tidak pernah berubah (contoh: angka $5, -12, \\pi$).</li>\n                <li><strong>Variabel:</strong> Simbol huruf penampung nilai yang belum diketahui atau dapat bervariasi nilainya.</li>\n                <li><strong>Nilai Aljabar:</strong> Nilai numerik yang diperoleh ketika variabel disubstitusikan dengan angka tertentu.</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-translate text-primary\"></i> 2. Menerjemahkan Bahasa Manusia ke Bahasa Aljabar</h3>\n              <p>Kunci penguasaan aljabar adalah kefasihan mengubah narasi verbal menjadi ekspresi simbolis:</p>\n              <ul class=\"dic-list\">\n                <li>'Sebuah angka ditambah 7' $\\rightarrow x + 7$.</li>\n                <li>'Tiga kali lipat umur Budi dikurangi 4 tahun' $\\rightarrow 3y - 4$.</li>\n                <li>'Keliling persegi dengan sisi s' $\\rightarrow K = 4s$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Saat memodelkan soal cerita, biasakan mendefinisikan variabel secara eksplisit di awal, misalnya: 'Misalkan x = harga 1 buah buku' agar logika perhitungan tidak tersesat!",
            "pitfall": "Hati-hati dengan pengurangan: '5 dikurangi x' ($5 - x$) BERBEDA TOTAL dengan 'x dikurangi dari 5' ($5 - x$) dan 'x dikurangi 5' ($x - 5$). Urutan sangat menentukan nilai!",
            "fun_fact": "Kata 'Aljabar' berasal dari kitab mahakarya matematikawan Persia Muhammad bin Musa Al-Khwarizmi abad ke-9 berjudul 'Al-Kitab al-mukhtasar fi hisab al-jabr wa'l-muqabala'. Kata 'Al-Jabr' secara harfiah bermakna 'mengembalikan / menyatukan kembali tulang yang patah', mengibaratkan pemindahan suku negatif ke ruas lain agar menjadi positif!",
            "formula": "ax + b = c \\iff ax = c - b \\implies x = \\frac{c - b}{a} \\quad (a \\neq 0)",
            "formula_params": [
                [
                    "x",
                    "Variabel peubah yang dicari nilainya."
                ],
                [
                    "a",
                    "Koefisien pengali variabel ($a \\neq 0$)."
                ],
                [
                    "b",
                    "Konstanta aditif pergeseran."
                ],
                [
                    "c",
                    "Target nilai kesetaraan ruas kanan."
                ]
            ],
            "formula_intuition": "Persamaan aljabar adalah neraca timbangan seimbang. Untuk mengisolasi variabel x sendirian di ruas kiri, kita harus membatalkan penjumlahan b dengan pengurangan b di kedua ruas, lalu membatalkan perkalian a dengan pembagian a di kedua ruas.",
            "example": {
                "question": "Sebuah dompet berisi sejumlah uang koin Rp 500-an sebanyak x keping. Jika diberi tambahan uang kertas Rp 3.000, total uang menjadi Rp 15.000. Tuliskan model persamaannya dan hitung berapa keping koin di dalam dompet tersebut!",
                "known": "Nilai 1 koin = Rp 500, Tambahan = Rp 3.000, Total = Rp 15.000.",
                "asked": "Model persamaan dan nilai x (banyak keping koin).",
                "steps": [
                    [
                        "Langkah 1: Menyusun Model Aljabar",
                        "Model: $500x + 3000 = 15000$."
                    ],
                    [
                        "Langkah 2: Mengurangkan Kedua Ruas dengan 3000",
                        "$500x = 15000 - 3000 \\implies 500x = 12000$."
                    ],
                    [
                        "Langkah 3: Membagi Kedua Ruas dengan 500",
                        "$x = \\frac{12000}{500} = 24$ keping."
                    ]
                ],
                "conclusion": "Di dalam dompet mula-mula terdapat 24 keping koin Rp 500-an."
            },
            "takeaways": [
                "Variabel adalah simbol huruf penampung nilai numerik yang belum diketahui nilainya.",
                "Aljabar menggeneralisasi aritmatika angka menjadi hubungan matematis universal.",
                "Prinsip kesetaraan: operasi matematika apa pun yang diterapkan di ruas kiri wajib diterapkan identik di ruas kanan."
            ],
            "quiz": [
                "Sebuah toko buku menjual pensil seharga Rp 2.500 per batang. Jika Budi membeli n batang pensil dan membayar dengan uang Rp 20.000 serta menerima kembalian Rp 5.000, berapakah nilai n?",
                [
                    "n = 6 batang",
                    "n = 8 batang",
                    "n = 5 batang"
                ],
                0,
                "2500n + 5000 = 20000 \\implies 2500n = 15000 \\implies n = 15000 / 2500 = 6\\text{ batang}."
            ]
        },
        {
            "title": "Anatomi: Struktur Suku, Koefisien & Sifat Operasi Aljabar",
            "objectives": [
                "Mengidentifikasi unsur-unsur bentuk aljabar: Suku, Koefisien, Variabel, Konstanta, dan Derajat Polinomial.",
                "Membedakan suku sejenis dan suku tidak sejenis.",
                "Melakukan operasi penyederhanaan aljabar dengan mengelompokkan suku-suku sejenis."
            ],
            "hook": "Dapatkah kamu menjumlahkan 3 buah apel dan 4 buah mangga menjadi 7 buah apel-mangga? Tentu tidak! Di dalam aljabar, kita hanya bisa menjumlahkan 'suku sejenis' yang memiliki variabel dan pangkat identik. Aturan anatomis ini menjamin keteraturan kalkulasi aljabar di seluruh cabang sains.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-diagram-3-fill text-primary\"></i> 1. Anatomi Bentuk Aljabar</h3>\n              <p>Perhatikan bentuk polinomial $5x^2 - 3x + 8$:</p>\n              <ul class=\"dic-list\">\n                <li><strong>Suku (Term):</strong> Bagian bentuk aljabar yang dipisahkan oleh tanda operasi $+$ atau $-$. Suku pada bentuk di atas adalah $5x^2$, $-3x$, dan $8$.</li>\n                <li><strong>Koefisien:</strong> Faktor pengali berupa angka yang melekat pada variabel (contoh: angka $5$ pada $5x^2$, dan $-3$ pada $-3x$).</li>\n                <li><strong>Variabel:</strong> Huruf peubah (contoh: $x$).</li>\n                <li><strong>Konstanta:</strong> Suku mandiri yang hanya berupa bilangan tetap tanpa variabel (contoh: angka $8$).</li>\n                <li><strong>Derajat:</strong> Pangkat tertinggi dari variabel pada bentuk aljabar (contoh: berderajat 2).</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-filter-square text-primary\"></i> 2. Hukum Suku Sejenis (Like Terms)</h3>\n              <p>Dua suku dikatakan <strong>sejenis</strong> jika memiliki variabel yang sama persis DAN pangkat variabel yang sama persis:</p>\n              <ul class=\"dic-list\">\n                <li>$4x$ dan $7x$ adalah <strong>sejenis</strong> (bisa dijumlahkan menjadi $11x$).</li>\n                <li>$3x^2$ dan $5x^2$ adalah <strong>sejenis</strong> (bisa dijumlahkan menjadi $8x^2$).</li>\n                <li>$2x$ dan $2y$ <strong>BUKAN suku sejenis</strong> (variabel berbeda, tidak bisa digabung!).</li>\n                <li>$4x^2$ dan $4x$ <strong>BUKAN suku sejenis</strong> (pangkat berbeda, tidak bisa digabung!).</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk menyederhanakan ekspresi aljabar yang panjang, gunakan metode penandaan visual: garis bawahi suku bertipe x dengan satu garis, suku bertipe y dengan dua garis, dan konstanta dilingkari sebelum dijumlahkan!",
            "pitfall": "Jangan lupakan tanda negatif di depan koefisien! Pada bentuk $7x - 4y$, koefisien dari y adalah $-4$, bukan $4$!",
            "fun_fact": "Dalam aljabar modern, suku sejenis adalah contoh langsung dari prinsip ruang vektor linear: koefisien bertindak sebagai skalar pengali, sedangkan variabel bertindak sebagai vektor basis!",
            "formula": "c_1 x^n + c_2 x^n = (c_1 + c_2)x^n \\quad ; \\quad a(bx + c) = abx + ac",
            "formula_params": [
                [
                    "c_1, c_2",
                    "Koefisien dari suku-suku sejenis."
                ],
                [
                    "x^n",
                    "Variabel dengan pangkat terikat identik."
                ],
                [
                    "a(bx + c)",
                    "Sifat distributif perkalian terhadap penjumlahan."
                ]
            ],
            "formula_intuition": "Sifat distributif aljabar menyatakan bahwa perkalian menyebar secara adil ke setiap anggota di dalam tanda kurung.",
            "example": {
                "question": "Sederhanakan bentuk aljabar berikut: $4(2x - 3y) + 3(x + 5y) - 2x + 7$!",
                "known": "Bentuk ekspresi aljabar bertanda kurung.",
                "asked": "Bentuk paling sederhana setelah digabungkan.",
                "steps": [
                    [
                        "Langkah 1: Distribusikan Angka Pengali Kurung",
                        "$4(2x - 3y) = 8x - 12y$ dan $3(x + 5y) = 3x + 15y$.<br>Ekspresi menjadi: $8x - 12y + 3x + 15y - 2x + 7$."
                    ],
                    [
                        "Langkah 2: Kelompokkan Suku-Suku Sejenis",
                        "Kelompokkan suku x: $(8 + 3 - 2)x = 9x$.<br>Kelompokkan suku y: $(-12 + 15)y = 3y$.<br>Konstanta: $+7$."
                    ],
                    [
                        "Langkah 3: Tuliskan Hasil Penggabungan",
                        "$9x + 3y + 7$."
                    ]
                ],
                "conclusion": "Bentuk sederhana dari ekspresi tersebut adalah $9x + 3y + 7$."
            },
            "takeaways": [
                "Hanya suku-suku sejenis yang dapat dijumlahkan atau dikurangkan koefisiennya.",
                "Sifat distributif $a(b + c) = ab + ac$ adalah pondasi untuk membuka tanda kurung aljabar.",
                "Tanda negatif di depan tanda kurung membalikkan seluruh tanda suku di dalamnya."
            ],
            "quiz": [
                "Bentuk paling sederhana dari $5x - 3(2x - 4y) + 2y$ adalah?",
                [
                    "-x + 14y",
                    "-x - 10y",
                    "11x + 14y"
                ],
                0,
                "5x - 6x + 12y + 2y = (5 - 6)x + (12 + 2)y = -x + 14y."
            ]
        },
        {
            "title": "Mekanika: Pemfaktoran & Ekspansi Aljabar",
            "objectives": [
                "Menguasai teknik ekspansi perkalian binomial menggunakan metode FOIL (First, Outer, Inner, Last).",
                "Mengenali dan menerapkan bentuk rumus kuadrat sempurna dan selisih dua kuadrat.",
                "Melakukan faktorisasi bentuk kuadrat $x^2 + bx + c$ menjadi perkalian faktor linear $(x + p)(x + q)$."
            ],
            "hook": "Bayangkan kamu memiliki kode rahasia yang terkunci dalam bentuk perkalian $(x+3)(x-3)$. Jika dibuka, hasilnya menjadi $x^2 - 9$. Faktorisasi adalah kebalikan dari ekspansi: kemampuan memecah bentuk polinomial rumit kembali menjadi bagian-bagian pembentuk dasarnya. Faktorisasi inilah yang menjadi dasar kriptografi RSA yang mengamankan transaksi perbankan dan enkripsi internet di seluruh dunia!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrows-angle-expand text-primary\"></i> 1. Tiga Identitas Aljabar Istimewa</h3>\n              <p>Tiga rumus identitas wajib hafal yang menjadi jalan pintas kalkulasi aljabar:</p>\n              <ul class=\"dic-list\">\n                <li><strong>Kuadrat Penjumlahan:</strong> $(a + b)^2 = a^2 + 2ab + b^2$. Perhatikan ada suku silang $2ab$!</li>\n                <li><strong>Kuadrat Pengurangan:</strong> $(a - b)^2 = a^2 - 2ab + b^2$.</li>\n                <li><strong>Selisih Dua Kuadrat:</strong> $a^2 - b^2 = (a - b)(a + b)$. Rumus paling sakti untuk menyederhanakan pecahan bentuk akar dan polinomial!</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-puzzle-fill text-primary\"></i> 2. Mekanisme Faktorisasi Trinom Kuadrat</h3>\n              <p>Untuk memfaktorkan bentuk $x^2 + bx + c$ menjadi $(x + p)(x + q)$:</p>\n              <div class=\"p-3 rounded my-2\" style=\"background:rgba(99,102,241,0.08); border-left:4px solid #6366f1;\">\n                <strong>Kaidah Pasangan Bilangan:</strong> Cari dua bilangan $p$ dan $q$ yang memenuhi:<br>\n                1. Hasil kalinya: $p \\times q = c$<br>\n                2. Hasil jumlahnya: $p + q = b$\n              </div>\n            </div>\n            ",
            "pro_tip": "Untuk menghitung kuadrat angka besar di kepala tanpa kalkulator, gunakan selisih dua kuadrat! Contoh: $52 \\times 48 = (50 + 2)(50 - 2) = 50^2 - 2^2 = 2500 - 4 = 2496$. Sangat cepat dan presisi!",
            "pitfall": "Kesalahan paling populer siswa di seluruh dunia: Menganggap $(a + b)^2 = a^2 + b^2$. INI SALAH BESAR! Jangan pernah melupakan suku tengah interaksi $2ab$!",
            "fun_fact": "Identitas kuadrat sempurna $(a+b)^2 = a^2 + 2ab + b^2$ dapat dibuktikan secara visual geometris menggunakan luas bujur sangkar besar bersisi $(a+b)$ yang tersusun atas 1 kotak $a^2$, 1 kotak $b^2$, dan 2 persegi panjang seluas $ab$!",
            "formula": "(a \\pm b)^2 = a^2 \\pm 2ab + b^2 \\quad ; \\quad a^2 - b^2 = (a - b)(a + b) \\quad ; \\quad x^2 + (p+q)x + pq = (x+p)(x+q)",
            "formula_params": [
                [
                    "a, b",
                    "Suku-suku pembentuk binomial."
                ],
                [
                    "2ab",
                    "Suku silang interaksi perkalian dua elemen."
                ],
                [
                    "p, q",
                    "Pasangan bilangan bulat faktor akar kuadrat."
                ]
            ],
            "formula_intuition": "Faktorisasi adalah proses dekomposisi struktur penjumlahan menjadi struktur perkalian faktor-faktor prima aljabar.",
            "example": {
                "question": "Faktorkan bentuk polinomial kuadrat berikut: (a) $x^2 - 16$, dan (b) $x^2 + 7x + 12$!",
                "known": "Bentuk kuadrat $x^2 - 16$ dan $x^2 + 7x + 12$.",
                "asked": "Bentuk faktorisasi perkalian linear.",
                "steps": [
                    [
                        "Langkah 1: Faktorisasi Selisih Dua Kuadrat",
                        "$x^2 - 16 = x^2 - 4^2$. Dengan rumus $a^2 - b^2 = (a-b)(a+b)$, hasilnya adalah $(x - 4)(x + 4)$."
                    ],
                    [
                        "Langkah 2: Menentukan Pasangan Bilangan p dan q",
                        "Untuk $x^2 + 7x + 12$, kita butuh dua bilangan yang jika dikali = 12 dan jika ditambah = 7. Pasangan yang cocok adalah 3 dan 4 (karena $3 \\times 4 = 12$ dan $3 + 4 = 7$)."
                    ],
                    [
                        "Langkah 3: Tuliskan Faktor Linear",
                        "$(x + 3)(x + 4)$."
                    ]
                ],
                "conclusion": "Hasil faktorisasi berturut-turut adalah $(x - 4)(x + 4)$ dan $(x + 3)(x + 4)$."
            },
            "takeaways": [
                "Ekspansi kuadrat sempurna selalu memuat suku tengah $2ab$: $(a+b)^2 = a^2 + 2ab + b^2$.",
                "Selisih dua kuadrat $a^2 - b^2$ selalu terurai menjadi $(a-b)(a+b)$.",
                "Faktorisasi adalah teknik invers dari perkalian untuk mencari pembuat nol persamaan."
            ],
            "quiz": [
                "Bentuk faktorisasi penuh dari ekspresi $x^2 - 10x + 21$ adalah?",
                [
                    "(x - 3)(x - 7)",
                    "(x + 3)(x - 7)",
                    "(x - 1)(x - 21)"
                ],
                0,
                "Cari dua angka dijumlah -10, dikali +21: yaitu -3 dan -7. Maka faktornya adalah (x - 3)(x - 7)."
            ]
        },
        {
            "title": "Pemodelan: Persamaan Linear Satu Variabel (PLSV) & Neraca Solusi",
            "objectives": [
                "Menyelesaikan persamaan linear satu variabel dengan teknik isolasi variabel bertahap.",
                "Menangani PLSV yang memuat tanda kurung dan pecahan aljabar.",
                "Memodelkan masalah optimasi biaya, tarif sewa, dan selisih usia dalam kehidupan nyata."
            ],
            "hook": "Sebuah perusahaan taksi online mematok tarif awal buka pintu Rp 8.000 ditambah tarif per kilometer sebesar Rp 3.500. Jika kamu hanya memiliki saldo dompet digital tepat Rp 50.000, berapa kilometer jarak maksimal yang dapat kamu tempuh? Inilah penerapan murni Persamaan Linear Satu Variabel (PLSV) yang kamu gunakan dalam kalkulasi finansial sehari-hari!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-balance text-primary\"></i> 1. Prinsip Kesetaraan Neraca Timbangan</h3>\n              <p>Tanda sama dengan ($=$) bertindak seperti titik tumpu neraca analitik. Neraca akan tetap seimbang sempurna jika:</p>\n              <ul class=\"dic-list\">\n                <li>Kedua ruas ditambah dengan bilangan yang sama ($A = B \\implies A + k = B + k$).</li>\n                <li>Kedua ruas dikurang dengan bilangan yang sama ($A = B \\implies A - k = B - k$).</li>\n                <li>Kedua ruas dikali bilangan bukan nol ($A = B \\implies Ak = Bk$).</li>\n                <li>Kedua ruas dibagi bilangan bukan nol ($A = B \\implies A/k = B/k$).</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-gear-fill text-primary\"></i> 2. Empat Langkah Prosedural Menyelesaikan PLSV Rumit</h3>\n              <ol class=\"dic-list\">\n                <li><strong>Eliminasi Tanda Kurung:</strong> Gunakan sifat distributif.</li>\n                <li><strong>Eliminasi Pecahan:</strong> Kalikan seluruh ruas dengan KPK dari penyebut jika ada pecahan.</li>\n                <li><strong>Kumpulkan Suku Sejenis:</strong> Pindahkan semua suku bervariabel ke ruas kiri dan semua konstanta ke ruas kanan.</li>\n                <li><strong>Bagi dengan Koefisien:</strong> Dapatkan $x = \\text{nilai solusi}$.</li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Saat memindahkan suku ke seberang tanda sama dengan, tandanya selalu berganti (+ menjadi -, dan - menjadi +). Ini adalah jalan pintas dari prinsip menambah/mengurang kedua ruas!",
            "pitfall": "Hati-hati saat membagi dengan koefisien bertanda negatif! Contoh: $-3x = 12 \\implies x = 12 / (-3) = -4$, bukan $+4$!",
            "fun_fact": "Dalam komputasi algoritma pencarian biner dan pemrosesan grafis, persamaan linear adalah jenis persamaan yang dapat diselesaikan dengan kompleksitas waktu komputasi paling cepat ($O(1)$) tanpa memerlukan iterasi berulang!",
            "formula": "a(x - d) + b = c(x + e) \\implies ax - c x = ce + ad - b \\implies x = \\frac{ce + ad - b}{a - c}",
            "formula_params": [
                [
                    "x",
                    "Variabel linear berderajat satu."
                ],
                [
                    "a, c",
                    "Koefisien variabel pada masing-masing ruas."
                ],
                [
                    "b, d, e",
                    "Konstanta pemodelan."
                ]
            ],
            "formula_intuition": "Menyatukan suku-suku sejenis pada satu ruas dan konstanta pada ruas lainnya untuk mengisolasi variabel tunggal.",
            "example": {
                "question": "Selesaikan persamaan linear berikut: $3(2x - 4) = 2(x + 6) + 4$!",
                "known": "Persamaan linear dengan kurung di kedua ruas.",
                "asked": "Nilai himpunan penyelesaian x.",
                "steps": [
                    [
                        "Langkah 1: Buka Kurung dengan Sifat Distributif",
                        "$6x - 12 = 2x + 12 + 4 \\implies 6x - 12 = 2x + 16$."
                    ],
                    [
                        "Langkah 2: Pindahkan Suku Variabel ke Ruas Kiri",
                        "Kurangkan kedua ruas dengan $2x$: $6x - 2x - 12 = 16 \\implies 4x - 12 = 16$."
                    ],
                    [
                        "Langkah 3: Pindahkan Konstanta ke Ruas Kanan",
                        "Tambahkan kedua ruas dengan 12: $4x = 16 + 12 \\implies 4x = 28$."
                    ],
                    [
                        "Langkah 4: Isolasi Variabel x",
                        "$x = \\frac{28}{4} = 7$."
                    ]
                ],
                "conclusion": "Nilai penyelesaian yang memenuhi persamaan adalah $x = 7$."
            },
            "takeaways": [
                "PLSV memiliki tepat satu solusi unik pada himpunan bilangan riil jika $a \\neq c$.",
                "Operasi pada kedua ruas harus selalu seimbang untuk menjaga kebenaran matematis.",
                "Verifikasi jawaban dapat dilakukan dengan mensubstitusikan nilai x kembali ke persamaan awal."
            ],
            "quiz": [
                "Selesaikan nilai x dari persamaan: $4(x - 3) = 2x + 10$!",
                [
                    "x = 11",
                    "x = 7",
                    "x = 9"
                ],
                0,
                "4x - 12 = 2x + 10 \\implies 4x - 2x = 10 + 12 \\implies 2x = 22 \\implies x = 11."
            ]
        },
        {
            "title": "Capstone: Proyek Evaluasi Sintesis Pemodelan Aljabar",
            "objectives": [
                "Mengintegrasikan konsep variabel, ekspansi aljabar, dan persamaan linear untuk merancang pemodelan lahan real estate.",
                "Membuat formulasi matematis untuk mencari dimensi optimal (panjang, lebar, dan luas) dari kendala keliling fisik.",
                "Mengevaluasi keputusan finansial berdasarkan solusi aljabar yang diperoleh."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Project Consultant untuk sebuah pengembang perumahan. Sebuah lapangan fasilitas olahraga terbuka berbentuk persegi panjang harus dipagari dengan anggaran kawat keliling tepat 64 meter. Arsitek menetapkan aturan bahwa panjang lapangan harus berukuran $(3x + 2)$ meter dan lebarnya $(x + 6)$ meter. Bisakah kamu menemukan nilai x, menentukan ukuran fisik lapangan, dan menghitung total luas lapangan tersebut?",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Studi Kasus Lapangan Real Estate</h3>\n              <p>Pemodelan geometri terikat oleh hukum keliling persegi panjang:</p>\n              \\[ K = 2(p + l) \\]\n              <p>Dengan menyubstitusikan ekspresi aljabar panjang dan lebar ke dalam formula keliling, kita mengubah masalah arsitektur fisik menjadi satu persamaan linear satu variabel formal yang dapat diselesaikan secara presisi!</p>\n            </div>\n            ",
            "pro_tip": "Dalam proyek aljabar terapan, selalu uji kelayakan fisik dari solusi x: nilai dimensi panjang dan lebar harus selalu bernilai positif riil ($p > 0$ dan $l > 0$)!",
            "pitfall": "Jangan lupa bahwa rumus keliling adalah $2(p + l)$, bukan $p + l$! Melewatkan faktor pengali 2 akan membuat dimensi yang dihasilkan salah dua kali lipat.",
            "fun_fact": "Teknik pemodelan aljabar linear terikat keliling ini adalah cikal bakal dari Linear Programming (Program Linear) yang diciptakan oleh Leonid Kantorovich untuk memenangkan Hadiah Nobel Ekonomi pada tahun 1975!",
            "formula": "K = 2(p + l) \\implies K = 2((ax + b) + (cx + d)) \\implies Luas = p \\times l",
            "formula_params": [
                [
                    "K",
                    "Keliling total lapangan (meter)."
                ],
                [
                    "p",
                    "Ekspresi aljabar panjang."
                ],
                [
                    "l",
                    "Ekspresi aljabar lebar."
                ],
                [
                    "Luas",
                    "Hasil kali dimensi fisik ($p \\times l$)."
                ]
            ],
            "formula_intuition": "Menghubungkan kendala batas keliling luar fisik dengan perkalian luas area fungsional.",
            "example": {
                "question": "Sebuah lapangan memiliki keliling 64 meter. Panjangnya $p = (3x + 2)$ meter dan lebarnya $l = (x + 6)$ meter. Tentukan: (a) Nilai x, (b) Panjang dan lebar aktual lapangan, dan (c) Luas total lapangan olahraga tersebut!",
                "known": "$K = 64\\text{ m}$, $p = 3x + 2$, $l = x + 6$.",
                "asked": "Nilai x, dimensi p dan l, serta Luas.",
                "steps": [
                    [
                        "Langkah 1: Masukkan ke Rumus Keliling",
                        "$64 = 2((3x + 2) + (x + 6)) \\implies 64 = 2(4x + 8)$."
                    ],
                    [
                        "Langkah 2: Sederhanakan Ruas Kanan",
                        "$64 = 8x + 16$."
                    ],
                    [
                        "Langkah 3: Selesaikan Nilai x",
                        "$8x = 64 - 16 \\implies 8x = 48 \\implies x = 6$."
                    ],
                    [
                        "Langkah 4: Hitung Dimensi Fisik Aktual",
                        "Panjang $p = 3(6) + 2 = 18 + 2 = 20\\text{ meter}$.<br>Lebar $l = 6 + 6 = 12\\text{ meter}$.<br>Cek keliling: $2(20 + 12) = 2(32) = 64\\text{ m}$ (Valid!)."
                    ],
                    [
                        "Langkah 5: Hitung Luas Area Lapangan",
                        "$\\text{Luas} = p \\times l = 20 \\times 12 = 240\\text{ meter persegi (m}^2\\text{)}$."
                    ]
                ],
                "conclusion": "Nilai x = 6. Lapangan berukuran panjang 20 meter, lebar 12 meter, dengan luas total 240 m²."
            },
            "takeaways": [
                "Aljabar memungkinkan integrasi masalah geometri fisik ke dalam persamaan matematika yang solutif.",
                "Sintesis menyeluruh menguji kemampuan aljabar dari pemodelan, isolasi variabel, hingga substitusi kembali ke besaran nyata.",
                "Selamat! Kamu telah menguasai fondasi aljabar dengan standar pemahaman yang solid!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE ALJABAR: Suatu kebun berbentuk persegi panjang dengan keliling 60 m memiliki panjang p = (2x + 5) m dan lebar l = (x + 10) m. Berapakah luas kebun tersebut?",
                [
                    "225 m² (Panjang 15 m, Lebar 15 m)",
                    "200 m² (Panjang 20 m, Lebar 10 m)",
                    "216 m² (Panjang 18 m, Lebar 12 m)"
                ],
                0,
                "2((2x + 5) + (x + 10)) = 60 \\implies 2(3x + 15) = 60 \\implies 6x + 30 = 60 \\implies 6x = 30 \\implies x = 5. Maka p = 2(5)+5 = 15 m, l = 5+10 = 15 m. Luas = 15 \\times 15 = 225\\text{ m}^2 (berupa persegi)."
            ]
        }
    ]
}
