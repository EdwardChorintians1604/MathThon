#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MathThon - Interactive Math Simulator & Chapter Generator (Dicoding Standard)
=============================================================================
Pembelajaran Matematika Interaktif Tanpa Coding untuk Siswa:
- Mengadopsi standar pedagogis Dicoding Academy:
  * Reading time & difficulty metadata
  * 5-Stage pedagogical progression (Fondasi -> Anatomi -> Mekanika -> Pemodelan -> Capstone)
  * Learning objectives checklist
  * Real-world hook / engineered motivation
  * Multi-section deep concept breakdowns
  * Dicoding callout boxes (💡 Pro-Tip, ⚠️ Common Pitfall, 🧠 Wawasan & Komputasi)
  * KaTeX mathematical formula with annotated parameter tables & mathematical intuition
  * Step-by-step guided examples (Diketahui, Ditanya, Langkah Terperinci, Kesimpulan Fisis)
  * Interactive Live Simulator Lab with dynamic sliders & reactive JS calculations
  * Active Recall Quiz with educational feedback explanation
  * Key takeaways summary checklist
- Dilengkapi integrasi sistem progres backend MathThon (/user/materi/api/bab-progress)
"""

import os
import json
from materi_data import (
    aljabar, bangun_datar_dan_bangun_ruang, desimal, eksponensial,
    fungsi_turunan, integral, limit, logaritma,
    matematika_diskrit, matriks, operasi_kabataku, persamaan_linear,
    probabilitas, sistem_bilangan, statistika, vektor
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "Front_End", "templates", "user", "materi")

# Map of all 16 math subjects
SUBJECT_MODULES = {
    "aljabar": aljabar.DATA,
    "bangun_datar_dan_bangun_ruang": bangun_datar_dan_bangun_ruang.DATA,
    "desimal": desimal.DATA,
    "eksponensial": eksponensial.DATA,
    "fungsi_turunan": fungsi_turunan.DATA,
    "integral": integral.DATA,
    "limit": limit.DATA,
    "logaritma": logaritma.DATA,
    "matematika_diskrit": matematika_diskrit.DATA,
    "matriks": matriks.DATA,
    "operasi_kabataku": operasi_kabataku.DATA,
    "persamaan_linear": persamaan_linear.DATA,
    "probabilitas": probabilitas.DATA,
    "sistem_bilangan": sistem_bilangan.DATA,
    "statistika": statistika.DATA,
    "vektor": vektor.DATA,
}

# Definisi Standar 5 Tahap Pedagogis Dicoding
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
        "role_desc": "Peruntukan Bab 4: Menerjemahkan masalah dunia nyata (fisika, sains komputer, ekonomi, rekayasa data) ke dalam pemodelan matematis formal.",
        "icon": "bi-lightbulb-fill"
    },
    {
        "badge": "TAHAP 5: CAPSTONE PROJECT & EVALUASI SINTESIS",
        "role_desc": "Peruntukan Bab 5: Mengintegrasikan seluruh materi Bab 1 s/d Bab 4 dalam satu proyek tantangan komprehensif sebagai standar penguasaan modul.",
        "icon": "bi-trophy-fill"
    }
]

# Modul Laboratorium Interaktif per Subjek (Lengkap 16 Subjek)
WIDGET_DATA = {
    "aljabar": {
        "title": "Laboratorium Penalaran: Neraca Keseimbangan Aljabar & Prinsip Kesetaraan",
        "desc": "🎯 Misi Berpikir: Bagaimana cara menjaga kesetaraan persamaan ax + b = c saat kedua ruas dimanipulasi secara logis?",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-lightbulb"></i> Tantangan Penalaran:</div>
          <p class="small text-light mb-0">Aljabar adalah ilmu menjaga kesetaraan neraca timbangan. Geser nilai <strong>Koefisien a</strong>, <strong>Konstanta b</strong>, dan <strong>Target c</strong>, lalu amati rantai deduksi isolasi variabel x!</p>
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
            <label class="form-label small text-muted">Jumlah Partisi Persegi Panjang (n): <span id="val_n_part" class="fw-bold text-info">10</span></label>
            <input type="range" class="form-range" id="slider_n_part" min="2" max="200" value="10" oninput="updateIntegralSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Batas Atas Integrasi b: <span id="val_b_bound" class="fw-bold text-warning">4</span></label>
            <input type="range" class="form-range" id="slider_b_bound" min="1" max="10" value="4" oninput="updateIntegralSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Luas Eksak Analitik:</div>
              <div class="fs-5 fw-bold text-success" id="int_exact">21.33</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Aproksimasi Riemann:</div>
              <div class="fs-5 fw-bold text-info" id="int_riemann">18.24</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Galat / Error:</div>
              <div class="fs-5 fw-bold text-danger" id="int_error">3.09</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #10b981;">
            <div class="small text-success fw-bold mb-1"><i class="bi bi-graph-up-arrow"></i> Intuisi Konvergensi Fundamental:</div>
            <div class="small text-light" id="int_converg">Dengan 10 partisi, lebar tiap strip Δx = 0.40. Semakin banyak partisi, tangga balok melebur menjadi kurva mulus.</div>
          </div>
        </div>
        """,
        "js": """
        function updateIntegralSim() {
          const n = parseInt(document.getElementById('slider_n_part').value);
          const b = parseFloat(document.getElementById('slider_b_bound').value);
          document.getElementById('val_n_part').textContent = n;
          document.getElementById('val_b_bound').textContent = b;
          const exact = (b * b * b) / 3;
          const dx = b / n;
          let sum = 0;
          for (let i = 0; i < n; i++) {
            const x_i = i * dx;
            sum += (x_i * x_i) * dx;
          }
          const err = Math.abs(exact - sum);
          document.getElementById('int_exact').textContent = exact.toFixed(2);
          document.getElementById('int_riemann').textContent = sum.toFixed(2);
          document.getElementById('int_error').textContent = err.toFixed(3);
          document.getElementById('int_converg').innerHTML = `Dengan <strong>${n}</strong> partisi (lebar Δx = ${dx.toFixed(3)}), galat tersisa hanya <strong>${err.toFixed(3)}</strong> (${((err/exact)*100).toFixed(2)}%). Inilah bukti bahwa limit partisi riemann n→∞ menghasilkan nilai integral eksak!`;
        }
        """
    },
    "limit": {
        "title": "Laboratorium Limit: Eksplorasi Lubang Tak Terdefinisi (0/0) & Pendekatan Asimtotik",
        "desc": "🎯 Misi Berpikir: Geser nilai x sedekat mungkin ke titik lubang x = 2 untuk melihat nilai fungsi mendekati 4 tanpa pernah menyentuh 0/0!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(6,182,212,0.08); border:1px solid rgba(6,182,212,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-binoculars"></i> Mengapa Limit BUKAN Substitusi Buta?</div>
          <p class="small text-light mb-0">Pada fungsi f(x) = (x² - 4)/(x - 2), saat x = 2 tepat, fungsi hancur menjadi pembagian tak tentu 0/0. Namun dengan limit, kita mengamati perilaku saat x <strong>mendekati</strong> 2 dari kiri dan kanan!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Jarak Epsilon (ε) dari Titik x = 2: <span id="lim_eps_val" class="fw-bold text-info">0.1000</span></label>
            <input type="range" class="form-range" id="lim_slider" min="1" max="1000" value="100" oninput="updateLimitSim()">
          </div>
          <div class="col-md-6 text-end">
            <span class="badge bg-info-subtle text-info border border-info-subtle px-2 py-1">Titik Singularity: x = 2</span>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Pendekatan Kiri (x → 2⁻):</div>
              <div class="fs-6 fw-bold text-light" id="lim_left_x">x = 1.9000</div>
              <div class="fs-5 fw-bold text-warning" id="lim_left_y">f(x) = 3.9000</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Titik Tepat (x = 2):</div>
              <div class="fs-6 fw-bold text-danger">x = 2.0000</div>
              <div class="fs-5 fw-bold text-danger">0 / 0 (Tak Tentu)</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Pendekatan Kanan (x → 2⁺):</div>
              <div class="fs-6 fw-bold text-light" id="lim_right_x">x = 2.1000</div>
              <div class="fs-5 fw-bold text-success" id="lim_right_y">f(x) = 4.1000</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #06b6d4;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-bullseye"></i> Kesimpulan Nilai Limit:</div>
            <div class="small text-light" id="lim_conclusion">Limit kiri (3.9000) dan limit kanan (4.1000) menyatu menuju L = 4.0000.</div>
          </div>
        </div>
        """,
        "js": """
        function updateLimitSim() {
          const raw = parseInt(document.getElementById('lim_slider').value);
          const eps = raw / 1000;
          document.getElementById('lim_eps_val').textContent = eps.toFixed(4);
          const x_left = 2 - eps;
          const x_right = 2 + eps;
          const y_left = (x_left * x_left - 4) / (x_left - 2);
          const y_right = (x_right * x_right - 4) / (x_right - 2);
          document.getElementById('lim_left_x').textContent = `x = ${x_left.toFixed(4)}`;
          document.getElementById('lim_left_y').textContent = `f(x) = ${y_left.toFixed(4)}`;
          document.getElementById('lim_right_x').textContent = `x = ${x_right.toFixed(4)}`;
          document.getElementById('lim_right_y').textContent = `f(x) = ${y_right.toFixed(4)}`;
          document.getElementById('lim_conclusion').innerHTML = `Dengan toleransi ε = ${eps.toFixed(4)}, f(x) mendekati rentang [${y_left.toFixed(4)}, ${y_right.toFixed(4)}]. Kedua arah sepakat bahwa <strong>lim (x→2) f(x) = 4</strong>.`;
        }
        """
    },
    "fungsi_turunan": {
        "title": "Laboratorium Garis Singgung: Tali Busur (Secant) Menuju Garis Singgung (Tangent)",
        "desc": "🎯 Misi Berpikir: Geser nilai Δx menuju nol untuk melihat kemiringan rata-rata bertransformasi menjadi turunan sesaat f'(x)!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.25);">
          <div class="small fw-bold text-danger mb-1"><i class="bi bi-speedometer2"></i> Kecepatan Rata-Rata vs Kecepatan Sesaat:</div>
          <p class="small text-light mb-0">Jika speedometer mobil Anda membaca 80 km/jam saat ini, itu bukan rata-rata perjalanan 2 jam, melainkan laju perubahan jarak dalam selang waktu Δt yang sangat mendekati nol!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Titik Evaluasi x₀: <span id="tur_val_x" class="fw-bold text-info">2.0</span></label>
            <input type="range" class="form-range" id="tur_slider_x" min="1" max="5" value="2" step="0.5" oninput="updateTurunanSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Lebar Selang Δx: <span id="tur_val_dx" class="fw-bold text-warning">1.00</span></label>
            <input type="range" class="form-range" id="tur_slider_dx" min="1" max="100" value="100" oninput="updateTurunanSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Gradien Tali Busur (Secant):</div>
              <div class="fs-5 fw-bold text-warning" id="tur_secant">5.00</div>
              <div class="small text-muted">Δy / Δx rata-rata</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Turunan Eksak f'(x₀) = 2x₀:</div>
              <div class="fs-5 fw-bold text-success" id="tur_exact">4.00</div>
              <div class="small text-muted">Laju sesaat presisi</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Penyimpangan Gradien:</div>
              <div class="fs-5 fw-bold text-danger" id="tur_diff">1.00</div>
              <div class="small text-muted">Galat tali busur</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #ef4444;">
            <div class="small text-danger fw-bold mb-1"><i class="bi bi-activity"></i> Makna Matematis Turunan:</div>
            <div class="small text-light" id="tur_summary">Saat Δx mengecil dari 1.00 menuju 0.01, tali busur berputar presisi menjadi garis singgung kurva di x = 2.0.</div>
          </div>
        </div>
        """,
        "js": """
        function updateTurunanSim() {
          const x0 = parseFloat(document.getElementById('tur_slider_x').value);
          const rawDx = parseInt(document.getElementById('tur_slider_dx').value);
          const dx = rawDx / 100;
          document.getElementById('tur_val_x').textContent = x0.toFixed(1);
          document.getElementById('tur_val_dx').textContent = dx.toFixed(2);
          const y0 = x0 * x0;
          const y1 = (x0 + dx) * (x0 + dx);
          const secant = (y1 - y0) / dx;
          const exact = 2 * x0;
          const diff = Math.abs(secant - exact);
          document.getElementById('tur_secant').textContent = secant.toFixed(2);
          document.getElementById('tur_exact').textContent = exact.toFixed(2);
          document.getElementById('tur_diff').textContent = diff.toFixed(3);
          document.getElementById('tur_summary').innerHTML = `Pada f(x) = x², f'(${x0}) = 2(${x0}) = <strong>${exact.toFixed(2)}</strong>. Nilai tali busur secant = <strong>${secant.toFixed(2)}</strong> (galat = ${diff.toFixed(3)}).`;
        }
        """
    },
    "matriks": {
        "title": "Laboratorium Geometri Matriks: Distorsi Ruang 2D & Determinan Skala Luas",
        "desc": "🎯 Misi Berpikir: Geser entri matriks 2x2 dan amati bagaimana determinan mengukur perbesaran luas bidang dan orientasi arah!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-grid-3x3"></i> Determinan Bukan Sekadar Angka Rumus:</div>
          <p class="small text-light mb-0">Secara geometris, determinan matriks 2x2 merepresentasikan <strong>faktor pengali luas</strong> bujur sangkar satuan yang ditransformasikan. Jika det(M) = 0, ruang 2D runtuh menjadi garis atau titik 1D (ruang kehilangan dimensi)!</p>
        </div>
        <div class="row g-2 align-items-center">
          <div class="col-3">
            <label class="form-label small text-muted">a (x-scale): <span id="m_val_a" class="fw-bold text-info">2</span></label>
            <input type="range" class="form-range" id="m_a" min="-4" max="4" value="2" oninput="updateMatriksSim()">
          </div>
          <div class="col-3">
            <label class="form-label small text-muted">b (y-shear): <span id="m_val_b" class="fw-bold text-info">1</span></label>
            <input type="range" class="form-range" id="m_b" min="-4" max="4" value="1" oninput="updateMatriksSim()">
          </div>
          <div class="col-3">
            <label class="form-label small text-muted">c (x-shear): <span id="m_val_c" class="fw-bold text-warning">0</span></label>
            <input type="range" class="form-range" id="m_c" min="-4" max="4" value="0" oninput="updateMatriksSim()">
          </div>
          <div class="col-3">
            <label class="form-label small text-muted">d (y-scale): <span id="m_val_d" class="fw-bold text-warning">3</span></label>
            <input type="range" class="form-range" id="m_d" min="-4" max="4" value="3" oninput="updateMatriksSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Bentuk Matriks Transformasi:</div>
              <div class="fs-6 fw-bold text-light font-monospace" id="m_matrix">[ 2 , 1 ; 0 , 3 ]</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Determinan (ad - bc):</div>
              <div class="fs-5 fw-bold text-success" id="m_det">det = 6</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Invertibilitas:</div>
              <div class="fs-5 fw-bold text-info" id="m_invert">Memiliki Invers</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #3b82f6;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-aspect-ratio"></i> Efek Terhadap Bidang Ruang:</div>
            <div class="small text-light" id="m_desc">Luas bidang berukuran 1 satuan diperbesar 6x lipat menjadi 6 satuan persegi.</div>
          </div>
        </div>
        """,
        "js": """
        function updateMatriksSim() {
          const a = parseInt(document.getElementById('m_a').value);
          const b = parseInt(document.getElementById('m_b').value);
          const c = parseInt(document.getElementById('m_c').value);
          const d = parseInt(document.getElementById('m_d').value);
          document.getElementById('m_val_a').textContent = a;
          document.getElementById('m_val_b').textContent = b;
          document.getElementById('m_val_c').textContent = c;
          document.getElementById('m_val_d').textContent = d;
          document.getElementById('m_matrix').textContent = `[ ${a} , ${b} ; ${c} , ${d} ]`;
          const det = (a * d) - (b * c);
          document.getElementById('m_det').textContent = `det = ${det}`;
          if (det === 0) {
            document.getElementById('m_invert').textContent = "Singular (Tak Berinvers)";
            document.getElementById('m_invert').className = "fs-5 fw-bold text-danger";
            document.getElementById('m_desc').innerHTML = "Determinan nol menyebabkan seluruh bidang datar 2D runtuh menjadi garis lurus atau satu titik. Informasi spasial hilang secara permanen.";
          } else {
            document.getElementById('m_invert').textContent = "Invertibel (Dapat Dibalik)";
            document.getElementById('m_invert').className = "fs-5 fw-bold text-success";
            const orient = det > 0 ? "mempertahankan orientasi searah jarum jam" : "membalik orientasi bidang (seperti cermin refleksi)";
            document.getElementById('m_desc').innerHTML = `Luas objek diperbesar <strong>${Math.abs(det)}x</strong> lipat dan transformasi ${orient}. Matriks ini memiliki balikan (invers).`;
          }
        }
        """
    },
    "statistika": {
        "title": "Laboratorium Ketahanan: Sensitivitas Mean (Rata-rata) vs Median terhadap Outlier",
        "desc": "🎯 Misi Berpikir: Geser nilai pencilan (outlier ekstrim) dan amati mengapa Mean bergeser drastis sementara Median tetap kokoh!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(20,184,166,0.08); border:1px solid rgba(20,184,166,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-shield-lock"></i> Mengapa Gaji Rata-Rata Sering Menipu?</div>
          <p class="small text-light mb-0">Jika 9 karyawan bergaji Rp 5 juta dan 1 direktur bergaji Rp 100 juta, rata-rata (mean) adalah Rp 14,5 juta (tidak mewakili siapa pun). Namun median tetap Rp 5 juta. Amati fenomena ini secara langsung!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-8">
            <label class="form-label small text-muted">Nilai Data Pencilan / Outlier: <span id="stat_out_val" class="fw-bold text-danger">100</span></label>
            <input type="range" class="form-range" id="stat_slider" min="10" max="300" value="100" step="5" oninput="updateStatSim()">
          </div>
          <div class="col-md-4 text-end">
            <span class="small text-muted">Data Dasar: [ 4, 6, 7, 8, Outlier ]</span>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Nilai Mean (Sensitif):</div>
              <div class="fs-5 fw-bold text-danger" id="stat_mean">25.00</div>
              <div class="small text-muted">Terdistorsi outlier</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Nilai Median (Robust):</div>
              <div class="fs-5 fw-bold text-success" id="stat_med">7.00</div>
              <div class="small text-muted">Kukuh & stabil</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Disparitas Deviasi:</div>
              <div class="fs-5 fw-bold text-warning" id="stat_disp">18.00</div>
              <div class="small text-muted">Selisih distorsi</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #14b8a6;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-lightbulb-fill"></i> Prinsip Pemilihan Ukuran Pemusatan:</div>
            <div class="small text-light" id="stat_concl">Saat outlier sebesar 100 masuk, Mean melonjak ke 25.00, padahal 80% sampel berada di bawah 8! Gunakan Median untuk distribusi data condong (skewed).</div>
          </div>
        </div>
        """,
        "js": """
        function updateStatSim() {
          const outlier = parseInt(document.getElementById('stat_slider').value);
          document.getElementById('stat_out_val').textContent = outlier;
          const data = [4, 6, 7, 8, outlier].sort((a,b)=>a-b);
          const mean = (4 + 6 + 7 + 8 + outlier) / 5;
          const median = data[2];
          const diff = Math.abs(mean - median);
          document.getElementById('stat_mean').textContent = mean.toFixed(2);
          document.getElementById('stat_med').textContent = median.toFixed(2);
          document.getElementById('stat_disp').textContent = diff.toFixed(2);
          document.getElementById('stat_concl').innerHTML = `Outlier <strong>${outlier}</strong> mendongkrak Mean menjadi <strong>${mean.toFixed(2)}</strong>, sedangkan Median tetap kokoh di angka <strong>${median}</strong>. Inilah alasan mengapa praktisi data sains wajib memeriksa outlier sebelum mengandalkan rata-rata.`;
        }
        """
    },
    "probabilitas": {
        "title": "Laboratorium Hukum Bilangan Besar (LLN): Dari Keacakan Menuju Kepastian Frekuensi",
        "desc": "🎯 Misi Berpikir: Tingkatkan jumlah lemparan koin dari 10 hingga 5.000 kali untuk membuktikan konvergensi peluang teoretis 50%!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(234,179,8,0.08); border:1px solid rgba(234,179,8,0.25);">
          <div class="small fw-bold text-warning mb-1"><i class="bi bi-dice-5"></i> Mengapa Kasino Selalu Menang dalam Jangka Panjang?</div>
          <p class="small text-light mb-0">Hukum Bilangan Besar (Law of Large Numbers) menyatakan bahwa dalam jumlah percobaan kecil, fluktuasi acak mendominasi. Namun saat N bertumbuh masif, frekuensi empiris pasti mengunci nilai peluang teoretis!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-8">
            <label class="form-label small text-muted">Jumlah Lemparan Koin Simulative (N): <span id="prob_n_val" class="fw-bold text-info">50</span></label>
            <input type="range" class="form-range" id="prob_slider" min="10" max="5000" value="50" step="10" oninput="updateProbSim()">
          </div>
          <div class="col-md-4 text-end">
            <button class="btn btn-sm btn-outline-warning" onclick="updateProbSim()"><i class="bi bi-shuffle"></i> Acak Ulang Sampel</button>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Peluang Teoretis:</div>
              <div class="fs-5 fw-bold text-light">50.00%</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Frekuensi Gambar (Empiris):</div>
              <div class="fs-5 fw-bold text-success" id="prob_emp">52.00%</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Galat Deviasi dari Teori:</div>
              <div class="fs-5 fw-bold text-warning" id="prob_err">2.00%</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #eab308;">
            <div class="small text-warning fw-bold mb-1"><i class="bi bi-graph-up"></i> Evaluasi Konvergensi LLN:</div>
            <div class="small text-light" id="prob_text">Pada N=50 percobaan, galat acak masih terasa. Tingkatkan N hingga 5000 untuk melihat deviasi menyusut mendekati 0%.</div>
          </div>
        </div>
        """,
        "js": """
        function updateProbSim() {
          const N = parseInt(document.getElementById('prob_slider').value);
          document.getElementById('prob_n_val').textContent = N.toLocaleString('id-ID');
          let heads = 0;
          for (let i = 0; i < N; i++) {
            if (Math.random() < 0.5) heads++;
          }
          const pEmp = (heads / N) * 100;
          const err = Math.abs(50 - pEmp);
          document.getElementById('prob_emp').textContent = `${pEmp.toFixed(2)}%`;
          document.getElementById('prob_err').textContent = `${err.toFixed(2)}%`;
          document.getElementById('prob_text').innerHTML = `Dari <strong>${N.toLocaleString('id-ID')}</strong> lemparan, muncul gambar sebanyak <strong>${heads}</strong> kali (${pEmp.toFixed(2)}%). Deviasi dari probabilitas teoretis 50% tersisa <strong>${err.toFixed(2)}%</strong>. Semakin besar N, fluktuasi acak semakin teredam.`;
        }
        """
    },
    "eksponensial": {
        "title": "Laboratorium Pertumbuhan Eksponensial: Bunga Majemuk & Ledakan Skala",
        "desc": "🎯 Misi Berpikir: Geser laju pertumbuhan r dan periode waktu t untuk menyaksikan percepatan kurva eksponensial melampaui pertumbuhan linier!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(244,63,94,0.08); border:1px solid rgba(244,63,94,0.25);">
          <div class="small fw-bold text-danger mb-1"><i class="bi bi-graph-up-arrow"></i> Keajaiban Pertumbuhan Majemuk:</div>
          <p class="small text-light mb-0">Pertumbuhan linier bertambah dengan konstanta tetap (1, 2, 3, 4...), sedangkan eksponensial melipatgandakan dirinya sendiri (1, 2, 4, 8, 16...). Dalam jangka panjang, eksponensial selalu mengalahkan linier secara telak!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Laju Pertumbuhan (r): <span id="exp_r_val" class="fw-bold text-info">10% per periode</span></label>
            <input type="range" class="form-range" id="exp_slider_r" min="2" max="30" value="10" oninput="updateExpSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Periode Waktu (t): <span id="exp_t_val" class="fw-bold text-warning">12 Periode</span></label>
            <input type="range" class="form-range" id="exp_slider_t" min="1" max="30" value="12" oninput="updateExpSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Modal Awal P₀:</div>
              <div class="fs-6 fw-bold text-light">1.000.000</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Hasil Linier Sederhana:</div>
              <div class="fs-5 fw-bold text-info" id="exp_lin">2.200.000</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Hasil Eksponensial Majemuk:</div>
              <div class="fs-5 fw-bold text-success" id="exp_res">3.138.428</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #f43f5e;">
            <div class="small text-danger fw-bold mb-1"><i class="bi bi-trophy-fill"></i> Keunggulan Multiplikatif:</div>
            <div class="small text-light" id="exp_adv">Eksponensial menghasilkan keuntungan Rp 938.428 lebih tinggi dari pertumbuhan linier.</div>
          </div>
        </div>
        """,
        "js": """
        function updateExpSim() {
          const r = parseInt(document.getElementById('exp_slider_r').value);
          const t = parseInt(document.getElementById('exp_slider_t').value);
          document.getElementById('exp_r_val').textContent = `${r}% per periode`;
          document.getElementById('exp_t_val').textContent = `${t} Periode`;
          const p0 = 1000000;
          const rate = r / 100;
          const linear = p0 * (1 + rate * t);
          const exp = p0 * Math.pow(1 + rate, t);
          const diff = exp - linear;
          document.getElementById('exp_lin').textContent = Math.round(linear).toLocaleString('id-ID');
          document.getElementById('exp_res').textContent = Math.round(exp).toLocaleString('id-ID');
          document.getElementById('exp_adv').innerHTML = `Bunga majemuk menghasilkan <strong>Rp ${Math.round(diff).toLocaleString('id-ID')}</strong> ekstra dibanding bunga biasa. Inilah efek pelipatgandaan eksponensial P(t) = P₀(1+r)ᵗ.`;
        }
        """
    },
    "desimal": {
        "title": "Laboratorium Presisi: Representasi Pecahan Desimal & Galat Floating-Point IEEE 754",
        "desc": "🎯 Misi Berpikir: Geser pecahan pembilang dan penyebut untuk mengamati fenomena desimal berulang tak hingga dan tantangan komputasi 0.1 + 0.2!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(14,165,233,0.08); border:1px solid rgba(14,165,233,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-cpu"></i> Mengapa Komputer Menghasilkan 0.1 + 0.2 = 0.30000000000000004?</div>
          <p class="small text-light mb-0">Bilangan desimal berbasis 10 (faktor 2 dan 5). Sementara prosesor komputer menggunakan basis 2 (biner). Pecahan 1/10 yang tampak sederhana menjadi bilangan berulang biner tak hingga, memicu galat pembulatan halus!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Pembilang (Numerator a): <span id="dec_val_a" class="fw-bold text-info">1</span></label>
            <input type="range" class="form-range" id="dec_slider_a" min="1" max="20" value="1" oninput="updateDesimalSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Penyebut (Denominator b): <span id="dec_val_b" class="fw-bold text-warning">7</span></label>
            <input type="range" class="form-range" id="dec_slider_b" min="2" max="20" value="7" oninput="updateDesimalSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Bentuk Pecahan Biasa:</div>
              <div class="fs-5 fw-bold text-light" id="dec_frac">1 / 7</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Ekspansi Desimal:</div>
              <div class="fs-6 fw-bold text-success font-monospace" id="dec_res">0.142857142857...</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Tipe Pola Desimal:</div>
              <div class="fs-6 fw-bold text-warning" id="dec_type">Berulang Tak Hingga</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #0ea5e9;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-lightbulb-fill"></i> Analisis Faktor Prima Penyebut:</div>
            <div class="small text-light" id="dec_factor">Penyebut 7 memiliki faktor prima selain 2 dan 5, sehingga pasti menghasilkan desimal berulang tanpa henti (non-terminating periodic decimal).</div>
          </div>
        </div>
        """,
        "js": """
        function isTerminating(b) {
          while (b % 2 === 0) b /= 2;
          while (b % 5 === 0) b /= 5;
          return b === 1;
        }
        function updateDesimalSim() {
          const a = parseInt(document.getElementById('dec_slider_a').value);
          const b = parseInt(document.getElementById('dec_slider_b').value);
          document.getElementById('dec_val_a').textContent = a;
          document.getElementById('dec_val_b').textContent = b;
          document.getElementById('dec_frac').textContent = `${a} / ${b}`;
          const val = (a / b).toString();
          document.getElementById('dec_res').textContent = (a / b).toFixed(8);
          const term = isTerminating(b);
          if (term) {
            document.getElementById('dec_type').textContent = "Berhenti Terbatas (Terminating)";
            document.getElementById('dec_type').className = "fs-6 fw-bold text-success";
            document.getElementById('dec_factor').innerHTML = `Penyebut ${b} hanya memiliki faktor prima 2 dan/atau 5. Pecahan ini berhenti secara presisi dalam sistem desimal desimal basis 10.`;
          } else {
            document.getElementById('dec_type').textContent = "Berulang Tak Hingga (Periodic)";
            document.getElementById('dec_type').className = "fs-6 fw-bold text-warning";
            document.getElementById('dec_factor').innerHTML = `Penyebut ${b} mengandung faktor prima selain 2 dan 5. Angka akan berulang secara periodik tak hingga, menuntut strategi pembulatan pada komputasi digital.`;
          }
        }
        """
    },
    "sistem_bilangan": {
        "title": "Laboratorium Arsitektur Biner: Konversi Radiks (Basis 10, 2, 8, 16)",
        "desc": "🎯 Misi Berpikir: Geser nilai desimal dan saksikan dekomposisi nilai tempat menjadi representasi Biner (Bit mesin) dan Heksadesimal (Alamat memori)!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-motherboard"></i> Bahasa Mesin vs Bahasa Manusia:</div>
          <p class="small text-light mb-0">Manusia berhitung basis 10 karena memiliki 10 jari. Transistor komputer hanya mengenali 2 kondisi fisik (tegangan tinggi/rendah: 1 dan 0). Heksadesimal (basis 16) menjembatani keduanya dengan mengemas 4 bit biner dalam 1 digit hex!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-12">
            <label class="form-label small text-muted">Input Bilangan Desimal (Basis 10): <span id="sys_val_dec" class="fw-bold text-info">42</span></label>
            <input type="range" class="form-range" id="sys_slider" min="0" max="255" value="42" oninput="updateSistemSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Biner (Basis 2 - 8 Bit Byte):</div>
              <div class="fs-5 fw-bold text-success font-monospace" id="sys_bin">00101010</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Oktal (Basis 8):</div>
              <div class="fs-5 fw-bold text-warning font-monospace" id="sys_oct">52</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Heksadesimal (Basis 16):</div>
              <div class="fs-5 fw-bold text-info font-monospace" id="sys_hex">0x2A</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #6366f1;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-cpu-fill"></i> Dekomposisi Pembobotan Bit Biner:</div>
            <div class="small text-light font-monospace" id="sys_breakdown">32 + 8 + 2 = 42</div>
          </div>
        </div>
        """,
        "js": """
        function updateSistemSim() {
          const val = parseInt(document.getElementById('sys_slider').value);
          document.getElementById('sys_val_dec').textContent = val;
          const bin = val.toString(2).padStart(8, '0');
          const oct = val.toString(8);
          const hex = '0x' + val.toString(16).toUpperCase();
          document.getElementById('sys_bin').textContent = bin;
          document.getElementById('sys_oct').textContent = oct;
          document.getElementById('sys_hex').textContent = hex;
          let terms = [];
          for (let i = 0; i < 8; i++) {
            if (bin[7 - i] === '1') {
              terms.push(`2^${i} (${Math.pow(2, i)})`);
            }
          }
          const breakdown = terms.length > 0 ? terms.reverse().join(' + ') + ` = ${val}` : '0';
          document.getElementById('sys_breakdown').innerHTML = `Pembobotan: ${breakdown}`;
        }
        """
    },
    "vektor": {
        "title": "Laboratorium Vektor 2D: Resultan & Perkalian Titik (Dot Product)",
        "desc": "🎯 Misi Berpikir: Geser komponen vektor u dan v, amati perubahan panjang resultan serta sudut orientasi melalui Dot Product!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-compass"></i> Mengapa Arah dan Sudut Kritis?</div>
          <p class="small text-light mb-0">Dalam grafika 3D dan fisika game, dot product menentukan intensitas pencahayaan (Lambertian shading) dan arah gerakan. Amati saat u·v bernilai 0 (tegak lurus/ortogonal) atau negatif (berlawanan arah)!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-3">
            <label class="form-label small text-muted">Vektor u_x: <span id="val_ux" class="fw-bold text-info">3</span></label>
            <input type="range" class="form-range" id="slider_ux" min="-10" max="10" value="3" oninput="updateVektorSim()">
          </div>
          <div class="col-md-3">
            <label class="form-label small text-muted">Vektor u_y: <span id="val_uy" class="fw-bold text-info">4</span></label>
            <input type="range" class="form-range" id="slider_uy" min="-10" max="10" value="4" oninput="updateVektorSim()">
          </div>
          <div class="col-md-3">
            <label class="form-label small text-muted">Vektor v_x: <span id="val_vx" class="fw-bold text-warning">4</span></label>
            <input type="range" class="form-range" id="slider_vx" min="-10" max="10" value="4" oninput="updateVektorSim()">
          </div>
          <div class="col-md-3">
            <label class="form-label small text-muted">Vektor v_y: <span id="val_vy" class="fw-bold text-warning">0</span></label>
            <input type="range" class="form-range" id="slider_vy" min="-10" max="10" value="0" oninput="updateVektorSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Panjang Magnitudo |u|:</div>
              <div class="fs-5 fw-bold text-info" id="vektor_mag_u">5.00</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Panjang Magnitudo |v|:</div>
              <div class="fs-5 fw-bold text-warning" id="vektor_mag_v">4.00</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Dot Product (u · v):</div>
              <div class="fs-5 fw-bold text-success" id="vektor_dot">12.00</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #6366f1;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-arrows-angle"></i> Sudut Orientasi Antara u dan v (θ):</div>
            <div class="small text-light" id="vektor_angle">Sudut θ = 53.13° (Lancip). Dot product bernilai positif menandakan kedua vektor mengarah ke kuadran yang searah.</div>
          </div>
        </div>
        """,
        "js": """
        function updateVektorSim() {
          const ux = parseFloat(document.getElementById('slider_ux').value);
          const uy = parseFloat(document.getElementById('slider_uy').value);
          const vx = parseFloat(document.getElementById('slider_vx').value);
          const vy = parseFloat(document.getElementById('slider_vy').value);
          document.getElementById('val_ux').textContent = ux;
          document.getElementById('val_uy').textContent = uy;
          document.getElementById('val_vx').textContent = vx;
          document.getElementById('val_vy').textContent = vy;
          const magU = Math.sqrt(ux*ux + uy*uy);
          const magV = Math.sqrt(vx*vx + vy*vy);
          const dot = ux*vx + uy*vy;
          document.getElementById('vektor_mag_u').textContent = magU.toFixed(2);
          document.getElementById('vektor_mag_v').textContent = magV.toFixed(2);
          document.getElementById('vektor_dot').textContent = dot.toFixed(2);
          let angleText = "";
          if (magU === 0 || magV === 0) {
            angleText = "Vektor bernilai nol tidak memiliki orientasi arah terdefinisi.";
          } else {
            let cosTheta = dot / (magU * magV);
            cosTheta = Math.max(-1, Math.min(1, cosTheta));
            const deg = (Math.acos(cosTheta) * (180 / Math.PI)).toFixed(1);
            let rel = "Lancip";
            if (Math.abs(dot) < 0.001) rel = "Tegak Lurus (Ortogonal 90°)";
            else if (dot < 0) rel = "Tumpul (> 90°)";
            angleText = `Sudut θ = <strong>${deg}°</strong> (${rel}). Hasil dot product = <strong>${dot.toFixed(2)}</strong>.`;
          }
          document.getElementById('vektor_angle').innerHTML = angleText;
        }
        """
    },
    "logaritma": {
        "title": "Laboratorium Skala Logaritmik: Dekompresi Angka & Fenomena Sensorik",
        "desc": "🎯 Misi Berpikir: Geser nilai input x dan amati bagaimana fungsi logaritma mentransformasi kenaikan eksponensial ekstrem menjadi skala linier manusiawi!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(217,70,239,0.08); border:1px solid rgba(217,70,239,0.25);">
          <div class="small fw-bold text-warning mb-1"><i class="bi bi-soundwave"></i> Hukum Weber-Fechner & Skala Logaritmik:</div>
          <p class="small text-light mb-0">Manusia mendengar volume suara (Decibel) dan merasakan gempa (Skala Richter) secara logaritmik! Jika intensitas energi melonjak 1.000 kali lipat, persepsi otak manusia hanya merasakan kenaikan skala log 3 tingkat.</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Basis Logaritma b: <span id="val_log_b" class="fw-bold text-info">10</span></label>
            <input type="range" class="form-range" id="slider_log_b" min="2" max="10" value="10" oninput="updateLogSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Intensitas / Input x: <span id="val_log_x" class="fw-bold text-warning">1000</span></label>
            <input type="range" class="form-range" id="slider_log_x" min="1" max="5000" value="1000" step="10" oninput="updateLogSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-md-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Bentuk Logaritma:</div>
              <div class="fs-6 fw-bold text-light" id="log_expr">log₁₀(1000)</div>
            </div>
            <div class="col-md-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Nilai Eksponen y:</div>
              <div class="fs-4 fw-bold text-success" id="log_res">3.000</div>
            </div>
            <div class="col-md-4">
              <div class="small text-muted">Verifikasi Eksponensial:</div>
              <div class="fs-6 fw-bold text-info" id="log_verify">10³ = 1000</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #d946ef;">
            <div class="small text-warning fw-bold mb-1"><i class="bi bi-compress"></i> Rasio Kompresi Skala:</div>
            <div class="small text-light" id="log_ratio">Input x sebesar 1000 telah terkompresi secara elegan menjadi angka ringkas 3.00.</div>
          </div>
        </div>
        """,
        "js": """
        function updateLogSim() {
          const b = parseInt(document.getElementById('slider_log_b').value);
          const x = parseFloat(document.getElementById('slider_log_x').value);
          document.getElementById('val_log_b').textContent = b;
          document.getElementById('val_log_x').textContent = x;
          const y = Math.log(x) / Math.log(b);
          document.getElementById('log_expr').textContent = `log_${b}(${x})`;
          document.getElementById('log_res').textContent = y.toFixed(3);
          document.getElementById('log_verify').textContent = `${b}^(${y.toFixed(2)}) ≈ ${x}`;
          const compRatio = (x / Math.max(0.1, y)).toFixed(1);
          document.getElementById('log_ratio').innerHTML = `Input nilai <strong>${x}</strong> diringkas menjadi skala <strong>${y.toFixed(3)}</strong> (Rasio kompresi informasi ~${compRatio}x).`;
        }
        """
    },
    "persamaan_linear": {
        "title": "Laboratorium SPLDV: Determinant Cramer & Titik Potong Geometris",
        "desc": "🎯 Misi Berpikir: Geser koefisien dari 2 garis linear ax + by = c dan amati secara langsung letak titik potong (solusi unik) atau kondisi garis sejajar!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.25);">
          <div class="small fw-bold text-info mb-1"><i class="bi bi-intersect"></i> Dua Garis di Ruang 2D:</div>
          <p class="small text-light mb-0">Solusi sistem persamaan linear dua variabel (SPLDV) adalah koordinat perpotongan dua garis lurus di bidang Kartesius. Jika determinan koefisien D = 0, garis bersifat sejajar (tidak ada solusi) atau berimpit.</p>
        </div>
        <div class="row g-2 align-items-center">
          <div class="col-md-6 border-end border-secondary border-opacity-25 pe-3">
            <div class="small fw-bold text-info mb-1">Garis 1: a₁x + b₁y = c₁</div>
            <div class="d-flex gap-2">
              <input type="number" class="form-control form-control-sm bg-dark text-light border-secondary" id="spldv_a1" value="2" oninput="updateSPLDVSim()">
              <input type="number" class="form-control form-control-sm bg-dark text-light border-secondary" id="spldv_b1" value="1" oninput="updateSPLDVSim()">
              <input type="number" class="form-control form-control-sm bg-dark text-light border-secondary" id="spldv_c1" value="8" oninput="updateSPLDVSim()">
            </div>
          </div>
          <div class="col-md-6 ps-3">
            <div class="small fw-bold text-warning mb-1">Garis 2: a₂x + b₂y = c₂</div>
            <div class="d-flex gap-2">
              <input type="number" class="form-control form-control-sm bg-dark text-light border-secondary" id="spldv_a2" value="1" oninput="updateSPLDVSim()">
              <input type="number" class="form-control form-control-sm bg-dark text-light border-secondary" id="spldv_b2" value="-1" oninput="updateSPLDVSim()">
              <input type="number" class="form-control form-control-sm bg-dark text-light border-secondary" id="spldv_c2" value="1" oninput="updateSPLDVSim()">
            </div>
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Determinan Utama D:</div>
              <div class="fs-5 fw-bold text-info" id="spldv_det">D = -3</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Nilai Solusi x:</div>
              <div class="fs-5 fw-bold text-success" id="spldv_sol_x">x = 3.00</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Nilai Solusi y:</div>
              <div class="fs-5 fw-bold text-success" id="spldv_sol_y">y = 2.00</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #3b82f6;">
            <div class="small text-info fw-bold mb-1"><i class="bi bi-geo-alt-fill"></i> Titik Potong Koordinat (Solusi SPLDV):</div>
            <div class="small text-light" id="spldv_status">Kedua garis berpotongan unik tepat di titik (3.00, 2.00).</div>
          </div>
        </div>
        """,
        "js": """
        function updateSPLDVSim() {
          const a1 = parseFloat(document.getElementById('spldv_a1').value) || 0;
          const b1 = parseFloat(document.getElementById('spldv_b1').value) || 0;
          const c1 = parseFloat(document.getElementById('spldv_c1').value) || 0;
          const a2 = parseFloat(document.getElementById('spldv_a2').value) || 0;
          const b2 = parseFloat(document.getElementById('spldv_b2').value) || 0;
          const c2 = parseFloat(document.getElementById('spldv_c2').value) || 0;
          const D = (a1 * b2) - (a2 * b1);
          const Dx = (c1 * b2) - (c2 * b1);
          const Dy = (a1 * c2) - (a2 * c1);
          document.getElementById('spldv_det').textContent = `D = ${D}`;
          if (Math.abs(D) < 0.0001) {
            document.getElementById('spldv_sol_x').textContent = "Tidak Unik";
            document.getElementById('spldv_sol_y').textContent = "Tidak Unik";
            if (Math.abs(Dx) < 0.0001 && Math.abs(Dy) < 0.0001) {
              document.getElementById('spldv_status').innerHTML = "Kedua garis <strong>berhimpit</strong> (D=0, Dx=0, Dy=0), menghasilkan tak hingga solusi konsisten.";
            } else {
              document.getElementById('spldv_status').innerHTML = "Kedua garis <strong>sejajar</strong> sempurna (D=0 namun Dx≠0). Tidak ada titik potong (inkonsisten / himpunan kosong).";
            }
          } else {
            const x = Dx / D;
            const y = Dy / D;
            document.getElementById('spldv_sol_x').textContent = `x = ${x.toFixed(2)}`;
            document.getElementById('spldv_sol_y').textContent = `y = ${y.toFixed(2)}`;
            document.getElementById('spldv_status').innerHTML = `Kedua garis berpotongan unik tepat di koordinat <strong>(${x.toFixed(2)}, ${y.toFixed(2)})</strong>. Solusi didapat via Aturan Cramer D_x/D dan D_y/D.`;
          }
        }
        """
    },
    "matematika_diskrit": {
        "title": "Laboratorium Kombinatorika: Urutan (Permutasi) vs Pilihan Bebas (Kombinasi)",
        "desc": "🎯 Misi Berpikir: Geser total elemen n dan ukuran pemilihan r untuk melihat disparitas pertumbuhan permutasi P(n, r) versus kombinasi C(n, r)!",
        "html": """
        <div class="p-3 mb-3 rounded" style="background:rgba(234,88,12,0.08); border:1px solid rgba(234,88,12,0.25);">
          <div class="small fw-bold text-warning mb-1"><i class="bi bi-diagram-2"></i> Perbedaan Esensial: Apakah Posisi / Urutan Diperhitungkan?</div>
          <p class="small text-light mb-0">Permutasi memperhitungkan urutan (seperti kata sandi PIN atau juara 1, 2, 3), sedangkan Kombinasi tidak peduli urutan (seperti memilih tim delegasi). Faktor r! membagi permutasi menjadi kombinasi!</p>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col-md-6">
            <label class="form-label small text-muted">Jumlah Total Objek n: <span id="val_n" class="fw-bold text-info">6</span></label>
            <input type="range" class="form-range" id="slider_n" min="1" max="10" value="6" oninput="updateDiskritSim()">
          </div>
          <div class="col-md-6">
            <label class="form-label small text-muted">Jumlah Objek Dipilih r: <span id="val_r" class="fw-bold text-warning">3</span></label>
            <input type="range" class="form-range" id="slider_r" min="1" max="10" value="3" oninput="updateDiskritSim()">
          </div>
        </div>
        <div class="mt-3 p-3 rounded" style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);">
          <div class="row text-center g-2 mb-2">
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Faktorial n! (Total susunan):</div>
              <div class="fs-5 fw-bold text-light" id="diskrit_fac">720</div>
            </div>
            <div class="col-4 border-end border-secondary border-opacity-25">
              <div class="small text-muted">Permutasi P(n, r) [Urutan Penting]:</div>
              <div class="fs-5 fw-bold text-warning" id="diskrit_perm">120</div>
            </div>
            <div class="col-4">
              <div class="small text-muted">Kombinasi C(n, r) [Bebas Urutan]:</div>
              <div class="fs-5 fw-bold text-success" id="diskrit_comb">20</div>
            </div>
          </div>
          <div class="p-2 rounded mt-2" style="background:rgba(0,0,0,0.3); border-left:3px solid #ea580c;">
            <div class="small text-warning fw-bold mb-1"><i class="bi bi-lightbulb-fill"></i> Analisis Rasio Simetri r!:</div>
            <div class="small text-light" id="diskrit_ratio">Ada 6 cara menata ulang 3 objek yang sama (3! = 6). Sehingga Kombinasi bernilai 6x lebih sedikit daripada Permutasi.</div>
          </div>
        </div>
        """,
        "js": """
        function fact(num) {
          if (num <= 1) return 1;
          let res = 1;
          for (let i = 2; i <= num; i++) res *= i;
          return res;
        }
        function updateDiskritSim() {
          let n = parseInt(document.getElementById('slider_n').value);
          let r = parseInt(document.getElementById('slider_r').value);
          if (r > n) {
            r = n;
            document.getElementById('slider_r').value = r;
          }
          document.getElementById('val_n').textContent = n;
          document.getElementById('val_r').textContent = r;
          const fn = fact(n);
          const fnr = fact(n - r);
          const fr = fact(r);
          const perm = Math.round(fn / fnr);
          const comb = Math.round(fn / (fr * fnr));
          document.getElementById('diskrit_fac').textContent = fn.toLocaleString('id-ID');
          document.getElementById('diskrit_perm').textContent = perm.toLocaleString('id-ID');
          document.getElementById('diskrit_comb').textContent = comb.toLocaleString('id-ID');
          document.getElementById('diskrit_ratio').innerHTML = `Ada <strong>${fr}</strong> permutasi internal (r! = ${r}! = ${fr}) untuk setiap himpunan bagian. Karena itu, P(${n}, ${r}) = ${comb} × ${fr} = <strong>${perm}</strong> susunan.`;
        }
        """
    }
}

def get_widget(subj_key):
    return WIDGET_DATA[subj_key]


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
      max-width: 920px;
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

    /* Target Box */
    .dic-target-box {{
      background: rgba(99, 102, 241, 0.06);
      border: 1px solid rgba(99, 102, 241, 0.25);
      border-radius: 14px;
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
    }}
    .dic-target-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #818cf8;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .dic-target-list {{
      margin: 0;
      padding-left: 1.25rem;
      font-size: 0.92rem;
      color: #cbd5e1;
      line-height: 1.7;
    }}
    .dic-target-list li {{ margin-bottom: 0.4rem; }}

    /* Real-World Hook Box */
    .dic-hook-box {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.08), rgba(245, 158, 11, 0.02));
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-left: 4px solid #f59e0b;
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      margin: 1.75rem 0;
    }}
    .dic-hook-title {{
      font-size: 0.88rem;
      font-weight: 800;
      color: #fbbf24;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .dic-hook-body {{
      font-size: 0.95rem;
      color: #e2e8f0;
      line-height: 1.75;
      margin: 0;
    }}

    /* Section Title */
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

    /* Concepts Cards */
    .dic-concept-card {{
      background: #111622;
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.5rem;
      margin: 1.25rem 0;
    }}
    .dic-h3 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #f8fafc;
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .dic-list {{
      margin: 0.5rem 0 0.75rem 1.25rem;
      color: #cbd5e1;
      font-size: 0.92rem;
      line-height: 1.75;
    }}
    .dic-list li {{ margin-bottom: 0.35rem; }}

    /* Dicoding Callout Boxes */
    .dic-callout {{
      border-radius: 12px;
      padding: 1.15rem 1.4rem;
      margin: 1.5rem 0;
      display: flex;
      gap: 1rem;
      align-items: flex-start;
    }}
    .dic-callout-icon {{
      font-size: 1.35rem;
      line-height: 1;
      flex-shrink: 0;
      margin-top: 0.15rem;
    }}
    .dic-callout-content {{ flex-grow: 1; font-size: 0.91rem; line-height: 1.7; }}
    .dic-callout-title {{
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 0.3rem;
    }}
    
    .dic-callout.pro-tip {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-left: 4px solid #10b981;
    }}
    .dic-callout.pro-tip .dic-callout-title {{ color: #34d399; }}
    .dic-callout.pro-tip .dic-callout-icon {{ color: #10b981; }}
    .dic-callout.pro-tip .dic-callout-content {{ color: #d1fae5; }}

    .dic-callout.pitfall {{
      background: rgba(244, 63, 94, 0.08);
      border: 1px solid rgba(244, 63, 94, 0.25);
      border-left: 4px solid #f43f5e;
    }}
    .dic-callout.pitfall .dic-callout-title {{ color: #fb7185; }}
    .dic-callout.pitfall .dic-callout-icon {{ color: #f43f5e; }}
    .dic-callout.pitfall .dic-callout-content {{ color: #ffe4e6; }}

    .dic-callout.fun-fact {{
      background: rgba(139, 92, 246, 0.08);
      border: 1px solid rgba(139, 92, 246, 0.25);
      border-left: 4px solid #8b5cf6;
    }}
    .dic-callout.fun-fact .dic-callout-title {{ color: #c084fc; }}
    .dic-callout.fun-fact .dic-callout-icon {{ color: #8b5cf6; }}
    .dic-callout.fun-fact .dic-callout-content {{ color: #ede9fe; }}

    /* Formula & Parameter Table */
    .dic-formula-card {{
      background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
      border: 1px solid var(--accent-glow);
      border-radius: 14px;
      padding: 1.75rem;
      margin: 1.25rem 0;
      text-align: center;
      overflow-x: auto;
      box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }}
    .dic-param-table-wrap {{
      margin: 1.25rem 0;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border-color);
    }}
    .dic-param-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}
    .dic-param-table th {{
      background: #161d2e;
      color: #94a3b8;
      font-weight: 700;
      padding: 0.65rem 1rem;
      text-align: left;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--border-color);
    }}
    .dic-param-table td {{
      padding: 0.75rem 1rem;
      color: #cbd5e1;
      border-bottom: 1px solid rgba(255,255,255,0.04);
      vertical-align: middle;
    }}
    .dic-param-table tr:last-child td {{ border-bottom: none; }}
    .dic-param-table tr:hover td {{ background: rgba(255,255,255,0.02); }}
    .dic-symbol-badge {{
      font-family: 'Fira Code', monospace;
      color: #38bdf8;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.1);
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
      font-size: 0.85rem;
    }}

    .dic-formula-explain {{
      font-size: 0.9rem;
      color: #cbd5e1;
      border-left: 3px solid var(--accent);
      padding: 0.75rem 1rem;
      background: rgba(255,255,255,0.02);
      border-radius: 0 8px 8px 0;
      margin: 1rem 0;
      line-height: 1.7;
    }}

    /* Guided Step Box */
    .dic-step-box {{
      background: #111622;
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.5rem;
      margin: 1.5rem 0;
    }}
    .dic-step-problem {{
      background: rgba(255,255,255,0.02);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.25rem;
      font-size: 0.95rem;
      color: #f1f5f9;
      line-height: 1.7;
    }}
    .dic-step-item {{
      padding: 0.75rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      font-size: 0.9rem;
    }}
    .dic-step-item.diketahui {{
      background: rgba(99, 102, 241, 0.05);
      border-left: 3px solid #6366f1;
      color: #cbd5e1;
    }}
    .dic-step-item.ditanya {{
      background: rgba(245, 158, 11, 0.05);
      border-left: 3px solid #f59e0b;
      color: #cbd5e1;
    }}
    .dic-step-item.langkah {{
      background: rgba(16, 185, 129, 0.05);
      border-left: 3px solid #10b981;
      color: #cbd5e1;
      line-height: 1.8;
    }}
    .dic-step-item.kesimpulan {{
      background: rgba(56, 189, 248, 0.08);
      border-left: 3px solid #38bdf8;
      color: #e0f2fe;
      font-weight: 500;
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

    /* Takeaways Box */
    .dic-takeaway-box {{
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.06), rgba(16, 185, 129, 0.01));
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 14px;
      padding: 1.5rem;
      margin: 2rem 0;
    }}
    .dic-takeaway-title {{
      font-size: 0.88rem;
      font-weight: 800;
      color: #34d399;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .dic-takeaway-list {{
      margin: 0;
      padding-left: 1.25rem;
      font-size: 0.92rem;
      color: #cbd5e1;
      line-height: 1.7;
    }}
    .dic-takeaway-list li {{ margin-bottom: 0.45rem; }}
    
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
    babs = data["babs"]
    total = len(babs)
    idx = bab_num - 1
    bab = babs[idx]
    bab_title = bab["title"]
    stage = STAGE_DEFINITIONS[idx]
    widget = get_widget(subj_key)

    # 1. Objectives list
    obj_lis = "".join(f"<li>{obj}</li>" for obj in bab["objectives"])

    # 2. Concepts sections (already formatted rich HTML from data modules)
    concepts_html = bab["concepts"]

    # 3. Formula Parameter Table
    param_rows = []
    for p in bab["formula_params"]:
        if isinstance(p, (list, tuple)) and len(p) >= 2:
            sym = p[0]
            desc = p[1]
            param_rows.append(f"""
            <tr>
              <td style="width:25%;"><span class="dic-symbol-badge">{sym}</span></td>
              <td class="text-light">{desc}</td>
            </tr>""")
    param_table_html = f"""
    <div class="dic-param-table-wrap">
      <table class="dic-param-table">
        <thead>
          <tr>
            <th>Simbol / Notasi</th>
            <th>Makna & Interpretasi Matematis</th>
          </tr>
        </thead>
        <tbody>
          {"".join(param_rows)}
        </tbody>
      </table>
    </div>"""

    # 4. Worked Example Step Box
    ex = bab["example"]
    q_text = ex.get("question", ex.get("problem", ""))
    known = ex.get("known", ex.get("diketahui", ""))
    asked = ex.get("asked", ex.get("ditanya", ""))
    conclusion = ex.get("conclusion", ex.get("kesimpulan", ""))
    steps_list = ex.get("steps", ex.get("langkah", []))
    
    steps_html = []
    if isinstance(steps_list, list):
        for st in steps_list:
            if isinstance(st, (list, tuple)) and len(st) >= 2:
                st_title, st_desc = st[0], st[1]
                steps_html.append(f"<div class='mb-2'><strong>{st_title}:</strong> {st_desc}</div>")
            else:
                steps_html.append(f"<div class='mb-2'>{st}</div>")
    else:
        steps_html.append(str(steps_list))
    
    steps_joined = "".join(steps_html)

    example_html = f"""
    <div class="dic-step-box">
      <div class="dic-step-problem">
        <div class="small fw-bold text-success mb-1"><i class="bi bi-patch-question"></i> Skenario Studi Kasus:</div>
        <div>{q_text}</div>
      </div>
      <div class="dic-step-item diketahui">
        <div class="small fw-bold text-primary mb-1"><i class="bi bi-pin-angle-fill"></i> Diketahui:</div>
        <div>{known}</div>
      </div>
      <div class="dic-step-item ditanya">
        <div class="small fw-bold text-warning mb-1"><i class="bi bi-question-circle-fill"></i> Ditanya:</div>
        <div>{asked}</div>
      </div>
      <div class="dic-step-item langkah">
        <div class="small fw-bold text-success mb-1"><i class="bi bi-diagram-3-fill"></i> Langkah Penyelesaian Terpandu:</div>
        <div>{steps_joined}</div>
      </div>
      <div class="dic-step-item kesimpulan">
        <div class="small fw-bold text-info mb-1"><i class="bi bi-check-circle-fill"></i> Kesimpulan Akhir:</div>
        <div>{conclusion}</div>
      </div>
    </div>"""

    # 5. Core Takeaways
    takeaways_lis = "".join(f"<li>{item}</li>" for item in bab["takeaways"])

    # 6. Active Recall Quiz
    q_data = bab["quiz"]
    q_question, q_options, q_correct_idx, q_explanation = q_data[0], q_data[1], q_data[2], q_data[3]
    opt_buttons = []
    for i, opt in enumerate(q_options):
        is_correct = "true" if i == q_correct_idx else "false"
        escaped_exp = str(q_explanation).replace("'", "\\'").replace('"', '&quot;')
        opt_buttons.append(f"""
        <button class="dic-opt-btn" onclick="checkAnswer(this, {is_correct}, '{escaped_exp}')">
          <span>{opt}</span>
          <i class="bi bi-circle"></i>
        </button>""")
    opts_html = "\n".join(opt_buttons)

    # 7. Prev / Next Navigation
    prev_url = f"{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={bab_num - 1}) }}}}" if bab_num > 1 else f"{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}"
    next_url = f"{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={bab_num + 1}) }}}}" if bab_num < total else f"{{{{ url_for('materi.subject_index', subject='{subj_key}') }}}}"
    
    prev_label = f"← Bab {bab_num - 1}: {babs[bab_num - 2]['title'].split(':')[0]}" if bab_num > 1 else f"← Silabus {short}"
    next_label = f"Lanjut ke Bab {bab_num + 1}: {babs[bab_num]['title'].split(':')[0]} →" if bab_num < total else f"Selesai Modul {short} ✓"

    # 8. Sidebar items
    sidebar_items = []
    for i, b_item in enumerate(babs):
        n = i + 1
        active_cls = " active" if n == bab_num else ""
        sidebar_items.append(f"""
        <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={n}) }}}}" 
           class="dic-chapter-link{active_cls} {{{{ 'done' if all_bab_status[{i}]['is_completed'] else '' }}}}">
          <span class="dic-num-badge">{{{{ '✓' if all_bab_status[{i}]['is_completed'] else '{n}' }}}}</span>
          <span>{b_item['title']}</span>
        </a>""")
    sidebar_html = "\n".join(sidebar_items)

    formula_str = bab['formula']

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

      <!-- In-Page Anchor Links (TOC) -->
      <div class="dic-sb-nav-title">Daftar Isi Halaman (TOC)</div>
      <div class="dic-anchor-box">
        <a href="#peruntukan" class="dic-anchor-link"><i class="bi bi-compass me-1"></i> Peruntukan & Sasaran</a>
        <a href="#hook" class="dic-anchor-link"><i class="bi bi-lightbulb me-1"></i> Mengapa Ini Penting?</a>
        <a href="#konsep" class="dic-anchor-link"><i class="bi bi-bookmark-fill me-1"></i> Pembahasan Konsep</a>
        <a href="#tips" class="dic-anchor-link"><i class="bi bi-patch-check me-1"></i> Tips & Jebakan Umum</a>
        <a href="#formula" class="dic-anchor-link"><i class="bi bi-calculator me-1"></i> Formulasi KaTeX</a>
        <a href="#contoh" class="dic-anchor-link"><i class="bi bi-journal-check me-1"></i> Contoh Soal Terpandu</a>
        <a href="#simulator" class="dic-anchor-link"><i class="bi bi-sliders me-1"></i> Simulator Interaktif</a>
        <a href="#latihan" class="dic-anchor-link"><i class="bi bi-pencil-square me-1"></i> Active Recall Quiz</a>
        <a href="#rangkuman" class="dic-anchor-link"><i class="bi bi-check2-all me-1"></i> Rangkuman Intisari</a>
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

      <!-- Reading Meta Badges -->
      <div class="d-flex align-items-center gap-2 mb-3">
        <span class="badge bg-secondary-subtle text-light border border-secondary-subtle px-2 py-1 small">
          <i class="bi bi-clock-history me-1"></i> ~12-15 Menit Baca Mendalam
        </span>
        <span class="badge bg-primary-subtle text-primary border border-primary-subtle px-2 py-1 small">
          <i class="bi bi-mortarboard me-1"></i> Standar Akademi Dicoding
        </span>
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
          {obj_lis}
        </ul>
      </div>

      <!-- Real-World Motivation Hook -->
      <div class="dic-hook-box" id="hook">
        <div class="dic-hook-title"><i class="bi bi-lightbulb-fill"></i> Mengapa Konsep Ini Sangat Penting? (Perspektif Praktisi & Rekayasa)</div>
        <p class="dic-hook-body">{bab['hook']}</p>
      </div>

      <!-- Core Concept Sections -->
      <h2 class="dic-section-title" id="konsep">
        <i class="bi bi-book-half" style="color:{color};"></i> Pembahasan Konsep & Teori Mendalam
      </h2>
      {concepts_html}

      <!-- Dicoding Insights & Callouts -->
      <h2 class="dic-section-title" id="tips">
        <i class="bi bi-patch-check" style="color:{color};"></i> Tips Praktisi & Wawasan Kritis
      </h2>
      
      <div class="dic-callout pro-tip">
        <div class="dic-callout-icon"><i class="bi bi-lightbulb-fill"></i></div>
        <div>
          <div class="dic-callout-title">💡 Dicoding Pro-Tip / Praktik Terbaik</div>
          <div class="dic-callout-content">{bab['pro_tip']}</div>
        </div>
      </div>

      <div class="dic-callout pitfall">
        <div class="dic-callout-icon"><i class="bi bi-exclamation-triangle-fill"></i></div>
        <div>
          <div class="dic-callout-title">⚠️ Common Pitfall / Jebakan Umum</div>
          <div class="dic-callout-content">{bab['pitfall']}</div>
        </div>
      </div>

      <div class="dic-callout fun-fact">
        <div class="dic-callout-icon"><i class="bi bi-cpu-fill"></i></div>
        <div>
          <div class="dic-callout-title">🧠 Wawasan Komputasi & Fakta Menarik</div>
          <div class="dic-callout-content">{bab['fun_fact']}</div>
        </div>
      </div>

      <!-- Formula Section -->
      <h2 class="dic-section-title" id="formula">
        <i class="bi bi-calculator" style="color:{color};"></i> Formulasi KaTeX & Anatomi Parameter
      </h2>
      <div class="dic-formula-card">
        \\[ {formula_str} \\]
      </div>
      <div class="dic-formula-explain">
        <strong>💡 Makna & Intuisi Formulasi:</strong> {bab['formula_intuition']}
      </div>

      <div class="small fw-bold text-muted text-uppercase mb-2 mt-3"><i class="bi bi-table me-1"></i> Bedah Anatomi Variabel Formulasi:</div>
      {param_table_html}

      <!-- Worked Example -->
      <h2 class="dic-section-title" id="contoh">
        <i class="bi bi-journal-text text-success"></i> Contoh Soal & Pembahasan Terpandu (Langkah Demi Langkah)
      </h2>
      {example_html}

      <!-- Interactive Math Simulator Widget -->
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

      <!-- Active Recall Quiz -->
      <div class="dic-quiz-card {'border border-warning border-opacity-50 shadow-lg' if bab_num == 5 else ''}" id="latihan" style="{'background: linear-gradient(145deg, #131b2e, #111622);' if bab_num == 5 else ''}">
        <div class="dic-quiz-tag" style="{'color:#eab308; font-size:0.82rem;' if bab_num == 5 else ''}">
          <i class="bi {'bi-trophy-fill' if bab_num == 5 else 'bi-patch-question-fill'}"></i> 
          {'🏆 CAPSTONE CHALLENGE - UJI SINTESIS AKHIR MODUL' if bab_num == 5 else f'Active Recall Quiz - Bab {bab_num}'}
        </div>
        <div class="dic-quiz-q" style="{'font-size:1.1rem; color:#fef08a;' if bab_num == 5 else ''}">{q_question}</div>
        {opts_html}
        <div class="dic-feedback" id="quizFeedback"></div>
      </div>

      <!-- Core Takeaways -->
      <div class="dic-takeaway-box" id="rangkuman">
        <div class="dic-takeaway-title"><i class="bi bi-bookmark-check-fill"></i> Ringkasan Intisari Dicoding (Key Takeaways):</div>
        <ul class="dic-takeaway-list">
          {takeaways_lis}
        </ul>
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
    babs = data["babs"]
    total = len(babs)

    # 5-Stage Framework Visual Cards
    stages_html_list = []
    for i, stg in enumerate(STAGE_DEFINITIONS):
        num = i + 1
        b_title = babs[i]["title"]
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
    for i, b_item in enumerate(babs):
        n = i + 1
        stg = STAGE_DEFINITIONS[i]
        card = f"""
      <a href="{{{{ url_for('materi.subject_bab', subject='{subj_key}', bab_num={n}) }}}}" 
         class="dic-card-item {{{{ 'completed' if bab_progress[{i}]['is_completed'] else '' }}}}">
        <div class="dic-card-num" style="background:{color}20; color:{color};">{n}</div>
        <div class="flex-grow-1">
          <div style="font-size:0.75rem; color:{color}; font-weight:700; text-transform:uppercase;">{stg['badge']}</div>
          <div class="dic-card-title">{b_item['title']}</div>
          <div class="dic-card-meta"><i class="bi bi-clock"></i> ~12-15 Menit &bull; Dilengkapi Simulator & Contoh Kasus</div>
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
        Setiap bab dirancang secara pedagogis dengan peruntukan berjenjang ala Dicoding Academy:
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
    print("  MathThon: Dicoding-Standard Interactive Math Chapter Generator")
    print("=" * 65)
    created_count = 0

    for subj_key, data in SUBJECT_MODULES.items():
        subject_dir = os.path.join(TEMPLATES_DIR, subj_key)
        os.makedirs(subject_dir, exist_ok=True)

        # 1. Generate index.html
        index_file = os.path.join(subject_dir, "index.html")
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(build_index_html(subj_key, data))
        created_count += 1
        print(f"  [OK] Index  -> {subj_key}/index.html")

        # 2. Generate bab_1.html ... bab_5.html
        for bab_num in range(1, len(data["babs"]) + 1):
            bab_file = os.path.join(subject_dir, f"bab_{bab_num}.html")
            with open(bab_file, "w", encoding="utf-8") as f:
                f.write(build_bab_html(subj_key, data, bab_num))
            created_count += 1
            print(f"  [OK] Bab {bab_num}  -> {subj_key}/bab_{bab_num}.html")

    print("=" * 65)
    print(f"  [SUKSES] Sebanyak {created_count} file materi standar Dicoding telah dibangun.")
    print("  Setiap bab memiliki silabus, peruntukan stage, analogi hook nyata,")
    print("  bedah konsep komprehensif, pro-tip, pitfall, KaTeX formula dengan")
    print("  tabel parameter, contoh bertahap, live simulator lab, active recall quiz,")
    print("  dan rangkuman intisari.")
    print("=" * 65)


if __name__ == "__main__":
    main()
