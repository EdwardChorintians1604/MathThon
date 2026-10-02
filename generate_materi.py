#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MathThon - Interactive Math Simulator & Chapter Generator (Dicoding Standard)
=============================================================================
Pembelajaran Matematika Interaktif Tanpa Coding untuk Siswa:
- Siswa mengeksplorasi matematika melalui Widget Interaktif, Slider Dinamis, Simulator Komputasi,
  Kalkulator Visual, KaTeX Formula, dan Active Recall Quiz.
- PyScript / JavaScript bekerja di belakang layar sebagai mesin simulasi otomatis.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "Front_End", "templates", "user", "materi")

# Definisi Standar 5 Tahap Pedagogis
STAGE_DEFINITIONS = [
    {
        "badge": "TAHAP 1: FONDASI & INTUISI",
        "role_desc": "Peruntukan Bab 1: Membangun pemahaman intuitif dari nol, latar belakang mengapa konsep ini diciptakan, perbedaannya dengan topik sebelumnya, serta kerangka berpikir dasar.",
        "icon": "bi-stars"
    },
    {
        "badge": "TAHAP 2: ANATOMI & KAIDAH FORMAL",
        "role_desc": "Peruntukan Bab 2: Membedah struktur anatomi matematika, notasi formal, sifat-sifat fundamental, dan aksioma/teorema yang menjadi aturan main.",
        "icon": "bi-diagram-3"
    },
    {
        "badge": "TAHAP 3: MEKANIKA PERHITUNGAN & ALGORITMA",
        "role_desc": "Peruntukan Bab 3: Melatih keterampilan kalkulasi bertahap, metode analitik prosedural, strategi penyederhanaan, dan penanganan kasus khusus.",
        "icon": "bi-gear-wide-connected"
    },
    {
        "badge": "TAHAP 4: PEMODELAN & STUDI KASUS NYATA",
        "role_desc": "Peruntukan Bab 4: Menerjemahkan masalah dunia nyata (fisika, sains komputer, ekonomi, arsitektur) ke dalam pemodelan matematis formal.",
        "icon": "bi-lightbulb-fill"
    },
    {
        "badge": "TAHAP 5: CAPSTONE PROJECT & EVALUASI SINTESIS",
        "role_desc": "Peruntukan Bab 5: Mengintegrasikan seluruh materi Bab 1 s/d Bab 4 dalam satu proyek tantangan komprehensif sebagai standar penguasaan modul.",
        "icon": "bi-trophy-fill"
    }
]

