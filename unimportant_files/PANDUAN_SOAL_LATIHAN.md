# Panduan Implementasi Soal Latihan Massal

## Daftar Isi
1. [Pengenalan Sistem](#pengenalan-sistem)
2. [Setup & Instalasi](#setup--instalasi)
3. [Cara Menggunakan Script Seed](#cara-menggunakan-script-seed)
4. [Cara Menambah Soal Manual](#cara-menambah-soal-manual)
5. [Import Soal dari CSV](#import-soal-dari-csv)
6. [Struktur Database](#struktur-database)
7. [API Endpoints](#api-endpoints)
8. [Troubleshooting](#troubleshooting)

---

## Pengenalan Sistem

Sistem ini memungkinkan Anda untuk:
- ✅ Menambah soal latihan dalam jumlah besar secara otomatis
- ✅ Menambah soal secara manual melalui admin panel
- ✅ Import soal dari file CSV
- ✅ Mengelola topik/bab untuk setiap materi
- ✅ Mengatur tingkat kesulitan (mudah, sedang, sulit)

---

## Setup & Instalasi

### 1. Verifikasi Database
Pastikan database Anda memiliki tabel-tabel berikut:
- `daftar_materi` - Tabel data materi
- `topics` - Tabel topik/bab
- `questions` - Tabel soal latihan
- `user_progress` - Tabel progress user

```sql
-- Contoh struktur minimal
CREATE TABLE daftar_materi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul_materi VARCHAR(255) NOT NULL,
    deskripsi TEXT,
    status ENUM('active', 'inactive') DEFAULT 'active'
);

CREATE TABLE topics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    materi_id INT NOT NULL,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    FOREIGN KEY (materi_id) REFERENCES daftar_materi(id) ON DELETE CASCADE
);

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    topic_id INT NOT NULL,
    content TEXT NOT NULL,
    answer VARCHAR(255) NOT NULL,
    difficulty ENUM('easy', 'medium', 'hard') NOT NULL,
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);
```

### 2. Verifikasi Environment Variables
Pastikan file `.env` berisi:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=maththon_db
```

---

## Cara Menggunakan Script Seed

### Method 1: Menjalankan Script Seed Otomatis

Script `seed_soal_latihan.py` akan membuat soal-soal otomatis untuk 3 materi:
- **Aljabar** (3 topik × 10 soal = 30 soal)
- **Matriks** (2 topik × 10 soal = 20 soal)  
- **Operasi Kabataku** (3 topik × 10 soal = 30 soal)

**Total: 80 soal siap digunakan!**

#### Langkah-langkah:

1.  Buka Terminal/PowerShell di folder project
```bash
cd e:\MathThon
```

2. Aktifkan virtual environment
```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Atau bash/cmd
source .venv/Scripts/activate
```

3. Jalankan script seed
```bash
python seed_soal_latihan.py
```

4. Lihat output:
```
============================================================
MEMULAI SEED SOAL LATIHAN KE DATABASE
============================================================

[ALJABAR]
  ✓ Materi 'Aljabar' dibuat
  └─ Persamaan Linear
    ✓ Topic 'Persamaan Linear' dibuat
      ✓ Ditambahkan 10 soal baru
  └─ Persamaan Kuadrat
    ...
```

5. Selesai! Database sudah terisi dengan soal-soal.

---

## Cara Menambah Soal Manual

### 1. Akses Admin Panel
```
http://localhost:5000/admin/add_soal_materi
```

### 2. Form Tambah Soal

#### Field yang harus diisi:
- **Materi**: Pilih materi (Aljabar, Matriks, dsb)
- **Topik**: Pilih topik dalam materi tersebut
- **Pertanyaan**: Soal yang akan ditanyakan
- **Jawaban**: Jawaban yang benar
- **Tingkat Kesulitan**: Easy / Medium / Hard

#### Contoh:
```
Materi: Aljabar
Topik: Persamaan Linear
Pertanyaan: Jika x + 5 = 12, berapa nilai x?
Jawaban: 7
Tingkat Kesulitan: Easy
```

### 3. Submit Form
Klik tombol **"Tambah Soal"** untuk menyimpan.

---

## Import Soal dari CSV

### Format CSV yang Diperlukan

```csv
content;answer;difficulty;topic_name
Berapakah 5 + 3?;8;easy;Penjumlahan dan Pengurangan
Selesaikan: x + 5 = 12;7;medium;Persamaan Linear
Berapa determinan matriks [1 2; 3 4]?;-2;hard;Matriks Dasar
```

**Delimiter**: Gunakan `;` (semicolon) atau `,` (comma)

**Kolom**:
1. **content** - Pertanyaan/soal
2. **answer** - Jawaban yang benar
3. **difficulty** - easy / medium / hard
4. **topic_name** - Nama topik

### Cara Upload:

1. Siapkan file CSV dengan format di atas
2. Buka halaman admin soal
3. Pada bagian **"Import Soal Massal"**, upload file CSV
4. Klik **"Import CSV"**
5. Tunggu proses selesai

---

## Struktur Database

### Tabel: daftar_materi
```
id (PK)          INT
judul_materi     VARCHAR(255)
deskripsi        TEXT
status           ENUM('active', 'inactive')
rating           VARCHAR(32)
```

### Tabel: topics
```
id (PK)          INT
name             VARCHAR(100) UNIQUE
description      TEXT
```

### Tabel: questions
```
id (PK)          INT
topic_id (FK)    INT → topics.id
content          TEXT
answer           VARCHAR(255)
difficulty       ENUM('easy', 'medium', 'hard')
created_at       TIMESTAMP
```

### Relasi
```
daftar_materi (1) ─── (n) topics ─── (n) questions
```

---

## API Endpoints

### GET Topics untuk Materi Tertentu
```
GET /api/topics/{materi_id}
Response: [
    {"id": 1, "name": "Persamaan Linear", "description": "..."},
    {"id": 2, "name": "Persamaan Kuadrat", "description": "..."}
]
```

### GET Soal untuk Topic Tertentu
```
GET /api/questions/{topic_id}
Response: [
    {"id": 1, "content": "...", "answer": "...", "difficulty": "easy"},
    ...
]
```

### POST Tambah Soal
```
POST /api/questions
Content-Type: application/json
{
    "topic_id": 1,
    "content": "Soal...",
    "answer": "Jawaban...",
    "difficulty": "easy"
}
```

### GET Statistik
```
GET /api/soal-stats/{materi_id}
Response: {
    "total_questions": 30,
    "total_topics": 3,
    "easy": 10,
    "medium": 12,
    "hard": 8
}
```

---

## Troubleshooting

### Problem: Script tidak bisa terhubung ke database

**Solusi:**
1. Verifikasi `.env` file sudah correct
```bash
cat .env  # atau type .env di Windows
```

2. Pastikan MySQL/database service sudah running
```bash
# Windows
net start MySQL80  # atau service name yang sesuai

# Linux/Mac
sudo systemctl start mysql
```

3. Test koneksi database
```bash
python -c "
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
try:
    conn = mysql.connector.connect(**{
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    })
    print('✓ Koneksi database berhasil!')
    conn.close()
except Exception as e:
    print(f'✗ Error: {e}')
"
```

### Problem: Soal tidak muncul di halaman latihan

**Solusi:**
1. Refresh browser dengan Ctrl+F5 (hard refresh)
2. Check bahwa topic sudah di-create:
```bash
# Di database
SELECT COUNT(*) FROM topics;
SELECT COUNT(*) FROM questions;
```

3. Verifikasi route `/user/latihan` sudah benar di backend

### Problem: Import CSV gagal

**Solusi:**
1. Pastikan format CSV benar (gunakan semicolon `;` sebagai delimiter)
2. Jangan ada header row - mulai langsung dari data
3. Make sure topik sudah ada dalam database sebelum import
4. Cek encoding file CSV (harus UTF-8)

### Problem: Tingkat kesulitan tidak terbaca

**Solusi:**
Pastikan hanya menggunakan:
- `easy` (mudah)
- `medium` (sedang)
- `hard` (sulit)

Jangan gunakan case berbeda seperti `Easy`, `EASY`, dsb.

---

## Contoh Data Seed

Script sudah menyediakan 80 soal untuk 3 materi:

### Aljabar (30 soal)
- Persamaan Linear (10 soal)
- Persamaan Kuadrat (10 soal)
- Fungsi dan Grafik (10 soal)

### Matriks (20 soal)
- Operasi Matriks (10 soal)
- Determinan dan Invers (10 soal)

### Operasi Kabataku (30 soal)
- Penjumlahan dan Pengurangan (10 soal)
- Perkalian dan Pembagian (10 soal)
- Operasi Campuran (10 soal)

Untuk menambah materi lain, edit file `seed_soal_latihan.py` dan tambahkan di `SOAL_DATA` dictionary.

---

## Tips & Best Practices

1. **Variasi Soal**: Buat soal dengan tingkat kesulitan yang berbeda
2. **Konsistensi Format Jawaban**: Gunakan format yang sama untuk soal serupa
3. **Validasi Jawaban**: Pastikan jawaban benar sebelum save
4. **Backup Database**: Selalu backup sebelum import massal
5. **Testing**: Test soal dengan user account sebelum publish

---

## Kontak & Support

Jika ada pertanyaan atau issue, lihat:
- File logs di `/logs`
- Database error messages
- Browser console (F12)

**Happy teaching! 🎓**
