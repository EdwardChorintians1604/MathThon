# 📐 MathThon

> Platform belajar matematika interaktif berbasis web dengan AI tutor, latihan soal adaptif, dan dashboard analitik — dibangun dengan **Flask (Python)** di backend dan **HTML/CSS/JS** di frontend.

---

## 📋 Daftar Isi

- [Gambaran Umum](#-gambaran-umum)
- [Fitur Utama](#-fitur-utama)
- [Arsitektur Sistem](#-arsitektur-sistem)
- [Struktur Proyek](#-struktur-proyek)
- [Database Schema](#-database-schema)
- [Alur Autentikasi](#-alur-autentikasi)
- [Modul Backend](#-modul-backend)
- [Halaman Frontend](#-halaman-frontend)
- [Keamanan](#-keamanan)
- [API Endpoints](#-api-endpoints)
- [Konfigurasi & Environment](#-konfigurasi--environment)
- [Cara Menjalankan](#-cara-menjalankan)
- [Deployment](#-deployment)
- [Tech Stack](#-tech-stack)

---

## 🌟 Gambaran Umum

**MathThon** adalah platform edukasi matematika yang menggabungkan:
- 📖 **Materi terstruktur** — topik-topik matematika dari dasar hingga lanjutan
- 🧠 **AI Tutor** (Google Gemini) — chatbot matematika yang membantu langkah demi langkah
- 🏋️ **Latihan soal adaptif** — soal dengan tingkat kesulitan easy/medium/hard
- 📊 **Analitik progres** — grafik perkembangan belajar per user
- 🛡️ **Keamanan berlapis** — deteksi SQL Injection, XSS, rate limiting, enkripsi Fernet

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 🔐 **Registrasi & Login** | Form biasa + Google OAuth (Sign In with Google) |
| 🤖 **AI Chat Tutor** | Powered by Google Gemini 1.5 Flash, menyimpan riwayat percakapan |
| 📚 **Materi Belajar** | Daftar materi dengan rating bintang, deskripsi, dan konten rich-text |
| ✏️ **Latihan Soal** | Soal per topik, dinilai otomatis, progres tersimpan |
| 📈 **Dashboard User** | Ringkasan progres, skor analisis, histori belajar |
| 🔑 **Reset Password** | Kode OTP via email (SMTP Gmail) |
| 👨‍💼 **Panel Admin** | CRUD materi, manajemen user, export database, monitoring feedback |
| 🛡️ **Crime Detection** | Log akses mencurigakan, deteksi serangan real-time |
| 📡 **Ngrok Integration** | Tunnel publik otomatis saat development |
| 📊 **Data Visualisasi** | Grafik data pendidikan Indonesia (CSV + pandas + matplotlib) |

---

## 🏗️ Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────┐
│                    Browser (Client)                      │
│         HTML + CSS + Vanilla JS + Jinja2                │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP / HTTPS
┌────────────────────▼────────────────────────────────────┐
│              Flask Application (app.py)                  │
│                                                          │
│  ┌──────────────┐  ┌────────────┐  ┌─────────────────┐  │
│  │  Blueprint   │  │ Middleware │  │  Extensions     │  │
│  │  - main      │  │ - CSRF     │  │  - SQLAlchemy   │  │
│  │  - auth      │  │ - CORS     │  │  - Flask-Limiter│  │
│  │  - user      │  │ - Security │  │  - Flask-WTF    │  │
│  │  - admin     │  │   Headers  │  │  - Flask-CORS   │  │
│  │  - api       │  │ - Rate Lim │  └─────────────────┘  │
│  │  - ai        │  └────────────┘                        │
│  │  - materi    │                                        │
│  │  - latihan   │                                        │
│  │  - feedback  │                                        │
│  └──────────────┘                                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐    │
│  │              Security Layer                       │    │
│  │  SQLi Detection │ XSS Filter │ File Integrity    │    │
│  │  Fernet Encrypt │ Rate Limit │ ClamAV (opsional) │    │
│  └──────────────────────────────────────────────────┘    │
└──────────────┬──────────────────────┬───────────────────┘
               │                      │
┌──────────────▼───────┐  ┌───────────▼──────────────────┐
│   MySQL Database     │  │   External Services           │
│   (maththon_db)      │  │   - Google Gemini AI API      │
│                      │  │   - Google OAuth 2.0          │
│   11 Tabel           │  │   - Gmail SMTP                │
│   (users, materi,    │  │   - Ngrok (dev tunnel)        │
│    soal, progres,    │  │   - Ollama (local LLM alt)    │
│    chat, dst...)     │  └──────────────────────────────┘
└──────────────────────┘
```

---

## 📁 Struktur Proyek

```
MathThon/
│
├── app.py                        # Entry point — inisialisasi Flask + Ngrok
├── config.py                     # Konfigurasi base (development/production)
├── requirements.txt              # Dependency Python
├── runtime.txt                   # Versi Python untuk hosting
├── vercel.json                   # Konfigurasi deploy ke Vercel
├── ngrok.yml                     # Konfigurasi Ngrok
├── secret.key                    # Kunci enkripsi Fernet (auto-generated)
├── .env                          # Environment variables (tidak di-commit)
├── .env.example                  # Template .env
│
├── Back_End/                     # Semua logika server
│   ├── __init__.py               # Flask App Factory (create_app)
│   ├── config.py                 # Konfigurasi backend (paths, AI, DB)
│   ├── models.py                 # Schema DB & inisialisasi tabel
│   ├── math.py                   # Utilitas kalkulasi matematika
│   ├── progres_user.py           # Tracker progres belajar user
│   │
│   ├── routes/                   # Semua Blueprint (route handlers)
│   │   ├── main.py               # Route utama: home, about, privacy
│   │   ├── auth.py               # Registrasi, login, logout, Google OAuth
│   │   ├── user.py               # Dashboard user, profil, pengaturan
│   │   ├── admin.py              # Panel admin: CRUD materi & user
│   │   ├── api.py                # REST API endpoints
│   │   ├── ai.py                 # AI chat endpoints (Gemini)
│   │   ├── materi.py             # Halaman detail materi
│   │   ├── latihan.py            # Sesi latihan soal
│   │   ├── feedback.py           # Endpoint pengiriman feedback
│   │   ├── security_for_web.py   # Dekorator auth & enkripsi Fernet
│   │   ├── security_utils.py     # Utilitas keamanan tambahan
│   │   ├── utils.py              # Helper: template context, email
│   │   ├── seed_daftar_materi.py # Seed data materi awal
│   │   └── seed_soal_latihan.py  # Seed data soal latihan
│   │
│   ├── db/
│   │   └── database_mysql.py     # Koneksi & query helper MySQL
│   │
│   ├── ai/
│   │   └── chat_api.py           # Integrasi Gemini API & Ollama
│   │
│   ├── bug_and_crime_detection/
│   │   └── bug_and_crime_detection.py  # Middleware deteksi serangan
│   │
│   ├── jumlah_user/
│   │   └── jumlah_user.py        # Statistik jumlah user & chat
│   └── security/                 # Modul keamanan tambahan
│
├── Front_End/                    # Semua aset UI
│   ├── templates/
│   │   ├── home.html             # Landing page
│   │   ├── about.html            # Halaman tentang
│   │   ├── privacy.html          # Kebijakan privasi
│   │   ├── terms.html            # Syarat & ketentuan
│   │   ├── error_security.html   # Halaman error 403/429
│   │   ├── user/                 # Template halaman user
│   │   │   ├── login_user.html
│   │   │   ├── register_user.html
│   │   │   ├── dashboard_user.html
│   │   │   ├── materi_user.html
│   │   │   ├── latihan_soal_user.html
│   │   │   ├── latihan_session.html
│   │   │   ├── ai_feature_user.html
│   │   │   ├── analyze_user.html
│   │   │   ├── progres_user.html
│   │   │   ├── calculator.html
│   │   │   ├── feedback_user.html
│   │   │   ├── pengaturan.html
│   │   │   ├── forget_password_user.html
│   │   │   └── reset_password_user.html
│   │   └── admin/                # Template halaman admin
│   │       ├── login_admin.html
│   │       ├── dashboard.html
│   │       ├── manage_users.html
│   │       ├── manage_materi.html
│   │       ├── manage_feedback.html
│   │       ├── crime_detection.html
│   │       ├── export_database.html
│   │       └── ...
│   └── static/                   # CSS, JS, gambar, uploads
│
└── uploads/                      # Foto profil user yang diupload
```

---

## 🗄️ Database Schema

Database: **`maththon_db`** (MySQL)

```
┌─────────────┐       ┌─────────────────┐       ┌──────────────┐
│   users     │       │  daftar_materi  │       │    topics    │
│─────────────│       │─────────────────│       │──────────────│
│ id (PK)     │       │ id (PK)         │       │ id (PK)      │
│ name        │       │ judul_materi    │       │ materi_id(FK)│
│ username    │       │ deskripsi       │       │ name         │
│ email       │       │ status          │       │ description  │
│ password    │       │ rating          │       └──────┬───────┘
│ born_place  │       │ image_url       │              │
│ born_date   │       │ content         │              │
│ photo       │       │ slug            │       ┌──────▼───────┐
│ google_sub  │       └─────────────────┘       │  questions   │
└──────┬──────┘                                 │──────────────│
       │                                        │ id (PK)      │
       │         ┌──────────────────┐           │ topic_id (FK)│
       │         │  user_progress   │           │ content      │
       │         │──────────────────│           │ answer       │
       ├────────▶│ user_id (FK)     │           │ difficulty   │
       │         │ topic_id (FK)    │           └──────────────┘
       │         │ correct_answers  │
       │         │ questions_answered│
       │         └──────────────────┘
       │
       │         ┌─────────────────────┐
       │         │ user_analysis_results│
       ├────────▶│ user_id (FK)        │
       │         │ materi_id (FK)      │
       │         │ score               │
       │         │ total_questions     │
       │         │ correct_answers     │
       │         │ incorrect_answers   │
       │         │ completion_date     │
       │         │ feedback            │
       │         └─────────────────────┘
       │
       │         ┌──────────────────┐    ┌───────────────────┐
       │         │  conversations   │    │   chat_messages   │
       ├────────▶│ id (PK, varchar) │───▶│ conversation_id   │
       │         │ user_id (FK)     │    │ role (user/asst)  │
       │         │ title            │    │ content           │
       │         │ created_at       │    │ created_at        │
       │         └──────────────────┘    └───────────────────┘
       │
       │         ┌──────────────────────┐
       └────────▶│ password_reset_codes │
                 │ password_reset_tokens│
                 └──────────────────────┘

Tabel lain:
  testimonials  — Pesan dari pengguna di halaman home
  feedback      — Laporan/saran dari pengguna
```

### Ringkasan 11 Tabel

| Tabel | Fungsi |
|-------|--------|
| `users` | Data akun pengguna |
| `daftar_materi` | Katalog materi belajar |
| `topics` | Topik-topik dalam setiap materi |
| `questions` | Soal latihan per topik (easy/medium/hard) |
| `user_progress` | Progres latihan user per topik |
| `user_analysis_results` | Hasil analisis belajar user |
| `conversations` | Sesi percakapan AI |
| `chat_messages` | Pesan dalam percakapan AI |
| `password_reset_codes` | Kode OTP reset password |
| `password_reset_tokens` | Token reset password |
| `testimonials` | Testimoni di halaman home |
| `feedback` | Feedback & laporan user |

---

## 🔐 Alur Autentikasi

### Login Biasa
```
User isi form → POST /auth/register_user
  → Hash password (Werkzeug) → Simpan ke DB
  → Redirect ke login

User isi form → POST /auth/login_user
  → Cek DB → Cocokkan hash → Set session['user_id']
  → Redirect ke /user/dashboard
```

### Google OAuth
```
User klik "Sign in with Google"
  → Google mengirim id_token
  → Backend verifikasi token dengan google-auth
  → Ambil/buat user berdasarkan google_sub
  → Set session['user_id']
```

### Admin Login
```
POST /admin/login_admin
  → Cocokkan ADMIN_USERNAME & ADMIN_PASSWORD (dari .env)
  → Set session['admin_logged_in']
  → Redirect ke /admin/dashboard_admin
```

### Dekorator Akses
| Dekorator | Fungsi |
|-----------|--------|
| `@user_required` | Wajib login sebagai user |
| `@admin_required` | Wajib login sebagai admin |
| `@login_required(role='user')` | Fleksibel role-based |

---

## 🔧 Modul Backend

### `Back_End/__init__.py` — App Factory
- Menginisialisasi semua Flask extensions (SQLAlchemy, CSRF, CORS, Limiter)
- Mendaftarkan semua Blueprint
- Menyetel security headers (`X-Frame-Options`, `X-Content-Type-Options`, dll.)
- Menjalankan `init_db_schema()` saat startup

### `Back_End/routes/auth.py` — Autentikasi
- `GET/POST /auth/register_user` — Form registrasi + upload foto profil
- `GET/POST /auth/login_user` — Login dengan password
- `POST /auth/google_login` — Google OAuth sign-in
- `POST /auth/forget_password` — Kirim kode OTP via email
- `POST /auth/reset_password` — Reset password dengan kode OTP
- `GET /auth/logout` — Hapus session

### `Back_End/routes/user.py` — Area User
- `GET /user/dashboard` — Dashboard utama user
- `GET /user/options` — Menu pilihan fitur
- `GET/POST /user/pengaturan` — Update profil & foto
- `GET /user/analyze` — Halaman analisis hasil belajar
- `GET /user/progres` — Visualisasi progres belajar
- `GET /user/calculator` — Kalkulator interaktif
- `GET /user/feedback` — Form feedback

### `Back_End/routes/admin.py` — Panel Admin
- `GET/POST /admin/login_admin` — Login admin
- `GET /admin/dashboard_admin` — Dashboard statistik admin
- `GET /admin/manage_users` — Lihat & cari daftar user
- `GET/POST /admin/add_materi` — Tambah materi baru
- `POST /admin/edit_materi/<id>` — Edit materi
- `POST /admin/delete_materi/<id>` — Hapus materi
- `GET /admin/manage_feedback` — Kelola feedback user
- `GET /admin/crime_detection` — Monitor log keamanan
- `GET /admin/export_database` — Export data ke Excel/CSV

### `Back_End/routes/ai.py` — AI Chat
- `GET/POST /api/ai/chat` — Kirim pesan, terima balasan Gemini
- `GET /api/ai/conversations` — Daftar riwayat percakapan
- `GET /api/ai/conversations/<id>` — Isi satu percakapan
- `POST /api/ai/conversations/<id>/messages` — Tambah pesan ke percakapan
- `DELETE /api/ai/conversations/<id>` — Hapus percakapan

### `Back_End/ai/chat_api.py` — Integrasi AI
- Menghubungi **Google Gemini API** (`gemini-1.5-flash`)
- Fallback ke **Ollama** (local LLM, model `phi4-mini`)
- System prompt: *"Asisten matematika yang membantu langkah demi langkah"*

### `Back_End/routes/materi.py` — Konten Materi
- `GET /user/materi` — Daftar semua materi
- `GET /user/materi/<slug>` — Detail satu materi

### `Back_End/routes/latihan.py` — Sesi Latihan
- `GET /user/latihan/<topic_id>` — Mulai sesi latihan soal
- Soal diambil per topik dari tabel `questions`
- Progres disimpan ke `user_progress`

---

## 🖥️ Halaman Frontend

### Halaman Publik
| URL | Template | Deskripsi |
|-----|----------|-----------|
| `/` | `home.html` | Landing page dengan testimonial & statistik |
| `/tentang` | `about.html` | Halaman tentang MathThon |
| `/privasi_kebijakan` | `privacy.html` | Kebijakan privasi |
| `/syarat_dan_ketentuan` | `terms.html` | Syarat & ketentuan |

### Halaman User (Login Required)
| URL | Template | Deskripsi |
|-----|----------|-----------|
| `/user/dashboard` | `dashboard_user.html` | Dashboard utama |
| `/user/options` | `options.html` | Pilihan fitur |
| `/user/materi` | `materi_user.html` | Daftar materi belajar |
| `/user/latihan/<id>` | `latihan_soal_user.html` | Soal latihan |
| `/api/ai/chat` | `ai_feature_user.html` | AI tutor chat |
| `/user/analyze` | `analyze_user.html` | Analisis hasil |
| `/user/progres` | `progres_user.html` | Grafik progres |
| `/user/calculator` | `calculator.html` | Kalkulator |
| `/user/feedback` | `feedback_user.html` | Kirim feedback |
| `/user/pengaturan` | `pengaturan.html` | Pengaturan akun |

### Halaman Admin
| URL | Template | Deskripsi |
|-----|----------|-----------|
| `/admin/login_admin` | `login_admin.html` | Login admin |
| `/admin/dashboard_admin` | `dashboard.html` | Statistik platform |
| `/admin/manage_users` | `manage_users.html` | Kelola pengguna |
| `/admin/manage_materi` | `manage_materi.html` | Kelola materi |
| `/admin/manage_feedback` | `manage_feedback.html` | Kelola feedback |
| `/admin/crime_detection` | `crime_detection.html` | Monitor keamanan |
| `/admin/export_database` | `export_database.html` | Export data |

---

## 🛡️ Keamanan

MathThon mengimplementasikan lapisan keamanan berlapis:

### 1. Security Headers (setiap response)
```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
```

### 2. SQL Injection Detection
- RegEx patterns mendeteksi: `UNION SELECT`, `DROP TABLE`, `' OR '1'='1`, dll.
- Request langsung ditolak jika pola ditemukan dalam input

### 3. XSS Prevention
- Input dibersihkan dengan library `bleach`
- CSRF Protection via Flask-WTF pada semua form POST

### 4. Rate Limiting
- Global via **Flask-Limiter**
- Respons 429 dengan halaman error khusus

### 5. Enkripsi Data (Fernet)
- Kunci enkripsi simetris tersimpan di `secret.key`
- Fungsi: `encrypt_data()`, `decrypt_data()`, `encrypt_json_data()`
- Digunakan untuk data sensitif antar-modul

### 6. File Integrity Monitoring
- Hash SHA-256 dihitung untuk file-file kritis
- Deteksi perubahan yang tidak sah (anti-ransomware)

### 7. Upload Validation
- Batas ukuran: **2MB**
- MIME type yang diizinkan: PNG, JPEG, PDF, DOCX
- Opsional: scan ClamAV (jika daemon aktif)

### 8. Log Keamanan
- `security_logs.json` — log terstruktur (JSON)
- `security.log` — log teks biasa
- Dapat dimonitor via halaman `/admin/crime_detection`

---

## 🔌 API Endpoints

### AI Chat
```
POST /api/ai/chat
Body: { "messages": [...], "conversation_id": "..." }
Response: { "response": "...", "conversation_id": "..." }

GET    /api/ai/conversations                    # Daftar percakapan user
GET    /api/ai/conversations/<id>               # Pesan dalam 1 percakapan
POST   /api/ai/conversations/<id>/messages      # Kirim pesan
DELETE /api/ai/conversations/<id>               # Hapus percakapan
```

### Data & Visualisasi
```
GET /api/education_data             # Data CSV pendidikan Indonesia (JSON)
GET /chart/education.png            # Chart matplotlib
```

### Feedback
```
POST /api/feedback/submit           # Kirim feedback
```

---

## ⚙️ Konfigurasi & Environment

Buat file `.env` di root proyek berdasarkan `.env.example`:

```env
# Flask
FLASK_ENV=development
SECRET_KEY=your-very-secret-key-here
PORT=5000

# Database MySQL
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_db_password
MYSQL_DB=maththon_db

# Google Gemini AI
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-1.5-flash

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com

# Email SMTP (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_secure_admin_password

# CORS
ALLOWED_ORIGINS=http://localhost:5000,http://127.0.0.1:5000

# Optional: Ollama (local LLM)
MODEL_NAME=phi4-mini:latest
```

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.10+
- MySQL Server (running)
- Database `maththon_db` sudah dibuat

### Langkah-langkah

**1. Masuk ke folder proyek:**
```bash
cd E:\MathThon
```

**2. Aktifkan virtual environment:**
```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Jika muncul error execution policy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Buat file `.env`:**
```bash
copy .env.example .env
# Lalu isi nilai-nilainya
```

**5. Buat database MySQL:**
```sql
CREATE DATABASE maththon_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**6. Jalankan aplikasi:**
```bash
python app.py
```

**7. Buka browser:**
```
http://localhost:5000
```

> 💡 Saat development, Ngrok otomatis membuat tunnel publik dan menampilkan URL-nya di terminal.

### Seed Data (Opsional)
Untuk mengisi data awal materi & soal:
```bash
python -c "from Back_End.routes.seed_daftar_materi import seed; seed()"
python -c "from Back_End.routes.seed_soal_latihan import seed; seed()"
```

---

## 📦 Deployment

### Vercel (Serverless)
File `vercel.json` sudah dikonfigurasi. Deploy dengan:
```bash
vercel --prod
```
> ⚠️ Vercel tidak mendukung MySQL native. Gunakan PlanetScale atau Railway untuk database.

### VPS / Server Tradisional
```bash
# Production mode
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:8000 "Back_End:create_app()"
```

> Pastikan semua variabel `.env` di-set di server (jangan upload file `.env` ke repo publik).

---

## 🛠️ Tech Stack

### Backend
| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| Python | 3.10+ | Bahasa utama |
| Flask | 2.3.3 | Web framework |
| Flask-SQLAlchemy | 3.0.5 | ORM database |
| Flask-CORS | 4.0.0 | Cross-origin requests |
| Flask-Limiter | 3.5.0 | Rate limiting |
| Flask-WTF | latest | CSRF protection |
| Werkzeug | 2.3.7 | Password hashing, utils |
| mysql-connector-python | 9.0.0 | Koneksi MySQL |
| google-generativeai | 0.3.2 | Gemini AI API |
| google-auth | 2.23.4 | Google OAuth |
| cryptography (Fernet) | latest | Enkripsi data |
| pandas | latest | Analisis data CSV |
| matplotlib | latest | Visualisasi grafik |
| pyngrok | 7.1.1 | Dev tunnel |
| gunicorn | 21.2.0 | Production server |
| bleach | latest | XSS sanitization |

### Frontend
| Teknologi | Kegunaan |
|-----------|----------|
| HTML5 + Jinja2 | Template engine |
| CSS3 (Vanilla) | Styling & animasi |
| JavaScript (Vanilla) | Interaktivitas |
| Google Fonts | Tipografi |

### Database
| Teknologi | Kegunaan |
|-----------|----------|
| MySQL | Database utama (11 tabel) |

### Layanan Eksternal
| Service | Kegunaan |
|---------|----------|
| Google Gemini | AI chat tutor |
| Google OAuth 2.0 | Login with Google |
| Gmail SMTP | Kirim email OTP |
| Ngrok | Dev tunnel publik |
| Ollama (opsional) | Local LLM fallback |

---

*Dokumentasi ini dibuat berdasarkan analisis kode sumber MathThon.*