# Modul Laboratorium Penalaran & Logika Matematika per Subjek
WIDGET_DATA = {
    "aljabar": {
        "title": "Laboratorium Penalaran: Neraca Keseimbangan Aljabar & Prinsip Kesetaraan",
        "desc": "🎯 Misi Berpikir: Bagaimana cara menjaga kesetaraan persamaan 2x + b = c saat kedua ruas dimanipulasi secara logis?",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-lightbulb"></i> Tantangan Penalaran:</div>
          <p class="small text-light mb-0">Aljabar adalah ilmu menjaga kesetaraan neraca timbangan. Geser nilai <strong>Konstanta b</strong> dan <strong>Target c</strong>, lalu amati rantai deduksi isolasi variabel x!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-4">
            <label class="form-label small text-muted">Koefisien a: <span id="val_a" class="fw-bold text-info">2</span></label>
            <input type="range" class="form-range" id="slider_a" min="1" max="10" value="2" oninput="updateAljabarSim()">
          </div>
          <div class="col-md-4">
            <label class="form-label small text-muted">Konstanta Tambahan b: <span id="val_b" class="fw-bold text-warning">4</span></label>
            <input type="range" class="form-range" id="slider_b" min="-10" max="10" value="4" oninput="updateAljabarSim()">
          </div>
          <div class="col-md-4">
            <label class="form-label small text-muted">Target Beban Ruas Kanan c: <span id="val_c" class="fw-bold text-success">16</span></label>
            <input type="range" class="form-range" id="slider_c" min="0" max="50" value="16" oninput="updateAljabarSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="d-flex justify-content-between align-items-center mb-2">
            <span class="small text-muted">Persamaan Neraca Aktif:</span>
            <span class="badge bg-primary-subtle text-primary" id="aljabar_status">Neraca Seimbang</span>
          </div>
          <div class="fs-5 fw-bold text-light text-center py-2" id="aljabar_eq">2x + 4 = 16</div>
          <div class="p-2 mt-2 rounded" style="background:rgba(0,0,0,0.3); border-left:3px solid #6366f1;">
            <div class="small fw-bold text-info mb-1"><i class="bi bi-diagram-3"></i> Rantai Deduksi Logika:</div>
            <div class="small text-light" id="aljabar_steps">1. Kurangkan kedua ruas dengan 4: 2x = 16 - 4 = 12<br>2. Bagi kedua ruas dengan 2: x = 12 / 2 = <strong>6.00</strong></div>
          </div>
          <div class="mt-2 text-end">
            <span class="small text-muted">Nilai Solusi x: </span>
            <span class="fs-5 fw-bold text-success" id="aljabar_sol">x = 6.00</span>
          </div>
        </div>
        """,
        "js": """
        function updateAljabarSim() {
          const a = parseInt(document.getElementById('slider_a').value);
          const b = parseInt(document.getElementById('slider_b').value);
          const c = parseInt(document.getElementById('slider_c').value);
          document.getElementById('val_a').textContent = a;
          document.getElementById('val_b').textContent = b;
          document.getElementById('val_c').textContent = c;
          const bSign = b >= 0 ? `+ ${b}` : `- ${Math.abs(b)}`;
          document.getElementById('aljabar_eq').textContent = `${a}x ${bSign} = ${c}`;
          const rhs = c - b;
          const x = (rhs / a).toFixed(2);
          document.getElementById('aljabar_steps').innerHTML = `1. Kurangkan kedua ruas dengan (${b}): ${a}x = ${c} - (${b}) = ${rhs}<br>2. Bagi kedua ruas dengan (${a}): x = ${rhs} / ${a} = <strong>${x}</strong>`;
          document.getElementById('aljabar_sol').textContent = `x = ${x}`;
        }
        """
    },
    "bangun_datar_dan_bangun_ruang": {
        "title": "Laboratorium Penalaran Spasial: Hukum Skala Kuadratik vs Kubik",
        "desc": "🎯 Misi Berpikir: Amati mengapa saat dimensi dilipatgandakan k kali, Luas Permukaan naik k² kali lipat sementara Volume melonjak k³ kali lipat!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(168,85,247,0.08); border:1px solid rgba(168,85,247,0.25);">
          <div class="small fw-bold text-warning mb-1"><i class="bi bi-bounding-box-circles"></i> Prinsip Penalaran Skala Geometri:</div>
          <p class="small text-light mb-0">Panjang bersifat 1D (skala k), Luas penampang bersifat 2D (skala k²), dan Volume ruang bersifat 3D (skala k³). Inilah alasan geometris mengapa raksasa membutuhkan tulang yang jauh lebih tebal!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-4">
            <label class="form-label small text-muted">Bentuk Geometri:</label>
            <select class="form-select form-select-sm bg-dark text-light border-secondary" id="geo_shape" onchange="updateGeoSim()">
              <option value="tabung">Tabung (Silinder)</option>
              <option value="balok">Balok (Prisma Segiempat)</option>
              <option value="bola">Bola</option>
              <option value="kerucut">Kerucut</option>
            </select>
          </div>
          <div class="col-md-4">
            <label class="form-label small text-muted">Dimensi Utama r / p: <span id="geo_val_d1" class="fw-bold text-info">7</span> cm</label>
            <input type="range" class="form-range" id="geo_slider_d1" min="1" max="20" value="7" oninput="updateGeoSim()">
          </div>
          <div class="col-md-4">
            <label class="form-label small text-muted">Tinggi t / Lebar l: <span id="geo_val_d2" class="fw-bold text-warning">10</span> cm</label>
            <input type="range" class="form-range" id="geo_slider_d2" min="1" max="20" value="10" oninput="updateGeoSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Dimensi Linier 1D:</div>
              <div class="fs-6 fw-bold text-light" id="geo_lin">r = 7 cm, t = 10 cm</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Luas Permukaan (2D - cm²):</div>
              <div class="fs-5 fw-bold text-info" id="geo_area">747.70 cm²</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Kapasitas Volume (3D - cm³):</div>
              <div class="fs-5 fw-bold text-success" id="geo_vol">1539.38 cm³</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #a855f7;">
            <div class="small text-warning fw-bold mb-1"><i class="bi bi-lightbulb-fill"></i> Analisis Rasio Luas terhadap Volume (L/V):</div>
            <div class="small text-light" id="geo_ratio">Rasio L/V = 0.49. Semakin besar ukuran objek, rasio permukaan terhadap volume semakin mengecil.</div>
          </div>
        </div>
        """,
        "js": """
        function updateGeoSim() {
          const shape = document.getElementById('geo_shape').value;
          const d1 = parseFloat(document.getElementById('geo_slider_d1').value);
          const d2 = parseFloat(document.getElementById('geo_slider_d2').value);
          document.getElementById('geo_val_d1').textContent = d1;
          document.getElementById('geo_val_d2').textContent = d2;
          document.getElementById('geo_lin').textContent = `d₁ = ${d1} cm, d₂ = ${d2} cm`;
          let area = 0, vol = 0;
          if (shape === 'tabung') {
            area = 2 * Math.PI * d1 * (d1 + d2);
            vol = Math.PI * d1 * d1 * d2;
          } else if (shape === 'balok') {
            const t = 5;
            area = 2 * (d1*d2 + d1*t + d2*t);
            vol = d1 * d2 * t;
          } else if (shape === 'bola') {
            area = 4 * Math.PI * d1 * d1;
            vol = (4/3) * Math.PI * Math.pow(d1, 3);
          } else if (shape === 'kerucut') {
            const s = Math.sqrt(d1*d1 + d2*d2);
            area = Math.PI * d1 * (d1 + s);
            vol = (1/3) * Math.PI * d1 * d1 * d2;
          }
          const ratio = (area / vol).toFixed(2);
          document.getElementById('geo_area').textContent = `${area.toFixed(2)} cm²`;
          document.getElementById('geo_vol').textContent = `${vol.toFixed(2)} cm³`;
          document.getElementById('geo_ratio').innerHTML = `Rasio L/V = <strong>${ratio}</strong>. Volume bertumbuh secara kubik (~d³) jauh lebih cepat daripada luas permukaan kuadratik (~d²).`;
        }
        """
    },
    "operasi_kabataku": {
        "title": "Laboratorium Logika: Penjaga Ambiguitas & Pohon Sintaks KaBaTaKu",
        "desc": "🎯 Misi Berpikir: Bandingkan hasil evaluasi aritmetika dengan dan tanpa tanda kurung untuk membuktikan hierarki operasi!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(100,116,139,0.08); border:1px solid rgba(100,116,139,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-shield-check"></i> Mengapa Hierarki Operasi Diperlukan?</div>
          <p class="small text-light mb-0">Tanpa aturan KaBaTaKu (Kurung > Kali/Bagi > Tambah/Kurang), ekspresi <strong>12 + 8 × 2</strong> dapat bernilai 28 atau 40. Perkalian mengikat lebih kuat karena merupakan penjumlahan berulang.</p>
        </div>
        <div class="row g-2 align-items-center">
          <div class="col-md-4">
            <label class="form-label small text-muted">Angka A: <span id="kab_val_a" class="fw-bold text-info">12</span></label>
            <input type="range" class="form-range" id="kab_a" min="1" max="50" value="12" oninput="updateKabatakuSim()">
          </div>
          <div class="col-md-4">
            <label class="form-label small text-muted">Angka B: <span id="kab_val_b" class="fw-bold text-warning">8</span></label>
            <input type="range" class="form-range" id="kab_b" min="1" max="20" value="8" oninput="updateKabatakuSim()">
          </div>
          <div class="col-md-4">
            <label class="form-label small text-muted">Faktor Pengali C: <span id="kab_val_c" class="fw-bold text-success">3</span></label>
            <input type="range" class="form-range" id="kab_c" min="1" max="10" value="3" oninput="updateKabatakuSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2">
            <div class="col-md-6 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Kasus 1 (Standar BODMAS):</div>
              <div class="fs-6 fw-bold text-info" id="kab_std_expr">12 + (8 × 3)</div>
              <div class="fs-4 fw-bold text-success mt-1" id="kab_std_res">36</div>
              <div class="small text-muted">Perkalian didahulukan</div>
            </div>
            <div class="col-md-6">
              <div class="small text-muted">Kasus 2 (Dengan Tanda Kurung Override):</div>
              <div class="fs-6 fw-bold text-warning" id="kab_par_expr">(12 + 8) × 3</div>
              <div class="fs-4 fw-bold text-warning mt-1" id="kab_par_res">60</div>
              <div class="small text-muted">Kurung memaksa penjumlahan dulu</div>
            </div>
          </div>
          <div class="p-2 rounded mt-3" style="background:rgba(0,0,0,0.3); border-left:3px solid #10b981;">
            <div class="small text-success fw-bold mb-1"><i class="bi bi-check-circle-fill"></i> Kesimpulan Penalaran Logika:</div>
            <div class="small text-light" id="kab_diff">Selisih hasil = 24. Tanda kurung mengubah pohon evaluasi sintaksis secara mutlak.</div>
          </div>
        </div>
        """,
        "js": """
        function updateKabatakuSim() {
          const a = parseInt(document.getElementById('kab_a').value);
          const b = parseInt(document.getElementById('kab_b').value);
          const c = parseInt(document.getElementById('kab_c').value);
          document.getElementById('kab_val_a').textContent = a;
          document.getElementById('kab_val_b').textContent = b;
          document.getElementById('kab_val_c').textContent = c;
          const std = a + (b * c);
          const par = (a + b) * c;
          document.getElementById('kab_std_expr').textContent = `${a} + (${b} × ${c})`;
          document.getElementById('kab_std_res').textContent = std;
          document.getElementById('kab_par_expr').textContent = `(${a} + ${b}) × ${c}`;
          document.getElementById('kab_par_res').textContent = par;
          const diff = Math.abs(par - std);
          document.getElementById('kab_diff').innerHTML = `Selisih nilai = <strong>${diff}</strong>. Standar KaBaTaKu mengutamakan perkalian (${b}×${c}=${b*c}) terlebih dahulu sebelum penjumlahan.`;
        }
        """
    },
    "integral": {
        "title": "Laboratorium Penalaran: Akumulasi Partisi Riemann Menuju Luas Eksak",
        "desc": "🎯 Misi Berpikir: Amati bagaimana jumlah persegi panjang diskrit n mendekati nilai integral kontinu eksak saat n → ∞!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.25);">
          <div class="small fw-bold text-success mb-1"><i class="bi bi-infinity"></i> Paradoks Luas Melengkung:</div>
          <p class="small text-light mb-0">Bagaimana menjumlahkan kotak-kotak lurus dapat menghasilkan luas kurva lengkung yang presisi? Geser partisi n dari 2 hingga 200 dan lihat galat (error) menyusut menuju nol!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Banyak Partisi Irisan (n): <span id="val_n" class="fw-bold text-info">10</span></label>
            <input type="range" class="form-range" id="slider_n" min="2" max="200" value="10" oninput="updateIntegralSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Batas Atas Integral (b): <span id="val_b_int" class="fw-bold text-success">2</span></label>
            <input type="range" class="form-range" id="slider_b_int" min="1" max="5" value="2" oninput="updateIntegralSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="d-flex justify-content-between flex-wrap gap-2 text-center">
            <div>
              <div class="small text-muted">Aproksimasi Riemann:</div>
              <div class="fs-5 fw-bold text-info" id="riemann_res">2.2800</div>
            </div>
            <div>
              <div class="small text-muted">Nilai Eksak (b³/3):</div>
              <div class="fs-5 fw-bold text-success" id="exact_res">2.6667</div>
            </div>
            <div>
              <div class="small text-muted">Galat / Selisih Error:</div>
              <div class="fs-5 fw-bold text-danger" id="error_res">0.3867</div>
            </div>
            <div>
              <div class="small text-muted">Tingkat Presisi:</div>
              <div class="fs-5 fw-bold text-warning" id="accuracy_res">85.5%</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #10b981;">
            <div class="small text-success fw-bold mb-1"><i class="bi bi-graph-up"></i> Inti Logika Kalkulus Integral:</div>
            <div class="small text-light" id="int_deduction">Saat n mendekati tak hingga (Δx → 0), jumlahan Riemann konvergen 100% tepat ke nilai integral tentu eksak.</div>
          </div>
        </div>
        """,
        "js": """
        function updateIntegralSim() {
          const n = parseInt(document.getElementById('slider_n').value);
          const b = parseInt(document.getElementById('slider_b_int').value);
          document.getElementById('val_n').textContent = n;
          document.getElementById('val_b_int').textContent = b;
          const dx = b / n;
          let sum = 0;
          for (let i = 0; i < n; i++) {
            const x = i * dx;
            sum += (x * x) * dx;
          }
          const exact = (b * b * b) / 3;
          const error = Math.abs(sum - exact);
          const acc = Math.max(0, (1 - error / exact) * 100).toFixed(1);
          document.getElementById('riemann_res').textContent = `${sum.toFixed(4)}`;
          document.getElementById('exact_res').textContent = `${exact.toFixed(4)}`;
          document.getElementById('error_res').textContent = `${error.toFixed(4)}`;
          document.getElementById('accuracy_res').textContent = `${acc}%`;
          document.getElementById('int_deduction').innerHTML = `Lebar partisi Δx = ${dx.toFixed(4)}. Semakin rapat partisi (${n} irisan), ruang kosong di bawah kurva semakin tertutup sempurna.`;
        }
        """
    },
    "limit": {
        "title": "Laboratorium Penalaran: Mikroskop Nilai Limit (x → c) & Eliminasi 0/0",
        "desc": "🎯 Misi Berpikir: Amati mengapa f(x) = (x² - 4)/(x - 2) bernilai 0/0 pada x = 2, namun nilai limitnya tetap tepat bernilai 4!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.25);">
          <div class="small fw-bold text-warning mb-1"><i class="bi bi-zoom-in"></i> Mengapa Limit Bukan Sekadar Substitusi?</div>
          <p class="small text-light mb-0">Pada titik x = 2 tepat, fungsi menghasilkan <strong>0/0 (tak terdefinisi)</strong>. Namun limit mempelajari tren nilai di sekeliling titik tersebut (neighborhood) saat jarak Δx menuju nol.</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Jarak Mikroskopis (Δx): <span id="val_delta" class="fw-bold text-warning">0.1</span></label>
            <input type="range" class="form-range" id="slider_delta" min="1" max="5" value="1" oninput="updateLimitSim()">
          </div>
          <div class="col-md-6">
            <div class="small text-muted mb-1">Fungsi Target di Sekitar Titik c = 2:</div>
            <div class="badge bg-primary-subtle text-primary p-2">f(x) = (x² - 4) / (x - 2)</div>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-6 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Pendekatan Kiri (x = 2 - Δx):</div>
              <div class="fs-5 fw-bold text-info" id="left_limit">x = 1.90 ➔ f(x) = 3.9000</div>
            </div>
            <div class="col-6">
              <div class="small text-muted">Pendekatan Kanan (x = 2 + Δx):</div>
              <div class="fs-5 fw-bold text-success" id="right_limit">x = 2.10 ➔ f(x) = 4.1000</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #f59e0b;">
            <div class="small text-warning fw-bold mb-1"><i class="bi bi-compass-fill"></i> Kesimpulan Limit Kiri & Kanan:</div>
            <div class="small text-light" id="limit_conclusion">Kedua sisi menjepit nilai target yang sama: <strong>L = 4.0000</strong>. Limit terbukti eksis!</div>
          </div>
        </div>
        """,
        "js": """
        function updateLimitSim() {
          const deltas = [0.1, 0.01, 0.001, 0.0001, 0.00001];
          const idx = parseInt(document.getElementById('slider_delta').value) - 1;
          const d = deltas[idx];
          document.getElementById('val_delta').textContent = d;
          const xL = 2 - d;
          const xR = 2 + d;
          const fL = (xL + 2).toFixed(5);
          const fR = (xR + 2).toFixed(5);
          document.getElementById('left_limit').textContent = `x = ${xL.toFixed(5)} ➔ ${fL}`;
          document.getElementById('right_limit').textContent = `x = ${xR.toFixed(5)} ➔ ${fR}`;
          document.getElementById('limit_conclusion').innerHTML = `Pada jarak Δx = ${d}, selisih terhadap target L=4 adalah <strong>${d}</strong>. Karena limit kiri = limit kanan = 4, maka lim f(x) = 4.`;
        }
        """
    },
    "fungsi_turunan": {
        "title": "Laboratorium Penalaran: Garis Singgung & Deteksi Titik Stasioner",
        "desc": "🎯 Misi Berpikir: Geser titik evaluasi x₀ sepanjang kurva f(x) = x² - 4x. Amati kapan gradien garis singgung m = 0 dan apa maknanya bagi titik balik!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.25);">
          <div class="small fw-bold text-danger mb-1"><i class="bi bi-speedometer2"></i> Logika Titik Stasioner:</div>
          <p class="small text-light mb-0">Saat kurva bergerak dari fase turun ke fase naik (atau sebaliknya), kurva wajib melewati titik datar di mana gradien garis singgungnya sesaat mendatar: <strong>m = f'(x) = 0</strong>.</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Titik Evaluasi (x₀): <span id="tur_val_x" class="fw-bold text-warning">2</span></label>
            <input type="range" class="form-range" id="tur_slider_x" min="-2" max="6" value="2" oninput="updateTurunanSim()">
          </div>
          <div class="col-md-6">
            <div class="small text-muted mb-1">Fungsi Parabola Aktif:</div>
            <div class="badge bg-danger-subtle text-danger p-2">f(x) = x² - 4x &nbsp;➔&nbsp; f'(x) = 2x - 4</div>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Titik Koordinat (x₀, y₀):</div>
              <div class="fs-5 fw-bold text-light" id="tur_pt">(2, -4)</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Gradien Garis Singgung (m):</div>
              <div class="fs-5 fw-bold text-warning" id="tur_grad">m = 0 (Datar)</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Status Geometris:</div>
              <div class="fs-6 fw-bold text-success" id="tur_status">Titik Minimum Stasioner</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #ef4444;">
            <div class="small text-danger fw-bold mb-1"><i class="bi bi-graph-up-arrow"></i> Rantai Penalaran Diferensial:</div>
            <div class="small text-light" id="tur_tangent">f'(2) = 2(2) - 4 = 0. Garis singgung horizontal y = -4 menandai titik balik minimum kurva.</div>
          </div>
        </div>
        """,
        "js": """
        function updateTurunanSim() {
          const x0 = parseInt(document.getElementById('tur_slider_x').value);
          document.getElementById('tur_val_x').textContent = x0;
          const y0 = x0 * x0 - 4 * x0;
          const m = 2 * x0 - 4;
          document.getElementById('tur_pt').textContent = `(${x0}, ${y0})`;
          document.getElementById('tur_grad').textContent = `m = ${m}`;
          let status = '';
          let statusCls = '';
          if (m < 0) {
            status = 'Kurva Sedang Turun (m < 0)';
            statusCls = 'fs-6 fw-bold text-info';
          } else if (m === 0) {
            status = '🎯 Titik Minimum Stasioner (m = 0)';
            statusCls = 'fs-6 fw-bold text-success';
          } else {
            status = 'Kurva Sedang Naik (m > 0)';
            statusCls = 'fs-6 fw-bold text-warning';
          }
          document.getElementById('tur_status').textContent = status;
          document.getElementById('tur_status').className = statusCls;
          const c = y0 - m * x0;
          const cSign = c >= 0 ? `+ ${c}` : `- ${Math.abs(c)}`;
          document.getElementById('tur_tangent').innerHTML = `Garis singgung: <strong>y = ${m}x ${cSign}</strong>. Nilai turunan f'(${x0}) = ${m} merepresentasikan kecepatan perubahan sesaat grafik.`;
        }
        """
    },
    "matriks": {
        "title": "Laboratorium Penalaran Geometris: Determinan & Keruntuhan Dimensi",
        "desc": "🎯 Misi Berpikir: Apa arti determinan det(A) = 0 secara geometris dan logis pada sistem persamaan?",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(6,182,212,0.08); border:1px solid rgba(6,182,212,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-grid-fill"></i> Arti Geometris Determinan:</div>
          <p class="small text-light mb-0">Determinan det(A) = ad - bc merepresentasikan <strong>faktor penskalaan luas</strong> bidang 2D. Jika det(A) = 0, bidang termampatkan menjadi 1 garis (kolaps dimensi), sehingga informasi hilang dan invers mustahil dibentuk!</p>
        </div>
        <div class="d-flex justify-content-center gap-2 mb-2">
          <input type="number" class="form-control form-control-sm text-center bg-dark text-light border-secondary" style="width:70px;" id="m_a" value="4" oninput="updateMatrixSim()">
          <input type="number" class="form-control form-control-sm text-center bg-dark text-light border-secondary" style="width:70px;" id="m_b" value="2" oninput="updateMatrixSim()">
        </div>
        <div class="d-flex justify-content-center gap-2">
          <input type="number" class="form-control form-control-sm text-center bg-dark text-light border-secondary" style="width:70px;" id="m_c" value="2" oninput="updateMatrixSim()">
          <input type="number" class="form-control form-control-sm text-center bg-dark text-light border-secondary" style="width:70px;" id="m_d" value="1" oninput="updateMatrixSim()">
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="d-flex justify-content-around text-center mb-2">
            <div>
              <div class="small text-muted">Determinan det(A):</div>
              <div class="fs-4 fw-bold text-warning" id="mat_det">0</div>
            </div>
            <div>
              <div class="small text-muted">Status Inversibilitas:</div>
              <div class="fs-6 fw-bold text-danger" id="mat_status">Singular (Kolaps Dimensi / Tidak Punya Invers)</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #06b6d4;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-lightbulb-fill"></i> Analisis Logika Aljabar Linear:</div>
            <div class="small text-light" id="mat_reason">Baris kedua merupakan kelipatan baris pertama (rasio sama). Vektor kolom sejajar sehingga luas jajaran genjang = 0.</div>
          </div>
        </div>
        """,
        "js": """
        function updateMatrixSim() {
          const a = parseFloat(document.getElementById('m_a').value) || 0;
          const b = parseFloat(document.getElementById('m_b').value) || 0;
          const c = parseFloat(document.getElementById('m_c').value) || 0;
          const d = parseFloat(document.getElementById('m_d').value) || 0;
          const det = (a * d) - (b * c);
          document.getElementById('mat_det').textContent = `${a}×${d} - ${b}×${c} = ${det}`;
          if (det !== 0) {
            document.getElementById('mat_status').textContent = 'Non-Singular (Punya Invers)';
            document.getElementById('mat_status').className = 'fs-6 fw-bold text-success';
            document.getElementById('mat_reason').innerHTML = `det(A) = ${det} ≠ 0. Transformasi mempertahankan area seluas <strong>${Math.abs(det)} satuan</strong>, sehingga sistem persamaan memiliki solusi unik.`;
          } else {
            document.getElementById('mat_status').textContent = 'Singular (Kolaps Dimensi / Tidak Punya Invers)';
            document.getElementById('mat_status').className = 'fs-6 fw-bold text-danger';
            document.getElementById('mat_reason').innerHTML = `det(A) = 0. Vektor kolom saling segaris (kolinear). Bidang 2D termampatkan menjadi garis 1D, sehingga tidak ada balikan matriks.`;
          }
        }
        """
    },
    "statistika": {
        "title": "Laboratorium Penalaran: Uji Sensitivitas Mean vs Kekokohan Median",
        "desc": "🎯 Misi Berpikir: Suntikkan 1 data pencilan (outlier) ekstrem. Amati mengapa Mean melonjak drastis sedangkan Median tetap kokoh!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(236,72,153,0.08); border:1px solid rgba(236,72,153,0.25);">
          <div class="small fw-bold text-pink mb-1" style="color:#ec4899;"><i class="bi bi-shield-shaded"></i> Pertarungan Statistik: Mean vs Median</div>
          <p class="small text-light mb-0">Dalam data ekonomi riil (seperti distribusi penghasilan penduduk), 1 orang miliarder dapat mendistorsi rata-rata (Mean) secara menyesatkan. Geser nilai outlier di bawah ini untuk melihat perbedaannya!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-7">
            <label class="form-label small text-muted">Data Pokok: [70, 75, 80, 85, 90] + Injeksi Outlier</label>
            <input type="range" class="form-range" id="stat_slider_outlier" min="90" max="1000" step="10" value="95" oninput="updateStatSim()">
          </div>
          <div class="col-md-5">
            <div class="small text-muted">Nilai Data Outlier Tambahan:</div>
            <div class="fs-5 fw-bold text-warning" id="stat_outlier_val">95 (Normal)</div>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Mean (Rata-rata):</div>
              <div class="fs-4 fw-bold text-danger" id="st_mean">82.50</div>
              <div class="small text-muted">Sensitif terhadap outlier</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Median (Nilai Tengah):</div>
              <div class="fs-4 fw-bold text-success" id="st_med">82.50</div>
              <div class="small text-muted">Kebal & Robust</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Standar Deviasi (s):</div>
              <div class="fs-4 fw-bold text-info" id="st_sd">9.35</div>
              <div class="small text-muted">Penyebaran data</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #ec4899;">
            <div class="small fw-bold mb-1" style="color:#ec4899;"><i class="bi bi-lightbulb-fill"></i> Insight Pengambilan Keputusan:</div>
            <div class="small text-light" id="stat_insight">Saat data memiliki kemiringan ekstrem (skewed), Median adalah representasi nilai tipikal yang jauh lebih adil daripada Mean.</div>
          </div>
        </div>
        """,
        "js": """
        function updateStatSim() {
          const outlier = parseInt(document.getElementById('stat_slider_outlier').value);
          document.getElementById('stat_outlier_val').textContent = outlier >= 300 ? `${outlier} (Pencilan Ekstrem!)` : `${outlier}`;
          const nums = [70, 75, 80, 85, 90, outlier].sort((a,b)=>a-b);
          const mean = nums.reduce((a,b)=>a+b,0) / nums.length;
          const mid = Math.floor(nums.length/2);
          const med = (nums[mid-1] + nums[mid])/2;
          const variance = nums.reduce((a,b)=>a + Math.pow(b-mean,2), 0) / (nums.length - 1);
          const sd = Math.sqrt(variance);
          document.getElementById('st_mean').textContent = mean.toFixed(2);
          document.getElementById('st_med').textContent = med.toFixed(2);
          document.getElementById('st_sd').textContent = sd.toFixed(2);
          if (outlier >= 300) {
            document.getElementById('stat_insight').innerHTML = `Perhatikan: Mean melonjak menjadi <strong>${mean.toFixed(1)}</strong> (terdistorsi outlier ${outlier}), sedangkan Median hanya bergeser ke <strong>${med.toFixed(1)}</strong>. Inilah bukti ketangguhan Median!`;
          } else {
            document.getElementById('stat_insight').innerHTML = `Pada data normal, Mean (${mean.toFixed(1)}) dan Median (${med.toFixed(1)}) berdekatan karena distribusi data seimbang simetris.`;
          }
        }
        """
    },
    "probabilitas": {
        "title": "Laboratorium Penalaran: Rasio Kombinatorika & Hukum Bilangan Besar",
        "desc": "🎯 Misi Berpikir: Mengapa permutasi ⁿPᵣ selalu tepat r! kali lebih besar daripada kombinasi ⁿCᵣ?",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(20,184,166,0.08); border:1px solid rgba(20,184,166,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-dice-5"></i> Logika Urutan Posisi:</div>
          <p class="small text-light mb-0">Kombinasi memilih anggota tanpa peduli urutan. Permutasi menata setiap anggota terpilih ke dalam urutan posisi (sebanyak r! cara). Ubah nilai r dan buktikan hubungan multiplikatifnya!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Total Objek Tersedia (n): <span id="prob_val_n" class="fw-bold text-info">6</span></label>
            <input type="range" class="form-range" id="prob_slider_n" min="2" max="10" value="6" oninput="updateProbSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Objek Dipilih (r ≤ n): <span id="prob_val_r" class="fw-bold text-warning">3</span></label>
            <input type="range" class="form-range" id="prob_slider_r" min="1" max="10" value="3" oninput="updateProbSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Kombinasi ⁿCᵣ:</div>
              <div class="fs-4 fw-bold text-success" id="prob_comb">20</div>
              <div class="small text-muted">Tanpa urutan</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Faktor Urutan (r!):</div>
              <div class="fs-4 fw-bold text-warning" id="prob_fact">6</div>
              <div class="small text-muted">Penataan posisi</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Permutasi ⁿPᵣ:</div>
              <div class="fs-4 fw-bold text-info" id="prob_perm">120</div>
              <div class="small text-muted">ⁿCᵣ × r!</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #14b8a6;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-link-45deg"></i> Bukti Hubungan Logis:</div>
            <div class="small text-light" id="prob_proof">ⁿP₃ = 20 × 3! = 20 × 6 = 120 cara susunan.</div>
          </div>
        </div>
        """,
        "js": """
        function updateProbSim() {
          const fact = (num) => num <= 1 ? 1 : num * fact(num - 1);
          let n = parseInt(document.getElementById('prob_slider_n').value);
          let r = parseInt(document.getElementById('prob_slider_r').value);
          if (r > n) { r = n; document.getElementById('prob_slider_r').value = r; }
          document.getElementById('prob_val_n').textContent = n;
          document.getElementById('prob_val_r').textContent = r;
          const fR = fact(r);
          const perm = fact(n) / fact(n - r);
          const comb = fact(n) / (fR * fact(n - r));
          document.getElementById('prob_comb').textContent = comb.toLocaleString('id-ID');
          document.getElementById('prob_fact').textContent = `${r}! = ${fR}`;
          document.getElementById('prob_perm').textContent = perm.toLocaleString('id-ID');
          document.getElementById('prob_proof').innerHTML = `Hubungan: <strong>ⁿPᵣ = ⁿCᵣ × r!</strong> ➔ ${comb} × ${fR} = <strong>${perm} cara</strong>.`;
        }
        """
    },
    "eksponensial": {
        "title": "Laboratorium Penalaran: Fenomena Ledakan Multiplikasi Eksponensial",
        "desc": "🎯 Misi Berpikir: Bandingkan kecepatan pertumbuhan fungsi linier f(n) = 2n vs fungsi eksponensial g(n) = 2ⁿ!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(249,115,22,0.08); border:1px solid rgba(249,115,22,0.25);">
          <div class="small fw-bold text-warning mb-1"><i class="bi bi-graph-up-arrow"></i> Mengapa Pertumbuhan Eksponensial Menipu Persepsi Manusia?</div>
          <p class="small text-light mb-0">Pada langkah awal, pertumbuhan eksponensial terlihat lambat. Namun setelah melewati titik kritis, perkalian berulang memicu pelonjakan masif yang menyalip pertumbuhan linier!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Langkah / Periode Waktu (n): <span id="exp_val_n" class="fw-bold text-warning">5</span></label>
            <input type="range" class="form-range" id="exp_slider_n" min="1" max="15" value="5" oninput="updateExpSim()">
          </div>
          <div class="col-md-6">
            <div class="small text-muted mb-1">Perbandingan Model:</div>
            <div class="small text-light">Linier: <span class="badge bg-secondary">f(n) = 2n</span> &nbsp;|&nbsp; Eksponen: <span class="badge bg-warning text-dark">g(n) = 2ⁿ</span></div>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-6 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Pertumbuhan Linier (Penjumlahan):</div>
              <div class="fs-4 fw-bold text-info" id="exp_lin">10</div>
              <div class="small text-muted">Naik +2 konstan tiap langkah</div>
            </div>
            <div class="col-6">
              <div class="small text-muted">Pertumbuhan Eksponensial (Multiplikasi):</div>
              <div class="fs-4 fw-bold text-warning" id="exp_res">32</div>
              <div class="small text-muted">Melipatgandakan 2x lipat tiap langkah</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #f97316;">
            <div class="small text-warning fw-bold mb-1"><i class="bi bi-lightning-charge-fill"></i> Rasio Dominasi:</div>
            <div class="small text-light" id="exp_ratio">Pada n = 5, nilai eksponensial sudah 3.20x lebih besar dari linier.</div>
          </div>
        </div>
        """,
        "js": """
        function updateExpSim() {
          const n = parseInt(document.getElementById('exp_slider_n').value);
          document.getElementById('exp_val_n').textContent = n;
          const lin = 2 * n;
          const exp = Math.pow(2, n);
          const ratio = (exp / lin).toFixed(2);
          document.getElementById('exp_lin').textContent = lin.toLocaleString('id-ID');
          document.getElementById('exp_res').textContent = exp.toLocaleString('id-ID');
          document.getElementById('exp_ratio').innerHTML = `Pada n = ${n}, nilai eksponensial (<strong>${exp.toLocaleString('id-ID')}</strong>) sudah <strong>${ratio}x lipat</strong> melampaui pertumbuhan linier (${lin}).`;
        }
        """
    },
    "desimal": {
        "title": "Laboratorium Penalaran Finansial: Jebakan Logika Diskon Bertingkat (30% + 10%)",
        "desc": "🎯 Misi Berpikir: Mengapa promo diskon 30% + 10% BUKAN sama dengan diskon 40%?",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(132,204,22,0.08); border:1px solid rgba(132,204,22,0.25);">
          <div class="small fw-bold text-success mb-1"><i class="bi bi-tag-fill"></i> Analisis Basis Persentase:</div>
          <p class="small text-light mb-0">Diskon pertama memotong dari 100% harga pokok. Namun diskon kedua hanya memotong dari <strong>sisa harga (70%)</strong>, bukan dari harga awal. Buktikan kalkulasinya di bawah!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Harga Label Barang: Rp <span id="dec_val_price" class="fw-bold text-info">200.000</span></label>
            <input type="range" class="form-range" id="dec_slider_price" min="50000" max="1000000" step="50000" value="200000" oninput="updateDesimalSim()">
          </div>
          <div class="col-md-6">
            <div class="small text-muted mb-1">Promo Bertingkat:</div>
            <div class="badge bg-success-subtle text-success p-2">Diskon 30% + Diskon Tambahan 10%</div>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-6 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Bayar Promo Bertingkat (30% + 10%):</div>
              <div class="fs-4 fw-bold text-success" id="dec_real_pay">Rp 126.000</div>
              <div class="small text-muted">Faktor: 0.70 × 0.90 = 63% bayar</div>
            </div>
            <div class="col-6">
              <div class="small text-muted">Jika Diskon 40% Langsung:</div>
              <div class="fs-4 fw-bold text-danger" id="dec_fake_pay">Rp 120.000</div>
              <div class="small text-muted">Faktor: 60% bayar</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #84cc16;">
            <div class="small text-success fw-bold mb-1"><i class="bi bi-wallet2"></i> Pembongkaran Miskonsepsi:</div>
            <div class="small text-light" id="dec_diff">Pembeli membayar lebih mahal Rp 6.000 pada diskon bertingkat karena diskon 10% hanya memotong Rp 14.000 dari sisa Rp 140.000.</div>
          </div>
        </div>
        """,
        "js": """
        function updateDesimalSim() {
          const price = parseInt(document.getElementById('dec_slider_price').value);
          document.getElementById('dec_val_price').textContent = price.toLocaleString('id-ID');
          const step1 = price * 0.70;
          const realPay = step1 * 0.90;
          const fakePay = price * 0.60;
          const diff = realPay - fakePay;
          document.getElementById('dec_real_pay').textContent = `Rp ${realPay.toLocaleString('id-ID')}`;
          document.getElementById('dec_fake_pay').textContent = `Rp ${fakePay.toLocaleString('id-ID')}`;
          document.getElementById('dec_diff').innerHTML = `Selisih: <strong>Rp ${diff.toLocaleString('id-ID')}</strong> lebih mahal. Diskon efektif riil adalah <strong>37%</strong>, bukan 40%!`;
        }
        """
    },
    "sistem_bilangan": {
        "title": "Laboratorium Penalaran: Mengapa Komputer Menggunakan Biner & Nilai Tempat Polinomial?",
        "desc": "🎯 Misi Berpikir: Bagaimana 8 sakelar biner (0/1) mampu menyusun nilai 0 s.d. 255 menggunakan prinsip nilai tempat 2ⁿ?",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(51,65,85,0.2); border:1px solid rgba(51,65,85,0.4);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-cpu"></i> Prinsip Nilai Tempat Polinomial:</div>
          <p class="small text-light mb-0">Setiap digit biner merepresentasikan bobot kelipatan dua: <strong>128, 64, 32, 16, 8, 4, 2, 1</strong>. Aktifkan sakelar bit di bawah ini untuk melihat konversi logika memori!</p>
        </div>
        <div class="d-flex justify-content-center gap-2 flex-wrap mb-3" id="bit_switches">
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="7" onclick="toggleBit(7)">Bit 7 (128): <span id="b7">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="6" onclick="toggleBit(6)">Bit 6 (64): <span id="b6">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="5" onclick="toggleBit(5)">Bit 5 (32): <span id="b5">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="4" onclick="toggleBit(4)">Bit 4 (16): <span id="b4">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="3" onclick="toggleBit(3)">Bit 3 (8): <span id="b3">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="2" onclick="toggleBit(2)">Bit 2 (4): <span id="b2">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="1" onclick="toggleBit(1)">Bit 1 (2): <span id="b1">1</span></button>
          <button class="btn btn-sm btn-outline-info bit-btn" data-bit="0" onclick="toggleBit(0)">Bit 0 (1): <span id="b0">1</span></button>
        </div>
        <div class="p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Biner (Basis 2):</div>
              <div class="fs-5 fw-bold text-success font-monospace" id="b_bin_display">11111111</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Desimal (Basis 10):</div>
              <div class="fs-4 fw-bold text-info" id="b_dec_display">255</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Heksadesimal (Basis 16):</div>
              <div class="fs-4 fw-bold text-warning font-monospace" id="b_hex_display">FF</div>
            </div>
          </div>
        </div>
        """,
        "js": """
        let bits = [1, 1, 1, 1, 1, 1, 1, 1];
        function toggleBit(index) {
          bits[index] = bits[index] === 1 ? 0 : 1;
          document.getElementById(`b${index}`).textContent = bits[index];
          let dec = 0;
          let binStr = '';
          for (let i = 7; i >= 0; i--) {
            binStr += bits[i];
            dec += bits[i] * Math.pow(2, i);
          }
          document.getElementById('b_bin_display').textContent = binStr;
          document.getElementById('b_dec_display').textContent = dec;
          document.getElementById('b_hex_display').textContent = dec.toString(16).toUpperCase().padStart(2, '0');
        }
        """
    }
}

def get_widget(subj_key):
    if subj_key in WIDGET_DATA:
        return WIDGET_DATA[subj_key]
    return {
        "title": f"Laboratorium Parameter Interaktif {subj_key.replace('_', ' ').title()}",
        "desc": "🎯 Misi Berpikir: Geser slider variabel untuk mengamati respons dan kalkulasi matematis secara langsung.",
        "html": f"""
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Parameter x: <span id="gen_val_x" class="fw-bold text-info">5</span></label>
            <input type="range" class="form-range" id="gen_slider_x" min="1" max="50" value="5" oninput="updateGenericSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Faktor Skalar k: <span id="gen_val_k" class="fw-bold text-warning">2</span></label>
            <input type="range" class="form-range" id="gen_slider_k" min="1" max="10" value="2" oninput="updateGenericSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="d-flex justify-content-between">
            <div><span class="small text-muted">Output Kalkulasi f(x) = k · x²:</span><div class="fs-5 fw-bold text-success" id="gen_out">50</div></div>
            <div><span class="small text-muted">Nilai Invers / Akar:</span><div class="fs-5 fw-bold text-info" id="gen_sqrt">2.24</div></div>
          </div>
        </div>
        """,
        "js": """
        function updateGenericSim() {
          const x = parseInt(document.getElementById('gen_slider_x').value);
          const k = parseInt(document.getElementById('gen_slider_k').value);
          document.getElementById('gen_val_x').textContent = x;
          document.getElementById('gen_val_k').textContent = k;
          document.getElementById('gen_out').textContent = k * x * x;
          document.getElementById('gen_sqrt').textContent = Math.sqrt(x).toFixed(2);
        }
        """
    }




# 16 Subjek Terdaftar Lengkap
SUBJECTS = {
    "aljabar": {
        "title": "Pengenalan Aljabar & PLSV", "short": "Aljabar",
        "icon": "bi-calculator", "color": "#6366f1",
        "desc": "Kuasai dasar-dasar variabel, ekspresi aljabar, faktorisasi, dan persamaan linear satu variabel secara interaktif.",
        "bab_titles": [
            "Fondasi: Latar Belakang & Konsep Variabel",
            "Anatomi: Struktur Suku & Sifat Operasi Aljabar",
            "Mekanika: Pemfaktoran & Ekspansi Aljabar",
            "Pemodelan: Persamaan Linear Satu Variabel (PLSV)",
            "Capstone: Proyek Sintesis Pemodelan Nyata"
        ],
        "formulas": [
            r"ax + b = c \iff ax = c - b \implies x = \frac{c - b}{a} \quad (a \neq 0)",
            r"(a + b)^2 = a^2 + 2ab + b^2 \quad ; \quad (a - b)^2 = a^2 - 2ab + b^2",
            r"a^2 - b^2 = (a - b)(a + b) \quad ; \quad (x+p)(x+q) = x^2 + (p+q)x + pq",
            r"3(2x - 4) = 4x + 8 \implies 6x - 12 = 4x + 8 \implies 2x = 20 \implies x = 10",
            r"K = 2(p + l) \implies 48 = 2((2x+3) + (x-1)) \implies 48 = 2(3x + 2) \implies x = 7"
        ],
        "formula_meanings": [
            "x merepresentasikan variabel yang dicari, a adalah koefisien skalar pengali, b konstanta pergeseran, dan c nilai target.",
            "a² dan b² adalah kuadrat suku mandiri, sedangkan 2ab adalah suku interaksi perkalian silang antar dua variabel.",
            "Bentuk selisih dua kuadrat menyatakan bahwa a² - b² selalu dapat difaktorkan menjadi perkalian suku jumlah dan selisihnya.",
            "Prinsip ekuivalensi: operasi perkalian atau penjumlahan yang dilakukan pada ruas kiri wajib dilakukan persis sama pada ruas kanan.",
            "Formula keliling persegi panjang dimodelkan sebagai fungsi variabel x untuk mencari dimensi fisik optimal."
        ],
        "theories": [
            "Aljabar adalah bahasa universal matematika yang menggantikan angka konkrit dengan simbol/huruf (variabel) untuk menyatakan hubungan umum dan menemukan pola yang belum diketahui nilainya.",
            "Bentuk aljabar tersusun dari koefisien (angka pengali), variabel (huruf penampung nilai), konstanta (angka tetap), dan suku-suku yang dipisahkan oleh operator aritmatika.",
            "Pemfaktoran adalah teknik dekomposisi untuk menguraikan bentuk penjumlahan polinomial menjadi bentuk perkalian faktor-faktor prima aljabar.",
            "PLSV (Persamaan Linear Satu Variabel) adalah kalimat matematika terbuka bertanda sama dengan (=) dengan variabel berderajat satu.",
            "Capstone aljabar menguji kemampuan sintesis siswa dalam memodelkan permasalahan optimasi biaya, dimensi arsitektur, dan alokasi sumber daya."
        ],
        "examples": [
            "Contoh 1: Sebuah kotak memuat sejumlah pensil x. Jika ditambah 5 pensil totalnya menjadi 14, maka model aljabarnya adalah x + 5 = 14 => x = 9 pensil.",
            "Contoh 2: Sederhanakan bentuk 4x + 7y - 2x + 3y. Kelompokkan suku sejenis: (4x - 2x) + (7y + 3y) = 2x + 10y.",
            "Contoh 3: Faktorkan x² + 5x + 6. Cari dua bilangan yang jika dijumlahkan bernilai 5 dan dikalikan bernilai 6, yaitu 2 dan 3. Hasilnya (x + 2)(x + 3).",
            "Contoh 4: Selesaikan 5(x - 2) = 2x + 8. Distribusikan: 5x - 10 = 2x + 8 => 3x = 18 => x = 6.",
            "Contoh 5 (Capstone): Lapangan persegi panjang berukuran panjang (3x + 2) m dan lebar (x + 4) m memiliki keliling 44 m. Tentukan luasnya: K = 2(4x + 6) = 44 => 8x + 12 = 44 => 8x = 32 => x = 4. Maka p = 14 m, l = 8 m, Luas = 112 m²."
        ],
        "quiz": [
            ("Jika 4x - 8 = 16, berapakah nilai x?", ["x = 6", "x = 4", "x = 8"], 0, "4x = 16 + 8 = 24 => x = 24 / 4 = 6."),
            ("Bentuk sederhana dari 5x + 3y - 2x + 4y adalah?", ["3x + 7y", "7x + 7y", "3x - y"], 0, "Kelompokkan suku sejenis: (5x - 2x) + (3y + 4y) = 3x + 7y."),
            ("Hasil ekspansi dari (x - 3)(x + 3) adalah?", ["x² - 9", "x² + 9", "x² - 6x + 9"], 0, "Sifat selisih dua kuadrat: (a - b)(a + b) = a² - b²."),
            ("Himpunan penyelesaian dari 3x + 5 = x + 13 adalah?", ["x = 4", "x = 6", "x = 9"], 0, "3x - x = 13 - 5 => 2x = 8 => x = 4."),
            ("Jika keliling lapangan 44 m dengan p = 3x+2 dan l = x+4, berapakah luasnya?", ["112 m²", "96 m²", "120 m²"], 0, "Didapat x = 4, maka p = 14 m dan l = 8 m. Luas = 14 × 8 = 112 m².")
        ]
    }
}

# Definisi Detail Materi Matematika & Soal Latihan Nyata untuk 16 Subjek
SUBJECTS = {
    "aljabar": {
        "title": "Pengenalan Aljabar & PLSV", "short": "Aljabar",
        "icon": "bi-calculator", "color": "#6366f1",
        "desc": "Kuasai dasar-dasar variabel, ekspresi aljabar, faktorisasi, dan persamaan linear satu variabel secara interaktif.",
        "bab_titles": [
            "Fondasi: Latar Belakang & Konsep Variabel",
            "Anatomi: Struktur Suku & Sifat Operasi Aljabar",
            "Mekanika: Pemfaktoran & Ekspansi Aljabar",
            "Pemodelan: Persamaan Linear Satu Variabel (PLSV)",
            "Capstone: Proyek Evaluasi Sintesis Pemodelan Aljabar"
        ],
        "formulas": [
            r"ax + b = c \iff ax = c - b \implies x = \frac{c - b}{a} \quad (a \neq 0)",
            r"(a + b)^2 = a^2 + 2ab + b^2 \quad ; \quad (a - b)^2 = a^2 - 2ab + b^2",
            r"a^2 - b^2 = (a - b)(a + b) \quad ; \quad (x+p)(x+q) = x^2 + (p+q)x + pq",
            r"3(2x - 4) = 4x + 8 \implies 6x - 12 = 4x + 8 \implies 2x = 20 \implies x = 10",
            r"K = 2(p + l) = 44 \implies 2((3x+2) + (x+4)) = 44 \implies 8x + 12 = 44 \implies x = 4"
        ],
        "formula_meanings": [
            "x adalah variabel tak diketahui, a adalah koefisien pengali, b konstanta pergeseran, dan c target persamaan.",
            "Bentuk kuadrat sempurna menguraikan kuadrat mandiri a² dan b² serta suku silang interaksi 2ab.",
            "Selisih dua kuadrat menyatakan bahwa a² - b² dapat didekomposisi menjadi perkalian jumlah dan selisihnya.",
            "Prinsip ekuivalensi: manipulasi aljabar di ruas kiri harus diterapkan identik pada ruas kanan.",
            "Pemodelan dimensi fisik persegi panjang dengan ekspresi aljabar untuk menghitung luas maksimum."
        ],
        "theories": [
            "Aljabar menggantikan nilai konkrit dengan simbol variabel untuk merumuskan hukum universal matematika dan pola umum.",
            "Struktur aljabar tersusun atas koefisien, variabel, konstanta, dan suku sejenis yang dapat disederhanakan.",
            "Pemfaktoran adalah proses invers dari ekspansi perkalian untuk mencari akar-akar persamaan.",
            "PLSV memodelkan hubungan kesetaraan linier dengan tepat satu solusi unik pada himpunan bilangan riil.",
            "Capstone Aljabar menguji kemampuan sintesis siswa dalam memecahkan masalah optimasi dimensi dan alokasi sumber daya."
        ],
        "examples": [
            "Contoh 1: Sebuah kotak memuat x pensil. Ditambah 5 pensil menjadi 14. Model: x + 5 = 14 => x = 9.",
            "Contoh 2: Sederhanakan 5x + 7y - 2x + 3y. Kelompokkan suku sejenis: (5x - 2x) + (7y + 3y) = 3x + 10y.",
            "Contoh 3: Faktorkan x² + 7x + 12. Cari dua angka dijumlah 7, dikali 12 => (x + 3)(x + 4).",
            "Contoh 4: Selesaikan 4(x - 3) = 2x + 6 => 4x - 12 = 2x + 6 => 2x = 18 => x = 9.",
            "Contoh 5 (Capstone): Lapangan dengan p = (3x+2) m dan l = (x+4) m memiliki keliling 44 m. Didapat x = 4, maka p = 14 m, l = 8 m, Luas = 112 m²."
        ],
        "quiz": [
            ("Jika 4x - 8 = 16, berapakah nilai x?", ["x = 6", "x = 4", "x = 8"], 0, "4x = 16 + 8 = 24 => x = 24 / 4 = 6."),
            ("Bentuk sederhana dari 6x + 4y - 2x + 5y adalah?", ["4x + 9y", "8x + 9y", "4x - y"], 0, "Kelompokkan suku sejenis: (6x - 2x) + (4y + 5y) = 4x + 9y."),
            ("Hasil ekspansi aljabar dari (x - 5)(x + 5) adalah?", ["x² - 25", "x² + 25", "x² - 10x + 25"], 0, "Sifat selisih dua kuadrat: (a - b)(a + b) = a² - b² = x² - 25."),
            ("Himpunan penyelesaian dari 5x - 7 = 2x + 8 adalah?", ["x = 5", "x = 3", "x = 15"], 0, "5x - 2x = 8 + 7 => 3x = 15 => x = 5."),
            ("Tantangan Capstone: Lapangan memiliki keliling 44 m dengan p = (3x+2) dan l = (x+4). Berapakah luas area lapangan tersebut?", ["112 m²", "96 m²", "144 m²"], 0, "2(4x + 6) = 44 => 8x = 32 => x = 4. Dimensi: p = 14 m, l = 8 m. Luas = 14 × 8 = 112 m².")
        ]
    },
    "bangun_datar_dan_bangun_ruang": {
        "title": "Geometri: Bangun Datar & Ruang", "short": "Geometri",
        "icon": "bi-pentagon", "color": "#a855f7",
        "desc": "Kuasai keliling/luas 2D, volume/luas permukaan 3D, teorema Pythagoras, dan pemodelan spasial.",
        "bab_titles": [
            "Fondasi: Dimensi Geometri & Teorema Pythagoras",
            "Anatomi: Bangun Datar Baku (Segitiga, Lingkaran, Segiempat)",
            "Mekanika: Luas Permukaan & Volume Bangun Ruang 3D",
            "Pemodelan: Konstruksi & Estimasi Material Ruang",
            "Capstone: Proyek Rekayasa & Uji Evaluasi Kapasitas Ruang"
        ],
        "formulas": [
            r"c^2 = a^2 + b^2 \iff c = \sqrt{a^2 + b^2} \quad (\text{Pythagoras})",
            r"L_{\text{lingkaran}} = \pi r^2 \quad ; \quad K = 2\pi r",
            r"V_{\text{tabung}} = \pi r^2 t \quad ; \quad L_p = 2\pi r(r + t)",
            r"V_{\text{balok}} = p \cdot l \cdot t \quad ; \quad V_{\text{bola}} = \frac{4}{3}\pi r^3",
            r"V_{\text{sisa}} = V_{\text{tabung}} - V_{\text{bola}} = \pi r^2 t - \frac{4}{3}\pi r^3"
        ],
        "formula_meanings": [
            "Teorema Pythagoras menghubungkan sisi alas a, tinggi b, dan hipotenusa c pada segitiga siku-siku.",
            "Luas lingkaran merepresentasikan kerapatan kuadratik jari-jari r diskalakan konstanta pi.",
            "Volume silinder/tabung adalah luas penampang lingkaran yang diproyeksikan sepanjang tinggi t.",
            "Volume ruang 3D mengukur total kapasitas kubik fluida atau materi yang dapat ditampung.",
            "Volume fluida tersisa dihitung dari selisih volume penampung terhadap volume objek padat yang tercelup."
        ],
        "theories": [
            "Geometri mengkaji sifat ukuran, bentuk, posisi relatif bidang, dan sifat-sifat ruang dalam matematika formal.",
            "Bangun datar 2D dibatasi oleh garis lurus (poligon) atau kurva tertutup (lingkaran) dengan atribut keliling dan luas.",
            "Bangun ruang 3D memiliki kapasitas volume serta luas permukaan penutup (envelope).",
            "Aplikasi geometri mencakup perhitungan struktur sipil, arsitektur, dan optimasi kemasan logistik.",
            "Capstone Geometri menguji sintesis perhitungan volume air tumpah dan kapasitas penampungan tangki industri."
        ],
        "examples": [
            "Contoh 1: Segitiga siku-siku memiliki alas 6 cm dan tinggi 8 cm. Sisi miring c = √(6² + 8²) = √(36 + 64) = 10 cm.",
            "Contoh 2: Lingkaran dengan jari-jari r = 7 cm memiliki Luas = (22/7) × 7 × 7 = 154 cm².",
            "Contoh 3: Tabung dengan r = 7 cm dan t = 10 cm memiliki Volume = (22/7) × 49 × 10 = 1540 cm³.",
            "Contoh 4: Balok berukuran 12 cm × 8 cm × 5 cm memiliki Luas Permukaan = 2(96 + 60 + 40) = 392 cm².",
            "Contoh 5 (Capstone): Sebuah tangki tabung (r=7 cm, t=20 cm) berisi air penuh. Dimasukkan bola besi padat (r=7 cm). Berapakah volume air yang tumpah? Volume tumpah = V_bola = 4/3 × (22/7) × 343 = 1437.33 cm³."
        ],
        "quiz": [
            ("Sebuah segitiga siku-siku memiliki sisi 9 cm dan 12 cm. Berapakah panjang sisi miringnya?", ["15 cm", "21 cm", "18 cm"], 0, "c = √(9² + 12²) = √(81 + 144) = √225 = 15 cm."),
            ("Berapakah luas lingkaran yang memiliki diameter 14 cm (jari-jari 7 cm)?", ["154 cm²", "308 cm²", "88 cm²"], 0, "Luas = πr² = (22/7) × 7² = 154 cm²."),
            ("Sebuah tabung memiliki jari-jari alas 7 cm dan tinggi 10 cm. Berapakah volumenya?", ["1540 cm³", "770 cm³", "3080 cm³"], 0, "Volume = πr²t = (22/7) × 49 × 10 = 1540 cm³."),
            ("Sebuah balok berukuran 10 cm × 6 cm × 4 cm. Berapakah luas permukaannya?", ["248 cm²", "240 cm²", "124 cm²"], 0, "Lp = 2(pl + pt + lt) = 2(60 + 40 + 24) = 2(124) = 248 cm²."),
            ("Tantangan Capstone: Tangki silinder berisi air penuh (r=7 cm, t=20 cm). Jika bola besi pejal berdiameter 14 cm (r=7 cm) dicelupkan ke dalamnya, berapa volume air yang tumpah?", ["1437.33 cm³", "1540.00 cm³", "3080.00 cm³"], 0, "Volume air tumpah sama dengan volume bola yang tercelup = (4/3)πr³ = (4/3) × (22/7) × 343 ≈ 1437.33 cm³.")
        ]
    },
    "operasi_kabataku": {
        "title": "Operasi Ka-Ba-Ta-Ku & Hierarki", "short": "KaBaTaKu",
        "icon": "bi-plus-slash-minus", "color": "#64748b",
        "desc": "Kuasai hierarki operasi aritmetika PEMDAS/BODMAS, bilangan bulat, dan sifat distributif.",
        "bab_titles": [
            "Fondasi: Hierarki Operasi Hitung (BODMAS / PEMDAS)",
            "Anatomi: Bilangan Bulat Negatif & Tanda Operasi",
            "Mekanika: Prosedur Sifat Distributif & Asosiatif",
            "Pemodelan: Kalkulasi Finansial & Akuntansi Harian",
            "Capstone: Proyek Audit Neraca & Evaluasi Aritmetika"
        ],
        "formulas": [
            r"\text{Prioritas: } \text{Kurung ()} \succ \text{Pangkat } x^n \succ \text{Kali/Bagi } (\times, :) \succ \text{Tambah/Kurang } (+, -)",
            r"(-a) \times (-b) = +(a \cdot b) \quad ; \quad (-a) \times (+b) = -(a \cdot b)",
            r"a \times (b + c) = (a \times b) + (a \times c) \quad (\text{Distributif})",
            r"\text{Laba Bersih} = \text{Pendapatan} - (\text{HPP} + \text{Beban Operasional})",
            r"\text{Evaluasi Capstone: } 150 - 25 \times 4 + (72 : 8) \times 3^2"
        ],
        "formula_meanings": [
            "Urutan hierarki baku memastikan satu ekspresi matematika menghasilkan satu nilai tunggal yang konsisten.",
            "Perkalian dua bilangan bertanda sama selalu menghasilkan tanda positif, sedangkan tanda berlawanan menghasilkan negatif.",
            "Sifat distributif memungkinkan penguraian perkalian ke setiap suku dalam tanda kurung.",
            "Formulasi akuntansi mengelompokkan biaya sebelum dikurangkan terhadap penerimaan kotor.",
            "Sintesis operasi hitung multi-operator menggabungkan kurung, pangkat, perkalian, dan penjumlahan."
        ],
        "theories": [
            "Tanpa hierarki operasi baku, ekspresi seperti 2 + 3 × 4 dapat menghasilkan 20 atau 14 secara ambigu.",
            "Aturan KaBaTaKu (Kali-Bagi-Tambah-Kurang) mengevaluasi operator dari kiri ke kanan berdasarkan tingkat kekuatannya.",
            "Tanda kurung bertindak sebagai 'override' prioritas untuk memaksa kalkulasi internal diselesaikan terlebih dahulu.",
            "Kecermatan aritmatika adalah fondasi utama dalam akuntansi, sains komputer, dan rekayasa data.",
            "Capstone KaBaTaKu menguji ketelitian siswa dalam memecahkan persamaan majemuk bertingkat tanpa kesalahan hierarki."
        ],
        "examples": [
            "Contoh 1: Hitung 8 + 4 × 3. Perkalian didahulukan: 4 × 3 = 12 => 8 + 12 = 20.",
            "Contoh 2: Hitung (8 + 4) × 3. Tanda kurung didahulukan: 12 × 3 = 36.",
            "Contoh 3: Hitung -15 + (-4) × (-5). Perkalian: (-4) × (-5) = 20 => -15 + 20 = 5.",
            "Contoh 4: Hitung 100 - 60 : 5 × 2. Operasi bagi dan kali setingkat (kiri ke kanan): 60 : 5 = 12 => 12 × 2 = 24 => 100 - 24 = 76.",
            "Contoh 5 (Capstone): Evaluasi 150 - 25 × 4 + (72 : 8) × 3² => 150 - 100 + 9 × 9 = 50 + 81 = 131."
        ],
        "quiz": [
            ("Berapakah hasil dari 18 + 6 : 2 × 4?", ["30", "48", "12"], 0, "Hierarki: 6 : 2 = 3 => 3 × 4 = 12 => 18 + 12 = 30."),
            ("Berapakah hasil dari 25 - 5 × (3 + 2)?", ["0", "100", "20"], 0, "Kurung dulu: (3 + 2) = 5 => 5 × 5 = 25 => 25 - 25 = 0."),
            ("Berapakah hasil dari (-8) × (-4) + (-30) : 5?", ["26", "38", "-26"], 0, "(-8)×(-4) = 32, dan (-30):5 = -6 => 32 + (-6) = 26."),
            ("Hitung: 64 : 4 × 2 - 8?", ["24", "0", "16"], 0, "Kiri ke kanan: 64 : 4 = 16 => 16 × 2 = 32 => 32 - 8 = 24."),
            ("Tantangan Capstone: Hitung nilai akhir dari 150 - 25 × 4 + (72 : 8) × 3²?", ["131", "121", "225"], 0, "150 - 100 + 9 × 9 = 50 + 81 = 131.")
        ]
    },
    "integral": {
        "title": "Integral & Kalkulus Integral", "short": "Integral",
        "icon": "bi-infinity", "color": "#10b981",
        "desc": "Kuasai konsep akumulasi luas, antiturunan, integral tak tentu, tentu, dan volume benda putar.",
        "bab_titles": [
            "Fondasi: Intuisi Partisi Riemann & Akumulasi",
            "Anatomi: Teorema Dasar Kalkulus & Notasi Baku",
            "Mekanika: Teknik Substitusi & Integral Parsial",
            "Pemodelan: Luas Bidang & Volume Benda Putar",
            "Capstone: Proyek Rekayasa Fluida & Sintesis Integral"
        ],
        "formulas": [
            r"\int x^n \, dx = \frac{1}{n+1}x^{n+1} + C \quad (n \neq -1)",
            r"\int_a^b f(x) \, dx = F(b) - F(a) \quad (\text{Teorema Dasar Kalkulus})",
            r"\int u \, dv = u \cdot v - \int v \, du \quad (\text{Integral Parsial})",
            r"L = \int_a^b (f(x) - g(x)) \, dx \quad ; \quad V = \pi \int_a^b [f(x)]^2 \, dx",
            r"V_{\text{putar}} = \pi \int_0^4 (\sqrt{x})^2 \, dx = \pi \int_0^4 x \, dx = \pi \left[ \frac{x^2}{2} \right]_0^4 = 8\pi"
        ],
        "formula_meanings": [
            "Antiturunan menaikkan derajat pangkat polinomial sebesar 1 dan membaginya dengan pangkat baru ditambah konstanta C.",
            "Nilai akumulasi total integral tentu adalah selisih nilai fungsi antiturunan pada batas atas dikurangi batas bawah.",
            "Rumus integrasi parsial mendekomposisi perkalian fungsi yang sulit diintegrasikan secara langsung.",
            "Volume benda putar mengintegrasikan luas irisan cakram lingkaran π[f(x)]² sepanjang sumbu rotasi.",
            "Sintesis Capstone menghitung volume solid hasil putaran kurva akar terhadap sumbu horizontal."
        ],
        "theories": [
            "Integral adalah proses akumulasi kuantitas kontinu yang bermula dari penjumlahan irisan-irisan kecil (Riemann Sum).",
            "Teorema Dasar Kalkulus menghubungkan dua pilar utama: diferensiasi (laju perubahan) dan integrasi (akumulasi).",
            "Teknik substitusi aljabar menyederhanakan bentuk komposit f(g(x))g'(x) menjadi bentuk baku f(u)du.",
            "Aplikasi integral mencakup kalkulasi pusat massa, debit aliran cairan, usaha fisika, dan probabilitas kontinu.",
            "Capstone Integral menguji pemecahan masalah volume benda putar geometris menggunakan integrasi cakram."
        ],
        "examples": [
            "Contoh 1: ∫ 3x² dx = 3(x³/3) + C = x³ + C.",
            "Contoh 2: ∫₀³ (2x + 1) dx = [x² + x]₀³ = (9 + 3) - 0 = 12.",
            "Contoh 3: ∫ 2x(x² + 4)³ dx. Misal u = x² + 4, du = 2x dx => ∫ u³ du = ¼(x² + 4)⁴ + C.",
            "Contoh 4: Luas daerah antara y = x² dan y = 4 dari x=0 s.d 2: ∫₀² (4 - x²) dx = [4x - x³/3]₀² = 8 - 8/3 = 16/3 satuan luas.",
            "Contoh 5 (Capstone): Hitung volume benda putar daerah y = √x dari x=0 sampai x=4 diputar mengelilingi sumbu-X: V = π ∫₀⁴ (√x)² dx = π [x²/2]₀⁴ = 8π satuan volume."
        ],
        "quiz": [
            ("Berapakah hasil dari ∫ (6x² - 4x + 3) dx?", ["2x³ - 2x² + 3x + C", "3x³ - 4x² + 3x + C", "6x³ - 2x² + C"], 0, "∫ 6x² dx = 2x³, ∫ -4x dx = -2x², ∫ 3 dx = 3x => 2x³ - 2x² + 3x + C."),
            ("Hitunglah nilai dari integral tentu ∫₁³ (3x²) dx?", ["26", "27", "24"], 0, "[x³]₁³ = 3³ - 1³ = 27 - 1 = 26."),
            ("Dengan substitusi u = x² + 1, tentukan ∫ 2x(x² + 1)⁴ dx?", ["⅕(x² + 1)⁵ + C", "¼(x² + 1)⁵ + C", "(x² + 1)⁵ + C"], 0, "du = 2x dx => ∫ u⁴ du = ⅕u⁵ + C = ⅕(x² + 1)⁵ + C."),
            ("Luas daerah di bawah kurva f(x) = 2x dari x = 1 sampai x = 4 adalah?", ["15 satuan luas", "16 satuan luas", "12 satuan luas"], 0, "[x²]₁⁴ = 4² - 1² = 16 - 1 = 15."),
            ("Tantangan Capstone: Daerah yang dibatasi kurva y = √x, sumbu-X, dan garis x = 4 diputar 360° mengelilingi sumbu-X. Berapakah volume benda putar yang dihasilkan?", ["8π satuan volume", "16π satuan volume", "4π satuan volume"], 0, "V = π ∫₀⁴ (√x)² dx = π ∫₀⁴ x dx = π [x²/2]₀⁴ = π(16/2) = 8π satuan volume.")
        ]
    },
    "limit": {
        "title": "Limit Fungsi Aljabar", "short": "Limit",
        "icon": "bi-arrow-right-short", "color": "#f59e0b",
        "desc": "Pahami perilaku fungsi saat mendekati titik kritis, bentuk tak tentu 0/0, dan limit tak hingga.",
        "bab_titles": [
            "Fondasi: Konsep Pendekatan & Limit Kiri-Kanan",
            "Anatomi: Bentuk Tentu vs Bentuk Tak Tentu (0/0)",
            "Mekanika: Teknik Faktorisasi & Perkalian Sekawan",
            "Pemodelan: Limit Menuju Tak Hingga & Laju Perubahan",
            "Capstone: Proyek Kecepatan Sesaat & Uji Sintesis Limit"
        ],
        "formulas": [
            r"\lim_{x \to c} f(x) = L \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L",
            r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x+2) = 4",
            r"\lim_{x \to 0} \frac{\sqrt{x+4} - 2}{x} \times \frac{\sqrt{x+4} + 2}{\sqrt{x+4} + 2} = \frac{1}{4}",
            r"\lim_{x \to \infty} \frac{ax^n + \dots}{bx^n + \dots} = \frac{a}{b} \quad (\text{Derajat Sama})",
            r"v(t_0) = \lim_{h \to 0} \frac{s(t_0 + h) - s(t_0)}{h} \quad (\text{Kecepatan Sesaat})"
        ],
        "formula_meanings": [
            "Limit ada jika dan hanya jika pendekatan dari sisi kiri dan sisi kanan menghasilkan nilai target yang sama.",
            "Bentuk tak tentu 0/0 diselesaikan dengan memfaktorkan faktor pembuat nol pada pembilang dan penyebut.",
            "Perkalian bentuk sekawan merasionalkan bentuk akar untuk mengeliminasi ketaknentuan 0/0.",
            "Perilaku asimtotik limit tak hingga ditentukan oleh rasio koefisien suku berderajat tertinggi.",
            "Kecepatan sesaat roket/benda dimodelkan sebagai limit perubahan posisi terhadap selang waktu mendekati nol."
        ],
        "theories": [
            "Limit mempelajari tren nilai fungsi ketika input mendekati suatu titik tertentu tanpa harus tepat berada di titik tersebut.",
            "Bila substitusi langsung menghasilkan 0/0, nilai limit sesungguhnya tersembunyi dan memerlukan manipulasi aljabar.",
            "Metode sekawan memanfaatkan identitas selisih kuadrat (a-b)(a+b) = a²-b² untuk membuka bentuk akar.",
            "Limit tak hingga memodelkan keadaan stabil jangka panjang (steady-state) dalam ekologi dan ekonomi.",
            "Capstone Limit menguji sintesis konsep kecepatan sesaat fisika menggunakan definisi limit turunan."
        ],
        "examples": [
            "Contoh 1: lim_{x->3} (2x + 4) = 2(3) + 4 = 10.",
            "Contoh 2: lim_{x->4} (x² - 16)/(x - 4) = lim_{x->4} (x - 4)(x + 4)/(x - 4) = 4 + 4 = 8.",
            "Contoh 3: lim_{x->0} (√(x+9) - 3)/x. Kalikan sekawan: x / [x(√(x+9) + 3)] = 1/(3+3) = 1/6.",
            "Contoh 4: lim_{x->inf} (6x² + 2x)/(2x² - 5) = 6/2 = 3.",
            "Contoh 5 (Capstone): Posisi roket s(t) = 2t² + 5t meter. Kecepatan sesaat pada t=3 detik: v(3) = lim_{h->0} [s(3+h) - s(3)]/h = lim_{h->0} [2(3+h)² + 5(3+h) - 33]/h = lim_{h->0} (17h + 2h²)/h = 17 m/s."
        ],
        "quiz": [
            ("Tentukan nilai dari lim_{x -> 5} (x² - 25)/(x - 5)?", ["10", "5", "0"], 0, "Faktorkan: (x-5)(x+5)/(x-5) => lim (x+5) = 5+5 = 10."),
            ("Berapakah nilai dari lim_{x -> 2} (3x² - 4x + 1)?", ["5", "9", "3"], 0, "Substitusi langsung: 3(2)² - 4(2) + 1 = 12 - 8 + 1 = 5."),
            ("Tentukan nilai dari lim_{x -> ∞} (4x³ - 2x + 1) / (2x³ + 5x²)?", ["2", "∞", "0"], 0, "Derajat tertinggi pembilang dan penyebut sama (x³), maka hasilnya 4 / 2 = 2."),
            ("Hitung lim_{x -> 0} (√(4+x) - 2) / x?", ["¼", "½", "0"], 0, "Kalikan sekawan (√(4+x)+2) => x / [x(√(4+x)+2)] => 1/(2+2) = ¼."),
            ("Tantangan Capstone: Posisi partikel dinyatakan dengan s(t) = 2t² + 5t (meter). Berapakah kecepatan sesaat partikel pada t = 3 detik?", ["17 m/s", "12 m/s", "33 m/s"], 0, "v(3) = lim_{h->0} [s(3+h)-s(3)]/h = [2(9+6h+h²) + 15+5h - 33]/h = (17h+2h²)/h => 17 m/s.")
        ]
    },
    "fungsi_turunan": {
        "title": "Fungsi Turunan & Diferensial", "short": "Turunan",
        "icon": "bi-graph-up", "color": "#ef4444",
        "desc": "Kuasai laju perubahan sesaat, aturan turunan, garis singgung, dan masalah optimasi laba maksimum.",
        "bab_titles": [
            "Fondasi: Gradien Garis Singgung & Laju Perubahan",
            "Anatomi: Kaidah Pangkat, Perkalian & Pembagian Turunan",
            "Mekanika: Aturan Rantai & Turunan Tingkat Tinggi",
            "Pemodelan: Titik Stasioner, Nilai Ekstrim & Kecekungan",
            "Capstone: Proyek Optimasi Keuntungan & Desain Maksimum"
        ],
        "formulas": [
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \quad ; \quad \frac{d}{dx}[x^n] = n x^{n-1}",
            r"(u \cdot v)' = u'v + uv' \quad ; \quad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}",
            r"\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} \quad (\text{Aturan Rantai})",
            r"f'(x) = 0 \implies x_{\text{stasioner}} \quad ; \quad f''(x) < 0 \implies \text{Maksimum}",
            r"U(x) = -2x^2 + 40x - 50 \implies U'(x) = -4x + 40 = 0 \implies x = 10 \implies U_{\text{maks}} = 150"
        ],
        "formula_meanings": [
            "Turunan adalah limit kemiringan garis secant saat jarak dua titik mendekati nol.",
            "Kaidah perkalian dan pembagian memperhitungkan interaksi simultan dua fungsi variabel.",
            "Aturan rantai mendiferensiasi fungsi komposit terluar dikalikan turunan fungsi dalamnya.",
            "Kondisi stasioner f'(x) = 0 menentukan titik puncak (maksimum) atau lembah (minimum) fungsi.",
            "Model fungsi keuntungan kuadratik dimaksimalkan dengan menetapkan turunan pertama sama dengan nol."
        ],
        "theories": [
            "Diferensial mengukur sensitivitas perubahan nilai output terhadap perubahan kecil pada variabel input.",
            "Gradien garis singgung kurva di sembarang titik x diberikan langsung oleh nilai f'(x).",
            "Uji turunan kedua (f'') menentukan kecekungan kurva (concavity) dan mengonfirmasi sifat titik ekstrim.",
            "Dalam industri, kalkulus diferensial digunakan untuk meminimalkan biaya produksi dan memaksimalkan pendapatan.",
            "Capstone Turunan menguji kemampuan merumuskan fungsi objektif bisnis dan mencari titik optimasi optimal."
        ],
        "examples": [
            "Contoh 1: f(x) = 4x³ => f'(x) = 12x².",
            "Contoh 2: f(x) = (2x+3)(x-1) => f'(x) = 2(x-1) + (2x+3)(1) = 4x + 1.",
            "Contoh 3: f(x) = (3x² - 5)⁴ => f'(x) = 4(3x² - 5)³ · (6x) = 24x(3x² - 5)³.",
            "Contoh 4: Tentukan titik puncak f(x) = -x² + 6x - 5. f'(x) = -2x + 6 = 0 => x = 3, y = -(9) + 18 - 5 = 4.",
            "Contoh 5 (Capstone): Perusahaan memodelkan laba U(x) = -2x² + 40x - 50 (dalam juta rupiah) untuk x unit produk. Laba maksimal tercapai saat U'(x) = -4x + 40 = 0 => x = 10 unit, dengan Laba Maks = -2(100) + 400 - 50 = 150 juta rupiah."
        ],
        "quiz": [
            ("Jika f(x) = 5x⁴ - 3x² + 7, berapakah f'(x)?", ["20x³ - 6x", "20x³ - 6x + 7", "5x³ - 6x"], 0, "f'(x) = 4·5x³ - 2·3x = 20x³ - 6x."),
            ("Gradien garis singgung kurva y = x² - 3x + 2 di titik x = 4 adalah?", ["m = 5", "m = 8", "m = 3"], 0, "y' = 2x - 3. Untuk x = 4, m = 2(4) - 3 = 5."),
            ("Turunan dari f(x) = (2x + 1)³ adalah?", ["6(2x + 1)²", "3(2x + 1)²", "2(2x + 1)²"], 0, "Aturan rantai: 3(2x + 1)² · 2 = 6(2x + 1)²."),
            ("Titik stasioner dari f(x) = x² - 8x + 12 terjadi pada x = ?", ["x = 4", "x = 8", "x = 6"], 0, "f'(x) = 2x - 8 = 0 => 2x = 8 => x = 4."),
            ("Tantangan Capstone: Fungsi keuntungan penjualan dinyatakan oleh U(x) = -2x² + 40x - 50 (juta rupiah). Berapakah keuntungan maksimum yang bisa diperoleh?", ["Rp 150 Juta", "Rp 200 Juta", "Rp 100 Juta"], 0, "U'(x) = -4x + 40 = 0 => x = 10. U(10) = -2(100) + 40(10) - 50 = -200 + 400 - 50 = Rp 150 Juta.")
        ]
    },
    "matriks": {
        "title": "Matriks & Aljabar Linear", "short": "Matriks",
        "icon": "bi-grid-3x3", "color": "#06b6d4",
        "desc": "Kuasai operasi matriks, transpose, determinan, invers, dan pemecahan SPLDV menggunakan matriks.",
        "bab_titles": [
            "Fondasi: Konsep Matriks, Ordo & Representasi Data",
            "Anatomi: Operasi Penjumlahan, Skalar & Perkalian Matriks",
            "Mekanika: Determinan & Invers Matriks Ordo 2x2",
            "Pemodelan: Penyelesaian SPLDV dengan Metode Invers & Cramer",
            "Capstone: Proyek Transformasi Spasial & Uji Sintesis Matriks"
        ],
        "formulas": [
            r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies \det(A) = ad - bc",
            r"A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \quad (\det(A) \neq 0)",
            r"\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} e & f \\ g & h \end{pmatrix} = \begin{pmatrix} ae+bg & af+bh \\ ce+dg & cf+dh \end{pmatrix}",
            r"A X = B \implies X = A^{-1} B \quad (\text{Solusi Sistem Linear})",
            r"\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 8 \\ 9 \end{pmatrix} \implies \begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 8 \\ 9 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}"
        ],
        "formula_meanings": [
            "Determinan mengukur faktor penskalaan luas daerah yang ditransformasikan oleh matriks.",
            "Invers matriks adalah balikan multiplikatif sehingga berlaku perkalian A · A⁻¹ = I (Matriks Identitas).",
            "Perkalian matriks mengalikan elemen baris matriks pertama dengan elemen kolom matriks kedua.",
            "Metode invers matriks menyelesaikan persamaan simultan multi-variabel dalam satu langkah aljabar linear.",
            "Sintesis Capstone memecahkan sistem transaksi ekonomi dua komoditas dengan matriks invers."
        ],
        "theories": [
            "Matriks adalah susunan skalar dalam baris dan kolom yang digunakan untuk memproses array data dan transformasi geometri.",
            "Perkalian matriks tidak bersifat komutatif secara umum (A · B ≠ B · A).",
            "Matriks yang memiliki determinan nol disebut matriks singular dan tidak memiliki invers.",
            "Aljabar linear dan matriks adalah tulang punggung dari grafika 3D komputer, AI, dan Machine Learning.",
            "Capstone Matriks menguji sintesis permodelan sistem persamaan multi-variabel secara simultan."
        ],
        "examples": [
            "Contoh 1: Ordo matriks A dengan 2 baris dan 3 kolom adalah 2x3.",
            "Contoh 2: Diketahui A=[[2, 3], [1, 4]]. det(A) = (2×4) - (3×1) = 8 - 3 = 5.",
            "Contoh 3: Invers dari A=[[4, 1], [3, 1]] dengan det=4-3=1 adalah A⁻¹ = [[1, -1], [-3, 4]].",
            "Contoh 4: Kalikan [[1, 2], [3, 4]] dengan [[2, 0], [1, 3]] = [[1·2+2·1, 1·0+2·3], [3·2+4·1, 3·0+4·3]] = [[4, 6], [10, 12]].",
            "Contoh 5 (Capstone): Selesaikan SPLDV 2x + y = 8 dan x + 3y = 9 dengan matriks invers. det = 6 - 1 = 5. X = 1/5 · [[3, -1], [-1, 2]] · [[8], [9]] = 1/5 · [[15], [10]] = [[3], [2]], maka x = 3 dan y = 2."
        ],
        "quiz": [
            ("Diketahui matriks A = [[4, 2], [3, 5]]. Berapakah nilai determinan det(A)?", ["14", "26", "10"], 0, "det(A) = (4 × 5) - (2 × 3) = 20 - 6 = 14."),
            ("Manakah kondisi agar suatu matriks bujur sangkar memiliki invers?", ["Determinan tidak sama dengan 0", "Determinan sama dengan 0", "Semua elemen bernilai positif"], 0, "Matriks memiliki invers jika non-singular (det ≠ 0)."),
            ("Jika A · B = I, maka matriks B adalah?", ["Invers dari matriks A (A⁻¹)", "Transpose dari matriks A", "Determinan dari A"], 0, "Perkalian matriks dengan inversnya menghasilkan matriks identitas I."),
            ("Hasil perkalian [[2, 1]] berordo 1x2 dengan [[3], [4]] berordo 2x1 adalah?", ["[[10]] (ordo 1x1)", "[[6, 4]]", "[[7]]"], 0, "Perkalian: (2×3) + (1×4) = 6 + 4 = 10 (ordo 1x1)."),
            ("Tantangan Capstone: Sistem persamaan 2x + y = 8 dan x + 3y = 9 diubah ke bentuk matriks AX = B. Berapakah nilai pasangan solusi (x, y)?", ["x = 3, y = 2", "x = 2, y = 4", "x = 1, y = 6"], 0, "det(A) = 2(3)-1(1) = 5. A⁻¹ = 1/5 [[3, -1], [-1, 2]]. X = 1/5 [[3·8 - 1·9], [-1·8 + 2·9]] = 1/5 [[15], [10]] = (3, 2).")
        ]
    },
    "statistika": {
        "title": "Statistika & Analisis Data", "short": "Statistika",
        "icon": "bi-bar-chart-fill", "color": "#ec4899",
        "desc": "Kuasai pemusatan data (Mean, Median, Modus), penyebaran (Varians, Standar Deviasi), dan Z-Score.",
        "bab_titles": [
            "Fondasi: Populasi, Sampel & Ukuran Pemusatan Data",
            "Anatomi: Median, Modus & Kuartil Data Tunggal/Kelompok",
            "Mekanika: Jangkauan, Ragam (Varians) & Standar Deviasi",
            "Pemodelan: Distribusi Normal & Standarisasi Skor Z",
            "Capstone: Proyek Analisis Kualitas & Evaluasi Data"
        ],
        "formulas": [
            r"\bar{x} = \frac{\sum_{i=1}^n x_i}{n} \quad (\text{Mean / Rata-rata})",
            r"Me = x_{\frac{n+1}{2}} \quad ; \quad Q_k = x_{\frac{k(n+1)}{4}}",
            r"s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} \quad ; \quad s = \sqrt{s^2} \quad (\text{Standar Deviasi})",
            r"Z = \frac{x - \mu}{\sigma} \quad (\text{Skor Standar Z})",
            r"\text{Evaluasi Data: } [70, 80, 80, 90, 100] \implies \bar{x} = 84 \implies s = 11.40"
        ],
        "formula_meanings": [
            "Mean menghitung titik keseimbangan gravitasi numerik dari seluruh data observasi.",
            "Median membagi data terurut menjadi dua bagian sama besar tanpa terpengaruh nilai ekstrem (outlier).",
            "Standar deviasi mengukur seberapa jauh sebaran data individual menyimpang dari nilai rata-ratanya.",
            "Z-Score mengonversi nilai mentah menjadi unit standar deviasi untuk membandingkan distribusi berbeda.",
            "Sintesis Capstone menghitung parameter statistik lengkap pada data evaluasi kualitas produksi."
        ],
        "theories": [
            "Statistika adalah disiplin ilmu mengenai pengumpulan, pengolahan, analisis, dan penarikan kesimpulan dari data.",
            "Ukuran pemusatan (Mean/Median/Modus) memberikan representasi nilai tipikal dari suatu gugus data.",
            "Ukuran penyebaran (Varians/Standar Deviasi) mengukur homogenitas atau heterogenitas data.",
            "Statistika deskriptif dan inferensial digunakan dalam riset sains data, bisnis intelijen, dan kontrol kualitas.",
            "Capstone Statistika menguji sintesis analisis variasi sampel data nilai ujian untuk evaluasi kurikulum."
        ],
        "examples": [
            "Contoh 1: Data: 4, 6, 8, 10. Mean = (4+6+8+10)/4 = 28/4 = 7.",
            "Contoh 2: Data: 3, 5, 7, 8, 9. Median = 7. Data: 4, 6, 8, 10 => Median = (6+8)/2 = 7.",
            "Contoh 3: Data: 5, 5, 6, 7, 8, 8, 8, 9. Modus = 8 (muncul 3 kali).",
            "Contoh 4: Nilai ujian memiliki rata-rata 75 dan simpangan baku 10. Nilai siswa Andi adalah 95. Z-Score Andi = (95 - 75)/10 = +2.0.",
            "Contoh 5 (Capstone): Sampel nilai [70, 80, 80, 90, 100]. Rata-rata = 420/5 = 84. Kuadrat deviasi: (70-84)²=196, (80-84)²=16, 16, (90-84)²=36, (100-84)²=256. Total deviasi = 520. Varians s² = 520 / 4 = 130. Standar Deviasi s = √130 ≈ 11.40."
        ],
        "quiz": [
            ("Diberikan sekumpulan data: 6, 8, 7, 9, 10. Berapakah nilai rata-rata (Mean)?", ["8.0", "7.5", "8.5"], 0, "Mean = (6 + 8 + 7 + 9 + 10) / 5 = 40 / 5 = 8.0."),
            ("Median dari kumpulan data terurut: 4, 5, 7, 8, 10, 12 adalah?", ["7.5", "7.0", "8.0"], 0, "Median = (7 + 8) / 2 = 15 / 2 = 7.5."),
            ("Jika nilai standar deviasi suatu kelompok data bernilai 0, artinya?", ["Semua nilai data identik/sama", "Data sangat bervariasi", "Rata-rata data bernilai 0"], 0, "Standar deviasi 0 berarti tidak ada variasi (seluruh nilai data sama persis)."),
            ("Nilai ujian Budi adalah 85 pada distribusi dengan rata-rata 70 dan standar deviasi 5. Berapakah Z-score Budi?", ["+3.0", "+2.0", "+1.5"], 0, "Z = (85 - 70) / 5 = 15 / 5 = +3.0."),
            ("Tantangan Capstone: Diberikan sampel data [70, 80, 80, 90, 100]. Berapakah nilai standar deviasi sampel (s) tersebut?", ["11.40", "130.00", "8.50"], 0, "Mean = 84. Jumlah kuadrat deviasi = 196 + 16 + 16 + 36 + 256 = 520. Varians s² = 520/(5-1) = 130. s = √130 ≈ 11.40.")
        ]
    }
}

# Subjek sisa dilengkapi secara otomatis dengan dataset spesifik
OTHER_KEYS = [
    ("eksponensial", "Eksponen & Fungsi Eksponensial", "Eksponen", "bi-arrow-up-right-circle", "#f97316", "Kuasai sifat perpangkatan, fungsi eksponensial, pertumbuhan dan peluruhan.",
     [
         r"a^m \cdot a^n = a^{m+n} \quad ; \quad \frac{a^m}{a^n} = a^{m-n} \quad ; \quad (a^m)^n = a^{m \cdot n}",
         r"a^{-n} = \frac{1}{a^n} \quad ; \quad a^{m/n} = \sqrt[n]{a^m} \quad (a > 0)",
         r"2^{2x - 1} = 32 \implies 2^{2x - 1} = 2^5 \implies 2x - 1 = 5 \implies x = 3",
         r"N(t) = N_0 \cdot (1 + r)^t \quad (\text{Pertumbuhan Majemuk})",
         r"N(t) = 500 \cdot 2^{t/3} \implies N(9) = 500 \cdot 2^{9/3} = 500 \cdot 8 = 4000"
     ],
     [
         "Sifat eksponen menyederhanakan perkalian basis sama menjadi penjumlahan pangkat.",
         "Pangkat negatif menyatakan kebalikan pecahan, dan pangkat pecahan menyatakan operasi bentuk akar.",
         "Persamaan eksponensial diselesaikan dengan menyamakan basis kedua ruas.",
         "Model pertumbuhan eksponensial menggambarkan pertambahan kuantitas berbanding lurus dengan nilai saat ini.",
         "Sintesis Capstone memodelkan perkembangbiakan koloni mikroorganisme terhadap waktu."
     ],
     [
         "Eksponen adalah operasi perkalian berulang dari suatu bilangan pokok sebanyak n kali.",
         "Fungsi eksponensial y = aˣ bertumbuh sangat cepat untuk a > 1 dan meluruh untuk 0 < a < 1.",
         "Persamaan eksponen banyak diaplikasikan dalam pemodelan bunga majemuk finansial dan fisika nuklir.",
         "Peluruhan radioaktif mengikuti hukum eksponensial berbasis waktu paruh.",
         "Capstone Eksponen menguji pemodelan kalkulasi jumlah bakteri setelah periode multiplikasi tertentu."
     ],
     [
         "Contoh 1: 2³ × 2⁴ = 2³⁺⁴ = 2⁷ = 128.",
         "Contoh 2: 8^(2/3) = (∛8)² = 2² = 4.",
         "Contoh 3: Selesaikan 3^(x+1) = 81. 3^(x+1) = 3⁴ => x + 1 = 4 => x = 3.",
         "Contoh 4: Tabungan Rp 1.000.000 dengan bunga majemuk 10%/tahun setelah 2 tahun: 1.000.000 × (1.1)² = Rp 1.210.000.",
         "Contoh 5 (Capstone): Koloni bakteri mula-mula 500 sel membelah diri menjadi dua setiap 3 jam. Berapakah jumlah bakteri setelah 9 jam? N(9) = 500 × 2^(9/3) = 500 × 2³ = 500 × 8 = 4.000 bakteri."
     ],
     [
         ("Berapakah nilai dari (2³ × 2²) / 2⁴?", ["2", "4", "8"], 0, "2^(3+2-4) = 2¹ = 2."),
         ("Bentuk sederhana dari 27^(2/3) adalah?", ["9", "3", "18"], 0, "27^(2/3) = (∛27)² = 3² = 9."),
         ("Jika 4^(x - 1) = 64, berapakah nilai x?", ["x = 4", "x = 3", "x = 5"], 0, "4^(x-1) = 4³ => x - 1 = 3 => x = 4."),
         ("Bentuk pangkat positif dari (x⁻² y³) / z⁻⁴ adalah?", ["(y³ z⁴) / x²", "(x² y³) / z⁴", "y³ / (x² z⁴)"], 0, "Pangkat negatif berpindah posisi: (y³ · z⁴) / x²."),
         ("Tantangan Capstone: Suatu koloni bakteri berjumlah 500 membelah diri menjadi 2 kali lipat setiap 3 jam. Berapakah jumlah bakteri setelah 9 jam?", ["4.000 bakteri", "2.000 bakteri", "1.500 bakteri"], 0, "N(9) = 500 × 2^(9/3) = 500 × 2³ = 500 × 8 = 4.000 bakteri.")
     ]
    ),
    ("logaritma", "Logaritma & Aplikasinya", "Logaritma", "bi-reception-4", "#8b5cf6", "Kuasai invers eksponensial, sifat operasi logaritma, skala pH dan desibel.",
     [
         r"^a\log b = c \iff a^c = b \quad (a > 0, a \neq 1, b > 0)",
         r"^a\log(b \cdot c) = ^a\log b + ^a\log c \quad ; \quad ^a\log\left(\frac{b}{c}\right) = ^a\log b - ^a\log c",
         r"^a\log b^n = n \cdot ^a\log b \quad ; \quad ^a\log b \cdot ^b\log c = ^a\log c",
         r"\text{pH} = -\log[H^+] \quad ; \quad \beta = 10 \log\left(\frac{I}{I_0}\right)",
         r"[H^+] = 10^{-5} \text{ M} \implies \text{pH} = -\log(10^{-5}) = -(-5) = 5"
     ],
     [
         "Logaritma adalah inversi perpangkatan yang mencari nilai eksponen dari suatu basis terhadap numerus.",
         "Perkalian di dalam numerus terurai menjadi penjumlahan logaritma mandiri.",
         "Pangkat pada numerus dapat ditarik ke depan sebagai faktor pengali skalar.",
         "Skala logaritmik mengompresi rentang dinamis yang sangat luas menjadi skala praktis linier.",
         "Sintesis Capstone menghitung derajat keasaman kimia berdasarkan konsentrasi ion hidrogen."
     ],
     [
         "Logaritma diciptakan oleh John Napier untuk menyederhanakan kalkulasi perkalian astronomis menjadi penjumlahan.",
         "Basis 10 disebut logaritma umum (Briggsian / log), sedangkan basis e (2.71828) disebut logaritma natural (ln).",
         "Sifat rantai logaritma memungkinkan perubahan basis untuk evaluasi komputasi numerik.",
         "Aplikasi logaritma mencakup skala Richter gempa bumi, intensitas bunyi desibel, dan peluruhan radioaktif.",
         "Capstone Logaritma menguji kalkulasi skala keasaman larutan kimiawi."
     ],
     [
         "Contoh 1: ²log 8 = 3 karena 2³ = 8.",
         "Contoh 2: ²log 4 + ²log 8 = ²log(4 × 8) = ²log 32 = 5.",
         "Contoh 3: ³log 81 - ³log 9 = ³log(81/9) = ³log 9 = 2.",
         "Contoh 4: Jika ²log 3 = a, tentukan ⁸log 27. ⁸log 27 = ^(2³)log(3³) = (3/3) · ²log 3 = a.",
         "Contoh 5 (Capstone): Suatu larutan memiliki konsentrasi ion hidrogen [H+] = 10⁻⁵ M. Berapakah pH larutan tersebut? pH = -log[H+] = -log(10⁻⁵) = -(-5) = 5 (Larutan bersifat asam lemah)."
     ],
     [
         ("Berapakah nilai dari ²log 64?", ["6", "5", "8"], 0, "2⁶ = 64, maka ²log 64 = 6."),
         ("Berapakah nilai dari ³log 18 - ³log 2?", ["2", "3", "9"], 0, "³log(18 / 2) = ³log 9 = 2."),
         ("Jika ⁵log x = 3, berapakah nilai x?", ["125", "15", "243"], 0, "x = 5³ = 125."),
         ("Bentuk sederhana dari ²log 3 · ³log 5 · ⁵log 8 adalah?", ["3", "8", "2"], 0, "Sifat rantai: ²log 8 = 3."),
         ("Tantangan Capstone: Hitung nilai derajat keasaman (pH) suatu larutan kimia jika konsentrasi ion hidrogen [H⁺] = 10⁻⁵ M?", ["pH = 5", "pH = -5", "pH = 9"], 0, "pH = -log(10⁻⁵) = -(-5) = 5.")
     ]
    ),
    ("probabilitas", "Probabilitas & Kombinatorik", "Probabilitas", "bi-dice-5", "#14b8a6", "Kuasai ruang sampel, permutasi, kombinasi, dan peluang majemuk.",
     [
         r"P(A) = \frac{n(A)}{n(S)} \quad (0 \leq P(A) \leq 1)",
         r"^n P_r = \frac{n!}{(n - r)!} \quad (\text{Permutasi - Urutan Diperhatikan})",
         r"^n C_r = \frac{n!}{r!(n - r)!} \quad (\text{Kombinasi - Urutan Bebas})",
         r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
         r"P(\text{2P, 1W}) = \frac{^6C_2 \cdot ^4C_1}{^{10}C_3} = \frac{15 \cdot 4}{120} = \frac{60}{120} = 0.50"
     ],
     [
         "Peluang teoritis adalah rasio banyaknya kejadian yang diharapkan terhadap total ruang sampel semesta.",
         "Permutasi menghitung susunan objek di mana urutan posisi berpengaruh (seperti juara 1, 2, 3).",
         "Kombinasi menghitung pemilihan kelompok objek tanpa memedulikan urutan penempatan.",
         "Aturan penjumlahan peluang mengeliminasi irisan ganda antar dua kejadian yang tidak saling lepas.",
         "Sintesis Capstone menghitung peluang pemilihan delegasi gabungan pria dan wanita dari suatu komite."
     ],
     [
         "Teori peluang memodelkan fenomena acak dan mengukur derajat kepastian suatu peristiwa terjadi.",
         "Faktorial n! merepresentasikan total permutasi dari n objek yang disusun berjajar.",
         "Peluang bersyarat P(A|B) mengukur peluang kejadian A dengan syarat kejadian B telah terjadi.",
         "Aplikasi peluang mencakup analisis risiko aktuaria asuransi, kecerdasan buatan, dan kontrol kualitas sampel.",
         "Capstone Probabilitas menguji sintesis kombinatorika hipergeometrik pemilihan delegasi tim."
     ],
     [
         "Contoh 1: Peluang muncul mata dadu prima (2,3,5) dari pelemparan dadu 6 sisi: P = 3/6 = 1/2.",
         "Contoh 2: Banyak susunan pengurus (Ketua, Sekretaris, Bendahara) dari 5 calon: ⁵P₃ = 5! / 2! = 60 cara.",
         "Contoh 3: Memilih 3 anggota tim dari 7 kandidat: ⁷C₃ = 7! / (3! · 4!) = 35 cara.",
         "Contoh 4: Dua dadu dilempar. Ruang sampel n(S) = 36. Peluang jumlah mata dadu 10: {(4,6), (5,5), (6,4)} => P = 3/36 = 1/12.",
         "Contoh 5 (Capstone): Dalam komite 10 orang (6 pria, 4 wanita) dipilih 3 orang delegasi. Peluang terpilih 2 pria dan 1 wanita: [⁶C₂ × ⁴C₁] / ¹⁰C₃ = (15 × 4) / 120 = 60/120 = 0.50 (50%)."
     ],
     [
         ("Dari pelemparan sebuah dadu, berapakah peluang muncul mata dadu genap?", ["½", "⅓", "⅙"], 0, "Genap = {2, 4, 6}, P = 3/6 = ½."),
         ("Banyak cara memilih Ketua dan Wakil Ketua dari 6 orang calon adalah?", ["30 cara", "15 cara", "12 cara"], 0, "Permutasi ⁶P₂ = 6 × 5 = 30 cara."),
         ("Berapakah nilai kombinasi dari ⁸C₃?", ["56", "336", "24"], 0, "⁸C₃ = (8 × 7 × 6) / (3 × 2 × 1) = 56."),
         ("Dua koin dilempar bersamaan. Peluang muncul paling sedikit 1 gambar adalah?", ["¾", "½", "¼"], 0, "Ruang sampel = {AA, AG, GA, GG}. Kejadian = {AG, GA, GG} => P = ¾."),
         ("Tantangan Capstone: Dari 10 anggota (6 pria, 4 wanita) dipilih 3 orang. Berapakah peluang terpilih 2 pria dan 1 wanita?", ["0.50 (50%)", "0.25 (25%)", "0.75 (75%)"], 0, "[⁶C₂ × ⁴C₁] / ¹⁰C₃ = (15 × 4) / 120 = 60 / 120 = 0.50.")
     ]
    ),
    ("vektor", "Vektor & Geometri Ruang", "Vektor", "bi-arrows-move", "#3b82f6", "Kuasai besaran vektor, aljabar vektor, dot product, cross product, dan proyeksi.",
     [
         r"|\vec{v}| = \sqrt{x^2 + y^2 + z^2} \quad ; \quad \hat{u} = \frac{\vec{v}}{|\vec{v}|}",
         r"\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z = |\vec{a}| |\vec{b}| \cos\theta",
         r"\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| |\vec{b}|} \quad (\theta = 90^\circ \iff \vec{a} \cdot \vec{b} = 0)",
         r"W = \vec{F} \cdot \vec{s} \quad (\text{Usaha Fisika})",
         r"W = (4\hat{i} + 3\hat{j} + 2\hat{k}) \cdot (5\hat{i} + 2\hat{j} - \hat{k}) = 20 + 6 - 2 = 24 \text{ Joule}"
     ],
     [
         "Panjang atau magnitudo vektor dihitung menggunakan generalisasi Pythagoras 3 dimensi.",
         "Dot product mengalikan komponen skalar yang sebidang untuk mengukur proyeksi ortogonal.",
         "Dua vektor saling tegak lurus (ortogonal) jika dan hanya jika hasil dot product-nya bernilai nol.",
         "Usaha mekanika fisika didefinisikan sebagai perkalian titik antara vektor gaya dan vektor perpindahan.",
         "Sintesis Capstone menghitung usaha skalar total yang dilakukan oleh vektor gaya spasial 3D."
     ],
     [
         "Vektor adalah besaran yang memiliki nilai (magnitudo) dan arah spesifik di dalam ruang.",
         "Penjumlahan vektor mengikuti aturan jajaran genjang atau metode segitiga grafis.",
         "Cross product (perkalian silang) menghasilkan vektor baru yang tegak lurus terhadap kedua vektor pembentuknya.",
         "Vektor digunakan secara masif dalam fisika gerak, mekanika robotika, dan grafika game engine 3D.",
         "Capstone Vektor menguji kalkulasi usaha mekanika energi menggunakan perkalian skalar dot product."
     ],
     [
         "Contoh 1: Vektor v = (3, 4). Panjang |v| = √(3² + 4²) = √25 = 5 satuan.",
         "Contoh 2: Diketahui a = (2, -1, 3) dan b = (4, 2, -1). a · b = (2)(4) + (-1)(2) + (3)(-1) = 8 - 2 - 3 = 3.",
         "Contoh 3: Tentukan apakah u = (2, 3) dan v = (-6, 4) saling tegak lurus. u · v = 2(-6) + 3(4) = -12 + 12 = 0 => Tegak lurus.",
         "Contoh 4: Vektor satuan dari v = (0, 3, 4) dengan |v|=5 adalah û = (0, 3/5, 4/5).",
         "Contoh 5 (Capstone): Gaya F = (4, 3, 2) N memindahkan benda sejauh s = (5, 2, -1) m. Usaha total yang dilakukan gaya: W = F · s = (4×5) + (3×2) + (2×-1) = 20 + 6 - 2 = 24 Joule."
     ],
     [
         ("Berapakah panjang magnitudo dari vektor v = (3, 4, 12)?", ["13", "15", "19"], 0, "|v| = √(3² + 4² + 12²) = √(9 + 16 + 144) = √169 = 13."),
         ("Hasil perkalian titik (dot product) dari a = (2, 3) dan b = (4, -1) adalah?", ["5", "11", "8"], 0, "a · b = (2×4) + (3×-1) = 8 - 3 = 5."),
         ("Jika dua vektor saling tegak lurus (sudut 90°), berapakah hasil dot product-nya?", ["0", "1", "-1"], 0, "cos 90° = 0, sehingga a · b = 0."),
         ("Vektor satuan dari v = (6, 8) adalah?", ["(0.6, 0.8)", "(6, 8)", "(3, 4)"], 0, "|v| = 10, maka û = (6/10, 8/10) = (0.6, 0.8)."),
         ("Tantangan Capstone: Gaya F = (4, 3, 2) Newton bekerja memindahkan balok sejauh s = (5, 2, -1) meter. Berapakah usaha W (dalam Joule) yang dihasilkan?", ["24 Joule", "28 Joule", "20 Joule"], 0, "W = F · s = 4(5) + 3(2) + 2(-1) = 20 + 6 - 2 = 24 Joule.")
     ]
    ),
    ("desimal", "Pecahan, Desimal & Persen", "Desimal", "bi-percent", "#84cc16", "Kuasai konversi pecahan, desimal, persentase, diskon bertingkat, dan rasio.",
     [
         r"\frac{a}{b} = a \div b \quad ; \quad \text{Persen} = \left(\frac{a}{b}\right) \times 100\%",
         r"\text{Harga Diskon} = \text{Harga Awal} \times (1 - d)",
         r"\text{Diskon Ganda } d_1 + d_2 \implies \text{Faktor Bayar} = (1 - d_1) \times (1 - d_2)",
         r"\text{Pajak PPN} = \text{Harga} \times (1 + \text{Tarif})",
         r"\text{Bayar Capstone} = 200.000 \times (1 - 0.30) \times (1 - 0.10) = 200.000 \times 0.70 \times 0.90 = \text{Rp } 126.000"
     ],
     [
         "Pecahan biasa menyatakan proporsi bagian dari keseluruhan yang dapat diekspresikan sebagai desimal dan persen.",
         "Diskon tunggal mengurangi persentase harga dasar secara linier.",
         "Diskon bertingkat diaplikasikan secara sekuensial terhadap sisa harga, bukan dijumlahkan secara langsung.",
         "Pajak pertambahan nilai meningkatkan kewajiban pembayaran akhir secara proporsional.",
         "Sintesis Capstone menghitung harga akhir belanja setelah dikenakan promosi diskon ganda bertingkat."
     ],
     [
         "Representasi numerik rasional menghubungkan bentuk pecahan murni, format desimal desis, dan format persentil.",
         "Kecermatan konversi desimal krusial dalam komputasi moneter, perbankan, dan perdagangan ritel.",
         "Kesalahan umum dalam diskon bertingkat (30% + 10%) adalah menganggapnya sama dengan diskon 40%.",
         "Aritmetika desimal digunakan dalam penentuan margin laba, rasio finansial, dan konversi satuan metrik.",
         "Capstone Desimal menguji ketepatan kalkulasi transaksi finansial konsumen pada promo diskon bertingkat."
     ],
     [
         "Contoh 1: Bentuk desimal dari 3/8 adalah 3 ÷ 8 = 0.375 = 37.5%.",
         "Contoh 2: 0.65 dalam bentuk pecahan paling sederhana: 65/100 = 13/20.",
         "Contoh 3: Celana seharga Rp 150.000 diskon 20%. Harga bayar = 150.000 × 0.80 = Rp 120.000.",
         "Contoh 4: Hitung 2.45 + 1.8 - 0.65 = 3.60.",
         "Contoh 5 (Capstone): Baju berlabel Rp 200.000 mendapatkan diskon bertingkat 30% + 10%. Harga akhir yang harus dibayar kasir: 200.000 × (1 - 0.30) × (1 - 0.10) = 200.000 × 0.70 × 0.90 = 140.000 × 0.90 = Rp 126.000."
     ],
     [
         ("Berapakah bentuk persen dari pecahan ⅘?", ["80%", "75%", "85%"], 0, "⅘ × 100% = 80%."),
         ("Bentuk pecahan paling sederhana dari 0.375 adalah?", ["⅜", "⅗", "¼"], 0, "375/1000 disederhanakan dibagi 125 = ⅜."),
         ("Barang seharga Rp 100.000 diskon 25%. Berapakah yang harus dibayar?", ["Rp 75.000", "Rp 80.000", "Rp 25.000"], 0, "100.000 × (1 - 0.25) = Rp 75.000."),
         ("Berapakah hasil dari 0.4 × 0.25?", ["0.10", "0.01", "1.00"], 0, "0.4 × 0.25 = 0.10."),
         ("Tantangan Capstone: Suatu barang seharga Rp 200.000 mendapatkan promo diskon bertingkat 30% + 10%. Berapakah harga akhir yang harus dibayar pembeli?", ["Rp 126.000", "Rp 120.000", "Rp 140.000"], 0, "200.000 × 0.70 × 0.90 = 140.000 × 0.90 = Rp 126.000.")
     ]
    ),
    ("matematika_diskrit", "Matematika Diskrit & Logika", "Mat. Diskrit", "bi-diagram-3", "#475569", "Kuasai tabel kebenaran, teori himpunan, relasi fungsi, kardinalitas, dan graf.",
     [
         r"n(A \cup B) = n(A) + n(B) - n(A \cap B) \quad (\text{Prinsip Inklusi-Eksklusi})",
         r"p \implies q \equiv \neg p \lor q \quad (\text{Implikasi Ekuivalen})",
         r"\neg(p \land q) \equiv \neg p \lor \neg q \quad (\text{Hukum De Morgan})",
         r"|P(S)| = 2^{|S|} \quad (\text{Banyak Himpunan Kuasa})",
         r"n((A \cup B)^c) = 100 - (60 + 50 - 25) = 100 - 85 = 15 \text{ orang}"
     ],
     [
         "Prinsip inklusi-eksklusi menghitung gabungan himpunan dengan mengurangi irisan ganda.",
         "Implikasi matematis ekuivalen logis dengan disjungsi negasi anteseden dan konsekuen.",
         "Hukum De Morgan mendistribusikan negasi ke dalam konjungsi atau disjungsi logika.",
         "Himpunan kuasa berisi semua kombinasi sub-himpunan yang dapat dibentuk dari himpunan dasar.",
         "Sintesis Capstone menghitung jumlah populasi yang tidak termasuk dalam kedua kelompok minat."
     ],
     [
         "Matematika diskrit mengkaji struktur matematika berhingga yang tidak kontinu, menjadi landasan ilmu komputer.",
         "Logika proposisional membangun fondasi pembuktian formal dan sirkuit logika digital gerbang biner.",
         "Teori himpunan mendasari struktur database relasional (SQL joins/unions).",
         "Teori graf memodelkan jaringan telekomunikasi, rute terpendek (Dijkstra), dan jejaring sosial.",
         "Capstone Diskrit menguji analisis survei menggunakan diagram Venn dan prinsip inklusi-eksklusi."
     ],
     [
         "Contoh 1: Himpunan A = {1, 2, 3}, B = {3, 4, 5}. A ∩ B = {3}, A ∪ B = {1, 2, 3, 4, 5}.",
         "Contoh 2: Jika himpunan S memiliki 3 anggota, banyak himpunan bagian |P(S)| = 2³ = 8 himpunan.",
         "Contoh 3: Tabel kebenaran implikasi p => q bernilai Salah hanya jika p Benar dan q Salah.",
         "Contoh 4: Negasi dari 'Hari hujan dan jalan basah' adalah 'Hari tidak hujan ATAU jalan tidak basah'.",
         "Contoh 5 (Capstone): Dari survei 100 mahasiswa: 60 suka Algoritma, 50 suka Kalkulus, 25 suka keduanya. Jumlah mahasiswa yang tidak suka keduanya: 100 - (60 + 50 - 25) = 100 - 85 = 15 mahasiswa."
     ],
     [
         ("Jika A = {a, b, c, d}, berapakah banyak himpunan bagian yang mungkin dibuat dari A?", ["16", "8", "12"], 0, "Banyak himpunan bagian = 2⁴ = 16."),
         ("Pernyataan majemuk p ∧ q (konjungsi) bernilai Benar hanya jika?", ["Kedua p dan q bernilai Benar", "Salah satu bernilai Benar", "p bernilai Salah"], 0, "Konjungsi mensyaratkan kedua proposisi bernilai Benar."),
         ("Negasi dari implikasi p ⇒ q adalah?", ["p ∧ ¬q", "¬p ∨ q", "¬p ⇒ ¬q"], 0, "¬(p ⇒ q) ≡ ¬(¬p ∨ q) ≡ p ∧ ¬q."),
         ("Diketahui n(A) = 20, n(B) = 15, dan n(A ∩ B) = 5. Berapakah n(A ∪ B)?", ["30", "35", "25"], 0, "n(A ∪ B) = 20 + 15 - 5 = 30."),
         ("Tantangan Capstone: Dari 100 mahasiswa, 60 menyukai Algoritma, 50 menyukai Kalkulus, dan 25 menyukai keduanya. Berapa mahasiswa yang TIDAK menyukai keduanya?", ["15 orang", "25 orang", "10 orang"], 0, "Total gabungan = 60 + 50 - 25 = 85. Yang tidak suka = 100 - 85 = 15 orang.")
     ]
    ),
    ("persamaan_linear", "Sistem Persamaan Linear", "SPLDV", "bi-braces-asterisk", "#d97706", "Kuasai SPLDV dan SPLTV dengan eliminasi, substitusi, dan titik potong grafik.",
     [
         r"\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases} \implies (x^*, y^*)",
         r"x = \frac{c_1 b_2 - c_2 b_1}{a_1 b_2 - a_2 b_1} \quad ; \quad y = \frac{a_1 c_2 - a_2 c_1}{a_1 b_2 - a_2 b_1}",
         r"\text{Eliminasi: Menyamakan koefisien variabel untuk dieliminasi}",
         r"\text{Titik Potong Grafik} = \text{Solusi Tunggal Himpunan Penyelesaian}",
         r"\begin{cases} x + y = 50 \\ 2x + 4y = 140 \end{cases} \implies 2x + 2y = 100 \implies 2y = 40 \implies y = 20, x = 30"
     ],
     [
         "SPLDV mencari pasangan nilai koordinat (x, y) yang memenuhi kedua persamaan secara simultan.",
         "Aturan Cramer menghitung solusi dari perbandingan determinan minor matriks koefisien.",
         "Metode eliminasi mengurangkan persamaan linier setelah menyesuaikan faktor pengali koefisien.",
         "Representasi geometris menunjukkan solusi sebagai titik perpotongan dua garis lurus di bidang kartesius.",
         "Sintesis Capstone memodelkan sistem parkir kendaraan roda 2 dan roda 4."
     ],
     [
         "Sistem persamaan linear mendeskripsikan hubungan interaksi banyak variabel dengan derajat pangkat satu.",
         "Tiga kemungkinan solusi SPL: tepat satu solusi (berpotongan), tak hingga solusi (berimpit), atau tidak ada solusi (sejajar).",
         "Metode substitusi menggantikan variabel dari satu persamaan ke persamaan lainnya.",
         "Pemodelan SPLDV digunakan dalam riset operasional, optimasi logistik, dan ekonomi mikro.",
         "Capstone SPLDV menguji pemecahan studi kasus nyata inventaris kendaraan parkir."
     ],
     [
         "Contoh 1: x + y = 10 dan x - y = 4. Jumlahkan: 2x = 14 => x = 7, maka y = 3.",
         "Contoh 2: 2x + y = 7 dan x + 2y = 8. Eliminasi x: 2(x+2y=8) => 2x+4y=16. Kurangkan: 3y = 9 => y = 3, x = 2.",
         "Contoh 3: Tentukan titik potong y = 2x + 1 dan y = -x + 4. 2x + 1 = -x + 4 => 3x = 3 => x = 1, y = 3. HP = {(1, 3)}.",
         "Contoh 4: Harga 2 buku dan 3 pensil Rp 17.000, sedangkan 1 buku dan 2 pensil Rp 10.000. Didapat harga 1 buku = Rp 4.000, 1 pensil = Rp 3.000.",
         "Contoh 5 (Capstone): Tempat parkir memuat 50 kendaraan (motor x dan mobil y) dengan total roda 140. Model: x + y = 50 dan 2x + 4y = 140. Kalikan persamaan 1 dengan 2: 2x + 2y = 100. Kurangkan: 2y = 40 => y = 20 mobil, maka x = 30 motor."
     ],
     [
         ("Himpunan penyelesaian dari sistem x + y = 8 dan x - y = 2 adalah?", ["x = 5, y = 3", "x = 6, y = 2", "x = 4, y = 4"], 0, "2x = 10 => x = 5, y = 8 - 5 = 3."),
         ("Jika 2x + 3y = 12 dan x = 3, berapakah nilai y?", ["y = 2", "y = 3", "y = 1"], 0, "2(3) + 3y = 12 => 6 + 3y = 12 => 3y = 6 => y = 2."),
         ("Dua garis dalam SPLDV yang sejajar dan tidak berpotongan memiliki?", ["Tidak memiliki solusi", "Satu solusi unik", "Tak hingga solusi"], 0, "Garis sejajar tidak berpotongan sehingga tidak memiliki solusi."),
         ("Harga 3 buku dan 2 pulpen Rp 13.000, harga 1 buku dan 2 pulpen Rp 7.000. Berapa harga 1 buku?", ["Rp 3.000", "Rp 2.000", "Rp 4.000"], 0, "Kurangkan kedua persamaan: 2 buku = Rp 6.000 => 1 buku = Rp 3.000."),
         ("Tantangan Capstone: Di tempat parkir terdapat 50 kendaraan yang terdiri dari motor (2 roda) dan mobil (4 roda). Jika jumlah roda seluruhnya 140, berapakah banyak mobil di tempat parkir?", ["20 mobil", "30 mobil", "25 mobil"], 0, "x + y = 50 dan 2x + 4y = 140. 2(50 - y) + 4y = 140 => 100 + 2y = 140 => 2y = 40 => y = 20 mobil (dan 30 motor).")
     ]
    ),
    ("sistem_bilangan", "Sistem Bilangan (Biner, Oktal, Hex)", "Sis. Bilangan", "bi-cpu", "#334155", "Kuasai konversi basis 2, 8, 10, 16, aritmetika biner, dan representasi memori.",
     [
         r"N_{10} = \sum_{i=0}^n d_i \cdot b^i \quad (b = 2, 8, 10, 16)",
         r"\text{Desimal ke Biner: Pembagian berulang modulo 2}",
         r"1 \text{ Byte} = 8 \text{ Bits} \implies 00000000_2 \text{ s.d. } 11111111_2 = 255_{10}",
         r"\text{Heksadesimal: Basis 16 } (0\text{-}9, A=10, B=11, C=12, D=13, E=14, F=15)",
         r"2\text{F}_{16} = 2 \times 16^1 + 15 \times 16^0 = 32 + 15 = 47_{10} = 00101111_2"
     ],
     [
         "Sistem nilai tempat polinomial menghitung nilai absolut dengan mengalikan digit terhadap bobot basis berpangkat.",
         "Algoritma modulo mengumpulkan sisa bagi dari bawah ke atas untuk membentuk representasi basis baru.",
         "Satu byte data memori tersusun atas 8 digit biner yang merepresentasikan integer 0 hingga 255.",
         "Notasi heksadesimal mengelompokkan 4 bit biner (nibble) menjadi satu simbol heksa untuk efisiensi penulisan.",
         "Sintesis Capstone mengonversi kode warna CSS heksadesimal ke nilai intensitas desimal dan bit biner."
     ],
     [
         "Sistem bilangan adalah notasi matematis untuk menyatakan angka menggunakan simbol yang konsisten.",
         "Komputer digital bekerja dengan logika biner (0 dan 1) yang merepresentasikan status sakelar tegangan transistor.",
         "Oktal (basis 8) dan Heksadesimal (basis 16) digunakan sebagai representasi ringkas kode biner mesin.",
         "Representasi memori, alamat IP, dan kode warna RGB Web mengandalkan konversi heksadesimal.",
         "Capstone Sistem Bilangan menguji sintesis decoding nilai heksadesimal ke sistem desimal dan biner."
     ],
     [
         "Contoh 1: Konversi 13 desimal ke biner: 13/2 = 6 sisa 1; 6/2 = 3 sisa 0; 3/2 = 1 sisa 1; 1/2 = 0 sisa 1 => 1101₂.",
         "Contoh 2: Konversi 10110₂ ke desimal: 1·16 + 0·8 + 1·4 + 1·2 + 0·1 = 16 + 4 + 2 = 22₁₀.",
         "Contoh 3: Konversi 255 desimal ke Heksa: 255/16 = 15 sisa 15 (F); 15/16 = 0 sisa 15 (F) => FF₁₆.",
         "Contoh 4: Penjumlahan biner: 1010₂ (10) + 0011₂ (3) = 1101₂ (13).",
         "Contoh 5 (Capstone): Kode heksadesimal komponen warna CSS adalah 2F₁₆. Nilai desimalnya = (2 × 16) + 15 = 32 + 15 = 47₁₀. Nilai biner 8-bit = 00101111₂."
     ],
     [
         ("Berapakah representasi biner dari bilangan desimal 19?", ["10011₂", "10101₂", "11001₂"], 0, "19 = 16 + 2 + 1 = 10011₂."),
         ("Berapakah nilai desimal dari bilangan biner 1111₂?", ["15", "16", "14"], 0, "8 + 4 + 2 + 1 = 15."),
         ("Simbol huruf 'C' pada sistem heksadesimal merepresentasikan nilai desimal?", ["12", "11", "13"], 0, "A=10, B=11, C=12, D=13, E=14, F=15."),
         ("Berapakah representasi heksadesimal dari bilangan desimal 45?", ["2D₁₆", "2C₁₆", "3D₁₆"], 0, "45 / 16 = 2 sisa 13 (D) => 2D₁₆."),
         ("Tantangan Capstone: Nilai heksadesimal warna CSS #2F jika dikonversikan ke sistem desimal dan biner 8-bit adalah?", ["47₁₀ dan 00101111₂", "45₁₀ dan 00101101₂", "32₁₀ dan 00100000₂"], 0, "2F₁₆ = 2×16 + 15 = 47₁₀. Biner: 2 = 0010, F = 1111 => 00101111₂.")
     ]
    )
]

for key, title, short, icon, color, desc, forms, f_means, theos, examp, q_data in OTHER_KEYS:
    SUBJECTS[key] = {
        "title": title, "short": short, "icon": icon, "color": color, "desc": desc,
        "bab_titles": [
            f"Fondasi: Konsep Intuitif & Pengenalan {short}",
            f"Anatomi: Notasi, Kaidah & Sifat Baku {short}",
            f"Mekanika: Prosedur Perhitungan & Operasi {short}",
            f"Pemodelan: Aplikasi Nyata & Studi Kasus {short}",
            f"Capstone: Proyek Integratif & Uji Sintesis {short}"
        ],
        "formulas": forms,
        "formula_meanings": f_means,
        "theories": theos,
        "examples": examp,
        "quiz": q_data
    }



def build_head(page_title, color, is_reader=True):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} - MathThon</title>
  <link rel="icon" href="{{{{ url_for('static', filename='image/Toko Masabuk Jaya-fotor-bg-remover-2025102202457.png') }}}}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <link rel="stylesheet" href="{{{{ url_for('static', filename='css/materi_reader.css') }}}}">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <style>
    :root {{
      --accent: {color};
      --accent-glow: {color}33;
      --accent-dim: {color}15;
      --bg-dark: #0a0d14;
      --bg-card: #111622;
      --bg-surface: #161d2e;
      --border-color: rgba(255, 255, 255, 0.08);
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      background: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
      margin: 0;
      line-height: 1.65;
    }}
    /* Topbar */
    .dic-topbar {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(10, 13, 20, 0.94);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-color);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}
    .dic-topbar-left {{ display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; }}
    .dic-back-btn {{
      color: var(--accent);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 600;
      font-size: 0.88rem;
      padding: 0.4rem 0.75rem;
      background: var(--accent-dim);
      border: 1px solid var(--accent-glow);
      border-radius: 8px;
      transition: all 0.2s;
    }}
    .dic-back-btn:hover {{ background: var(--accent); color: #fff; transform: translateY(-1px); }}
    .dic-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      padding: 0.35rem 0.75rem;
      border-radius: 20px;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .dic-timer {{ font-family: 'Fira Code', monospace; color: #38bdf8; }}
    
    /* Layout */
    .dic-layout {{
      display: grid;
      grid-template-columns: 290px 1fr;
      min-height: calc(100vh - 58px);
      max-width: 1440px;
      margin: 0 auto;
    }}
    /* Sidebar */
    .dic-sidebar {{
      background: #0d121c;
      border-right: 1px solid var(--border-color);
      padding: 1.5rem 1rem;
      position: sticky;
      top: 58px;
      height: calc(100vh - 58px);
      overflow-y: auto;
      scrollbar-width: thin;
    }}
    .dic-sb-header {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.75rem;
      background: var(--accent-dim);
      border: 1px solid var(--accent-glow);
      border-radius: 12px;
      margin-bottom: 1.5rem;
    }}
    .dic-sb-icon {{
      width: 36px;
      height: 36px;
      border-radius: 9px;
      background: var(--accent);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      flex-shrink: 0;
    }}
    .dic-sb-nav-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin: 1.25rem 0 0.5rem 0.5rem;
    }}
    .dic-chapter-link {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.7rem 0.85rem;
      border-radius: 10px;
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.86rem;
      margin-bottom: 0.35rem;
      border-left: 3px solid transparent;
      transition: all 0.2s;
    }}
    .dic-chapter-link:hover {{
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-main);
    }}
    .dic-chapter-link.active {{
      background: rgba(255, 255, 255, 0.07);
      color: #fff;
      border-left-color: var(--accent);
      font-weight: 600;
    }}
    .dic-num-badge {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      flex-shrink: 0;
    }}
    .dic-chapter-link.done .dic-num-badge {{
      background: #10b981;
      color: #fff;
    }}
    /* Anchor TOC Links in Sidebar */
    .dic-anchor-box {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.75rem;
      margin-top: 1rem;
    }}
    .dic-anchor-link {{
      display: block;
      padding: 0.35rem 0.5rem;
      font-size: 0.78rem;
      color: #64748b;
      text-decoration: none;
      border-radius: 6px;
      transition: all 0.15s;
    }}
    .dic-anchor-link:hover {{ color: var(--accent); background: var(--accent-dim); }}
    
    /* Main Content Area */
    .dic-main {{
      padding: 2.5rem 3rem;
      max-width: 900px;
      margin: 0 auto;
      width: 100%;
    }}
    .dic-crumb {{
      font-size: 0.82rem;
      color: #64748b;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
    }}
    .dic-crumb a {{ color: #64748b; text-decoration: none; }}
    .dic-crumb a:hover {{ color: var(--accent); }}
    
    /* Role Banner */
    .dic-role-banner {{
      background: linear-gradient(135deg, var(--accent-dim), rgba(255,255,255,0.02));
      border: 1px solid var(--accent-glow);
      border-radius: 14px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: flex-start;
      gap: 1rem;
    }}
    .dic-role-icon {{
      font-size: 1.4rem;
      color: var(--accent);
      line-height: 1;
      padding-top: 0.2rem;
    }}
    .dic-role-title {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent);
      margin-bottom: 0.25rem;
    }}
    .dic-role-text {{
      font-size: 0.88rem;
      color: #cbd5e1;
      margin: 0;
      line-height: 1.5;
    }}
    
    .dic-h1 {{
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin: 0 0 1rem;
      color: #f8fafc;
      line-height: 1.25;
    }}
    
    .dic-target-box {{
      background: #111622;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .dic-target-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #f8fafc;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .dic-target-list {{
      margin: 0;
      padding-left: 1.25rem;
      font-size: 0.88rem;
      color: #94a3b8;
    }}
    .dic-target-list li {{ margin-bottom: 0.35rem; }}
    
    .dic-section-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #f1f5f9;
      margin: 2.5rem 0 1rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
    }}
    
    .dic-lead {{
      font-size: 1.02rem;
      color: #cbd5e1;
      line-height: 1.8;
      margin: 1rem 0 1.5rem;
    }}
    
    .dic-formula-card {{
      background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
      border: 1px solid var(--accent-glow);
      border-radius: 14px;
      padding: 1.5rem;
      margin: 1.25rem 0;
      text-align: center;
      overflow-x: auto;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    }}
    .dic-formula-explain {{
      font-size: 0.88rem;
      color: var(--text-muted);
      border-left: 3px solid var(--accent);
      padding-left: 1rem;
      margin: 1rem 0;
      line-height: 1.6;
    }}
    
    .dic-example-box {{
      background: rgba(16, 185, 129, 0.05);
      border: 1px solid rgba(16, 185, 129, 0.2);
      border-radius: 12px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .dic-example-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #34d399;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    
    /* Interactive Math Simulation Box */
    .dic-sim-box {{
      background: #111622;
      border: 1px solid var(--accent-glow);
      border-radius: 16px;
      overflow: hidden;
      margin: 2rem 0;
      box-shadow: 0 12px 30px rgba(0,0,0,0.35);
    }}
    .dic-sim-topbar {{
      background: linear-gradient(135deg, var(--accent-dim), #161d2e);
      padding: 0.85rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-color);
    }}
    .dic-sim-title {{
      font-size: 0.9rem;
      font-weight: 700;
      color: #f8fafc;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .dic-sim-body {{
      padding: 1.5rem;
    }}
    
    /* Quiz & Recall */
    .dic-quiz-card {{
      background: #111622;
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.75rem;
      margin: 2.5rem 0;
      box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }}
    .dic-quiz-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--accent);
      letter-spacing: 0.06em;
      margin-bottom: 0.5rem;
    }}
    .dic-quiz-q {{
      font-size: 1.05rem;
      font-weight: 600;
      color: #f8fafc;
      margin-bottom: 1.25rem;
      line-height: 1.6;
    }}
    .dic-opt-btn {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.85rem 1.25rem;
      width: 100%;
      text-align: left;
      color: #cbd5e1;
      font-size: 0.9rem;
      margin-bottom: 0.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s;
    }}
    .dic-opt-btn:hover {{
      background: rgba(255, 255, 255, 0.06);
      border-color: var(--accent);
      color: #fff;
    }}
    .dic-opt-btn.ok {{
      background: rgba(16, 185, 129, 0.15);
      border-color: #10b981;
      color: #6ee7b7;
    }}
    .dic-opt-btn.bad {{
      background: rgba(239, 68, 68, 0.15);
      border-color: #ef4444;
      color: #fca5a5;
    }}
    .dic-feedback {{
      display: none;
      margin-top: 1rem;
      padding: 0.85rem 1.25rem;
      border-radius: 10px;
      font-size: 0.88rem;
    }}
    .dic-feedback.show {{ display: block; }}
    .dic-feedback.ok {{
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }}
    .dic-feedback.bad {{
      background: rgba(239, 68, 68, 0.1);
      border: 1px solid rgba(239, 68, 68, 0.3);
      color: #fca5a5;
    }}
    
    /* Bottom Navigation */
    .dic-bottom-nav {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding-top: 2rem;
      margin-top: 3rem;
      border-top: 1px solid var(--border-color);
      flex-wrap: wrap;
    }}
    .dic-nav-btn {{
      padding: 0.65rem 1.4rem;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      background: transparent;
      cursor: pointer;
    }}
    .dic-nav-btn:hover {{ background: rgba(255,255,255,0.06); color: #fff; }}
    .dic-nav-btn.primary {{
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }}
    .dic-nav-btn.primary:hover {{ opacity: 0.9; transform: translateY(-1px); }}
    
    @media (max-width: 860px) {{
      .dic-layout {{ grid-template-columns: 1fr; }}
      .dic-sidebar {{ display: none; }}
      .dic-main {{ padding: 1.5rem 1rem; }}
    }}
  </style>
</head>"""


def build_bab_html(subj_key, data, bab_num):
    color = data["color"]
    icon = data["icon"]
    short = data["short"]
    title = data["title"]
    titles = data["bab_titles"]
    total = len(titles)
    idx = bab_num - 1
    bab_title = titles[idx]
    stage = STAGE_DEFINITIONS[idx]
    widget = get_widget(subj_key)
    
    formula = data["formulas"][idx]
    formula_meaning = data["formula_meanings"][idx]
    theory = data["theories"][idx]
    example = data["examples"][idx]
    q_text, opts, correct_idx, explain = data["quiz"][idx]

    # Prev and Next URLs (Intra-Module Chapter Navigation)
    prev_url = f"{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={bab_num - 1}) }}}}" if bab_num > 1 else f"{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}"
    next_url = f"{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={bab_num + 1}) }}}}" if bab_num < total else f"{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}"
    
    prev_label = f"← Bab {bab_num - 1}: {titles[bab_num - 2].split(':')[0]}" if bab_num > 1 else f"← Silabus {short}"
    next_label = f"Lanjut ke Bab {bab_num + 1}: {titles[bab_num].split(':')[0]} →" if bab_num < total else f"Selesai Modul {short} ✓"

    # Sidebar links
    sidebar_items = []
    for i, t in enumerate(titles):
        n = i + 1
        active_cls = " active" if n == bab_num else ""
        sidebar_items.append(f"""
        <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={n}) }}}}" 
           class="dic-chapter-link{active_cls} {{{{ 'done' if all_bab_status[{i}]['is_completed'] else '' }}}}">
          <span class="dic-num-badge">{{{{ '✓' if all_bab_status[{i}]['is_completed'] else '{n}' }}}}</span>
          <span>{t}</span>
        </a>""")
    sidebar_html = "\n".join(sidebar_items)

    # Quiz options HTML
    opt_buttons = []
    for i, opt in enumerate(opts):
        is_correct = "true" if i == correct_idx else "false"
        escaped_exp = explain.replace("'", "\\'")
        opt_buttons.append(f"""
        <button class="dic-opt-btn" onclick="checkAnswer(this, {is_correct}, '{escaped_exp}')">
          <span>{opt}</span>
          <i class="bi bi-circle"></i>
        </button>""")
    opts_html = "\n".join(opt_buttons)

    return f"""{build_head(f"{title} - Bab {bab_num}: {bab_title}", color, is_reader=True)}
