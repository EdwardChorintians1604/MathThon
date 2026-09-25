# 🔐 Sistem Reset Password Sederhana - MathThon

## 📋 Ringkasan Perubahan

Sistem reset password telah diperbaharui dari sistem token rumit menjadi **sistem kode verifikasi 6 digit yang sederhana dan user-friendly**.

---

## ✨ Fitur Baru

### **Step 1: Verifikasi Email**
- User masukkan email → sistem kirim kode 6 digit ke email
- Kode berlaku **10 menit**
- User tidak perlu klik link atau token rumit

### **Step 2: Verifikasi Kode + Reset Password**
- User input kode 6 digit yang diterima
- User langsung input password baru + konfirmasi
- Validasi password real-time
- Timer countdown menampilkan sisa waktu kode

### **Keamanan**
- ✅ Kode OTP 6 digit yang random
- ✅ Kode otomatis kadaluarsa setelah 10 menit
- ✅ Validasi password minimal 6 karakter
- ✅ Password harus sama saat konfirmasi
- ✅ CSRF protection pada semua form

---

## 🗄️ Database Setup

### **Buat Tabel Baru**

Jalankan query SQL berikut di phpMyAdmin atau CLI:

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### **Hapus Tabel Lama (Opsional)**

Jika sudah tidak perlu sistem token lama:

```sql
DROP TABLE IF EXISTS password_reset_tokens;
```

---

## 🔧 Konfigurasi Email

Pastikan file `.env` memiliki konfigurasi SMTP yang benar:

```env
# SMTP Configuration untuk Email
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

**Catatan untuk Gmail:**
- Gunakan **App Password** bukan password biasa
- Enable 2FA di akun Google Anda
- Generate App Password di: https://myaccount.google.com/apppasswords

---

## 📱 Flow Pengguna

```
1. User klik "Lupa Password" di halaman login
   ↓
2. User masukkan email → klik "Kirim Kode Verifikasi"
   ↓
3. Sistem kirim email dengan kode 6 digit
   ↓
4. User input kode yang diterima
   ↓
5. User input password baru + konfirmasi
   ↓
6. Klik "Reset Password"
   ↓
7. ✅ Password berhasil direset!
   ↓
8. User bisa login dengan password baru
```

---

## 🎨 UI/UX Improvements

- **Step Indicator**: Menunjukkan progress (Step 1 dari 2, Step 2 dari 2)
- **Timer Countdown**: Menampilkan sisa waktu kode berlaku
- **Visual Feedback**: Icon dan warna untuk status sukses/error
- **Input Validation**: Real-time validation untuk password match
- **Auto-focus**: Field input berpindah otomatis saat kode selesai
- **Responsive Design**: Optimal di mobile, tablet, desktop

---

## 📧 Email Template

Kode verifikasi dikirim dengan format:

```
Halo,

Anda menerima email ini karena ada permintaan reset password untuk akun Anda di MathThon.

🔑 KODE VERIFIKASI ANDA:
[6-DIGIT-CODE]

⏱️ Kode ini berlaku selama 10 menit.

Jika Anda tidak meminta reset password, abaikan email ini.

Terima kasih,
Tim MathThon
```

---

## 🛡️ Security Features

| Feature | Deskripsi |
|---------|-----------|
| **CSRF Protection** | Token CSRF pada setiap form |
| **OTP Code** | 6 digit random, sulit ditebak |
| **Time Expiry** | Kode hanya berlaku 10 menit |
| **Rate Limiting** | Cegah brute force (via security middleware) |
| **Password Hashing** | Menggunakan werkzeug.security |
| **Email Verification** | Hanya email terdaftar yang bisa reset |
| **DB Index** | Optimisasi query dengan index |

---

## 🔍 Testing Checklist

- [ ] Kode email berhasil dikirim
- [ ] Kode 6 digit muncul di email
- [ ] Kode hanya berlaku 10 menit
- [ ] Validasi kode 6 digit benar-benar numeric
- [ ] Password harus sama saat konfirmasi
- [ ] Password minimal 6 karakter
- [ ] Setelah reset, user bisa login dengan password baru
- [ ] Kode otomatis dihapus setelah digunakan
- [ ] Bekerja di mobile dan desktop

---

## 🚀 Deployment Notes

1. **Database Migration**: Jalankan SQL script untuk create table
2. **Email Config**: Pastikan MAIL_USERNAME dan MAIL_PASSWORD di .env
3. **Testing**: Test kirim email sebelum production
4. **Backup**: Backup database sebelum migrate

---

## 📞 Troubleshooting

### **Email tidak terkirim**
- Cek MAIL_USERNAME dan MAIL_PASSWORD di .env
- Cek SMTP server configuration
- Cek app logs untuk error message

### **Kode tidak valid**
- Pastikan user input kode dengan benar (6 digit)
- Pastikan kode belum expire (10 menit)
- Cek database apakah kode tersimpan

### **Password tidak bisa direset**
- Cek apakah user email terdaftar
- Cek CSRF token ada di form
- Lihat browser console untuk error message

---

## 📚 File yang Diubah

- `Front_End/templates/user/forget_password_user.html` ✅ Redesign UI/UX
- `Back_End/__init__.py` ✅ Logic baru untuk kode verifikasi
- Database: Tabel baru `password_reset_codes` ✅

---

**Sistem reset password sudah diperbaharui dan siap digunakan! 🎉**
