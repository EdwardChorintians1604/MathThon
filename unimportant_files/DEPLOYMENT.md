# 🚀 MathThon Deployment Guide

Dokumen ini berisi panduan lengkap untuk men-deploy aplikasi MathThon ke production environment agar bisa diakses oleh khalayak umum.

---

## 1. Persiapan Database Production

Aplikasi menggunakan MySQL. Jangan gunakan database lokal di production. Gunakan managed database service:

- **PlanetScale** (Recommended)
- **Railway MySQL**
- **Render MySQL**
- **Amazon RDS**

**Langkah:**

1. Buat database instance baru.
2. Catat host, user, password, dan nama database.
3. Jalankan skrip inisialisasi tabel jika perlu (aplikasi akan mencoba membuatnya otomatis saat start).

---

## 2. Persiapan Google OAuth

Anda perlu mengupdate konfigurasi Google Cloud Console:

1. Buka [Google Cloud Console](https://console.cloud.google.com/).
2. Pilih project MathThon.
3. Ke menu **APIs & Services** > **Credentials**.
4. Edit OAuth 2.0 Client ID.
5. Tambahkan domain production Anda di:
   - **Authorized JavaScript origins**: `https://yourdomain.com`
   - **Authorized redirect URIs**: `https://yourdomain.com/user/google_login`

---

## 3. Deployment ke Render.com (Recommended)

Render adalah platform termudah untuk aplikasi Flask.

1. **Connect GitHub**: Hubungkan repo Anda ke Render.
2. **New Web Service**:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT "Back_End:create_app()"`
3. **Konfigurasi Environment Variables**:
   Buka tab **Environment** dan tambahkan:
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: (Hasilkan kunci random panjang)
   - `GOOGLE_CLIENT_ID`: (Dari Google Console)
   - `GEMINI_API_KEY`: (Dari Google AI Studio)
   - `MYSQL_HOST`: (Host database production)
   - `MYSQL_USER`: (User database)
   - `MYSQL_PASSWORD`: (Password database)
   - `MYSQL_DB`: `maththon_db`
   - `ALLOWED_ORIGINS`: `https://yourdomain.com,https://www.yourdomain.com`

---

## 4. Deployment ke Railway.app

1. **New Project** > **Deploy from GitHub repo**.
2. Railway akan otomatis mendeteksi Flask.
3. Tambahkan environment variables yang sama seperti langkah di atas.
4. Pastikan `PORT` diatur secara otomatis oleh Railway.

---

## 5. Keamanan Pasca-Deployment

- **SSL/HTTPS**: Pastikan aplikasi diakses via HTTPS (Render dan Railway mengaktifkan ini secara otomatis).
- **API Keys**: Jangan pernah men-share API keys Anda ke publik atau commit ke Git.
- **Monitoring**: Cek tab **Logs** di platform hosting untuk memantau error.

---

## 🛠 Troubleshooting

- **Error 400: origin_mismatch**: Cek kembali domain di Google Cloud Console. Pastikan tidak ada `/` di akhir domain origin.
- **Database Connection Error**: Pastikan IP hosting sudah masuk allowed list di firewall database Anda.
- **ModuleNotFoundError: gunicorn**: Pastikan `gunicorn` tercantum di `requirements.txt`.