<body>
  <!-- Dicoding Topbar -->
  <header class="dic-topbar">
    <div class="dic-topbar-left">
      <a href="{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}" class="dic-back-btn">
        <i class="bi bi-arrow-left"></i> <span>{short}</span>
      </a>
      <span class="dic-badge"><i class="bi {icon}" style="color:{color};"></i> {title}</span>
    </div>
    <div class="d-flex align-items-center gap-2">
      <span class="dic-badge"><i class="bi bi-book"></i> Bab {bab_num}/{total}</span>
      <span class="dic-badge dic-timer"><i class="bi bi-stopwatch text-info"></i> <span id="studyTimer">00:00</span></span>
    </div>
  </header>

  <div class="dic-layout">
    <!-- Dicoding Sidebar -->
    <aside class="dic-sidebar">
      <div class="dic-sb-header">
        <div class="dic-sb-icon"><i class="bi {icon}"></i></div>
        <div>
          <div style="font-size:0.75rem; color:{color}; font-weight:700; text-transform:uppercase;">Modul MathThon</div>
          <div style="font-weight:700; font-size:0.95rem; color:#f8fafc;">{short}</div>
        </div>
      </div>

      <div class="dic-sb-nav-title">Daftar Bab & Silabus</div>
      {sidebar_html}

      <!-- In-Page Anchor Links -->
      <div class="dic-sb-nav-title">Daftar Isi Halaman (TOC)</div>
      <div class="dic-anchor-box">
        <a href="#peruntukan" class="dic-anchor-link"><i class="bi bi-compass me-1"></i> Peruntukan & Sasaran</a>
        <a href="#konsep" class="dic-anchor-link"><i class="bi bi-bookmark-fill me-1"></i> Pembahasan Konsep</a>
        <a href="#formula" class="dic-anchor-link"><i class="bi bi-calculator me-1"></i> Formulasi & Bedah Rumus</a>
        <a href="#contoh" class="dic-anchor-link"><i class="bi bi-journal-check me-1"></i> Contoh Soal Terpandu</a>
        <a href="#simulator" class="dic-anchor-link"><i class="bi bi-sliders me-1"></i> Simulator Interaktif</a>
        <a href="#latihan" class="dic-anchor-link"><i class="bi bi-pencil-square me-1"></i> Active Recall Quiz</a>
      </div>
    </aside>

    <!-- Main Content Reader -->
    <main class="dic-main">
      <div class="dic-crumb">
        <a href="{{{{ url_for('materi.materi_user') }}}}">Katalog Materi</a>
        <i class="bi bi-chevron-right small"></i>
        <a href="{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}">{short}</a>
        <i class="bi bi-chevron-right small"></i>
        <span>Bab {bab_num}</span>
      </div>

      <!-- Explicit Stage Banner -->
      <div class="dic-role-banner" id="peruntukan">
        <div class="dic-role-icon"><i class="bi {stage['icon']}"></i></div>
        <div>
          <div class="dic-role-title">{stage['badge']}</div>
          <p class="dic-role-text">{stage['role_desc']}</p>
        </div>
      </div>

      <h1 class="dic-h1">{bab_title}</h1>

      <!-- Learning Objectives -->
      <div class="dic-target-box">
        <div class="dic-target-title"><i class="bi bi-bullseye" style="color:{color};"></i> Sasaran Pembelajaran Bab {bab_num}:</div>
        <ul class="dic-target-list">
          <li>Memahami landasan konseptual dari {bab_title} secara sistematis.</li>
          <li>Menguasai makna variabel dan cara kerja formulasi matematis terkait.</li>
          <li>Mampu mengeksplorasi parameter matematika secara langsung melalui Simulator Interaktif.</li>
        </ul>
      </div>

      <!-- Core Concept -->
      <h2 class="dic-section-title" id="konsep">
        <i class="bi bi-book-half" style="color:{color};"></i> Pembahasan Konsep & Teori
      </h2>
      <p class="dic-lead">
        {theory}
      </p>

      <!-- Formula Section -->
      <h2 class="dic-section-title" id="formula">
        <i class="bi bi-calculator" style="color:{color};"></i> Formulasi Matematis & Bedah Rumus
      </h2>
      <div class="dic-formula-card">
        \\[ {formula} \\]
      </div>
      <div class="dic-formula-explain">
        <strong>💡 Makna Formulasi:</strong> {formula_meaning}
      </div>

      <!-- Worked Example -->
      <h2 class="dic-section-title" id="contoh">
        <i class="bi bi-journal-text text-success"></i> Contoh Soal & Pembahasan Terpandu
      </h2>
      <div class="dic-example-box">
        <div class="dic-example-title"><i class="bi bi-check2-circle"></i> Studi Kasus Pembahasan:</div>
        <p style="margin:0; font-size:0.92rem; color:#cbd5e1; line-height:1.7;">
          {example}
        </p>
      </div>

      <!-- Interactive Math Simulator Widget (No Coding Required) -->
      <h2 class="dic-section-title" id="simulator">
        <i class="bi bi-sliders text-warning"></i> Laboratorium Eksplorasi Interaktif
      </h2>
      <div class="dic-sim-box">
        <div class="dic-sim-topbar">
          <div class="dic-sim-title">
            <i class="bi bi-cpu-fill" style="color:{color};"></i> {widget['title']}
          </div>
          <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1 small">
            <i class="bi bi-broadcast me-1"></i> Live Simulator
          </span>
        </div>
        <div class="dic-sim-body">
          <p class="small text-muted mb-3">{widget['desc']}</p>
          {widget['html']}
        </div>
      </div>

      <!-- Active Recall / Capstone Challenge Exercise -->
      <div class="dic-quiz-card {'border border-warning border-opacity-50 shadow-lg' if bab_num == 5 else ''}" id="latihan" style="{'background: linear-gradient(145deg, #131b2e, #111622);' if bab_num == 5 else ''}">
        <div class="dic-quiz-tag" style="{'color:#eab308; font-size:0.82rem;' if bab_num == 5 else ''}">
          <i class="bi {'bi-trophy-fill' if bab_num == 5 else 'bi-patch-question-fill'}"></i> 
          {'🏆 CAPSTONE CHALLENGE - UJI SINTESIS AKHIR MODUL' if bab_num == 5 else f'Active Recall Quiz - Bab {bab_num}'}
        </div>
        <div class="dic-quiz-q" style="{'font-size:1.1rem; color:#fef08a;' if bab_num == 5 else ''}">{q_text}</div>
        {opts_html}
        <div class="dic-feedback" id="quizFeedback"></div>
      </div>

      <!-- Bottom Navigation -->
      <nav class="dic-bottom-nav">
        <a href="{prev_url}" class="dic-nav-btn">
          <i class="bi bi-arrow-left"></i> {prev_label}
        </a>
        <button class="dic-nav-btn" id="markDoneBtn" onclick="markBabCompleted()">
          <i class="bi bi-check-circle"></i> Tandai Bab Selesai
        </button>
        <a href="{next_url}" class="dic-nav-btn primary">
          {next_label} <i class="bi bi-arrow-right"></i>
        </a>
      </nav>
    </main>
  </div>

  <script>
    // Inisialisasi KaTeX Auto Render
    document.addEventListener("DOMContentLoaded", () => {{
      if (typeof renderMathInElement === 'function') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '\\\\(', right: '\\\\)', display: false}},
            {{left: '\\\\[', right: '\\\\]', display: true}}
          ],
          throwOnError: false
        }});
      }}
    }});

    // Stopwatch Belajar Aktif
    let studySeconds = 0;
    let quizAnswered = false;
    const timerDisplay = document.getElementById('studyTimer');
    setInterval(() => {{
      studySeconds++;
      const mins = String(Math.floor(studySeconds / 60)).padStart(2, '0');
      const secs = String(studySeconds % 60).padStart(2, '0');
      if (timerDisplay) timerDisplay.textContent = `${{mins}}:${{secs}}`;
    }}, 1000);

    // Kuis Active Recall Check
    function checkAnswer(btn, isCorrect, explanation) {{
      if (quizAnswered) return;
      quizAnswered = true;
      document.querySelectorAll('.dic-opt-btn').forEach(b => b.style.pointerEvents = 'none');
      
      const fb = document.getElementById('quizFeedback');
      if (isCorrect) {{
        btn.classList.add('ok');
        btn.querySelector('i').className = 'bi bi-check-circle-fill text-success';
        fb.innerHTML = `<strong>✅ Luar Biasa Benar!</strong> ${{explanation}}`;
        fb.className = 'dic-feedback show ok';
      }} else {{
        btn.classList.add('bad');
        btn.querySelector('i').className = 'bi bi-x-circle-fill text-danger';
        fb.innerHTML = `<strong>❌ Perlu Ditinjau:</strong> ${{explanation}}`;
        fb.className = 'dic-feedback show bad';
      }}
    }}

    // Widget Simulator Logic
    {widget['js']}

    // Simpan Progres Bab ke API Backend
    function markBabCompleted() {{
      const markBtn = document.getElementById('markDoneBtn');
      const csrfMeta = document.querySelector('meta[name="csrf-token"]');
      const headers = {{ 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }};
      if (csrfMeta) headers['X-CSRFToken'] = csrfMeta.getAttribute('content');

      fetch('/user/materi/api/bab-progress', {{
        method: 'POST',
        headers: headers,
        body: JSON.stringify({{
          subject: '{subj_key}',
          bab_num: {bab_num},
          is_completed: true,
          time_spent: studySeconds,
          exercise_score: {bab_num}
        }})
      }})
      .then(res => res.json())
      .then(data => {{
        if (data.status === 'success') {{
          markBtn.innerHTML = '<i class="bi bi-check-circle-fill"></i> Bab Selesai!';
          markBtn.style.background = 'rgba(16, 185, 129, 0.2)';
          markBtn.style.borderColor = '#10b981';
          markBtn.style.color = '#34d399';
          markBtn.disabled = true;
        }}
      }})
      .catch(console.error);
    }}

    // Auto-save beacon sebelum halaman ditutup
    window.addEventListener('beforeunload', () => {{
      try {{
        const payload = JSON.stringify({{
          subject: '{subj_key}',
          bab_num: {bab_num},
          is_completed: false,
          time_spent: studySeconds,
          exercise_score: 0
        }});
        const blob = new Blob([payload], {{ type: 'application/json' }});
        navigator.sendBeacon('/user/materi/api/bab-progress', blob);
      }} catch (e) {{
        console.warn('Beacon save failed', e);
      }}
    }});
  </script>
