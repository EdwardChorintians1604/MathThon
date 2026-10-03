# -*- coding: utf-8 -*-
DATA = {
    "title": "Statistika & Analisis Data",
    "short": "Statistika",
    "icon": "bi-bar-chart-line",
    "color": "#ec4899",
    "desc": "Kuasai seni membaca data, ukuran pemusatan (Mean, Median, Modus), ukuran penyebaran (Varians, Standar Deviasi), Z-Score, dan deteksi anomali data (outlier).",
    "babs": [
        {
            "title": "Fondasi: Sains Membaca Data & Populasi vs Sampel",
            "objectives": [
                "Memahami peran statistika dalam sains data, riset sosial, dan pengambilan keputusan berbasis bukti.",
                "Membedakan konsep Populasi (seluruh objek) dan Sampel (sebagian representasi representatif).",
                "Mengklasifikasikan jenis data kuantitatif (diskrit & kontinu) serta data kualitatif (nominal & ordinal)."
            ],
            "hook": "Ketika lembaga survei memprediksi hasil pemilu presiden hanya dari 2.000 responden dan prediksinya meleset kurang dari 1% dari total 150 juta pemilih, bagaimana sihir matematika itu bisa terjadi? Lembaga survei tidak perlu bertanya pada semua orang! Statistika adalah seni mengambil kesimpulan objektif dan akurat tentang seluruh populasi besar hanya dengan memeriksa sampel kecil yang representatif.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-people-fill text-primary\"></i> 1. Populasi vs Sampel</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Populasi:</strong> Keseluruhan objek, individu, atau peristiwa lengkap yang menjadi sasaran penyelidikan (contoh: seluruh 270 juta rakyat Indonesia). Karakteristik populasi dinamakan <em>Parameter</em>.</li>\n                <li><strong>Sampel:</strong> Bagian kecil dari populasi yang dipilih secara acak dan terukur untuk diobservasi (contoh: 2.000 responden acak). Karakteristik sampel dinamakan <em>Statistik</em>.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Sampel yang baik BUKAN sampel yang banyak, melainkan sampel yang REPRESENTATIF (tidak bias dan mencerminkan keragaman populasi)!",
            "pitfall": "Waspadai bias pengambilan sampel (Sampling Bias): jika kamu meneliti rata-rata uang saku mahasiswa dengan hanya mewawancarai orang yang sedang makan di restoran mewah kampus, datamu pasti bias dan tidak valid!",
            "fun_fact": "Pelopor statistika modern Florence Nightingale adalah seorang perawat Inggris yang menyelamatkan ribuan nyawa tentara pada Perang Krimea tahun 1850-an bukan hanya dengan obat, melainkan dengan diagram statistik diagram polar 'Coxcomb' yang meyakinkan Ratu Victoria untuk merombak sanitasi rumah sakit militer.",
            "formula": "\\text{Populasi } (N, \\mu, \\sigma) \\quad \\xrightarrow{\\text{Sampling Acak}} \\quad \\text{Sampel } (n, \\bar{x}, s)",
            "formula_params": [
                [
                    "N",
                    "Ukuran total populasi."
                ],
                [
                    "n",
                    "Ukuran sampel terpilih."
                ],
                [
                    "\\mu, \\bar{x}",
                    "Rata-rata populasi vs rata-rata sampel."
                ],
                [
                    "\\sigma, s",
                    "Standar deviasi populasi vs sampel."
                ]
            ],
            "formula_intuition": "Menyederhanakan pengamatan parameter semesta besar menggunakan data terukur sampel mikro.",
            "example": {
                "question": "Sebuah pabrik lampu memproduksi 100.000 bohlam LED setiap hari. Quality Control mengambil 500 bohlam secara acak untuk diuji ketahanan masa pakainya. Tentukan manakah yang merupakan populasi dan manakah yang merupakan sampel!",
                "known": "100.000 bohlam diproduksi, 500 bohlam diuji.",
                "asked": "Identifikasi populasi dan sampel.",
                "steps": [
                    [
                        "Langkah 1: Identifikasi Keseluruhan Objek",
                        "Populasi adalah seluruh 100.000 bohlam LED yang diproduksi pada hari tersebut."
                    ],
                    [
                        "Langkah 2: Identifikasi Subgrup Terpilih",
                        "Sampel adalah 500 bohlam LED yang dipilih secara acak untuk diuji."
                    ]
                ],
                "conclusion": "Populasi: 100.000 bohlam (N), Sampel: 500 bohlam (n)."
            },
            "takeaways": [
                "Populasi adalah kelompok semesta lengkap, sedangkan sampel adalah bagian representatifnya.",
                "Metode sampling acak yang tepat menghindarkan kesimpulan dari bias kesalahan.",
                "Statistika mentransformasikan tumpukan data mentah menjadi wawasan bermakna."
            ],
            "quiz": [
                "Karakteristik numerik yang dihitung dari seluruh anggota populasi disebut sebagai?",
                [
                    "Parameter",
                    "Statistik",
                    "Sampel"
                ],
                0,
                "Karakteristik populasi disebut Parameter (seperti rata-rata mu), sedangkan karakteristik sampel disebut Statistik (seperti rata-rata x-bar)."
            ]
        },
        {
            "title": "Anatomi: Ukuran Pemusatan (Mean, Median, Modus) & Ketahanan Outlier",
            "objectives": [
                "Menghitung rata-rata aritmetika (Mean), nilai tengah (Median), dan nilai yang paling sering muncul (Modus).",
                "Memahami sensitivitas Mean terhadap nilai pencilan ekstrem (outlier).",
                "Memilih ukuran pemusatan yang paling tepat dan adil berdasarkan bentuk distribusi data."
            ],
            "hook": "Jika sembilan orang buruh berpenghasilan Rp 3 juta per bulan sedang duduk di sebuah kafe, lalu masuklah Elon Musk (dengan kekayaan triliunan rupiah) bergabung ke dalam kafe tersebut. Tiba-tiba rata-rata (Mean) penghasilan orang di kafe itu melonjak menjadi Rp 10 miliar per orang! Apakah sembilan buruh itu tiba-tiba kaya mendadak? Tentu tidak! Di sinilah letak jebakan Mean: Mean sangat rapuh terhadap angka ekstrem (outlier), sedangkan Median (nilai tengah) tetap kokoh dan jujur!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-bullseye text-primary\"></i> 1. Tiga Pilar Ukuran Pemusatan Data</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Mean (Rata-rata Hitung $\\bar{x}$):</strong> Jumlah seluruh nilai data dibagi dengan banyaknya data:\n                  \\[ \\bar{x} = \\frac{\\sum x_i}{n} \\]\n                </li>\n                <li><strong>Median (Nilai Tengah):</strong> Nilai data yang berada tepat di tengah setelah data <strong>diurutkan dari terkecil ke terbesar</strong>. Sangat tahan (robust) terhadap pencilan ekstrem.</li>\n                <li><strong>Modus:</strong> Nilai data yang memiliki frekuensi kemunculan paling tinggi.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Jika datamu berdistribusi miring (skewed) atau memiliki angka ekstrem—seperti data gaji karyawan, harga properti rumah, atau durasi pengguna di website—selalu laporkan MEDIAN, bukan Mean!",
            "pitfall": "Jangan lupa mengurutkan data dari terkecil ke terbesar terlebih dahulu sebelum mencari Median! Jika jumlah data genap, Median adalah rata-rata dari dua angka yang berada di tengah.",
            "fun_fact": "Dalam platform e-commerce seperti Tokopedia dan Amazon, algoritma penentuan harga barang rekomendasi mengabaikan Mean dan menggunakan Median harga pasar untuk melindungi pengguna dari manipulasi harga penjual nakal.",
            "formula": "\\bar{x} = \\frac{\\sum_{i=1}^n x_i}{n} \\quad ; \\quad \\text{Med} = x_{\\frac{n+1}{2}} \\quad (n \\text{ ganjil})",
            "formula_params": [
                [
                    "\\bar{x}",
                    "Mean (rata-rata sampel)."
                ],
                [
                    "\\sum x_i",
                    "Total jumlah seluruh nilai data mentah."
                ],
                [
                    "n",
                    "Jumlah total sampel data observasi."
                ]
            ],
            "formula_intuition": "Membagi rata beban nilai secara merata ke setiap anggota kumpulan data.",
            "example": {
                "question": "Diberikan data nilai kuis 7 siswa: 70, 75, 80, 80, 85, 90, 100. Tentukan: (a) Mean, (b) Median, dan (c) Modus!",
                "known": "Data terurut n = 7: [70, 75, 80, 80, 85, 90, 100].",
                "asked": "Mean, Median, Modus.",
                "steps": [
                    [
                        "Langkah 1: Menghitung Mean",
                        "Total = $70 + 75 + 80 + 80 + 85 + 90 + 100 = 580$.<br>$\\bar{x} = \\frac{580}{7} \\approx 82.86$."
                    ],
                    [
                        "Langkah 2: Menentukan Median",
                        "Data sudah terurut. Posisi tengah data ke-$(7+1)/2 = 4$. Nilai data ke-4 adalah 80. Maka Median = 80."
                    ],
                    [
                        "Langkah 3: Menentukan Modus",
                        "Angka 80 muncul sebanyak 2 kali (paling sering dibanding angka lain). Maka Modus = 80."
                    ]
                ],
                "conclusion": "Mean = 82.86, Median = 80, dan Modus = 80."
            },
            "takeaways": [
                "Mean membagi rata seluruh nilai data namun rentan terhadap outlier.",
                "Median adalah nilai tengah yang kebal terhadap angka ekstrem.",
                "Modus adalah nilai dengan frekuensi kemunculan terbanyak."
            ],
            "quiz": [
                "Diberikan data: 4, 6, 8, 10, 100. Manakah ukuran pemusatan yang paling baik mewakili nilai tipikal kelompok tersebut?",
                [
                    "Median (nilai 8)",
                    "Mean (nilai 25.6)",
                    "Modus"
                ],
                0,
                "Angka 100 adalah outlier ekstrem yang mendistorsi Mean menjadi 25.6. Median (8) jauh lebih jujur mewakili kelompok mayoritas."
            ]
        },
        {
            "title": "Mekanika: Ukuran Penyebaran (Varians, Standar Deviasi & Z-Score)",
            "objectives": [
                "Memahami konsep dispersi data: seberapa jauh data menyebar dari nilai rata-ratanya.",
                "Menghitung Varians Sampel (s^2) dan Standar Deviasi Sampel (s) dengan pembagi derjat kebebasan (n - 1).",
                "Menghitung Z-Score untuk menstandarisasi dan membandingkan dua distribusi nilai yang berbeda."
            ],
            "hook": "Dua orang pasien disuntik obat penurun demam. Obat A menurunkan suhu pasien rata-rata 3 derajat dengan standar deviasi 0.1 derajat. Obat B menurunkan suhu rata-rata 3 derajat dengan standar deviasi 4 derajat! Rata-ratanya sama persis, tetapi obat B bisa membekukan pasien atau memicu kejang fatal! Rata-rata saja TIDAK PERNAH CUKUP: kamu wajib mengetahui seberapa besar 'Standar Deviasi' (risiko variabilitas) dari data tersebut!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-arrows-expand text-primary\"></i> 1. Standar Deviasi Sampel (s)</h3>\n              <p>Standar deviasi mengukur rata-rata jarak penyimpangan setiap titik data terhadap nilai rata-ratanya:</p>\n              \\[ s = \\sqrt{\\frac{\\sum (x_i - \\bar{x})^2}{n - 1}} \\]\n              <ul class=\"dic-list\">\n                <li><strong>Standar Deviasi Kecil ($s \\to 0$):</strong> Data bersifat homogen (seragam dan mengumpul rapat di sekitar rata-rata).</li>\n                <li><strong>Standar Deviasi Besar:</strong> Data bersifat heterogen (sangat bervariasi dan menyebar jauh).</li>\n                <li><strong>Koreksi Bessel ($n - 1$):</strong> Pembagi sampel menggunakan $n - 1$ (bukan $n$) untuk mengoreksi bias agar estimasi varians tidak terlalu optimis.</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-calculator text-primary\"></i> 2. Skor Standar (Z-Score)</h3>\n              <p>Z-Score mengukur berapa unit standar deviasi suatu nilai data mentah $x$ berada di atas atau di bawah rata-rata:</p>\n              \\[ Z = \\frac{x - \\bar{x}}{s} \\]\n            </div>\n            ",
            "pro_tip": "Aturan praktis Z-Score: Jika nilai $Z > +2$ atau $Z < -2$, data tersebut tergolong 'Luar Biasa / Anomali' (hanya terjadi pada kurang dari 5% populasi normal)!",
            "pitfall": "Jangan lupa bahwa Standar Deviasi adalah AKAR KUADRAT dari Varians ($s = \\sqrt{s^2}$). Varians memiliki satuan kuadrat (seperti $\\text{kg}^2$), sedangkan Standar Deviasi kembali ke satuan asli data (seperti $\\text{kg}$)!",
            "fun_fact": "Dalam dunia investasi keuangan kuantitatif Wall Street, Standar Deviasi dikenal sebagai 'Volatilitas' yang menjadi indikator utama untuk mengukur risiko fluktuasi harga saham.",
            "formula": "s^2 = \\frac{\\sum (x_i - \\bar{x})^2}{n - 1} \\quad ; \\quad s = \\sqrt{s^2} \\quad ; \\quad Z = \\frac{x - \\mu}{\\sigma}",
            "formula_params": [
                [
                    "s^2",
                    "Varians sampel."
                ],
                [
                    "s",
                    "Standar deviasi sampel."
                ],
                [
                    "n - 1",
                    "Derajat kebebasan (Koreksi Bessel)."
                ],
                [
                    "Z",
                    "Z-Score (nilai terstandarisasi)."
                ]
            ],
            "formula_intuition": "Mengkuadratkan deviasi agar tanda negatif tidak saling menghilangkan, lalu menarik akarnya kembali ke skala semula.",
            "example": {
                "question": "Diberikan sampel data: [6, 8, 10]. Hitung rata-rata ($\bar{x}$), varians sampel ($s^2$), dan standar deviasi ($s$)!",
                "known": "Data n = 3: 6, 8, 10.",
                "asked": "Mean, Varians, Standar Deviasi.",
                "steps": [
                    [
                        "Langkah 1: Hitung Nilai Rata-Rata",
                        "$\\bar{x} = \\frac{6 + 8 + 10}{3} = \\frac{24}{3} = 8$."
                    ],
                    [
                        "Langkah 2: Hitung Kuadrat Deviasi Setiap Data $(x_i - \\bar{x})^2$",
                        "$(6 - 8)^2 = (-2)^2 = 4$.<br>$(8 - 8)^2 = 0^2 = 0$.<br>$(10 - 8)^2 = 2^2 = 4$."
                    ],
                    [
                        "Langkah 3: Jumlahkan Kuadrat Deviasi",
                        "$\\sum (x_i - \\bar{x})^2 = 4 + 0 + 4 = 8$."
                    ],
                    [
                        "Langkah 4: Hitung Varians dengan Pembagi (n - 1)",
                        "$s^2 = \\frac{8}{3 - 1} = \\frac{8}{2} = 4$."
                    ],
                    [
                        "Langkah 5: Ambil Akar Kuadrat untuk Standar Deviasi",
                        "$s = \\sqrt{4} = 2$."
                    ]
                ],
                "conclusion": "Rata-rata = 8, Varians = 4, dan Standar Deviasi = 2."
            },
            "takeaways": [
                "Standar deviasi mengukur keragaman dispersi data di sekitar rata-rata.",
                "Pembagi sampel menggunakan $(n - 1)$ untuk menghilangkan bias sampling.",
                "Z-Score menstandarkan data ke dalam distribusi baku berpusat di nol."
            ],
            "quiz": [
                "Budi mendapat nilai ujian 85 pada kelas dengan rata-rata 70 dan standar deviasi 5. Berapakah nilai Z-score Budi?",
                [
                    "+3.0",
                    "+1.5",
                    "+2.0"
                ],
                0,
                "Z = (x - mean) / sd = (85 - 70) / 5 = 15 / 5 = +3.0 (Prestasi 3 standar deviasi di atas rata-rata kelas)."
            ]
        },
        {
            "title": "Pemodelan: Distribusi Normal Baku & Deteksi Kualitas Industri",
            "objectives": [
                "Memahami kurva lonceng Distribusi Normal Gauss yang simetris sempurna.",
                "Menerapkan Aturan Empiris 68-95-99.7% dalam analisis probabilitas populasi.",
                "Memodelkan pengawasan mutu (Quality Control) dan toleransi presisi manufaktur."
            ],
            "hook": "Mengapa bentuk tinggi badan manusia, berat buah apel di pohon, IQ masyarakat, hingga kesalahan pengukuran teleskop semuanya memiliki pola distribusi yang sama: Kurva Lonceng (Bell Curve)? Fenomena ajaib alam ini dirumuskan oleh Teorema Batas Pusat (Central Limit Theorem): jumlah dari banyak faktor acak independen akan selalu berkonvergen membentuk Distribusi Normal!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-bell-fill text-primary\"></i> 1. Karakteristik Kurva Normal Gauss</h3>\n              <p>Distribusi normal bersifat simetris sempurna di sekitar nilai rata-rata $\\mu$, di mana nilai <strong>$\\text{Mean} = \\text{Median} = \\text{Modus}$</strong> berimpit tepat di puncak lonceng.</p>\n              <h4 class=\"fw-bold text-info mt-3\"><i class=\"bi bi-percent\"></i> Aturan Empiris 68 - 95 - 99.7%:</h4>\n              <ul class=\"dic-list\">\n                <li><strong>$\\mu \\pm 1\\sigma$:</strong> Memuat sekitar <strong>68.2%</strong> dari seluruh populasi.</li>\n                <li><strong>$\\mu \\pm 2\\sigma$:</strong> Memuat sekitar <strong>95.4%</strong> dari seluruh populasi.</li>\n                <li><strong>$\\mu \\pm 3\\sigma$:</strong> Memuat sekitar <strong>99.7%</strong> dari seluruh populasi (hanya 0.3% yang berada di luar batas 3-sigma).</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Dalam industri manufaktur semikonduktor chip komputer (seperti TSMC dan Intel), metodologi 'Six Sigma' menuntut tingkat cacat produksi kurang dari 3.4 komponen per satu juta produk yang dihasilkan!",
            "pitfall": "Jangan berasumsi seluruh data pasti terdistribusi normal! Selalu periksa histogram data mentah untuk mendeteksi apakah data memiliki kemiringan (skewness) sebelum menerapkan aturan 68-95-99.7%.",
            "fun_fact": "Wajah fisikawan penemu distribusi normal, Carl Friedrich Gauss, bersama kurva lonceng normal diabadikan pada pecahan uang kertas 10 Deutsche Mark Jerman sebelum digantikan oleh mata uang Euro.",
            "formula": "P(\\mu - \\sigma \\le X \\le \\mu + \\sigma) \\approx 68\\% \\quad ; \\quad P(\\mu - 2\\sigma \\le X \\le \\mu + 2\\sigma) \\approx 95\\%",
            "formula_params": [
                [
                    "\\mu",
                    "Rata-rata populasi."
                ],
                [
                    "\\sigma",
                    "Simpangan baku populasi."
                ]
            ],
            "formula_intuition": "Menetapkan batas sebaran alami fenomena populasi di alam semesta.",
            "example": {
                "question": "Sebuah mesin pengisi otomatis botol minuman memiliki rata-rata volume $\\mu = 500\\text{ mL}$ dengan simpangan baku $\\sigma = 10\\text{ mL}$. Menggunakan Aturan Empiris, perkirakan berapa persentase botol yang memiliki volume isi antara 480 mL dan 520 mL!",
                "known": "$\\mu = 500\\text{ mL}$, $\\sigma = 10\\text{ mL}$.",
                "asked": "Persentase botol pada rentang 480 mL s.d. 520 mL.",
                "steps": [
                    [
                        "Langkah 1: Hitung Jarak Deviasi Batas Terhadap Rata-Rata",
                        "Batas bawah 480 = $500 - 2(10) = \\mu - 2\\sigma$.<br>Batas atas 520 = $500 + 2(10) = \\mu + 2\\sigma$."
                    ],
                    [
                        "Langkah 2: Terapkan Aturan Empiris 2-Sigma",
                        "Berdasarkan Aturan Empiris Distribusi Normal, rentang $[\\mu - 2\\sigma, \\mu + 2\\sigma]$ mencakup tepat sekitar 95% dari seluruh populasi."
                    ]
                ],
                "conclusion": "Sekitar 95% botol yang diproduksi memiliki volume aman antara 480 mL dan 520 mL."
            },
            "takeaways": [
                "Distribusi normal berbentuk lonceng simetris sempurna di sekitar mean.",
                "Aturan 68-95-99.7% membagi probabilitas populasi berdasarkan kelipatan standar deviasi.",
                "Distribusi normal adalah standar acuan pengawasan mutu industri dan riset sains data."
            ],
            "quiz": [
                "Berapa persentase data populasi yang berada dalam rentang 1 standar deviasi dari rata-rata (μ ± 1σ) pada distribusi normal?",
                [
                    "Sekitar 68%",
                    "Sekitar 95%",
                    "Sekitar 99.7%"
                ],
                0,
                "Aturan empiris menetapkan 68% populasi berada pada rentang 1-sigma, 95% pada 2-sigma, dan 99.7% pada 3-sigma."
            ]
        },
        {
            "title": "Capstone: Audit Kinerja Akademik Ribuan Siswa & Analisis Anomali",
            "objectives": [
                "Mengintegrasikan Mean, Standar Deviasi, dan Z-Score untuk mengevaluasi mutu kurikulum ujian nasional.",
                "Mendeteksi skor anomali kecurangan atau pencilan (outlier) menggunakan kriteria statistika formal.",
                "Menyusun rekomendasi kebijakan pendidikan berbasis bukti data numerik."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditugaskan sebagai Chief Data Scientist Kementerian Pendidikan. Dalam ujian standarisasi nasional, 10.000 siswa memperoleh nilai rata-rata 72 dengan standar deviasi 8. Seorang siswa dari sekolah terpencil berhasil meraih skor 96! Kepala dinas mencurigai adanya kebocoran soal. Menggunakan analisis Z-score dan distribusi normal, buktikan secara matematis apakah skor 96 tergolong pencilan anomali ekstrem (outlier) ataukah prestasi wajar!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-trophy-fill text-warning\"></i> Skenario Audit Statistika Skala Besar</h3>\n              <p>Dalam statistika inferensial dan deteksi anomali:</p>\n              \\[ Z = \\frac{x - \\mu}{\\sigma} \\]\n              <p>Jika nilai $|Z| > 3.0$, skor tersebut dinamakan <strong>Pencilan Ekstrem (Extreme Outlier)</strong> yang probabilitas kemunculannya secara acak murni kurang dari $0.15\\%$ (sangat jarang terjadi).</p>\n            </div>\n            ",
            "pro_tip": "Dalam deteksi anomali fraud industri perbankan (kartu kredit), transaksi dengan skor Z > 3.5 secara otomatis dibekukan oleh sistem AI untuk verifikasi OTP!",
            "pitfall": "Skor Z yang ekstrem membuktikan bahwa data tersebut sangat langka secara statistik, tetapi TIDAK membuktikan secara langsung adanya kecurangan tanpa bukti fisik investigasi lanjutan!",
            "fun_fact": "Metode analisis statistik Z-Score dan distribusi t-Student diciptakan oleh William Sealy Gosset pada tahun 1908 saat bekerja sebagai ahli kimia pembuat bir di pabrik bir Guinness Irlandia!",
            "formula": "Z_{\\text{score}} = \\frac{x - \\mu}{\\sigma} \\quad ; \\quad \\text{Outlier jika } |Z| > 3.0",
            "formula_params": [
                [
                    "x",
                    "Nilai siswa yang diuji (96)."
                ],
                [
                    "\\mu",
                    "Rata-rata nasional (72)."
                ],
                [
                    "\\sigma",
                    "Standar deviasi nasional (8)."
                ]
            ],
            "formula_intuition": "Menghitung berapa langkah simpangan baku posisi siswa melampaui rata-rata nasional.",
            "example": {
                "question": "Rata-rata nilai ujian nasional adalah $\\mu = 72$ dengan standar deviasi $\\sigma = 8$. Hitung nilai Z-Score untuk siswa dengan skor $x = 96$, lalu simpulkan status statistika siswa tersebut!",
                "known": "$\\mu = 72, \\sigma = 8, x = 96$.",
                "asked": "Nilai Z-score dan interpretasi status outlier.",
                "steps": [
                    [
                        "Langkah 1: Masukkan ke Rumus Z-Score",
                        "$Z = \\frac{96 - 72}{8}$."
                    ],
                    [
                        "Langkah 2: Evaluasi Pengurangan Pembilang",
                        "$96 - 72 = 24$."
                    ],
                    [
                        "Langkah 3: Bagi dengan Standar Deviasi",
                        "$Z = \\frac{24}{8} = +3.0$."
                    ],
                    [
                        "Langkah 4: Analisis Distribusi Probabilitas",
                        "Skor $Z = +3.0$ tepat berada di batas $3\\sigma$. Siswa tersebut berada di peringkat $0.15\\%$ teratas nasional (hanya sekitar 15 dari 10.000 siswa yang mampu mencapai skor ini)."
                    ]
                ],
                "conclusion": "Nilai Z-score adalah +3.0. Prestasi tersebut merupakan pencilan superior luar biasa (Top 0.15% nasional) yang layak diverifikasi secara khusus oleh tim penilai."
            },
            "takeaways": [
                "Z-Score mentransformasikan nilai mentah menjadi unit perbandingan yang adil antar-distribusi.",
                "Nilai $|Z| \\ge 3.0$ mengidentifikasi peristiwa statistik yang sangat langka di alam semesta.",
                "Selamat! Kamu telah menguasai seluruh kurikulum Statistika & Analisis Data dengan standar industri profesional!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE STATISTIKA: Jika seorang siswa mendapat skor Z = +3.0 pada distribusi normal, berapakah persentase siswa lain yang nilainya LEBIH TINGGI dari siswa tersebut?",
                [
                    "Sekitar 0.15%",
                    "Sekitar 2.5%",
                    "Sekitar 5%"
                ],
                0,
                "Karena 99.7% data berada di dalam rentang ±3σ, maka sisa 0.3% terbagi dua di ekor kanan dan kiri, menyisakan hanya sekitar 0.15% di atas +3σ."
            ]
        }
    ]
}
