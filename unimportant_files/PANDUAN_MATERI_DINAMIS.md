# Panduan Implementasi Sistem Materi Dinamis MathThon

## ✅ Yang Sudah Dikerjakan

### 1. **Database Schema**
- ✅ Tabel `daftar_materi` sudah ditambah field baru:
  - `slug` (VARCHAR 255, UNIQUE) - untuk URL yang SEO-friendly
  - `image_url` (VARCHAR 255) - untuk gambar header materi
  - `content` (LONGTEXT) - untuk menyimpan isi materi dalam Markdown/LaTeX

### 2. **Backend (Flask Routes)**
- ✅ **Route `/api/materi`** - API endpoint untuk fetch semua materi
- ✅ **Route `/user/materi/<slug>`** - Halaman detail materi berdasarkan slug
  - Hanya tampil jika status = 'active'
  - Include data user untuk layout sidebar

### 3. **Frontend (Templates)**
- ✅ **detail_materi.html** - Template untuk menampilkan detail materi
  - Render Markdown dengan library `marked.js`
  - Render LaTeX rumus dengan library `KaTeX`
  - Responsive design dengan sidebar konsisten
  - Styling otomatis untuk h1, h2, h3, p, code, blockquote, dll

- ✅ **materi_user.html** - Link "Pelajari Materi" sudah update
  - Sebelum: `/user/materi/judul_materi`
  - Sesudah: `/user/materi/{{ materi.slug }}`

- ✅ **add_materi.html** - Form untuk tambah materi
  - Input field: judul_materi, slug, deskripsi, status, rating, image_url, content
  - Textarea besar untuk Markdown/LaTeX content

- ✅ **edit_materi.html** - Form untuk edit materi
  - Sama seperti add_materi, dengan field yang sudah terisi

---

## 📋 Langkah-langkah Implementasi

### Step 1: Update Database
Jalankan perintah SQL di `Back_End/update_materi_table.sql`:

```sql
-- Jalankan di MySQL/MariaDB
ALTER TABLE daftar_materi ADD COLUMN IF NOT EXISTS slug VARCHAR(255) UNIQUE;
ALTER TABLE daftar_materi ADD COLUMN IF NOT EXISTS image_url VARCHAR(255);
ALTER TABLE daftar_materi ADD COLUMN IF NOT EXISTS content LONGTEXT;
ALTER TABLE daftar_materi MODIFY COLUMN rating INT DEFAULT 0;
```

### Step 2: Restart Flask Server
```bash
# Terminal di e:\MathThon
python run.py
```

### Step 3: Tambah Materi via Admin Panel
1. Buka `/admin/dashboard`
2. Klik "Manage Materi" → "Tambah Materi Baru"
3. Isi field:
   - **Judul Materi**: Aljabar
   - **Slug**: aljabar (penting! ini untuk URL)
   - **Deskripsi**: Pelajari konsep dasar aljabar
   - **Status**: active
   - **Rating**: 4
   - **URL Gambar**: https://example.com/aljabar.jpg (opsional)
   - **Isi Materi**: Tulis dalam Markdown + LaTeX

### Step 4: Format Content dengan Markdown + LaTeX

**Contoh:**
```markdown
# Aljabar

## Pengertian
Aljabar adalah cabang matematika yang mempelajari struktur dan operasi.

## Persamaan Linear
Bentuk umum: $ax + b = 0$

Solusi:
$$x = -\frac{b}{a}$$

### Contoh Soal
Tentukan $x$ dari $2x + 3 = 7$

**Jawab:**
- $2x = 7 - 3$
- $2x = 4$
- $x = 2$

---

## Sistem Persamaan Linear

> **Catatan**: Gunakan KaTeX untuk rumus kompleks!

Matriks:
$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}$$
```

---

## 🎨 Format Markdown yang Didukung

