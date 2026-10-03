# -*- coding: utf-8 -*-
"""
Materi Pembelajaran Berstandar Dicoding: Vektor & Geometri Ruang
"""

DATA = {
    "title": "Vektor & Geometri Ruang",
    "short": "Vektor",
    "icon": "bi-arrows-move",
    "color": "#3b82f6",
    "desc": "Kuasai besaran vektor di ruang 2D dan 3D, aljabar vektor, magnitudo, dot product, cross product, proyeksi ortogonal, serta aplikasinya dalam game engine, fisika gerak, dan robotika.",
    "babs": [
        {
            "title": "Fondasi: Konsep Intuitif & Pengenalan Vektor",
            "objectives": [
                "Membedakan secara tegas antara besaran skalar (hanya memiliki nilai) dan besaran vektor (memiliki nilai dan arah).",
                "Memahami representasi grafis panah berarah di bidang koordinat Cartesius 2D dan ruang 3D.",
                "Menghitung panjang (magnitudo) vektor dari titik pangkal ke titik ujung menggunakan perluasan Teorema Pythagoras.",
                "Menentukan dan membentuk vektor satuan (unit vector) melalui proses normalisasi arah."
            ],
            "hook": "Bayangkan kamu sedang menerbangkan drone pengantar barang di area terbuka dengan kecepatan mesin 30 km/jam ke arah utara. Tiba-tiba, hembusan angin kencang berkecepatan 40 km/jam bertiup ke arah timur. Ke mana drone kamu akan benar-benar bergerak dan berapa kecepatan totalnya terhadap tanah? Jika kamu hanya menjumlahkan angkanya (30 + 40 = 70 km/jam), jawabanmu SALAH BESAR! Fisika alam semesta tidak bekerja seperti itu. Drone kamu akan bergerak miring ke arah timur laut dengan kecepatan tepat 50 km/jam. Inilah keajaiban besaran vektor yang memiliki nilai sekaligus orientasi arah!",
            "concepts": """
            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-compass-fill text-primary"></i> 1. Skalar vs Vektor: Perbedaan Fundamental</h3>
              <p>Dalam sains, rekayasa teknologi, dan matematika, semua besaran di alam semesta diklasifikasikan ke dalam dua kategori besar:</p>
              <div class="row g-3 my-2">
                <div class="col-md-6">
                  <div class="p-3 rounded h-100" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
                    <div class="fw-bold text-info mb-1"><i class="bi bi-circle"></i> Besaran Skalar</div>
                    <p class="small text-muted mb-0">Hanya memiliki <strong>nilai numerik (magnitudo)</strong> dan satuan, tanpa bergantung pada orientasi arah. Operasi perhitungannya mengikuti hukum aritmetika dasar aljabar biasa.<br><br>
                    <strong>Contoh:</strong> Suhu ($27^\\circ\\text{C}$), Massa ($65\\text{ kg}$), Waktu ($15\\text{ detik}$), Kelajuan mobil ($60\\text{ km/jam}$), dan Energi listrik ($1200\\text{ Joule}$).</p>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="p-3 rounded h-100" style="background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.25);">
                    <div class="fw-bold text-primary mb-1"><i class="bi bi-arrow-up-right"></i> Besaran Vektor</div>
                    <p class="small text-muted mb-0">Wajib memiliki <strong>nilai (magnitudo)</strong> SEKALIGUS <strong>arah tujuan spesifik</strong> di dalam ruang. Perhitungannya harus mempertimbangkan sudut dan geometri ruang.<br><br>
                    <strong>Contoh:</strong> Perpindahan ($10\\text{ meter ke timur}$), Kecepatan ($60\\text{ km/jam arah } 45^\\circ$), Gaya dorong roket ($5000\\text{ N ke atas}$), dan Medan magnet bumi.</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-bounding-box text-primary"></i> 2. Representasi Geometris & Vektor Posisi</h3>
              <p>Secara geometris, vektor digambarkan sebagai ruas garis berarah (anak panah):</p>
              <ul class="dic-list">
                <li><strong>Titik Pangkal (Initial Point):</strong> Titik awal tempat fenomena atau gaya bermula (ekor panah).</li>
                <li><strong>Titik Ujung (Terminal Point):</strong> Titik akhir yang ditunjuk oleh ujung kepala panah.</li>
                <li><strong>Arah Panah:</strong> Menunjukkan orientasi lintasan atau aksi gaya di ruang.</li>
                <li><strong>Panjang Ruas Garis:</strong> Merepresentasikan besar atau magnitudo vektor secara proporsional.</li>
                <li><strong>Vektor Posisi (Position Vector):</strong> Vektor yang titik pangkalnya selalu terikat pada titik asal koordinat $O(0,0,0)$ dan ujungnya berada di titik koordinat $P(x,y,z)$, dinotasikan sebagai $\\vec{r} = \\vec{OP} = \\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix}$.</li>
              </ul>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-bullseye text-primary"></i> 3. Vektor Satuan & Konsep Normalisasi</h3>
              <p>Seringkali dalam komputasi 3D dan fisika, kita hanya membutuhkan <em>informasi arah murni</em> dari suatu vektor tanpa memedulikan panjang aslinya. Vektor yang memiliki panjang tepat 1 satuan disebut <strong>Vektor Satuan (Unit Vector)</strong>, dilambangkan dengan tanda topi $\\hat{u}$ (u-hat). Proses mengubah vektor sembarang menjadi vektor satuan disebut <strong>Normalisasi</strong>.</p>
            </div>
            """,
            "pro_tip": "Dalam game engine modern seperti Unity atau Unreal Engine, fungsi `vector.normalized` digunakan ribuan kali per detik untuk menentukan arah hadap karakter (facing direction) dan arah tembakan proyektil tanpa mengubah kecepatan dasarnya!",
            "pitfall": "Miskonsepsi fatal: Jangan menjumlahkan panjang dua vektor secara langsung seperti skalar ($|\\vec{a} + \\vec{b}| \\neq |\\vec{a}| + |\\vec{b}|$). Penjumlahan langsung hanya berlaku jika kedua vektor sejajar dan searah sempurna!",
            "fun_fact": "Aljabar vektor modern diformulasikan oleh fisikawan Amerika Josiah Willard Gibbs dan matematikawan Inggris Oliver Heaviside pada akhir abad ke-19 untuk menggantikan notasi kuaternion William Rowan Hamilton yang terlalu rumit dalam memodelkan medan elektromagnetik Maxwell.",
            "formula": r"|\vec{v}| = \sqrt{x^2 + y^2 + z^2} \quad ; \quad \hat{u} = \frac{\vec{v}}{|\vec{v}|} = \left(\frac{x}{|\vec{v}|}, \frac{y}{|\vec{v}|}, \frac{z}{|\vec{v}|}\right)",
            "formula_params": [
                ("x, y, z", "Komponen skalar proyeksi vektor terhadap sumbu Kartesius X, Y, dan Z."),
                (r"|\vec{v}|", "Magnitudo atau panjang mutlak vektor (selalu bernilai non-negatif $\\ge 0$)."),
                (r"\hat{u}", "Vektor satuan (unit vector) yang memiliki magnitudo tepat 1 satuan ($|\\hat{u}| = 1$).")
            ],
            "formula_intuition": "Rumus panjang vektor di ruang 3D adalah generalisasi Teorema Pythagoras bertingkat. Jarak proyeksi di bidang XY adalah $d = \\sqrt{x^2 + y^2}$, lalu digabungkan secara tegak lurus dengan elevasi sumbu Z sehingga menghasilkan diagonal ruang total $\\sqrt{d^2 + z^2} = \\sqrt{x^2 + y^2 + z^2}$.",
            "example": {
                "question": "Sebuah sensor robotik mendeteksi keberadaan objek rintangan pada koordinat spasial P(3, 4, 12) meter dari titik pusat sensor O(0,0,0). Tentukan jarak garis lurus langsung dari sensor ke objek tersebut, lalu hitung vektor satuan yang menunjukkan arah pandang sensor ke target!",
                "known": "Titik pangkal O(0,0,0), titik sasaran P(3, 4, 12). Maka komponen vektor $\\vec{v} = (3, 4, 12)$.",
                "asked": "Magnitudo jarak $|\\vec{v}|$ dan vektor satuan $\\hat{u}$.",
                "steps": [
                    ("Langkah 1: Menghitung Kuadrat Masing-Masing Komponen", "Hitung kuadrat tiap sumbu: $x^2 = 3^2 = 9$, $y^2 = 4^2 = 16$, $z^2 = 12^2 = 144$."),
                    ("Langkah 2: Menjumlahkan Komponen & Mengambil Akar Kuadrat", "Jumlahkan total kuadrat: $9 + 16 + 144 = 169$. Maka panjang vektor adalah $|\\vec{v}| = \\sqrt{169} = 13\\text{ meter}$."),
                    ("Langkah 3: Melakukan Normalisasi untuk Mendapatkan Vektor Satuan", "Bagi setiap komponen vektor dengan panjang totalnya: $\\hat{u} = \\frac{(3, 4, 12)}{13} = \\left(\\frac{3}{13}, \\frac{4}{13}, \\frac{12}{13}\\right) \\approx (0.231, 0.308, 0.923)$.")
                ],
                "conclusion": "Objek berjarak tepat 13 meter dari sensor, dengan vektor satuan penunjuk arah $\\hat{u} = \\left(\\frac{3}{13}, \\frac{4}{13}, \\frac{12}{13}\\right)$ yang memiliki magnitudo tepat 1."
            },
            "takeaways": [
                "Besaran skalar hanya memiliki nilai numerik, sedangkan besaran vektor memiliki nilai dan orientasi arah spasial.",
                "Panjang (magnitudo) vektor 3D dihitung menggunakan rumus Pythagoras ruang: $|\\vec{v}| = \\sqrt{x^2 + y^2 + z^2}$.",
                "Vektor satuan $\\hat{u} = \\vec{v} / |\\vec{v}|$ berfungsi menyimpan informasi orientasi arah murni dengan panjang terstandarisasi 1 satuan."
            ],
            "quiz": (
                "Sebuah partikel bergerak dengan vektor posisi $\\vec{r} = (6, 8, 0)\\text{ meter}$. Berapakah panjang lintasan partikel tersebut dari pusat koordinat, dan berapakah vektor satuannya?",
                ["Panjang 10 meter dengan vektor satuan (0.6, 0.8, 0)", "Panjang 14 meter dengan vektor satuan (6, 8, 0)", "Panjang 10 meter dengan vektor satuan (1, 1, 0)"],
                0,
                r"|r| = \sqrt{6^2 + 8^2 + 0^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ meter}. Vektor satuannya adalah \hat{u} = (6/10, 8/10, 0/10) = (0.6, 0.8, 0)."
            )
        },
        {
            "title": "Anatomi: Notasi, Kaidah & Sifat Baku Vektor",
            "objectives": [
                "Menguasai ragam notasi penulisan vektor: Vektor Basis $(\\hat{i}, \\hat{j}, \\hat{k})$, Vektor Kolom, dan Vektor Baris.",
                "Menerapkan aturan aljabar penjumlahan dan pengurangan vektor secara analitik dan geometrik.",
                "Menghitung vektor perpindahan antara dua titik sebarang menggunakan kaidah Ujung Kurang Pangkal ($\\vec{AB} = \\vec{B} - \\vec{A}$).",
                "Memahami operasi perkalian skalar terhadap vektor serta sifat-sifat komutatif, asosiatif, dan distributif."
            ],
            "hook": "Di dunia nyata, pergerakan jarang dimulai dari titik nol koordinat (0,0,0). Ketika seorang atlet berlari dari posisi A(2, 3, 1) ke posisi B(7, -1, 5), bagaimana kita memodelkan perpindahan geraknya secara matematis tanpa harus memindahkan lapangan lari ke titik origin? Notasi dan kaidah baku vektor memberikan bahasa matematika yang konsisten dan universal!",
            "concepts": """
            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-file-code-fill text-primary"></i> 1. Tiga Notasi Baku dalam Matematika & Komputasi</h3>
              <p>Sebuah vektor di ruang 3 dimensi dapat diekspresikan dalam tiga cara penulisan ekuivalen:</p>
              <ol class="dic-list">
                <li><strong>Notasi Basis Satuan Kartesius:</strong> $\\vec{v} = v_x\\hat{i} + v_y\\hat{j} + v_z\\hat{k}$, di mana $\\hat{i}=(1,0,0)$, $\\hat{j}=(0,1,0)$, $\\hat{k}=(0,0,1)$ adalah basis ortonormal standar pada sumbu X, Y, Z.</li>
                <li><strong>Notasi Vektor Kolom (Matrix Notation):</strong> $\\vec{v} = \\begin{pmatrix} v_x \\\\ v_y \\\\ v_z \\end{pmatrix}$. Format ini menjadi standar utama dalam aljabar linear, deep learning tensor, dan transformasi matriks.</li>
                <li><strong>Notasi Vektor Baris / Koordinat:</strong> $\\vec{v} = \\langle v_x, v_y, v_z \\rangle$ atau $(v_x, v_y, v_z)$. Sering digunakan dalam penulisan ringkas kode pemrograman.</li>
              </ol>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-arrows-collapse text-primary"></i> 2. Kaidah Vektor Perpindahan (Ujung - Pangkal)</h3>
              <p>Jika diketahui dua titik koordinat sebarang di dalam ruang, yaitu titik pangkal $A(x_1, y_1, z_1)$ dan titik ujung $B(x_2, y_2, z_2)$, maka vektor perpindahan dari A ke B dirumuskan sebagai:</p>
              <div class="text-center my-3 p-3 rounded" style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.08);">
                \\[ \\vec{AB} = \\vec{b} - \\vec{a} = (x_2 - x_1)\\hat{i} + (y_2 - y_1)\\hat{j} + (z_2 - z_1)\\hat{k} \\]
              </div>
              <p class="small text-muted">Ingat aturan emas: <strong>Vektor = Koordinat Titik Ujung dikurangi Koordinat Titik Pangkal</strong>.</p>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-calculator text-primary"></i> 3. Operasi Aljabar & Skalasi Vektor</h3>
              <p>Operasi aljabar pada vektor dilakukan secara independen pada masing-masing komponen sumbu:</p>
              <ul class="dic-list">
                <li><strong>Penjumlahan Vektor:</strong> $\\vec{a} + \\vec{b} = (a_x + b_x)\\hat{i} + (a_y + b_y)\\hat{j} + (a_z + b_z)\\hat{k}$. Secara geometris mengikuti metode jajaran genjang atau metode segitiga (head-to-tail).</li>
                <li><strong>Perkalian Skalar (Skalasi):</strong> Mengalikan skalar bilangan riil $k$ dengan vektor $\\vec{a}$ menghasilkan $k\\vec{a} = (ka_x)\\hat{i} + (ka_y)\\hat{j} + (ka_z)\\hat{k}$.
                  <ul>
                    <li>Jika $k > 1$: Vektor diperpanjang searah.</li>
                    <li>Jika $0 < k < 1$: Vektor diperpendek searah.</li>
                    <li>Jika $k < 0$: Vektor berbalik arah sebesar $180^\\circ$ (inversi arah).</li>
                  </ul>
                </li>
              </ul>
            </div>
            """,
            "pro_tip": "Untuk membuktikan apakah dua buah vektor sejajar (kolinear), periksa apakah salah satu vektor merupakan kelipatan skalar dari vektor lainnya (yaitu $\\vec{a} = k\\vec{b}$). Jika rasio $a_x/b_x = a_y/b_y = a_z/b_z = k$, maka kedua vektor pasti sejajar!",
            "pitfall": "Jangan tertukar arah vektor perpindahan! Vektor $\\vec{AB} = \\vec{B} - \\vec{A}$, sedangkan vektor $\\vec{BA} = \\vec{A} - \\vec{B} = -\\vec{AB}$. Arahnya berkebalikan $180^\\circ$ meskipun panjangnya sama persis!",
            "fun_fact": "Dalam kecerdasan buatan (NLP & LLM) seperti ChatGPT, kata-kata dipetakan ke dalam vektor berdimensi ribuan yang disebut 'Word Embeddings'. Kata 'Raja' dikurangi 'Pria' ditambah 'Wanita' secara mengejutkan menghasilkan vektor yang sangat dekat dengan kata 'Ratu'!",
            "formula": r"\vec{AB} = \begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix} \quad ; \quad k\vec{a} + m\vec{b} = \begin{pmatrix} k a_x + m b_x \\ k a_y + m b_y \\ k a_z + m b_z \end{pmatrix}",
            "formula_params": [
                (r"\vec{AB}", "Vektor perpindahan dengan titik pangkal A dan titik ujung B."),
                (r"x_A, y_A, z_A", "Koordinat titik asal / pangkal."),
                (r"x_B, y_B, z_B", "Koordinat titik tujuan / ujung."),
                ("k, m", "Faktor pengali skalar riil.")
            ],
            "formula_intuition": "Komponen-komponen ruang Cartesius X, Y, dan Z bersifat ortogonal (saling independen), sehingga manipulasi aljabar pada sumbu X tidak pernah mengganggu nilai pada sumbu Y atau Z.",
            "example": {
                "question": "Diketahui dua buah titik di ruang 3D: titik awal P(1, -2, 4) dan titik akhir Q(5, 2, 1). Tentukan vektor perpindahan $\\vec{PQ}$, hitung panjang jarak $|\\vec{PQ}|$, dan tentukan vektor $3\\vec{PQ}$!",
                "known": "Titik P = (1, -2, 4) dan Titik Q = (5, 2, 1).",
                "asked": "Vektor $\\vec{PQ}$, panjang $|\\vec{PQ}|$, dan vektor hasil skalasi $3\\vec{PQ}$.",
                "steps": [
                    ("Langkah 1: Menghitung Komponen Vektor Perpindahan (Ujung - Pangkal)", "$\\vec{PQ} = (5 - 1)\\hat{i} + (2 - (-2))\\hat{j} + (1 - 4)\\hat{k} = 4\\hat{i} + 4\\hat{j} - 3\\hat{k}$."),
                    ("Langkah 2: Menghitung Magnitudo Panjang Lintasan PQ", "$|\\vec{PQ}| = \\sqrt{4^2 + 4^2 + (-3)^2} = \\sqrt{16 + 16 + 9} = \\sqrt{41} \\approx 6.40\\text{ satuan}$."),
                    ("Langkah 3: Mengalikan Vektor dengan Skalar k = 3", "$3\\vec{PQ} = 3(4\\hat{i} + 4\\hat{j} - 3\\hat{k}) = 12\\hat{i} + 12\\hat{j} - 9\\hat{k} = \\begin{pmatrix} 12 \\\\ 12 \\\\ -9 \\end{pmatrix}$.")
                ],
                "conclusion": "Vektor perpindahan $\\vec{PQ} = (4, 4, -3)$ dengan panjang $\\sqrt{41}$ satuan, dan hasil perbesaran 3 kali lipatnya adalah $(12, 12, -9)$."
            },
            "takeaways": [
                "Vektor perpindahan dari titik A ke titik B selalu dihitung dengan kaidah Ujung Kurang Pangkal: $\\vec{AB} = \\vec{B} - \\vec{A}$.",
                "Operasi penjumlahan, pengurangan, dan perkalian skalar dievaluasi secara terpisah pada masing-masing komponen sumbu koordinat.",
                "Perkalian dengan skalar negatif membalikkan arah vektor $180^\\circ$ ke arah yang berlawanan."
            ],
            "quiz": (
                "Jika diketahui $\\vec{u} = 3\\hat{i} - 2\\hat{j} + \\hat{k}$ dan $\\vec{v} = -\\hat{i} + 4\\hat{j} + 2\\hat{k}$, berapakah vektor resultan dari $2\\vec{u} - \\vec{v}$?",
                ["7i - 8j + 0k", "5i + 2j + 4k", "7i - 8j + 4k"],
                0,
                r"2\vec{u} = 6\hat{i} - 4\hat{j} + 2\hat{k}. Maka 2\vec{u} - \vec{v} = (6 - (-1))\hat{i} + (-4 - 4)\hat{j} + (2 - 2)\hat{k} = 7\hat{i} - 8\hat{j} + 0\hat{k}."
            )
        },
        {
            "title": "Mekanika: Prosedur Perhitungan & Operasi Lanjutan Vektor",
            "objectives": [
                "Menguasai perhitungan Perkalian Titik (Dot Product / Scalar Product) secara komponen aljabar dan rumus sudut geometris.",
                "Menentukan besar sudut apit $\\theta$ antara dua vektor menggunakan fungsi invers cosinus.",
                "Menguji dan membuktikan kondisi dua vektor saling tegak lurus (ortogonal) dengan kriteria $\\vec{a} \\cdot \\vec{b} = 0$.",
                "Menghitung proyeksi skalar ortogonal dan proyeksi vektor ortogonal suatu vektor terhadap vektor lain."
            ],
            "hook": "Bagaimana kartu grafis modern (GPU) di komputer kamu dapat merender efek pencahayaan fotorealistik secara real-time pada game 3D? GPU menghitung sudut datang sinar lampu terhadap permukaan poligon dengan melakukan miliaran kalkulasi Dot Product per detik! Jika sudutnya tegak lurus, permukaannya menerima cahaya maksimum; jika membelakangi sinar, permukaannya menjadi gelap total.",
            "concepts": """
            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-dot text-primary"></i> 1. Perkalian Titik (Dot Product / Skalar)</h3>
              <p>Perkalian titik antara dua vektor $\\vec{a}$ dan $\\vec{b}$ menghasilkan <strong>sebuah bilangan skalar murni</strong> (bukan vektor). Ada dua cara ekuivalen untuk mengevaluasinya:</p>
              <ul class="dic-list">
                <li><strong>Formula Aljabar Komponen:</strong> Cukup kalikan komponen yang sebidang dan jumlahkan seluruhnya:
                  \\[ \\vec{a} \\cdot \\vec{b} = a_x b_x + a_y b_y + a_z b_z \\]
                </li>
                <li><strong>Formula Geometri Sudut Apit:</strong>
                  \\[ \\vec{a} \\cdot \\vec{b} = |\\vec{a}| |\\vec{b}| \\cos\\theta \\]
                  di mana $\\theta$ adalah sudut apit terkecil antara kedua vektor ($0^\\circ \\le \\theta \\le 180^\\circ$).
                </li>
              </ul>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-symmetry-vertical text-primary"></i> 2. Kriteria Ortogonalitas (Tegak Lurus)</h3>
              <p>Karena nilai $\\cos 90^\\circ = 0$, maka kita memperoleh teorema paling krusial dalam aljabar vektor:</p>
              <div class="p-3 rounded mb-3" style="background:rgba(16,185,129,0.08); border-left:4px solid #10b981;">
                <div class="fw-bold text-success mb-1">Teorema Ortogonalitas Baku:</div>
                <div class="text-light">Dua vektor non-nol $\\vec{a}$ dan $\\vec{b}$ saling <strong>tegak lurus (ortogonal)</strong> jika dan hanya jika hasil perkalian titik keduanya sama dengan nol: <strong>$\\vec{a} \\cdot \\vec{b} = 0$</strong>.</div>
              </div>
              <p>Sebaliknya, besar sudut apit dapat dihitung dengan mengisolasi nilai cosinus: $\\cos\\theta = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}| |\\vec{b}|}$.</p>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-box-arrow-in-down-right text-primary"></i> 3. Proyeksi Ortogonal: Skalar vs Vektor</h3>
              <p>Proyeksi ortogonal adalah 'panjang bayangan' tegak lurus yang dijatuhkan oleh satu vektor ke atas garis vektor lainnya:</p>
              <ul class="dic-list">
                <li><strong>Proyeksi Skalar Ortogonal $\\vec{a}$ pada $\\vec{b}$ ($|\\vec{c}|$):</strong> Menghasilkan nilai panjang skalar (bisa bertanda negatif jika sudut tumpul):
                  \\[ |\\vec{c}| = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|} \\]
                </li>
                <li><strong>Proyeksi Vektor Ortogonal $\\vec{a}$ pada $\\vec{b}$ ($\\vec{c}$):</strong> Menghasilkan vektor baru yang searah dengan $\\vec{b}$:
                  \\[ \\vec{c} = \\left( \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|^2} \\right) \\vec{b} \\]
                </li>
              </ul>
            </div>
            """,
            "pro_tip": "Untuk mengingat penyebut rumus proyeksi: jika soal meminta proyeksi vektor A pada B, maka yang menjadi landasan adalah B, sehingga pembaginya selalu panjang vektor landasan $|\\vec{b}|$!",
            "pitfall": "Jangan keliru: Hasil dari Dot Product adalah bilangan SKALAR (misal: 15), bukan vektor! Jangan pernah menuliskan hasil dot product dengan notasi $\\hat{i}, \\hat{j}, \\hat{k}$.",
            "fun_fact": "Konsep proyeksi ortogonal adalah tulang punggung algoritma PCA (Principal Component Analysis) dalam Machine Learning untuk mereduksi dimensi data besar dari ribuan variabel menjadi hanya beberapa variabel utama tanpa kehilangan informasi penting.",
            "formula": r"\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z = |\vec{a}| |\vec{b}| \cos\theta \quad ; \quad \vec{c}_{\text{proy}} = \left(\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|^2}\right)\vec{b}",
            "formula_params": [
                (r"\vec{a} \cdot \vec{b}", "Hasil perkalian skalar (bilangan riil murni)."),
                (r"\theta", "Sudut apit terkecil antara vektor $\\vec{a}$ dan $\\vec{b}$ ($0^\\circ \\le \\theta \\le 180^\\circ$)."),
                (r"\vec{c}_{\text{proy}}", "Vektor proyeksi ortogonal yang berimpit pada arah vektor landasan $\\vec{b}$.")
            ],
            "formula_intuition": "Dot product mengukur sejauh mana dua vektor 'bekerja sama' menunjuk ke arah yang sama. Nilai positif berarti sudut lancip, nol berarti independen/tegak lurus, dan negatif berarti saling berlawanan arah.",
            "example": {
                "question": "Diketahui vektor $\\vec{a} = (2, -1, 2)$ dan vektor $\\vec{b} = (4, 4, 2)$. Hitunglah hasil perkalian titik $\\vec{a} \\cdot \\vec{b}$, tentukan besar sudut apit $\\theta$, dan tentukan panjang proyeksi skalar $\\vec{a}$ pada $\\vec{b}$!",
                "known": "$\\vec{a} = (2, -1, 2)$ dan $\\vec{b} = (4, 4, 2)$.",
                "asked": "Dot product $\\vec{a} \\cdot \\vec{b}$, sudut $\\theta$, dan proyeksi skalar $|\\vec{c}|$.",
                "steps": [
                    ("Langkah 1: Menghitung Dot Product Aljabar", "$\\vec{a} \\cdot \\vec{b} = (2)(4) + (-1)(4) + (2)(2) = 8 - 4 + 4 = 8$."),
                    ("Langkah 2: Menghitung Magnitudo Kedua Vektor", "$|\\vec{a}| = \\sqrt{2^2 + (-1)^2 + 2^2} = \\sqrt{4 + 1 + 4} = \\sqrt{9} = 3$.<br>$|\\vec{b}| = \\sqrt{4^2 + 4^2 + 2^2} = \\sqrt{16 + 16 + 4} = \\sqrt{36} = 6$."),
                    ("Langkah 3: Menghitung Cosinus Sudut Apit", "$\\cos\\theta = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}| |\\vec{b}|} = \\frac{8}{(3)(6)} = \\frac{8}{18} = \\frac{4}{9} \\approx 0.4444$.<br>Maka $\\theta = \\arccos(0.4444) \\approx 63.6^\\circ$ (sudut lancip)."),
                    ("Langkah 4: Menghitung Proyeksi Skalar Ortogonal a pada b", "$|\\vec{c}| = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|} = \\frac{8}{6} = \\frac{4}{3} \\approx 1.33$ satuan panjang.")
                ],
                "conclusion": "Hasil dot product adalah 8, sudut apit kedua vektor adalah sekitar $63.6^\\circ$, dan panjang bayangan proyeksi skalar $\\vec{a}$ pada $\\vec{b}$ adalah $\\frac{4}{3}$ satuan."
            },
            "takeaways": [
                "Dot product aljabar dihitung dengan menjumlahkan hasil kali komponen sejenis: $a_x b_x + a_y b_y + a_z b_z$.",
                "Dua vektor saling tegak lurus (ortogonal) jika dan hanya jika $\\vec{a} \\cdot \\vec{b} = 0$.",
                "Proyeksi skalar mengukur panjang bayangan pada vektor tujuan, sedangkan proyeksi vektor memberikan bentuk vektor bayangannya."
            ],
            "quiz": (
                "Diberikan dua vektor $\\vec{u} = (m, 3, -2)$ dan $\\vec{v} = (4, -2, 3)$. Berapakah nilai skalar m agar kedua vektor tersebut saling tegak lurus (ortogonal)?",
                ["m = 3", "m = 4", "m = -3"],
                0,
                r"Syarat ortogonal: \vec{u} \cdot \vec{v} = 0 \implies (m)(4) + (3)(-2) + (-2)(3) = 0 \implies 4m - 6 - 6 = 0 \implies 4m = 12 \implies m = 3."
            )
        },
        {
            "title": "Pemodelan: Aplikasi Nyata & Studi Kasus Vektor",
            "objectives": [
                "Menerapkan konsep aljabar vektor pada fenomena mekanika fisika: Perhitungan Usaha Mekanika ($W = \\vec{F} \\cdot \\vec{s}$) dan Resultan Gaya Seimbang.",
                "Memodelkan sistem navigasi penerbangan dan maritim dengan mengintegrasikan vektor kecepatan mesin dan vektor gangguan fluida (angin/arus laut).",
                "Memahami pemodelan vektor dalam grafika komputer 3D, seperti simulasi pencahayaan Lambertian dan deteksi tabrakan (collision detection)."
            ],
            "hook": "Sebuah kapal kargo menyeberangi selat dengan haluan mesin lurus mengarah ke utara berkecepatan 15 knot. Namun arus laut transversal yang deras mengalir ke arah timur dengan kecepatan 8 knot. Jika nahkoda tidak memperhitungkan vektor resultan kecepatan, kapalnya akan melenceng bermil-mil dari pelabuhan tujuan! Di dunia penerbangan, autopilot pesawat jet komersial melakukan perhitungan vektor ini tanpa henti untuk menjamin pendaratan presisi di landasan pacu.",
            "concepts": """
            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-lightning-charge-fill text-primary"></i> 1. Pemodelan Usaha & Energi Mekanika (Work)</h3>
              <p>Dalam ilmu fisika, usaha didefinisikan secara presisi sebagai perkalian skalar antara vektor gaya $\\vec{F}$ yang bekerja dan vektor perpindahan $\\vec{s}$ yang dialami benda:</p>
              <div class="text-center my-3 p-3 rounded" style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.08);">
                \\[ W = \\vec{F} \\cdot \\vec{s} = F_x s_x + F_y s_y + F_z s_z = |\\vec{F}| |\\vec{s}| \\cos\\theta \\]
              </div>
              <p>Makna fisika mendalam: <em>Hanya komponen gaya yang bekerja searah dengan lintasan perpindahan yang menghasilkan kerja energi!</em> Jika gaya tegak lurus perpindahan ($\\theta = 90^\\circ$), maka usaha yang dilakukan adalah tepat <strong>0 Joule</strong> (seperti gaya gravitasi bumi pada satelit yang mengorbit melingkar sempurna).</p>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-airplane-fill text-primary"></i> 2. Navigasi & Kecepatan Relatif Vektor</h3>
              <p>Kecepatan aktual objek yang bergerak dalam medium fluida (seperti udara atau air) terhadap kerangka acuan tanah dinamakan <strong>Ground Velocity ($\\vec{v}_g$)</strong>. Kecepatan ini adalah hasil penjumlahan vektor:</p>
              <div class="text-center my-2">
                \\[ \\vec{v}_g = \\vec{v}_{heading} + \\vec{v}_{fluid} \\]
              </div>
              <p>Pilot menggunakan perhitungan trigonometri dan aljabar vektor untuk mengoreksi haluan (heading angle) agar vektor kecepatan ground speed tetap mengarah tepat ke bandara tujuan.</p>
            </div>

            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-sun-fill text-primary"></i> 3. Grafika Komputer: Pencahayaan Difus Lambertian</h3>
              <p>Dalam grafika 3D dan animasi film, intensitas cahaya pada permukaan poligon dihitung dengan mengalikan vektor normal permukaan $\\hat{N}$ dengan vektor arah datang sinar lampu $\\hat{L}$:</p>
              <div class="text-center my-2">
                \\[ I_{\\text{diffuse}} = I_0 \\cdot \\max(0, \\hat{N} \\cdot \\hat{L}) \\]
              </div>
              <p>Jika poligon menghadap tepat ke sumber cahaya ($\\hat{N} \\cdot \\hat{L} = 1$), poligon akan berwarna paling terang. Semakin miring sudutnya, intensitas cahaya semakin meredup.</p>
            </div>
            """,
            "pro_tip": "Saat memecahkan soal cerita fisika dengan vektor 3D, selalu uraikan informasi gaya dan koordinat ke dalam format komponen $\\hat{i}, \\hat{j}, \\hat{k}$ terlebih dahulu sebelum menghitung dot product!",
            "pitfall": "Perhatikan satuan internasional (SI)! Vektor gaya harus dalam satuan Newton (N), vektor perpindahan dalam meter (m), sehingga hasil usaha yang didapat valid dalam Joule ($1\\text{ J} = 1\\text{ N}\\cdot\\text{m}$).",
            "fun_fact": "Kendaraan antariksa Voyager 1 dan Voyager 2 menggunakan manuver gravitasi (Gravity Assist) yang memanfaatkan perubahan vektor kecepatan relatif terhadap planet Jupiter dan Saturnus untuk melempar wahana tersebut keluar dari tata surya tanpa memerlukan bahan bakar tambahan!",
            "formula": r"W = \vec{F} \cdot \vec{s} = (F_x s_x + F_y s_y + F_z s_z) \text{ Joule} \quad ; \quad \vec{v}_{\text{total}} = \vec{v}_1 + \vec{v}_2",
            "formula_params": [
                (r"\vec{F}", "Vektor gaya total yang bekerja pada benda (Newton)."),
                (r"\vec{s}", "Vektor perpindahan posisi lintasan benda (meter)."),
                ("W", "Usaha atau kerja mekanika yang dikonversi menjadi energi (Joule).")
            ],
            "formula_intuition": "Komponen gaya yang tegak lurus arah gerak tidak melakukan usaha karena tidak berkontribusi memindahkan benda ke arah lintasan tersebut.",
            "example": {
                "question": "Sebuah kabel derek menarik kontainer barang dengan vektor gaya $\\vec{F} = (50\\hat{i} + 30\\hat{j} + 20\\hat{k})\\text{ Newton}$. Akibat gaya tersebut, kontainer bergeser di atas lantai gudang dari koordinat awal A(2, 1, 0) meter menuju koordinat akhir B(8, 5, 0) meter. Tentukan vektor perpindahan $\\vec{s}$ kontainer dan hitunglah total usaha mekanika W yang dilakukan oleh kabel derek tersebut!",
                "known": "Gaya $\\vec{F} = (50, 30, 20)\\text{ N}$, Titik awal A(2, 1, 0) m, Titik akhir B(8, 5, 0) m.",
                "asked": "Vektor perpindahan $\\vec{s}$ dan total usaha mekanika W.",
                "steps": [
                    ("Langkah 1: Menghitung Vektor Perpindahan s (Ujung - Pangkal)", "$\\vec{s} = \\vec{B} - \\vec{A} = (8 - 2)\\hat{i} + (5 - 1)\\hat{j} + (0 - 0)\\hat{k} = (6\\hat{i} + 4\\hat{j} + 0\\hat{k})\\text{ meter}$."),
                    ("Langkah 2: Menghitung Usaha Mekanika dengan Dot Product", "$W = \\vec{F} \\cdot \\vec{s} = (F_x s_x) + (F_y s_y) + (F_z s_z) = (50)(6) + (30)(4) + (20)(0)$."),
                    ("Langkah 3: Mengevaluasi Penjumlahan Aljabar", "$W = 300 + 120 + 0 = 420\\text{ Joule}$.")
                ],
                "conclusion": "Kontainer berpindah sejauh $(6\\hat{i} + 4\\hat{j})\\text{ meter}$ dan total usaha energi mekanika yang dikerjakan kabel derek adalah 420 Joule."
            },
            "takeaways": [
                "Usaha mekanika fisika dimodelkan secara elegan melalui perkalian titik vektor gaya dan vektor perpindahan: $W = \\vec{F} \\cdot \\vec{s}$.",
                "Gaya yang bekerja tegak lurus terhadap arah perpindahan menghasilkan usaha sebesar nol Joule.",
                "Navigasi udara dan maritim mengandalkan resultan penjumlahan vektor kecepatan untuk mengantisipasi drift arus fluida."
            ],
            "quiz": (
                "Sebuah gaya $\\vec{F} = (10\\hat{i} - 5\\hat{j} + 8\\hat{k})\\text{ N}$ bekerja pada objek yang berpindah sejauh $\\vec{s} = (3\\hat{i} + 4\\hat{j} + 2\\hat{k})\\text{ m}$. Berapakah total usaha mekanika yang dikerjakan gaya tersebut?",
                ["26 Joule", "46 Joule", "30 Joule"],
                0,
                r"W = \vec{F} \cdot \vec{s} = (10)(3) + (-5)(4) + (8)(2) = 30 - 20 + 16 = 26\text{ Joule}."
            )
        },
        {
            "title": "Capstone: Proyek Integratif & Uji Sintesis Vektor",
            "objectives": [
                "Mengintegrasikan seluruh konsep dari Bab 1 hingga Bab 4 dalam memecahkan studi kasus navigasi drone logistik 3D.",
                "Menghitung vektor perpindahan spasial, jarak euklides, vektor satuan arah lintasan, dan efisiensi konsumsi energi propulsi dorong.",
                "Mengevaluasi hasil pemodelan matematis untuk pengambilan keputusan rekayasa sistem otomasi otonom."
            ],
            "hook": "Selamat datang di Tahap Capstone! Kamu ditunjuk sebagai Lead Flight Navigation Engineer untuk merancang algoritma penerbangan drone otonom pengantar suplai medis darurat. Drone harus menempuh jalur udara dari atap Rumah Sakit Pusat A ke Klinik Bencana B melintasi topografi kota dengan hembusan angin dinamis. Ujilah seluruh pemahaman vektor yang telah kamu kuasai untuk menuntaskan misi krusial ini!",
            "concepts": """
            <div class="dic-concept-card mb-4">
              <h3 class="dic-h3"><i class="bi bi-trophy-fill text-warning"></i> Skenario Capstone: Misi Koridor Udara Medis 3D</h3>
              <p>Sebuah drone logistik otomatis diprogram untuk mengirimkan kotak plasma darah darurat dengan parameter koordinat misi:</p>
              <ul class="dic-list">
                <li><strong>Posisi Peluncuran Rumah Sakit Pusat (Titik A):</strong> $A(10, 20, 50)$ meter dari datum kota.</li>
                <li><strong>Posisi Pendaratan Klinik Darurat (Titik B):</strong> $B(70, 100, 130)$ meter dari datum kota.</li>
                <li><strong>Vektor Gaya Dorong Rata-Rata Motor Propulsor:</strong> Mesin menghasilkan vektor gaya konstan $\\vec{F} = (12\\hat{i} + 16\\hat{j} + 16\\hat{k})\\text{ Newton}$ sepanjang koridor penerbangan.</li>
              </ul>
              <p>Tugas rekayasa sistem yang wajib kamu selesaikan:</p>
              <ol class="dic-list">
                <li>Tentukan vektor perpindahan penerbangan $\\vec{s}$ dari A ke B.</li>
                <li>Hitung panjang jarak terbang garis lurus total $|\\vec{s}|$.</li>
                <li>Tentukan vektor satuan orientasi autopilot $\\hat{u}$ agar sistem kompas drone mengunci arah penerbangan dengan tepat.</li>
                <li>Hitung total konsumsi energi usaha mekanika W yang dikerjakan motor penggerak drone.</li>
              </ol>
            </div>
            """,
            "pro_tip": "Untuk memverifikasi kebenaran kalkulasi unit vector autopilot $\\hat{u}$, pastikan jumlah kuadrat seluruh komponennya selalu sama dengan 1.00 ($u_x^2 + u_y^2 + u_z^2 = 1.00$)!",
            "pitfall": "Jangan mencampuradukkan besaran vektor dengan satuan yang berbeda! Vektor perpindahan $\\vec{s}$ bersatuan meter (m), sedangkan gaya dorong $\\vec{F}$ bersatuan Newton (N). Keduanya dihubungkan melalui perkalian dot product untuk menghasilkan satuan Joule (J).",
            "fun_fact": "Sistem autopiloting modern pada roket reusable Falcon 9 menjalankan jutaan kalkulasi vektor aljabar matriks State-Estimation setiap detiknya untuk menstabilkan posisi roket di udara saat melawan angin kencang hingga mendarat dengan akurasi sentimeter!",
            "formula": r"\vec{s} = \vec{B} - \vec{A} \quad ; \quad |\vec{s}| = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2} \quad ; \quad \hat{u} = \frac{\vec{s}}{|\vec{s}|} \quad ; \quad W = \vec{F} \cdot \vec{s}",
            "formula_params": [
                (r"\vec{s}", "Vektor perpindahan navigasi ruang 3D dari titik A ke titik B."),
                (r"|\vec{s}|", "Jarak garis lurus euklides 3D yang ditempuh (meter)."),
                (r"\hat{u}", "Vektor satuan orientasi kompas autopilot drone."),
                ("W", "Total usaha mekanika energi propulsi yang dikeluarkan mesin (Joule).")
            ],
            "formula_intuition": "Menggabungkan pipeline komputasi analitik: translasi koordinat, perhitungan magnitudo euklides, normalisasi arah vektor satuan, hingga kalkulasi energi skalar melalui dot product.",
            "example": {
                "question": "Berdasarkan skenario Capstone di atas, hitunglah: (a) Vektor perpindahan $\\vec{s}$, (b) Jarak terbang langsung $|\\vec{s}|$, (c) Vektor satuan arah $\\hat{u}$, dan (d) Total energi usaha mekanika W yang dikerjakan gaya dorong $\\vec{F} = (12, 16, 16)\\text{ N}$!",
                "known": "Titik A(10, 20, 50) m, Titik B(70, 100, 130) m, Gaya $\\vec{F} = (12, 16, 16)\\text{ N}$.",
                "asked": "Vektor $\\vec{s}$, magnitudo $|\\vec{s}|$, vektor satuan $\\hat{u}$, dan usaha W.",
                "steps": [
                    ("Langkah 1: Menghitung Vektor Perpindahan s", "$\\vec{s} = (70 - 10)\\hat{i} + (100 - 20)\\hat{j} + (130 - 50)\\hat{k} = (60\\hat{i} + 80\\hat{j} + 80\\hat{k})\\text{ meter}$."),
                    ("Langkah 2: Menghitung Jarak Tempuh Euklides Spasial", "$|\\vec{s}| = \\sqrt{60^2 + 80^2 + 80^2} = \\sqrt{3600 + 6400 + 6400} = \\sqrt{16400} \\approx 128.06\\text{ meter}$."),
                    ("Langkah 3: Menentukan Vektor Satuan Lintasan Autopilot", "$\\hat{u} = \\frac{(60, 80, 80)}{128.06} \\approx (0.468\\hat{i} + 0.625\\hat{j} + 0.625\\hat{k})$.<br>Verifikasi: $0.468^2 + 0.625^2 + 0.625^2 = 0.219 + 0.390 + 0.390 \\approx 1.00$."),
                    ("Langkah 4: Menghitung Total Usaha Konsumsi Energi W", "$W = \\vec{F} \\cdot \\vec{s} = (12)(60) + (16)(80) + (16)(80) = 720 + 1280 + 1280 = 3280\\text{ Joule}$ (atau $3.28\\text{ kJ}$).")
                ],
                "conclusion": "Misi Capstone Selesai Sempurna! Drone menempuh jarak langsung 128.06 meter pada orientasi arah unit vector (0.468, 0.625, 0.625) dan mengonsumsi energi kerja mekanika sebesar 3280 Joule."
            },
            "takeaways": [
                "Pemodelan vektor mengintegrasikan posisi fisik, arah navigasi normalisasi, dan kalkulasi energi propulsi dalam satu kerangka kerja utuh.",
                "Vektor satuan $\\hat{u}$ menjadi acuan matematis bagi pengendali autopilot untuk mempertahankan haluan terbang.",
                "Selamat! Kamu telah menguasai seluruh modul Vektor & Geometri Ruang dengan standar kompetensi pedagogis tertinggi!"
            ],
            "quiz": (
                "🏆 UJI SINTESIS CAPSTONE: Sebuah drone bergerak dari titik asal P(0, 0, 0) ke target Q(30, 40, 0) meter dengan dorongan gaya konstan F = (10, 5, 0) Newton. Berapakah jarak tempuh drone dan berapakah total usaha energi yang dikerjakan gaya dorong tersebut?",
                ["Jarak tempuh 50 meter dan Usaha total 500 Joule", "Jarak tempuh 70 meter dan Usaha total 450 Joule", "Jarak tempuh 50 meter dan Usaha total 350 Joule"],
                0,
                r"Vektor perpindahan \vec{s} = (30, 40, 0)\text{ m}. Jarak |\vec{s}| = \sqrt{30^2 + 40^2} = 50\text{ m}. Usaha W = \vec{F} \cdot \vec{s} = (10)(30) + (5)(40) + 0 = 300 + 200 = 500\text{ Joule}."
            )
        }
    ]
}
