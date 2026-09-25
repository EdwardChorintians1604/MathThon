## 🔍 DEBUGGING CHECKLIST - Reset Password System

### Problem: "Terjadi kesalahan tak terduga"

---

### ✅ Langkah 1: Verifikasi Database Setup
- [ ] Tabel `password_reset_codes` sudah dibuat?
  - Cek di phpMyAdmin atau jalankan:
  ```sql
  SHOW TABLES LIKE 'password_reset_codes';
  ```

- [ ] Jika tabel belum ada, aplikasi akan auto-create saat startup
  - Restart aplikasi: `python app.py`
  - Atau manual run:
  ```sql
  CREATE TABLE IF NOT EXISTS password_reset_codes (
      id INT AUTO_INCREMENT PRIMARY KEY,
      user_id INT NOT NULL UNIQUE,
      code VARCHAR(10) NOT NULL,
      expires_at DATETIME NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
      INDEX idx_user_id (user_id),
      INDEX idx_expires_at (expires_at)
  );
  ```

---

### ✅ Langkah 2: Verifikasi Email Configuration
- [ ] File `.env` ada di folder root?
  
- [ ] Konfigurasi email sudah benar?
  ```env
  MAIL_SERVER=smtp.gmail.com
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=your-email@gmail.com
  MAIL_PASSWORD=your-app-password
  ```

- [ ] Jika pakai Gmail:
  - Enable 2-Factor Authentication
  - Generate App Password di: https://myaccount.google.com/apppasswords
  - Use the 16-character password di MAIL_PASSWORD

---

### ✅ Langkah 3: Test Email Functionality
- [ ] Buka aplikasi console/terminal
- [ ] Coba kirim test email:
  ```python
  from app import create_app, send_email
  app = create_app()
  with app.app_context():
      result = send_email(
          "Test Email",
          "your-email@gmail.com",
          "recipient@gmail.com",
          "Test message"
      )
      print(f"Email sent: {result}")
  ```

---

### ✅ Langkah 4: Check Application Logs
- [ ] Buka application logs untuk melihat error detail
- [ ] Terminal output saat running `python app.py`
- [ ] Error message akan lebih spesifik sekarang

---

### ✅ Langkah 5: Manual Testing Flow

1. **Step 1 - Kirim Kode:**
   - Buka: `/user/forget_password_user`
   - Input email yang terdaftar
   - Klik "Kirim Kode Verifikasi"
   - Cek error message di screen
   - Cek email inbox

2. **Step 2 - Verifikasi + Reset:**
   - Input kode yang diterima (6 digit)
   - Input password baru (minimal 6 karakter)
   - Konfirmasi password
   - Klik "Reset Password"

3. **Verifikasi Success:**
   - Redirect ke login page
   - Coba login dengan password baru

---

### 🐛 Common Issues & Solutions

#### Issue: "Sistem belum disetup. Hubungi admin untuk run: create_password_reset_table.sql"
**Solution:** 
- Tabel belum dibuat
- Restart aplikasi atau manual run SQL script

#### Issue: "Email tidak terkirim"
**Solution:**
- Cek MAIL_USERNAME dan MAIL_PASSWORD di .env
- Untuk Gmail, gunakan App Password, bukan password biasa
- Cek 2FA enabled di Google Account

#### Issue: "Kode verifikasi tidak valid"
**Solution:**
- Pastikan kode 6 digit numeric
- Pastikan kode belum expired (10 menit)
- Copy-paste kode dari email, jangan manual type

---

### 📊 Database Query untuk Debugging

#### Cek password_reset_codes table:
```sql
SELECT * FROM password_reset_codes;
```

#### Cek user by email:
```sql
SELECT id, email FROM users WHERE email = 'test@example.com';
```

#### Cek kode untuk user tertentu:
```sql
SELECT * FROM password_reset_codes WHERE user_id = 1;
```

#### Hapus kode yang expired (manual cleanup):
```sql
DELETE FROM password_reset_codes WHERE expires_at < NOW();
```

---

### 📝 Application Configuration Check

File: `.env`
```
FLASK_ENV=development
SECRET_KEY=your-secret-key
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

---

### ✨ Testing Checklist Final

- [ ] Database tabel `password_reset_codes` ada
- [ ] `.env` email config benar
- [ ] Email bisa terkirim (test dulu)
- [ ] User email terdaftar di database
- [ ] Flow Step 1 → Step 2 berjalan
- [ ] Kode diterima di email
- [ ] Password baru bisa di-reset
- [ ] Login dengan password baru berhasil

---

**Jika masih error, output log message akan lebih detail sekarang untuk membantu debugging! 🎯**