| Element | Markdown | Render |
|---------|----------|--------|
| Heading 1 | `# Text` | Besar, warna biru |
| Heading 2 | `## Text` | Sedang, warna hijau |
| Heading 3 | `### Text` | Kecil, warna ungu |
| Bold | `**Text**` | **Text** |
| Italic | `*Text*` | *Text* |
| Code | `` `code` `` | `code` |
| List | `- Item` | • Item |
| Blockquote | `> Text` | Kutipan dengan border |
| Link | `[Text](url)` | Hyperlink |
| Inline Math | `$x^2$` | x² (inline) |
| Block Math | `$$x^2$$` | x² (centered) |

---

## 🔧 LaTeX Syntax Umum untuk Matematika

```latex
# Operasi Dasar
$a + b$           % Penjumlahan
$a - b$           % Pengurangan
$a \times b$      % Perkalian
$\frac{a}{b}$     % Pembagian

# Pangkat dan Akar
$x^2$             % Kuadrat
$\sqrt{x}$        % Akar kuadrat
$\sqrt[n]{x}$     % Akar ke-n

# Integral dan Turunan
$\int_0^1 x dx$   % Integral tertentu
$\frac{dy}{dx}$   % Turunan

# Matriks
$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$

# Fraction dan Kombinasi
$\frac{a}{b}$     % Pecahan
$\binom{n}{k}$    % Kombinasi
```

---

## 🧪 Testing

1. **Tambah Materi via Admin**:
   - Pergi ke `/admin/dashboard`
   - Manage Materi → Tambah Materi
   - Isi form dan submit

2. **Lihat di User Dashboard**:
   - Pergi ke `/user/materi` atau `/user/materi_user_page`
   - Materi akan muncul di grid
   - Klik "Pelajari Materi"

3. **Verifikasi Render**:
   - Markdown harus ter-render (heading, bold, italic, dll)
   - LaTeX rumus harus tampil rapi ($x^2$, $$\int$$ dll)
   - Sidebar, navbar harus konsisten
   - Desain harus responsive

---

## 📂 File yang Sudah Dimodifikasi

- ✅ `Back_End/__init__.py` - Route baru + API endpoint
- ✅ `Front_End/templates/user/detail_materi.html` - Template detail
- ✅ `Front_End/templates/user/materi_user.html` - Update link slug
- ✅ `Front_End/templates/admin/add_materi.html` - Form tambah dengan content
- ✅ `Front_End/templates/admin/edit_materi.html` - Form edit dengan content
- ✅ `Back_End/update_materi_table.sql` - Migration script

---

## ⚠️ Troubleshooting

### Rumus LaTeX tidak tampil
- Pastikan content dimulai dengan `$` atau `$$`
- Contoh: `$x^2 + y^2 = z^2$` atau `$$\int_0^1 x dx$$`

### Markdown tidak ter-render
- Pastikan tidak ada HTML di dalam content
- Gunakan markdown syntax, bukan HTML tags

### Link 404 saat klik "Pelajari Materi"
- Pastikan field `slug` sudah terisi di database
- Slug tidak boleh ada spasi, gunakan underscore
- Contoh slug yang benar: `aljabar`, `limit_dan_turunan`, `integral_tak_tentu`

### Gambar tidak muncul
- Pastikan `image_url` adalah URL lengkap: `https://...`
- Atau gunakan path relatif ke folder static: `/static/images/aljabar.jpg`

---

## 🚀 Next Steps (Opsional)

1. **Categories**: Tambah field `kategori` untuk mengelompokkan materi
2. **Tags**: Sistem tag untuk pencarian lebih baik
3. **Comments**: User bisa komentar di halaman materi
4. **Rating dari User**: User bisa rate materi
5. **Completion Tracking**: Track materi mana yang sudah user baca
6. **PDF Export**: Download materi sebagai PDF
7. **Video Integration**: Embed video YouTube di materi

---

**Status**: ✅ SIAP DIGUNAKAN
**Last Updated**: 5 Januari 2026
