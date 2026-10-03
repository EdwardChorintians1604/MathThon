# -*- coding: utf-8 -*-
DATA = {
    "title": "Probabilitas & Kombinatorik",
    "short": "Probabilitas",
    "icon": "bi-dice-5",
    "color": "#14b8a6",
    "desc": "Kuasai seni mengukur ketidakpastian, ruang sampel, kaidah pencacahan, faktorial, permutasi, kombinasi, peluang majemuk, dan Teorema Bayes.",
    "babs": [
        {
            "title": "Fondasi: Ketidakpastian di Alam Semesta & Ruang Sampel",
            "objectives": [
                "Memahami konsep dasar peluang klasik sebagai rasio kejadian diharapkan terhadap seluruh kemungkinan.",
                "Menentukan ruang sampel S dan titik sampel menggunakan diagram pohon dan tabel silang.",
                "Menguasai rentang nilai peluang: 0 (mustahil) hingga 1 (pasti)."
            ],
            "hook": "Berapakah kemungkinan esok hari akan turun hujan salju di Jakarta? Tepat 0% (kemustahilan). Berapakah kemungkinan matahari terbit dari timur esok pagi? Tepat 100% atau 1 (kepastian mutlak). Segala hal lain di kehidupan berada di antara 0 dan 1! Teori Peluang (Probabilitas) lahir pada abad ke-17 dari surat-menyurat antara matematikawan Blaise Pascal dan Pierre de Fermat yang menganalisis permainan lempar dadu untuk mengukur derajat kepastian suatu peristiwa acak.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-dice-3 text-primary\"></i> 1. Definisi Peluang Klasik Teoritis</h3>\n              <p>Jika setiap titik sampel memiliki kemungkinan yang sama untuk muncul (equally likely), peluang kejadian A didefinisikan sebagai:</p>\n              \\[ P(A) = \\frac{n(A)}{n(S)} \\]\n              <ul class=\"dic-list\">\n                <li>$n(A)$: Banyaknya anggota kejadian A yang diharapkan.</li>\n                <li>$n(S)$: Total banyaknya anggota ruang sampel semesta.</li>\n                <li><strong>Rentang Peluang:</strong> $0 \\le P(A) \\le 1$.</li>\n                <li><strong>Peluang Komplemen ($A'$):</strong> Peluang kejadian A TIDAK terjadi adalah $P(A') = 1 - P(A)$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Jika menghitung peluang kejadian A terasa sangat rumit dan panjang, cobalah hitung peluang komplemennya (kejadian sebaliknya A') lalu kurangkan dari 1: $P(A) = 1 - P(A')$!",
            "pitfall": "Nilai peluang TIDAK PERNAH bernilai negatif dan TIDAK PERNAH lebih besar dari 1 (atau lebih dari 100%)! Jika hasil perhitunganmu mendapat angka 1.4 atau -0.2, pasti ada kesalahan logika.",
            "fun_fact": "Kecerdasan buatan dalam mobil otonom (Self-Driving Cars) menghitung jutaan matriks probabilitas Bayesian per detik untuk memprediksi apakah pejalan kaki di trotoar akan melangkah menyeberang jalan atau tetap diam.",
            "formula": "P(A) = \\frac{n(A)}{n(S)} \\quad (0 \\le P(A) \\le 1) \\quad ; \\quad P(A') = 1 - P(A)",
            "formula_params": [
                [
                    "n(A)",
                    "Banyaknya titik sampel kejadian yang diinginkan."
                ],
                [
                    "n(S)",
                    "Banyaknya seluruh kemungkinan hasil percobaan acak."
                ],
                [
                    "P(A')",
                    "Peluang komplemen kejadian A."
                ]
            ],
            "formula_intuition": "Membagi jumlah skenario sukses dengan total kemungkinan semesta alam yang dapat terjadi.",
            "example": {
                "question": "Dua buah dadu bermata 6 dilemparkan secara bersamaan satu kali. Berapakah peluang munculnya jumlah mata dadu sama dengan 8?",
                "known": "Dua dadu dilempar. Ruang sampel total $n(S) = 6 \\times 6 = 36$.",
                "asked": "Peluang muncul jumlah mata dadu = 8.",
                "steps": [
                    [
                        "Langkah 1: Tentukan Pasangan Dadu yang Berjumlah 8",
                        "Pasangan $(d_1, d_2)$ yang menghasilkan jumlah 8:<br>$(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)$."
                    ],
                    [
                        "Langkah 2: Hitung Banyaknya Titik Sampel n(A)",
                        "Ada 5 pasangan, maka $n(A) = 5$."
                    ],
                    [
                        "Langkah 3: Hitung Nilai Peluang",
                        "$P(A) = \\frac{n(A)}{n(S)} = \\frac{5}{36} \\approx 0.1389$ (atau $13.89\\%$)."
                    ]
                ],
                "conclusion": "Peluang muncul jumlah kedua mata dadu sama dengan 8 adalah 5/36."
            },
            "takeaways": [
                "Peluang mengukur derajat kepastian suatu kejadian dalam skala rasional 0 hingga 1.",
                "Ruang sampel semesta $n(S)$ adalah pondasi penyebut dari seluruh kalkulasi peluang klasik.",
                "Hukum komplemen $P(A') = 1 - P(A)$ adalah jalan pintas tercepat untuk soal bernarasi 'paling sedikit satu'."
            ],
            "quiz": [
                "Sebuah kartu diambil secara acak dari satu set kartu bridge standar (52 kartu). Berapakah peluang terambil kartu As?",
                [
                    "4/52 = 1/13",
                    "1/52",
                    "2/52 = 1/26"
                ],
                0,
                "Dalam 52 kartu terdapat 4 kartu As (sekop, hati, keriting, wajik). Maka P = 4/52 = 1/13."
            ]
        },
        {
            "title": "Anatomi: Kaidah Pencacahan, Permutasi (Urutan Penting) vs Kombinasi",
            "objectives": [
                "Menguasai notasi faktorial n! = n * (n-1) * ... * 1 dengan definisi 0! = 1.",
                "Membedakan Permutasi (urutan posisi diperhatikan) dan Kombinasi (urutan posisi bebas).",
                "Menghitung banyaknya cara pemilihan pengurus organisasi dan formasi tim perwakilan."
            ],
            "hook": "Jika kamu memesan semangkuk es krim dengan tiga rasa: cokelat, vanila, dan stroberi—apakah rasa es krimmu berubah jika pelayan menaruh sendok vanila terlebih dahulu sebelum cokelat? Tidak berubah (Urutan Bebas = Kombinasi). Tetapi bagaimana jika kita memilih Juara 1, Juara 2, dan Juara 3 lomba lari? Hadiah Juara 1 tentu sangat berbeda dengan Juara 3 (Urutan Posisi Penting = Permutasi)! Memahami perbedaan anatomis inilah kunci kombinatorika!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-diagram-2 text-primary\"></i> 1. Permutasi vs Kombinasi</h3>\n              <div class=\"row g-3 my-2\">\n                <div class=\"col-md-6\">\n                  <div class=\"p-3 rounded h-100\" style=\"background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);\">\n                    <div class=\"fw-bold text-info mb-1\"><i class=\"bi bi-sort-numeric-down\"></i> Permutasi ($^n P_r$)</div>\n                    <p class=\"small text-muted mb-0\"><strong>Urutan Sangat Diperhatikan!</strong> Susunan $(A, B)$ dianggap BERBEDA dengan $(B, A)$.<br><br>\n                    <strong>Contoh:</strong> Menentukan susunan Ketua, Sekretaris, Bendahara; Nomor PIN rekening ATM; dan Urutan pelari estafet.</p>\n                    \\[ ^n P_r = \\frac{n!}{(n - r)!} \\]\n                  </div>\n                </div>\n                <div class=\"col-md-6\">\n                  <div class=\"p-3 rounded h-100\" style=\"background:rgba(20,184,166,0.08); border:1px solid rgba(20,184,166,0.25);\">\n                    <div class=\"fw-bold text-success mb-1\"><i class=\"bi bi-people\"></i> Kombinasi ($^n C_r$)</div>\n                    <p class=\"small text-muted mb-0\"><strong>Urutan Bebas / Diabaikan!</strong> Kelompok $\\{A, B\\}$ dianggap SAMA PERSIS dengan $\\{B, A\\}$.<br><br>\n                    <strong>Contoh:</strong> Memilih 3 orang anggota regu piket, memilih 5 kartu remi poker, dan mencampur warna cat.</p>\n                    \\[ ^n C_r = \\frac{n!}{r!(n - r)!} \\]\n                  </div>\n                </div>\n              </div>\n            </div>\n            ",
            "pro_tip": "Hubungan matematis penting: Permutasi selalu tepat $r!$ kali lebih besar daripada Kombinasi: $^n P_r = (^n C_r) \\times r!$. Karena kombinasi hanya memilih, sedangkan permutasi melanjutkannya dengan menata urutan susunan anggota terpilih tersebut!",
            "pitfall": "Jangan lupa bahwa $0!$ didefinisikan sama dengan 1 ($0! = 1$), bukan 0! Hal ini menjaga konsistensi aljabar pada $^n C_n = \\frac{n!}{n! 0!} = 1$.",
            "fun_fact": "Banyaknya kemungkinan susunan acak tumpukan 52 kartu remi adalah $52! \\approx 8 \\times 10^{67}$. Angka ini begitu masif sehingga setiap kali kamu mengocok satu set kartu dengan benar, hampir pasti susunan kartumu belum pernah ada sebelumnya dalam seluruh sejarah alam semesta!",
            "formula": "^n P_r = \\frac{n!}{(n - r)!} \\quad ; \\quad ^n C_r = \\binom{n}{r} = \\frac{n!}{r!(n - r)!}",
            "formula_params": [
                [
                    "n",
                    "Total jumlah objek yang tersedia."
                ],
                [
                    "r",
                    "Jumlah objek yang dipilih ($r \\le n$)."
                ],
                [
                    "n!",
                    "Notasi faktorial $n \\times (n-1) \\times \\dots \\times 1$."
                ]
            ],
            "formula_intuition": "Membagi dengan faktorial $(n - r)!$ untuk memotong cabang yang tidak terpakai, dan membagi dengan $r!$ untuk mengeliminasi duplikasi permutasi posisi.",
            "example": {
                "question": "Dari 7 orang kandidat pengurus kelas, akan dipilih: (a) Ketua, Sekretaris, dan Bendahara, serta (b) 3 orang delegasi regu belajar bersama. Hitung berapa banyak cara pemilihan untuk masing-masing kasus!",
                "known": "Total kandidat $n = 7$, dipilih $r = 3$.",
                "asked": "Banyak susunan pengurus (urutan penting) dan delegasi (urutan bebas).",
                "steps": [
                    [
                        "Langkah 1: Kasus (a) Pengurus Menggunakan Permutasi",
                        "Posisi jabatan memiliki hierarki berbeda (urutan penting):<br>$^7 P_3 = \\frac{7!}{(7 - 3)!} = \\frac{7!}{4!} = 7 \\times 6 \\times 5 = 210\\text{ cara}$."
                    ],
                    [
                        "Langkah 2: Kasus (b) Delegasi Menggunakan Kombinasi",
                        "Semua delegasi memiliki status setara tanpa jabatan (urutan bebas):<br>$^7 C_3 = \\frac{7!}{3! (7 - 3)!} = \\frac{7 \\times 6 \\times 5}{3 \\times 2 \\times 1} = \\frac{210}{6} = 35\\text{ cara}$."
                    ]
                ],
                "conclusion": "Ada 210 cara untuk memilih susunan jabatan pengurus (Permutasi) dan ada 35 cara untuk memilih kelompok delegasi belajar (Kombinasi)."
            },
            "takeaways": [
                "Permutasi digunakan saat urutan atau posisi memiliki makna berbeda ($^n P_r$).",
                "Kombinasi digunakan saat urutan pemilihan tidak membedakan hasil kelompok ($^n C_r$).",
                "Faktorial 0! didefinisikan bernilai 1."
            ],
            "quiz": [
                "Berapa banyak cara memilih 2 orang perwakilan siswa dari 5 calon yang tersedia?",
                [
                    "10 cara",
                    "20 cara",
                    "15 cara"
                ],
                0,
                "^5 C_2 = 5! / (2! * 3!) = (5 * 4) / (2 * 1) = 10 cara."
            ]
        },
        {
            "title": "Mekanika: Peluang Majemuk (Aturan Penjumlahan & Peluang Bersyarat)",
            "objectives": [
                "Menghitung peluang dua kejadian saling lepas vs tidak saling lepas menggunakan aturan penjumlahan.",
                "Menghitung peluang dua kejadian saling bebas (independen) menggunakan aturan perkalian.",
                "Memahami konsep Peluang Bersyarat P(A|B) dan Teorema Bayes dasar."
            ],
            "hook": "Jika kamu melempar koin sebanyak 10 kali berturut-turut dan hasilnya selalu keluar 'Gambar', apakah lemparan ke-11 pasti keluar 'Angka'? Penjudi amatir mengira 'sudah saatnya angka keluar' (Gambler's Fallacy). Namun matematika membuktikan bahwa koin tidak memiliki memori! Peluang lemparan ke-11 tetap tepat 50%! Memahami sifat independensi dan peluang bersyarat membedakan antara penalaran ilmiah yang jernih dan takhayul acak.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-intersect text-primary\"></i> 1. Aturan Penjumlahan Peluang</h3>\n              <p>Peluang kejadian A ATAU kejadian B terjadi ($P(A \\cup B)$):</p>\n              \\[ P(A \\cup B) = P(A) + P(B) - P(A \\cap B) \\]\n              <ul class=\"dic-list\">\n                <li><strong>Saling Lepas (Mutually Exclusive):</strong> Tidak mungkin terjadi bersamaan ($A \\cap B = \\emptyset \\implies P(A \\cap B) = 0$). Rumus menjadi: $P(A \\cup B) = P(A) + P(B)$.</li>\n                <li><strong>Tidak Saling Lepas:</strong> Memiliki irisan bersama, sehingga $P(A \\cap B)$ harus dikurangkan agar tidak terhitung ganda (double count).</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-node-plus text-primary\"></i> 2. Peluang Bersyarat (Conditional Probability)</h3>\n              <p>Peluang terjadinya kejadian A <strong>dengan syarat kejadian B telah terjadi lebih dulu</strong>:</p>\n              \\[ P(A | B) = \\frac{P(A \\cap B)}{P(B)} \\quad (P(B) > 0) \\]\n            </div>\n            ",
            "pro_tip": "Kata kunci dalam soal probabilitas: Kata hubung 'ATAU' mengindikasikan operasi PENJUMLAHAN ($+$), sedangkan kata hubung 'DAN' mengindikasikan operasi PERKALIAN ($\\times$)!",
            "pitfall": "Jangan lupa mengurangkan irisan pada dua kejadian yang tidak saling lepas! Jika kamu menghitung peluang terambil kartu Hati ATAU kartu Raja dari tumpukan kartu bridge: kartu Raja Hati jangan sampai terhitung dua kali!",
            "fun_fact": "Teorema Bayes yang dirumuskan oleh pendeta Thomas Bayes pada tahun 1763 digunakan oleh matematikawan Alan Turing untuk memecahkan kode mesin sandi Enigma Jerman Nazi di Bletchley Park pada Perang Dunia II.",
            "formula": "P(A \\cup B) = P(A) + P(B) - P(A \\cap B) \\quad ; \\quad P(A \\cap B) = P(A) \\cdot P(B) \\quad (\\text{Independen})",
            "formula_params": [
                [
                    "P(A \\cup B)",
                    "Peluang kejadian A ATAU B terjadi."
                ],
                [
                    "P(A \\cap B)",
                    "Peluang kejadian A DAN B terjadi bersamaan (irisan)."
                ]
            ],
            "formula_intuition": "Menggabungkan dua himpunan sembari mengeliminasi duplikasi elemen yang berada di irisan tengah.",
            "example": {
                "question": "Dari satu set kartu bridge standar (52 kartu), diambil satu kartu secara acak. Berapakah peluang terambil kartu bergambar Hati ATAU kartu bergambar Raja (King)?",
                "known": "Total kartu $n(S) = 52$. Kartu Hati ada 13 ($P(H) = 13/52$). Kartu Raja ada 4 ($P(K) = 4/52$).",
                "asked": "Peluang terambil Hati atau Raja ($P(H \\cup K)$).",
                "steps": [
                    [
                        "Langkah 1: Identifikasi Irisan Kejadian Bersama",
                        "Ada 1 kartu yang sekaligus merupakan kartu Hati DAN kartu Raja (Raja Hati). Maka $P(H \\cap K) = 1/52$."
                    ],
                    [
                        "Langkah 2: Terapkan Rumus Aturan Penjumlahan",
                        "$P(H \\cup K) = P(H) + P(K) - P(H \\cap K) = \\frac{13}{52} + \\frac{4}{52} - \\frac{1}{52}$."
                    ],
                    [
                        "Langkah 3: Hitung Hasil Akhir",
                        "$P(H \\cup K) = \\frac{16}{52} = \\frac{4}{13} \\approx 0.3077$ (atau $30.77\\%$)."
                    ]
                ],
                "conclusion": "Peluang terambil kartu Hati atau kartu Raja adalah 4/13."
            },
            "takeaways": [
                "Kata 'atau' mengacu pada gabungan $\\cup$, dan kata 'dan' mengacu pada irisan $\\cap$.",
                "Irisan harus dikurangkan jika kedua kejadian tidak saling lepas.",
                "Peluang bersyarat $P(A|B)$ memperbarui derajat kepastian setelah ada informasi awal yang diketahui."
            ],
            "quiz": [
                "Sebuah dadu dilempar sekali. Berapakah peluang muncul mata dadu ganjil ATAU mata dadu prima?",
                [
                    "4/6 = 2/3",
                    "3/6 = 1/2",
                    "5/6"
                ],
                0,
                "Ganjil = {1, 3, 5}, Prima = {2, 3, 5}. Gabungan = {1, 2, 3, 5} ada 4 elemen. Peluang = 4/6 = 2/3."
            ]
        },
        {
            "title": "Pemodelan: Distribusi Binomial & Hukum Bilangan Besar",
            "objectives": [
                "Memahami karakteristik eksperimen Bernoulli (tepat dua hasil: sukses vs gagal).",
                "Menghitung probabilitas sukses k kali dari n percobaan menggunakan rumus Binomial.",
                "Memahami Hukum Bilangan Besar (Law of Large Numbers) dalam konteks asuransi dan sains data."
            ],
            "hook": "Bagaimana perusahaan asuransi jiwa atau kasino Las Vegas bisa menjamin selalu untung secara stabil setiap tahun meskipun mereka tidak pernah tahu siapa individu yang akan meninggal besok atau pemain mana yang akan menang jackpot malam ini? Mereka bersandar pada Hukum Bilangan Besar (Law of Large Numbers): jika sebuah eksperimen diulang jutaan kali, fluktuasi acak akan lenyap dan frekuensi relatif akan konvergen tepat ke nilai probabilitas matematisnya!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-toggles text-primary\"></i> 1. Karakteristik Percobaan Binomial</h3>\n              <p>Sebuah fenomena mengikuti Distribusi Binomial jika memenuhi 4 kriteria:</p>\n              <ol class=\"dic-list\">\n                <li>Percobaan diulang sebanyak $n$ kali percobaan identik.</li>\n                <li>Setiap percobaan hanya memiliki 2 kemungkinan hasil: <strong>Sukses</strong> (peluang $p$) atau <strong>Gagal</strong> (peluang $q = 1 - p$).</li>\n                <li>Peluang sukses $p$ bernilai konstan dan tidak berubah di setiap percobaan.</li>\n                <li>Setiap percobaan bersifat saling bebas (independen).</li>\n              </ol>\n            </div>\n            ",
            "pro_tip": "Kombinasi $^n C_k$ pada rumus binomial berfungsi untuk menghitung berapa banyak urutan susunan kemenangan yang mungkin terjadi dari total n percobaan!",
            "pitfall": "Jangan tertukar antara peluang sukses $p$ dan peluang gagal $q$! Ingat selalu bahwa $p + q = 1$.",
            "fun_fact": "Algoritma filter spam email (seperti Gmail Spam Filter) menggunakan klasifikasi Naive Bayes berbasis distribusi binomial kata-kata mencurigakan untuk memblokir miliaran email penipuan setiap hari.",
            "formula": "P(X = k) = \\binom{n}{k} p^k q^{n - k} = \\frac{n!}{k!(n - k)!} p^k (1 - p)^{n - k}",
            "formula_params": [
                [
                    "n",
                    "Jumlah total percobaan yang dilakukan."
                ],
                [
                    "k",
                    "Jumlah kejadian sukses yang diharapkan ($k \\le n$)."
                ],
                [
                    "p",
                    "Peluang sukses dalam satu percobaan tunggal."
                ],
                [
                    "q = 1 - p",
                    "Peluang gagal dalam satu percobaan tunggal."
                ]
            ],
            "formula_intuition": "Mengalikan peluang urutan sukses-gagal spesifik dengan banyaknya permutasi posisi kemunculannya.",
            "example": {
                "question": "Sebuah koin seimbang dilemparkan sebanyak 5 kali. Berapakah peluang munculnya tepat 3 kali sisi Gambar?",
                "known": "$n = 5$ lemparan, diharapkan sukses $k = 3$ gambar. Peluang gambar $p = 0.5$, peluang angka $q = 0.5$.",
                "asked": "Peluang binomial $P(X = 3)$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Nilai Kombinasi $\\binom{5}{3}$",
                        "$\\binom{5}{3} = \\frac{5!}{3! 2!} = \\frac{5 \\times 4}{2 \\times 1} = 10\\text{ cara}$."
                    ],
                    [
                        "Langkah 2: Hitung Peluang Probabilitas $p^k q^{n-k}$",
                        "$p^3 q^{5-3} = (0.5)^3 \\times (0.5)^2 = 0.125 \\times 0.25 = 0.03125$ (atau $(1/2)^5 = 1/32$)."
                    ],
                    [
                        "Langkah 3: Kalikan Kombinasi dengan Peluang",
                        "$P(X = 3) = 10 \\times \\frac{1}{32} = \\frac{10}{32} = \\frac{5}{16} = 0.3125$ (atau $31.25\\%$)."
                    ]
                ],
                "conclusion": "Peluang muncul tepat 3 sisi gambar dari 5 kali lemparan koin adalah 5/16 (31.25%)."
            },
            "takeaways": [
                "Distribusi Binomial memodelkan jumlah sukses dari serangkaian percobaan biner independen.",
                "Rumus binomial mengombinasikan koefisien kombinatorik dengan probabilitas pangkat.",
                "Hukum Bilangan Besar menjamin stabilitas probabilitas pada pengulangan jangka panjang."
            ],
            "quiz": [
                "Sebuah kuis pilihan ganda terdiri dari 4 soal dengan masing-masing 2 opsi (Benar/Salah). Jika kamu menebak secara acak murni, berapakah peluang semua 4 soal dijawab benar?",
                [
                    "1/16",
                    "1/4",
                    "1/8"
                ],
                0,
                "P(semua 4 benar) = (1/2)^4 = 1/16."
            ]
        },
        {
            "title": "Capstone: Sistem Skrining Diagnostik Medis & Teorema Bayes",
            "objectives": [
                "Menerapkan Teorema Bayes untuk memecahkan Paradoks Negatif Palsu dan Positif Palsu dalam uji diagnostik medis laboratorium.",
                "Menghitung Nilai Prediktif Positif (PPV) berdasarkan sensitivitas alat uji dan prevalensi penyakit di masyarakat.",
                "Mengevaluasi keputusan medis klinis berbasis probabilitas posterior yang teruji secara matematis."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Epidemiologist Kementerian Kesehatan. Sebuah alat tes diagnostik cepat (Rapid Test) untuk penyakit langka memiliki tingkat akurasi akurat 99% (Sensitivitas 99% dan Spesifisitas 99%). Penyakit ini hanya menjangkiti 1 dari 1.000 orang di masyarakat (prevalensi 0.1%). Seseorang menjalani tes dan hasilnya POSITIF! Kebanyakan dokter awam mengira orang tersebut pasti 99% sakit. Padahal kenyataan matematis Teorema Bayes membuktikan bahwa peluang orang itu benar-benar sakit HANYA SEKITAR 9%! Mampukah kamu membuktikan paradoks probabilitas medis ini?",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Paradoks Teorema Bayes Medis</h3>\n              <p>Teorema Bayes menghitung probabilitas posterior terjadinya kondisi sakit ($S$) setelah diketahui hasil tes positif ($+$):</p>\n              \\[ P(S | +) = \\frac{P(+ | S) \\cdot P(S)}{P(+)} \\]\n              <p>Di mana total peluang hasil tes positif $P(+)$ berasal dari dua sumber: Orang yang <strong>Benar-benar Sakit dan Positif</strong> ditambah Orang yang <strong>Sehat tetapi Positif Palsu (False Positive)</strong>:</p>\n              \\[ P(+) = P(+ | S)P(S) + P(+ | \\text{Sehat})P(\\text{Sehat}) \\]\n            </div>\n            ",
            "pro_tip": "Untuk memahami Teorema Bayes dengan sangat mudah tanpa rumus rumit: Bayangkan populasi 100.000 orang! Hitung berapa banyak orang sakit nyata dan berapa banyak orang sehat yang mendapat positif palsu, lalu bagi keduanya secara langsung!",
            "pitfall": "Jangan abaikan angka PREVALENSI dasar (Base Rate Fallacy)! Pada penyakit langka, jumlah orang sehat yang mendapat positif palsu hampir selalu jauh lebih banyak daripada jumlah total orang yang benar-benar sakit.",
            "fun_fact": "Kesalahan penalaran Teorema Bayes di ruang pengadilan telah memicu banyak vonis salah dalam sejarah hukum pidana forensik (dikenal sebagai Prosecutor's Fallacy).",
            "formula": "P(S | +) = \\frac{P(+ | S) P(S)}{P(+ | S) P(S) + P(+ | H) P(H)}",
            "formula_params": [
                [
                    "P(S)",
                    "Prevalensi penyakit pada populasi umum (0.1%)."
                ],
                [
                    "P(+ | S)",
                    "Sensitivitas alat uji (akurasi positif benar = 99%)."
                ],
                [
                    "P(+ | H)",
                    "Tingkat positif palsu pada orang sehat (1 - 99% = 1%)."
                ]
            ],
            "formula_intuition": "Memperbarui keyakinan probabilitas awal menggunakan bukti eksperimental baru.",
            "example": {
                "question": "Pada populasi 100.000 orang, prevalensi penyakit adalah 0.1% (100 orang sakit, 99.900 orang sehat). Akurasi alat tes adalah 99% (Sensitivitas 99%, Spesifisitas 99%). Jika seseorang mendapat hasil tes positif, berapakah probabilitas bahwa ia benar-benar menderita penyakit tersebut?",
                "known": "Total 100.000 orang. Sakit: 100 orang, Sehat: 99.900 orang. Tingkat positif benar: 99%, Positif palsu: 1%.",
                "asked": "Peluang benar sakit bersyarat hasil positif $P(S | +)$.",
                "steps": [
                    [
                        "Langkah 1: Hitung Positif Benar dari Kelompok Sakit",
                        "Dari 100 orang sakit, yang terdeteksi positif = $99\\% \\times 100 = 99\\text{ orang}$."
                    ],
                    [
                        "Langkah 2: Hitung Positif Palsu dari Kelompok Sehat",
                        "Dari 99.900 orang sehat, yang keliru terdeteksi positif = $1\\% \\times 99.900 = 999\\text{ orang}$!"
                    ],
                    [
                        "Langkah 3: Hitung Total Seluruh Orang yang Mendapat Hasil Positif",
                        "Total positif = $99 + 999 = 1.098\\text{ orang}$."
                    ],
                    [
                        "Langkah 4: Hitung Rasio Bayes Peluang Benar Sakit",
                        "$P(S | +) = \\frac{99}{1.098} \\approx 0.0901$ (atau tepatnya hanya $9.01\\%$!)."
                    ]
                ],
                "conclusion": "Meskipun alat tes memiliki akurasi 99%, seseorang yang mendapat hasil positif hanya memiliki peluang sekitar 9.01% benar-benar sakit karena tingginya jumlah positif palsu dari populasi sehat."
            },
            "takeaways": [
                "Teorema Bayes membongkar bias intuisi manusia terhadap pengujian probabilitas bersyarat.",
                "Pada populasi penyakit langka, hasil tes positif awal wajib dikonfirmasi dengan tes kedua (Confirmation Test).",
                "Selamat! Kamu telah menguasai seluruh materi Probabilitas & Kombinatorik hingga tingkat sintesis mutakhir!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE PROBABILITAS: Mengapa pada penyakit sangat langka, hasil tes positif pertama tidak otomatis berarti orang tersebut pasti sakit?",
                [
                    "Karena jumlah positif palsu dari orang sehat melampaui jumlah orang sakit nyata",
                    "Karena alat tes laboratorium selalu rusak",
                    "Karena probabilitas tidak berlaku di dunia nyata"
                ],
                0,
                "Karena populasi sehat sangat dominan, kesalahan 1% dari populasi sehat menghasilkan lebih banyak orang positif palsu dibanding orang sakit sesungguhnya."
            ]
        }
    ]
}
