# 🛡️ MathThon Security Guidelines

Dokumen ini menjelaskan praktik keamanan yang diimplementasikan dalam MathThon dan bagaimana cara menjaga sistem tetap aman di production.

---

## 🔒 Fitur Keamanan yang Sudah Diimplementasikan

1. **Environment Variables**: Tidak ada kredensial (API keys, DB password) yang disimpan di kode sumber. Semua diambil dari environment variables atau file `.env`.
2. **Secure Session**:
   - `SESSION_COOKIE_HTTPONLY=True`: Mencegah JavaScript mengakses cookies.
   - `SESSION_COOKIE_SECURE=True` (di production): Mengirim cookies hanya melalui HTTPS.
   - `SESSION_COOKIE_SAMESITE='Lax'`: Perlindungan dasar terhadap CSRF.
3. **Restricted CORS**: Hanya mengizinkan origin yang terdaftar (via `ALLOWED_ORIGINS`) untuk mengakses API.
4. **File Upload Security**:
   - Menggunakan `werkzeug.utils.secure_filename` untuk mencegah path traversal.
   - Path upload bersifat relatif terhadap root aplikasi (tidak ada hardcoded local path).
   - Validasi keberadaan file sebelum di-serve.
5. **Rate Limiting** (Ready to use): Menggunakan `flask-limiter` untuk mencegah brute force atau DoS pada API login/reset password.

---

## 🔴 Kewajiban Operator (Anda)

1. **JANGAN PERNAH** men-commit file `.env` ke Git. File ini sudah ada di `.gitignore`.
2. **Regenerate API Keys**: Jika Anda pernah tidak sengaja men-commit API keys ke publik, segera hapus keys tersebut dan buat baru di Google Cloud Console/Google AI Studio.
3. **Secret Key**: Gunakan `SECRET_KEY` yang panjang dan acak di production.
   - Cara generate: `python -c "import secrets; print(secrets.token_hex(32))"`
4. **Password Admin**: Gantilah password admin default di environment variables Anda sebelum deployment publik.
5. **Database Host**: Pastikan password database Anda kuat dan unik.

---

## 🛡️ Penanganan Insiden

Jika terjadi kebocoran data atau API key terekspos:

1. Ganti semua kunci rahasia (`SECRET_KEY`).
2. Cabut (Revoke) semua API keys yang terdampak di dashboard layanan terkait.
3. Update environment variables di hosting platform dengan kunci yang baru.
4. Restart aplikasi.

---

## 📋 Checklist Keamanan Sebelum Launching

- [ ] `FLASK_ENV` diatur ke `production`.
- [ ] `SECRET_KEY` menggunakan nilai acak yang unik.
- [ ] `SESSION_COOKIE_SECURE` bernilai `True`.
- [ ] Tidak ada password plaintext di file `.env`.
- [ ] Debug mode dimatikan (`debug=False`).
- [ ] Origin Google OAuth hanya berisi domain production.
