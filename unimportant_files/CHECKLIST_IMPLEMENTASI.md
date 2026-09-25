# ✅ CHECKLIST IMPLEMENTASI - SISTEM MATERI DINAMIS

## 🎯 Fase 1: Setup Database & Backend
- [x] Tambah field `slug`, `image_url`, `content` ke tabel `daftar_materi`
- [x] Buat route Flask `/api/materi` untuk fetch semua materi
- [x] Buat route Flask `/user/materi/<slug>` untuk detail materi
- [x] Update route `/admin/add_materi` untuk input slug + content
- [x] Update route `/admin/edit_materi` untuk edit slug + content

## 🎨 Fase 2: Frontend Templates
- [x] Buat template `detail_materi.html` dengan render Markdown + LaTeX
- [x] Update `materi_user.html` untuk gunakan slug di link
- [x] Update form `add_materi.html` dengan textarea content
- [x] Update form `edit_materi.html` dengan textarea content
- [x] Tambah styling untuk h1, h2, h3, code, blockquote, dll

## 📋 Fase 3: Testing & Documentation
- [x] Buat file `update_materi_table.sql` untuk migration
- [x] Buat file `PANDUAN_MATERI_DINAMIS.md` sebagai dokumentasi lengkap
- [x] Buat file `CHECKLIST_IMPLEMENTASI.md` ini

---

## 🔧 YANG HARUS ANDA LAKUKAN SEKARANG

### 1. **UPDATE DATABASE** (Critical)
```bash
# Di MySQL/MariaDB, jalankan query dari:
# Back_End/update_materi_table.sql
```

Atau buka MySQL Workbench dan jalankan:
```sql
ALTER TABLE daftar_materi ADD COLUMN IF NOT EXISTS slug VARCHAR(255) UNIQUE;
ALTER TABLE daftar_materi ADD COLUMN IF NOT EXISTS image_url VARCHAR(255);
ALTER TABLE daftar_materi ADD COLUMN IF NOT EXISTS content LONGTEXT;
ALTER TABLE daftar_materi MODIFY COLUMN rating INT DEFAULT 0;
```

### 2. **RESTART FLASK SERVER**
```bash
# Di terminal PowerShell, di folder e:\MathThon
python run.py
```

### 3. **TEST ADMIN FORM**
- Buka browser: `http://localhost:5000/admin/dashboard`
- Login dengan akun admin
- Klik "Manage Materi" → "Tambah Materi Baru"
- Pastikan form ada field baru: `slug`, `image_url`, `content`

### 4. **TAMBAH MATERI CONTOH**
```
Judul: Aljabar
Slug: aljabar  ← PENTING! Harus unik, lowercase, no spaces
Deskripsi: Belajar konsep dasar aljabar
Status: active
Rating: 4
Image URL: (opsional)
Content:
# Aljabar

## Pengertian
Aljabar adalah cabang matematika.

## Rumus
Persamaan linear: $ax + b = 0$

Solusi:
$$x = -\frac{b}{a}$$
```

### 5. **TEST USER PAGE**
- Buka `http://localhost:5000/user/materi` atau `/user/materi_user_page`
- Materi "Aljabar" harus muncul di grid
- Klik "Pelajari Materi"
- Halaman detail harus:
  - ✅ Tampil judul materi
  - ✅ Tampil deskripsi
  - ✅ Render Markdown dengan styling
  - ✅ Render LaTeX rumus $ax + b = 0$ dan $$x = -\frac{b}{a}$$
  - ✅ Punya sidebar navigasi
  - ✅ Ada tombol "Kembali ke Daftar Materi"

---

## 📁 FILE STRUCTURE SETELAH IMPLEMENTASI

```
MathThon/
├── Back_End/
│   ├── __init__.py                  ✅ Updated dengan 2 route baru
│   └── update_materi_table.sql      ✅ Created (migration script)
├── Front_End/
│   └── templates/
│       ├── admin/
│       │   ├── add_materi.html      ✅ Updated (form dengan content)
│       │   └── edit_materi.html     ✅ Updated (form dengan content)
│       └── user/
│           ├── detail_materi.html   ✅ Created (template detail)
│           └── materi_user.html     ✅ Updated (link ke slug)
├── PANDUAN_MATERI_DINAMIS.md        ✅ Created (dokumentasi)
└── CHECKLIST_IMPLEMENTASI.md        ✅ Created (file ini)
```

---

## 🚨 JIKA ADA ERROR

### Error: "Table 'daftar_materi' doesn't have column 'slug'"
**Solusi**: Jalankan SQL migration di step 1 di atas

### Error: "404 Not Found" saat klik "Pelajari Materi"
**Solusi**: 
- Pastikan slug sudah terisi di database
- Slug harus lowercase, no spaces (contoh: `aljabar`, `limit_dan_turunan`)

### Error: "Markdown/LaTeX tidak ter-render"
**Solusi**:
- Pastikan browser sudah load library marked.js dan KaTeX
- Refresh browser (Ctrl+Shift+R untuk hard refresh)
- Check console browser untuk error (F12)

### Error: "Photo tidak muncul"
**Solusi**:
- Gunakan URL lengkap: `https://example.com/image.jpg`
- Atau path relatif: `/static/images/image.jpg`

---

## 💡 TIPS PENGGUNAAN

### Format Markdown yang Paling Penting:
```markdown
# Judul Utama (warna biru, besar)
## Judul Bagian (warna hijau, sedang)
### Sub Judul (warna ungu, kecil)

Teks normal dengan paragraph spacing.

**Bold text** dan *italic text*

- Bullet point 1
- Bullet point 2

> Blockquote atau catatan penting

Rumus inline: $x^2 + y^2 = z^2$

Rumus block (centered):
$$\int_0^1 x \, dx = \frac{1}{2}$$
```

### Slug Rules:
- ✅ Gunakan huruf kecil: `aljabar` ✓
- ✅ Gunakan underscore untuk spasi: `limit_dan_turunan` ✓
- ❌ Jangan gunakan spasi: `limit dan turunan` ✗
- ❌ Jangan gunakan uppercase: `Aljabar` ✗
- ❌ Jangan gunakan karakter spesial: `aljabar!@#` ✗

---

## 📞 SUPPORT

Jika ada masalah:
1. Baca file `PANDUAN_MATERI_DINAMIS.md`
2. Check console browser (F12)
3. Check Flask terminal log
4. Verifikasi database dengan MySQL Workbench

---

**Status**: 🟢 READY TO USE
**Last Updated**: 5 January 2026
**Time to Setup**: ~5-10 minutes
**Difficulty**: Easy to Moderate