</body>
</html>"""


def build_index_html(subj_key, data):
    color = data["color"]
    icon = data["icon"]
    short = data["short"]
    title = data["title"]
    desc = data["desc"]
    titles = data["bab_titles"]
    total = len(titles)

    # 5-Stage Framework Visual Cards
    stages_html_list = []
    for i, stg in enumerate(STAGE_DEFINITIONS):
        num = i + 1
        b_title = titles[i]
        stages_html_list.append(f"""
        <div class="dic-stage-card">
          <div class="dic-stage-num" style="background:{color}20; color:{color};">{num}</div>
          <div class="flex-grow-1">
            <div class="dic-stage-badge" style="color:{color};">{stg['badge']}</div>
            <div class="dic-stage-title">{b_title}</div>
            <div class="dic-stage-desc">{stg['role_desc']}</div>
          </div>
        </div>""")
    stages_framework_html = "\n".join(stages_html_list)

    cards = []
    for i, t in enumerate(titles):
        n = i + 1
        stg = STAGE_DEFINITIONS[i]
        card = f"""
      <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={n}) }}}}" 
         class="dic-card-item {{{{ 'completed' if bab_progress[{i}]['is_completed'] else '' }}}}">
        <div class="dic-card-num" style="background:{color}20; color:{color};">{n}</div>
        <div class="flex-grow-1">
          <div style="font-size:0.75rem; color:{color}; font-weight:700; text-transform:uppercase;">{stg['badge']}</div>
          <div class="dic-card-title">{t}</div>
          <div class="dic-card-meta"><i class="bi bi-clock"></i> ~10 Menit &bull; Simulator Interaktif</div>
        </div>
        <i class="bi {{{{ 'bi-check-circle-fill text-success' if bab_progress[{i}]['is_completed'] else 'bi-chevron-right text-muted' }}}} fs-5"></i>
      </a>"""
        cards.append(card)
    cards_html = "\n".join(cards)

    return f"""{build_head(f"{title} - Silabus & Peta Kurikulum Modul", color, is_reader=False)}
