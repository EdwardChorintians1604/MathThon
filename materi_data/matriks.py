# -*- coding: utf-8 -*-
DATA = {
    "title": "Matriks & Aljabar Linear",
    "short": "Matriks",
    "icon": "bi-grid-3x3",
    "color": "#ec4899",
    "desc": "Kuasai susunan data tabular matriks, operasi baris-kolom, perkalian matriks, determinan, invers, dan penerapannya dalam transformasi grafis dan kriptografi.",
    "babs": [
        {
            "title": "Fondasi: Tabel Data Multi-Dimensi Menuju Matriks",
            "objectives": [
                "Memahami matriks sebagai representasi susunan angka berbaris dan berkolom.",
                "Menentukan ordo matriks (ukuran m x n) dan mengidentifikasi entri a_ij.",
                "Mengenali representasi matriks dalam database relasional, citra digital (pixel), dan grafika komputer."
            ],
            "hook": "Tahukah kamu bahwa gambar foto di layar smartphonemu sebenarnya adalah matriks raksasa? Setiap piksel adalah sebuah sel entri matriks yang memuat angka intensitas warna merah (R), hijau (G), dan biru (B). Ketika kamu menerapkan filter foto hitam-putih atau vintage di Instagram, smartphonemu sedang melakukan operasi perkalian matriks secara real-time terhadap jutaan angka tersebut!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-grid-fill text-primary\"></i> 1. Pengertian Matriks & Notasi Ordo</h3>\n              <p>Matriks adalah sekumpulan bilangan real yang disusun secara teratur dalam baris horizontal dan kolom vertikal di dalam tanda kurung biasa $($ $)$ atau kurung siku $[$ $]$:</p>\n              \\[ A = \\begin{pmatrix} a_{11} & a_{12} & \\dots & a_{1n} \\\\ a_{21} & a_{22} & \\dots & a_{2n} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ a_{m1} & a_{m2} & \\dots & a_{mn} \\end{pmatrix} \\]\n              <ul class=\"dic-list\">\n                <li><strong>Baris:</strong> Susunan angka yang berbaris menyamping (horizontal).</li>\n                <li><strong>Kolom:</strong> Susunan angka yang tegak menurun (vertikal).</li>\n                <li><strong>Ordo Matriks ($m \\times n$):</strong> Menyatakan ukuran matriks dengan $m$ adalah jumlah baris dan $n$ adalah jumlah kolom.</li>\n                <li><strong>Entri $a_{ij}$:</strong> Elemen matriks yang terletak pada baris ke-$i$ dan kolom ke-$j$.</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mengingat urutan ordo matriks $m \\times n$, ingat kata kunci 'BASKOM' (BAris dikali KOloM). Baris selalu disebut pertama, kolom selalu disebut kedua!",
            "pitfall": "Jangan tertukar antara indeks baris dan kolom! Elemen $a_{23}$ artinya berada pada Baris ke-2 dan Kolom ke-3, BUKAN sebaliknya!",
            "fun_fact": "Film fiksi ilmiah legendaris 'The Matrix' (1999) mengambil namanya dari istilah matematika matriks, melambangkan dunia simulasi digital yang tersusun dari kisi-kisi kode numerik hijau yang mengalir.",
            "formula": "A_{m \\times n} = [a_{ij}] \\quad (i = 1, \\dots, m; \\ j = 1, \\dots, n) \\quad ; \\quad A^T_{n \\times m} \\implies (a^T)_{ij} = a_{ji}",
            "formula_params": [
                [
                    "m",
                    "Banyaknya baris matriks."
                ],
                [
                    "n",
                    "Banyaknya kolom matriks."
                ],
                [
                    "a_{ij}",
                    "Elemen pada baris ke-i dan kolom ke-j."
                ],
                [
                    "A^T",
                    "Matriks transpose (pertukaran baris menjadi kolom)."
                ]
            ],
            "formula_intuition": "Matriks mengorganisasikan data multi-variabel dalam struktur teratur agar operasi komputasi dapat dieksekusi secara simultan.",
            "example": {
                "question": "Diketahui matriks $M = \\begin{pmatrix} 3 & -1 & 5 \\\\ 2 & 7 & 0 \\end{pmatrix}$. Tentukan: (a) Ordo matriks M, (b) Nilai elemen $a_{13}$ dan $a_{22}$, dan (c) Bentuk transpose matriks $M^T$!",
                "known": "Matriks M berisikan 2 baris dan 3 kolom.",
                "asked": "Ordo, elemen tertentu, dan $M^T$.",
                "steps": [
                    [
                        "Langkah 1: Menentukan Ordo",
                        "Matriks memiliki 2 baris dan 3 kolom, maka ordonya adalah $2 \\times 3$."
                    ],
                    [
                        "Langkah 2: Menemukan Elemen $a_{13}$ dan $a_{22}$",
                        "$a_{13}$ = baris 1, kolom 3 = 5.<br>$a_{22}$ = baris 2, kolom 2 = 7."
                    ],
                    [
                        "Langkah 3: Menentukan Matriks Transpose $M^T$",
                        "Ubah baris menjadi kolom: Baris 1 $(3, -1, 5)$ menjadi Kolom 1. Baris 2 $(2, 7, 0)$ menjadi Kolom 2.<br>$M^T = \\begin{pmatrix} 3 & 2 \\\\ -1 & 7 \\\\ 5 & 0 \\end{pmatrix}$ berordo $3 \\times 2$."
                    ]
                ],
                "conclusion": "Ordo matriks adalah $2 \\times 3$, $a_{13} = 5, a_{22} = 7$, dan $M^T$ berukuran $3 \\times 2$."
            },
            "takeaways": [
                "Matriks adalah susunan bilangan berordo $m \\times n$ (baris $\\times$ kolom).",
                "Indeks $a_{ij}$ menunjukkan elemen pada baris ke-i dan kolom ke-j.",
                "Transpose matriks $A^T$ menukar baris menjadi kolom dan kolom menjadi baris."
            ],
            "quiz": [
                "Jika matriks A memiliki 3 baris dan 4 kolom, maka matriks transpose A^T memiliki ordo?",
                [
                    "4 x 3",
                    "3 x 4",
                    "12 x 1"
                ],
                0,
                "Transpose membalik dimensi ordo: matriks berordo m x n menjadi berordo n x m, sehingga 3 x 4 menjadi 4 x 3."
            ]
        },
        {
            "title": "Anatomi: Jenis-Jenis Matriks Baku & Operasi Aljabar Dasar",
            "objectives": [
                "Mengenali jenis matriks khusus: Matriks Persegi, Matriks Nol, Matriks Diagonal, dan Matriks Identitas I.",
                "Melakukan penjumlahan dan pengurangan matriks yang berordo sama.",
                "Melakukan perkalian matriks dengan skalar k."
            ],
            "hook": "Dalam aljabar angka, bilangan 1 adalah 'angka netral' perkalian ($5 \\times 1 = 5$). Apakah ada entitas yang setara dengan angka 1 di dunia matriks? Ya, namanya adalah Matriks Identitas I! Matriks istimewa ini memiliki angka 1 di diagonal utama dan 0 di tempat lainnya. Jika matriks apa pun dikalikan dengan I, hasilnya tidak akan berubah!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-collection-fill text-primary\"></i> 1. Jenis-Jenis Matriks Khusus</h3>\n              <ul class=\"dic-list\">\n                <li><strong>Matriks Persegi:</strong> Jumlah baris sama dengan jumlah kolom ($m = n$). Memiliki diagonal utama.</li>\n                <li><strong>Matriks Identitas ($I$):</strong> Matriks persegi dengan diagonal utama bernilai 1 dan elemen lainnya bernilai 0: $I = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}$.</li>\n                <li><strong>Matriks Nol ($O$):</strong> Seluruh elemennya bernilai 0.</li>\n              </ul>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-plus-slash-minus text-primary\"></i> 2. Penjumlahan & Perkalian Skalar Matriks</h3>\n              <p>Dua matriks HANYA DAPAT dijumlahkan atau dikurangkan jika <strong>ordonya sama persis</strong>. Operasi dilakukan dengan menjumlahkan elemen yang seletak (posisi yang sama):</p>\n              \\[ \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} + \\begin{pmatrix} e & f \\\\ g & h \\end{pmatrix} = \\begin{pmatrix} a+e & b+f \\\\ c+g & d+h \\end{pmatrix} \\]\n            </div>\n            ",
            "pro_tip": "Penjumlahan matriks bersifat komutatif ($A + B = B + A$), tetapi ingat: perkalian matriks NANTINYA TIDAK BERSIFAT KOMUTATIF ($AB \\neq BA$)!",
            "pitfall": "Jangan mencoba menjumlahkan matriks berordo $2 \\times 2$ dengan matriks $2 \\times 3$. Operasi tersebut tidak terdefinisi dalam matematika!",
            "fun_fact": "Dalam komputasi neural network (AI), lapisan layer feedforward melakukan perkalian skalar dan penambahan bias matrix terhadap miliaran bobot koneksi saraf tiruan secara paralel di GPU.",
            "formula": "A + B = [a_{ij} + b_{ij}] \\quad ; \\quad kA = [k \\cdot a_{ij}] \\quad ; \\quad A \\cdot I = I \\cdot A = A",
            "formula_params": [
                [
                    "A, B",
                    "Matriks-matriks dengan ordo yang identik."
                ],
                [
                    "k",
                    "Skalar bilangan riil."
                ],
                [
                    "I",
                    "Matriks identitas."
                ]
            ],
            "formula_intuition": "Penjumlahan matriks setara dengan menjumlahkan multi-data koordinat secara serentak pada posisi spasial yang bersesuaian.",
            "example": {
                "question": "Diketahui $A = \\begin{pmatrix} 2 & 3 \\\\ -1 & 4 \\end{pmatrix}$ dan $B = \\begin{pmatrix} 5 & -2 \\\\ 3 & 1 \\end{pmatrix}$. Tentukan matriks $2A + B$!",
                "known": "Matriks A dan B berordo $2 \\times 2$.",
                "asked": "Hasil dari $2A + B$.",
                "steps": [
                    [
                        "Langkah 1: Kalikan Matriks A dengan Skalar 2",
                        "$2A = \\begin{pmatrix} 2(2) & 2(3) \\\\ 2(-1) & 2(4) \\end{pmatrix} = \\begin{pmatrix} 4 & 6 \\\\ -2 & 8 \\end{pmatrix}$."
                    ],
                    [
                        "Langkah 2: Jumlahkan dengan Matriks B Elemen per Elemen",
                        "$2A + B = \\begin{pmatrix} 4 + 5 & 6 + (-2) \\\\ -2 + 3 & 8 + 1 \\end{pmatrix} = \\begin{pmatrix} 9 & 4 \\\\ 1 & 9 \\end{pmatrix}$."
                    ]
                ],
                "conclusion": "Hasil dari $2A + B$ adalah $\\begin{pmatrix} 9 & 4 \\\\ 1 & 9 \\end{pmatrix}$."
            },
            "takeaways": [
                "Syarat mutlak penjumlahan matriks: kedua matriks wajib memiliki ordo yang sama persis.",
                "Perkalian skalar $kA$ mengalikan seluruh elemen di dalam matriks dengan bilangan $k$.",
                "Matriks Identitas I berperan seperti angka 1 pada perkalian aritmatika biasa."
            ],
            "quiz": [
                "Jika $P = \\begin{pmatrix} 4 & 2 \\\\ 1 & 0 \\end{pmatrix}$ dan $Q = \\begin{pmatrix} 1 & -1 \\\\ 3 & 2 \\end{pmatrix}$, berapakah nilai elemen baris 1 kolom 2 dari $P - Q$?",
                [
                    "3",
                    "1",
                    "-3"
                ],
                0,
                "Elemen baris 1 kolom 2 adalah 2 - (-1) = 2 + 1 = 3."
            ]
        },
        {
            "title": "Mekanika: Prosedur Perkalian Matriks, Determinan & Invers 2x2",
            "objectives": [
                "Menguasai algoritma perkalian dua matriks menggunakan metode 'Baris kali Kolom' (Dot Product Baris-Kolom).",
                "Menghitung determinan matriks persegi berordo 2x2 (ad - bc).",
                "Menghitung matriks invers A^-1 dan mengidentifikasi syarat matriks singular."
            ],
            "hook": "Mengapa aturan perkalian matriks tidak mengalikan angka yang seletak saja? Karena perkalian matriks dirancang untuk memodelkan sistem persamaan linier simultan dan transformasi geometri! Kaidah 'Baris kali Kolom' adalah mesin komputasi paling fundamental yang menggerakkan pemrosesan grafis 3D dan algoritma deep learning di seluruh planet bumi saat ini.",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-x-circle-fill text-primary\"></i> 1. Syarat & Kaidah Perkalian Matriks</h3>\n              <p>Perkalian matriks $A \\times B$ <strong>HANYA BISA DILAKUKAN</strong> jika:<br>\n              <strong>Jumlah Kolom Matriks A = Jumlah Baris Matriks B</strong></p>\n              \\[ A_{m \\times p} \\times B_{p \\times n} = C_{m \\times n} \\]\n              <p>Setiap entri $c_{ij}$ diperoleh dari perkalian titik antara Baris ke-$i$ pada matriks A dengan Kolom ke-$j$ pada matriks B.</p>\n            </div>\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-calculator text-primary\"></i> 2. Determinan & Invers Matriks 2x2</h3>\n              <p>Untuk matriks $A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$:</p>\n              <ul class=\"dic-list\">\n                <li><strong>Determinan:</strong> $\\det(A) = |A| = ad - bc$. Determinan mengukur faktor penskalaan luas area transformasi.</li>\n                <li><strong>Matriks Invers ($A^{-1}$):</strong> Kebalikan matriks yang memenuhi $A \\cdot A^{-1} = I$:\n                  \\[ A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix} \\]\n                </li>\n                <li><strong>Matriks Singular:</strong> Matriks dengan $\\det(A) = 0$. Matriks singular <strong>TIDAK MEMILIKI INVERS</strong>!</li>\n              </ul>\n            </div>\n            ",
            "pro_tip": "Untuk mengingat rumus Adjoin matriks 2x2: Tukar posisi diagonal utama (a dan d saling bertukar), dan kalikan diagonal samping dengan minus (-b dan -c)!",
            "pitfall": "Perkalian matriks TIDAK KOMUTATIF! Secara umum $AB \\neq BA$. Bahkan seringkali jika AB terdefinisi, BA belum tentu bisa dikalikan karena ketidaksesuaian ordo!",
            "fun_fact": "Determinan matriks pertama kali ditemukan oleh matematikawan Jepang Seki Kowa pada tahun 1683 (lebih awal dari Gottfried Leibniz di Eropa) untuk memecahkan sistem persamaan simultan pertanian beras tradisional.",
            "formula": "\\det(A) = ad - bc \\quad ; \\quad A^{-1} = \\frac{1}{\\det(A)}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix} \\quad (\\det(A) \\neq 0)",
            "formula_params": [
                [
                    "ad - bc",
                    "Determinan skalar matriks 2x2."
                ],
                [
                    "A^{-1}",
                    "Matriks balikan / invers."
                ],
                [
                    "\\det(A) = 0",
                    "Kondisi singular di mana matriks tidak dapat diinverskan."
                ]
            ],
            "formula_intuition": "Invers matriks adalah analogi aljabar dari pembagian $1/x$, yang membatalkan efek transformasi linear matriks asal.",
            "example": {
                "question": "Diberikan matriks $A = \\begin{pmatrix} 4 & 2 \\\\ 3 & 2 \\end{pmatrix}$. Hitung determinan matriks A, lalu tentukan matriks invers $A^{-1}$!",
                "known": "$a = 4, b = 2, c = 3, d = 2$.",
                "asked": "$\\det(A)$ dan $A^{-1}$.",
                "steps": [
                    [
                        "Langkah 1: Menghitung Determinan ad - bc",
                        "$\\det(A) = (4)(2) - (2)(3) = 8 - 6 = 2$ (Karena $\\det \\neq 0$, invers ada)."
                    ],
                    [
                        "Langkah 2: Membentuk Matriks Adjoin",
                        "Tukar diagonal utama (4 dan 2 bertukar) dan negatifkan diagonal samping: $\\begin{pmatrix} 2 & -2 \\\\ -3 & 4 \\end{pmatrix}$."
                    ],
                    [
                        "Langkah 3: Mengalikan dengan $1/\\det(A)$",
                        "$A^{-1} = \\frac{1}{2} \\begin{pmatrix} 2 & -2 \\\\ -3 & 4 \\end{pmatrix} = \\begin{pmatrix} 1 & -1 \\\\ -1.5 & 2 \\end{pmatrix}$."
                    ]
                ],
                "conclusion": "Determinan bernilai 2, dan invers matriksnya adalah $\\begin{pmatrix} 1 & -1 \\\\ -1.5 & 2 \\end{pmatrix}$."
            },
            "takeaways": [
                "Perkalian matriks mengikuti prinsip Baris kali Kolom.",
                "Determinan matriks 2x2 dirumuskan dengan $ad - bc$.",
                "Matriks memiliki invers jika dan hanya jika nilai determinannya tidak sama dengan nol (non-singular)."
            ],
            "quiz": [
                "Berapakah determinan dari matriks $K = \\begin{pmatrix} 5 & 3 \\\\ 2 & 4 \\end{pmatrix}$?",
                [
                    "14",
                    "26",
                    "20"
                ],
                0,
                "det(K) = (5)(4) - (3)(2) = 20 - 6 = 14."
            ]
        },
        {
            "title": "Pemodelan: Transformasi Geometri 2D & Penyelesaian Sistem Persamaan Matriks",
            "objectives": [
                "Menerapkan matriks invers untuk menyelesaikan Sistem Persamaan Linear Dua Variabel (SPLDV).",
                "Memodelkan transformasi geometri koordinat (Rotasi, Refleksi, Dilatasi) menggunakan representasi matriks.",
                "Menyelesaikan studi kasus transaksi logistik bisnis menggunakan formulasi AX = B."
            ],
            "hook": "Ketika karakter game 3D bergerak, melompat, atau berputar menghadap kamera, mesin permainan tidak menghitung fisika secara manual satu per satu. GPU mengalikan vektor koordinat karakter dengan Matriks Transformasi Affine! Selain itu, persamaan pembelian barang multi-variabel dapat diselesaikan hanya dengan satu baris rumus matriks: $X = A^{-1}B$!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-braces-asterisk text-primary\"></i> 1. Menyelesaikan SPLDV dengan Metode Matriks</h3>\n              <p>Sistem persamaan linear:</p>\n              \\[ \\begin{cases} ax + by = p \\\\ cx + dy = q \\end{cases} \\implies \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} p \\\\ q \\end{pmatrix} \\]\n              <p>Dalam bentuk matriks singkat: $AX = B$. Solusi variabel diperoleh secara langsung dengan mengalikan kedua ruas dengan invers matriks A dari kiri:</p>\n              \\[ X = A^{-1} B \\]\n            </div>\n            ",
            "pro_tip": "Jangan kalikan dari kanan! Karena perkalian matriks tidak komutatif, $AX = B \\implies X = A^{-1}B$, BUKAN $B A^{-1}$!",
            "pitfall": "Jika determinan matriks koefisien A bernilai nol, sistem persamaan tidak memiliki solusi unik (garis sejajar atau berimpit).",
            "fun_fact": "Kamera smartphone modern menerapkan stabilisasi gambar optik digital (EIS) dengan memutar balik matriks rotasi gyro sensor secara real-time untuk menghasilkan rekaman video yang sangat mulus bebas guncangan.",
            "formula": "AX = B \\implies X = A^{-1}B = \\frac{1}{ad-bc}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}\\begin{pmatrix} p \\\\ q \\end{pmatrix}",
            "formula_params": [
                [
                    "A",
                    "Matriks koefisien variabel."
                ],
                [
                    "X",
                    "Vektor kolom variabel tak diketahui $\\begin{pmatrix} x \\\\ y \\end{pmatrix}$."
                ],
                [
                    "B",
                    "Vektor kolom konstanta target $\\begin{pmatrix} p \\\\ q \\end{pmatrix}$."
                ]
            ],
            "formula_intuition": "Mengubah manipulasi eliminasi aljabar bertahap menjadi satu operasi perkalian matriks invers kompak.",
            "example": {
                "question": "Selesaikan sistem persamaan linear berikut menggunakan metode matriks: $2x + y = 8$ dan $3x + 2y = 13$!",
                "known": "$A = \\begin{pmatrix} 2 & 1 \\\\ 3 & 2 \\end{pmatrix}$ dan $B = \\begin{pmatrix} 8 \\\\ 13 \\end{pmatrix}$.",
                "asked": "Nilai variabel x dan y.",
                "steps": [
                    [
                        "Langkah 1: Hitung Determinan Matriks A",
                        "$\\det(A) = (2)(2) - (1)(3) = 4 - 3 = 1$."
                    ],
                    [
                        "Langkah 2: Tentukan Matriks Invers $A^{-1}$",
                        "$A^{-1} = \\frac{1}{1} \\begin{pmatrix} 2 & -1 \\\\ -3 & 2 \\end{pmatrix} = \\begin{pmatrix} 2 & -1 \\\\ -3 & 2 \\end{pmatrix}$."
                    ],
                    [
                        "Langkah 3: Hitung $X = A^{-1}B$",
                        "$X = \\begin{pmatrix} 2 & -1 \\\\ -3 & 2 \\end{pmatrix} \\begin{pmatrix} 8 \\\\ 13 \\end{pmatrix} = \\begin{pmatrix} (2)(8) + (-1)(13) \\\\ (-3)(8) + (2)(13) \\end{pmatrix} = \\begin{pmatrix} 16 - 13 \\\\ -24 + 26 \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}$."
                    ]
                ],
                "conclusion": "Diperoleh solusi unik: $x = 3$ dan $y = 2$."
            },
            "takeaways": [
                "Sistem persamaan linear dapat direpresentasikan secara ringkas dalam format matriks $AX = B$.",
                "Solusi variabel diperoleh melalui perkalian invers matriks $X = A^{-1}B$.",
                "Metode matriks sangat efisien untuk diimplementasikan ke dalam program komputer."
            ],
            "quiz": [
                "Jika sistem matriks $AX = B$ memiliki $\\det(A) = 0$, maka?",
                [
                    "Sistem tidak memiliki solusi unik",
                    "Sistem pasti memiliki solusi x = 0, y = 0",
                    "Sistem dapat diselesaikan dengan mudah"
                ],
                0,
                "Determinan nol artinya matriks tidak memiliki invers sehingga tidak ada solusi unik."
            ]
        },
        {
            "title": "Capstone: Sistem Kriptografi Sandi Hill Cipher Berbasis Matriks",
            "objectives": [
                "Mengintegrasikan konsep perkalian matriks, determinan, dan modulo aritmetika untuk membangun sistem enkripsi pesan rahasia.",
                "Melakukan enkripsi pasangan huruf teks asli menjadi ciphertext sandi.",
                "Melakukan dekripsi pesan sandi menggunakan matriks invers kunci."
            ],
            "hook": "Selamat datang di Tantangan Capstone! Selama Perang Dunia, matematikawan Lester S. Hill menciptakan Hill Cipher, sistem kriptografi poligrafik pertama yang mengamankan pesan militer rahasia menggunakan aljabar matriks. Pesan teks diubah menjadi angka alfabet ($A=0, B=1, dst$), lalu dikalikan dengan Matriks Kunci Rahasia. Tanpa matriks invers kunci, musuh mustahil dapat membaca isi pesan tersebut!",
            "concepts": "\n            <div class=\"dic-concept-card mb-4\">\n              <h3 class=\"dic-h3\"><i class=\"bi bi-shield-lock-fill text-warning\"></i> Skenario Kriptografi Hill Cipher</h3>\n              <p>Pesan rahasia dienkripsi dengan persamaan matriks modulo 26 (jumlah huruf alfabet):</p>\n              \\[ C = (K \\cdot P) \\pmod{26} \\]\n              <p>Dan penerima pesan memulihkannya menggunakan invers matriks kunci:</p>\n              \\[ P = (K^{-1} \\cdot C) \\pmod{26} \\]\n            </div>\n            ",
            "pro_tip": "Dalam kriptografi matriks, matriks kunci wajib memiliki determinan yang koprima (relatif prima) terhadap modulus 26 agar invers modularnya selalu ada!",
            "pitfall": "Jangan lupa bahwa operasi pembagian pada invers matriks kriptografi digantikan oleh invers perkalian modular (modulo 26)!",
            "fun_fact": "Hill Cipher adalah cikal bakal konsep kriptografi blok modern seperti AES (Advanced Encryption Standard) yang kini melindungi data perbankan, kata sandi akun, dan privasi jutaan pengguna di seluruh dunia.",
            "formula": "C = (K \\cdot P) \\pmod{26} \\quad ; \\quad P = (K^{-1} \\cdot C) \\pmod{26}",
            "formula_params": [
                [
                    "P",
                    "Vektor teks asli (plaintext)."
                ],
                [
                    "K",
                    "Matriks kunci enkripsi rahasia berordo 2x2."
                ],
                [
                    "C",
                    "Vektor teks tersandi (ciphertext)."
                ]
            ],
            "formula_intuition": "Mentransformasikan posisi koordinat huruf alfabet ke dimensi ruang baru yang teracak matematis.",
            "example": {
                "question": "Enkripsikan pasangan huruf 'HI' menggunakan matriks kunci rahasia $K = \\begin{pmatrix} 3 & 2 \\\\ 5 & 7 \\end{pmatrix}$ dengan ketentuan huruf A=0, B=1, C=2, ..., H=7, I=8!",
                "known": "Huruf H = 7, I = 8. Maka vektor $P = \\begin{pmatrix} 7 \\\\ 8 \\end{pmatrix}$. Matriks $K = \\begin{pmatrix} 3 & 2 \\\\ 5 & 7 \\end{pmatrix}$.",
                "asked": "Vektor sandi C dan pasangan huruf ciphertext yang dihasilkan.",
                "steps": [
                    [
                        "Langkah 1: Kalikan Matriks Kunci dengan Vektor P",
                        "$K \\cdot P = \\begin{pmatrix} 3 & 2 \\\\ 5 & 7 \\end{pmatrix} \\begin{pmatrix} 7 \\\\ 8 \\end{pmatrix} = \\begin{pmatrix} 3(7) + 2(8) \\\\ 5(7) + 7(8) \\end{pmatrix} = \\begin{pmatrix} 21 + 16 \\\\ 35 + 56 \\end{pmatrix} = \\begin{pmatrix} 37 \\\\ 91 \\end{pmatrix}$."
                    ],
                    [
                        "Langkah 2: Terapkan Modulo 26",
                        "$37 \\pmod{26} = 11$.<br>$91 = (3 \\times 26) + 13 \\implies 91 \\pmod{26} = 13$."
                    ],
                    [
                        "Langkah 3: Konversi Angka Kembali ke Huruf Alfabet",
                        "Angka 11 = Huruf L.<br>Angka 13 = Huruf N."
                    ]
                ],
                "conclusion": "Teks asli 'HI' berhasil dienkripsi menjadi teks sandi 'LN'."
            },
            "takeaways": [
                "Matriks adalah fondasi penting dalam sains keamanan informasi dan kriptografi modern.",
                "Dekripsi pesan rahasia mengandalkan sifat pembatalan dari matriks invers $K^{-1}$.",
                "Selamat! Kamu telah menguasai konsep matriks dari teori dasar hingga aplikasi rekayasa keamanan digital!"
            ],
            "quiz": [
                "🏆 TANTANGAN CAPSTONE MATRIKS: Jika determinan matriks kunci enkripsi adalah det(K) = 11, berapakah nilai ad - bc dari matriks kunci tersebut?",
                [
                    "11",
                    "26",
                    "1"
                ],
                0,
                "Determinan matriks K didefinisikan secara langsung oleh ad - bc, sehingga bernilai 11."
            ]
        }
    ]
}