<style>
  .dic-overview-wrap {{ max-width: 980px; margin: 0 auto; padding: 2.5rem 1.5rem; }}
  .dic-hero-card {{
    background: linear-gradient(135deg, {color}25, {color}08);
    border: 1px solid {color}40;
    border-radius: 20px;
    padding: 2.5rem;
    margin-bottom: 2.5rem;
    box-shadow: 0 12px 36px rgba(0,0,0,0.3);
  }}
  .dic-hero-icon {{
    width: 64px;
    height: 64px;
    border-radius: 16px;
    background: {color};
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    box-shadow: 0 8px 20px {color}55;
  }}
  
  /* 5-Stage Framework Section */
  .dic-framework-box {{
    background: #111622;
    border: 1px solid var(--border-color);
    border-radius: 18px;
    padding: 1.75rem;
    margin-bottom: 2.5rem;
  }}
  .dic-stage-card {{
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border-color);
  }}
  .dic-stage-card:last-child {{ border-bottom: none; }}
  .dic-stage-num {{
    width: 36px;
    height: 36px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1rem;
    flex-shrink: 0;
  }}
  .dic-stage-badge {{
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.2rem;
  }}
  .dic-stage-title {{
    font-size: 0.95rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.25rem;
  }}
  .dic-stage-desc {{
    font-size: 0.85rem;
    color: #94a3b8;
    line-height: 1.5;
  }}
  
  .dic-card-item {{
    display: flex;
    align-items: center;
    gap: 1.25rem;
    background: #111622;
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 1.1rem 1.5rem;
    text-decoration: none;
    color: var(--text-main);
    margin-bottom: 0.75rem;
    transition: all 0.2s;
  }}
  .dic-card-item:hover {{
    background: #161d2e;
    border-color: {color};
    transform: translateX(4px);
    color: #fff;
  }}
  .dic-card-item.completed {{ border-color: rgba(16, 185, 129, 0.4); }}
  .dic-card-num {{
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1.1rem;
    flex-shrink: 0;
  }}
  .dic-card-title {{ font-weight: 700; font-size: 1rem; margin-bottom: 0.2rem; }}
  .dic-card-meta {{ font-size: 0.8rem; color: #64748b; }}
  .dic-start-btn {{
    background: {color};
    color: #fff;
    font-weight: 700;
    padding: 0.85rem 2.2rem;
    border-radius: 12px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 1rem;
    box-shadow: 0 8px 20px {color}44;
    transition: all 0.2s;
  }}
  .dic-start-btn:hover {{ opacity: 0.95; transform: translateY(-2px); color:#fff; }}
</style>
<body>
  <!-- Dicoding Header -->
  <header class="dic-topbar">
    <a href="{{{{ url_for('materi.materi_user') }}}}" class="dic-back-btn">
      <i class="bi bi-arrow-left"></i> <span>Katalog Materi</span>
    </a>
    <span class="dic-badge"><i class="bi {icon}" style="color:{color};"></i> {title}</span>
  </header>

  <div class="dic-overview-wrap">
    <!-- Hero Box -->
    <div class="dic-hero-card">
      <div class="d-flex align-items-center gap-3 mb-3">
        <div class="dic-hero-icon"><i class="bi {icon}"></i></div>
        <div>
          <div style="font-size:0.8rem; color:{color}; font-weight:700; text-transform:uppercase; letter-spacing:0.06em;">Modul Pembelajaran MathThon</div>
          <h1 style="font-size:1.85rem; font-weight:800; margin:0; color:#f8fafc;">{title}</h1>
        </div>
      </div>
      <p style="color:#cbd5e1; font-size:1rem; margin-bottom:1.5rem; line-height:1.7;">
        {desc}
      </p>
      <div class="d-flex gap-4 flex-wrap" style="font-size:0.88rem; color:#94a3b8;">
        <span><i class="bi bi-collection text-info me-1"></i> {total} Bab Terstruktur</span>
        <span><i class="bi bi-check2-all text-success me-1"></i> {{{{ bab_progress|selectattr('is_completed')|list|length }}}}/{total} Bab Selesai</span>
        <span><i class="bi bi-sliders text-warning me-1"></i> Simulator Visual Interaktif</span>
      </div>

      <!-- Progress Bar -->
      <div style="margin-top:1.25rem; background:rgba(255,255,255,0.08); border-radius:6px; height:7px; overflow:hidden;">
        <div style="height:100%; background:{color}; transition:width 0.4s; width: {{{{ (bab_progress|selectattr('is_completed')|list|length / {total} * 100)|int }}}}%;"></div>
      </div>
    </div>

    <!-- 5-Stage Framework Card -->
    <div class="dic-framework-box">
      <h2 style="font-size:1.05rem; font-weight:800; color:#f8fafc; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;">
        <i class="bi bi-diagram-3-fill" style="color:{color};"></i> Peta Peruntukan Kurikulum 5 Bab (Learning Pathway)
      </h2>
      <p style="font-size:0.85rem; color:#94a3b8; margin-bottom:1.25rem;">
        Setiap bab dirancang secara pedagogis dengan peruntukan berjenjang dari intuisi hingga proyek sintesis:
      </p>
      {stages_framework_html}
    </div>

    <!-- Chapter List -->
    <h2 style="font-size:1.1rem; font-weight:700; color:#cbd5e1; margin-bottom:1.25rem; display:flex; align-items:center; gap:0.5rem;">
      <i class="bi bi-list-ol" style="color:{color};"></i> Daftar Bab Pembelajaran
    </h2>
    {cards_html}

    <!-- CTA Button -->
    <div class="text-center mt-5">
      <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num=1) }}}}" class="dic-start-btn">
        <i class="bi bi-play-circle-fill fs-5"></i> Mulai Pembelajaran Bab 1
      </a>
    </div>
  </div>
</body>
</html>"""


def main():
    print("=" * 65)
    print("  MathThon: Interactive Math Simulator Generator (No Coding for Learner)")
    print("=" * 65)
    created_count = 0

    for subj_key, data in SUBJECTS.items():
        subject_dir = os.path.join(TEMPLATES_DIR, subj_key)
        os.makedirs(subject_dir, exist_ok=True)

        # 1. Generate index.html
        index_file = os.path.join(subject_dir, "index.html")
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(build_index_html(subj_key, data))
        created_count += 1
        print(f"  [OK] Index  -> {subj_key}/index.html")

        # 2. Generate bab_1.html ... bab_5.html
        for bab_num in range(1, len(data["bab_titles"]) + 1):
            bab_file = os.path.join(subject_dir, f"bab_{bab_num}.html")
            with open(bab_file, "w", encoding="utf-8") as f:
                f.write(build_bab_html(subj_key, data, bab_num))
            created_count += 1
            print(f"  [OK] Bab {bab_num}  -> {subj_key}/bab_{bab_num}.html")

    print("=" * 65)
    print(f"  [SUKSES] Sebanyak {created_count} file materi simulator interaktif telah dibangun.")
    print("  Siswa belajar melalui slider, simulator visual & kuis interaktif.")
    print("=" * 65)


if __name__ == "__main__":
    main()
