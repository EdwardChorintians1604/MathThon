# Setup & Usage Guide: Soal Latihan System

## ✅ System Status

All components are now **ready to use**:
- ✅ Backend API routes added to `Back_End/__init__.py`
- ✅ Admin panel HTML created at `Front_End/templates/admin/add_soal_materi.html`
- ✅ Seed script ready at `seed_soal_latihan.py`
- ✅ Database schema contains tables: `daftar_materi`, `topics`, `questions`

---

## 🚀 Quick Start (5 minutes)

### Step 1: Activate Virtual Environment
```powershell
cd e:\MathThon
.venv\Scripts\Activate.ps1
```

### Step 2: Run Seed Script (Generate 80 Questions)
```powershell
python seed_soal_latihan.py
```

**Output Expected:**
```
✓ Connected to database
✓ Creating/Getting materis...
✓ Seeding questions...
✓ Database seeding completed!

Statistics:
- Total Materis: 3
- Total Topics: 8
- Total Questions: 80
```

### Step 3: Start Flask Server
```powershell
python app.py
```

### Step 4: Access Admin Panel
Open browser: `http://localhost:5000/admin/add_soal_materi`

---

## 📊 What Gets Created

### 3 Materis (Materials):
1. **Aljabar** (30 soal)
   - Persamaan Linear (10 soal)
   - Persamaan Kuadrat (10 soal)
   - Fungsi dan Grafik (10 soal)

2. **Matriks** (20 soal)
   - Operasi Matriks (10 soal)
   - Determinan dan Invers (10 soal)

3. **Operasi Kabataku** (30 soal)
   - Penjumlahan/Pengurangan (10 soal)
   - Perkalian/Pembagian (10 soal)
   - Operasi Campuran (10 soal)

Each question has:
- `content` - Question text
- `answer` - Correct answer
- `difficulty` - easy | medium | hard

---

## 🎮 Admin Panel Features

### 1. Manual Soal Entry
1. Select **Materi** (e.g., "Aljabar")
2. Topics automatically populate
3. Select **Topic** (e.g., "Persamaan Linear")
4. Enter **Soal Content** (question text)
5. Enter **Jawaban** (answer)
6. Select **Difficulty** (easy/medium/hard)
7. Click **Tambah Soal** → Done!

### 2. Bulk Import from CSV
1. Prepare CSV file with columns: `content;answer;difficulty;topic_name`
2. Click **Choose File** under "Bulk Import"
3. Click **Import Soal**
4. See count of imported questions

### 3. View Statistics
- Total questions per materi
- Questions by difficulty (easy/medium/hard)
- Total topics

---

## 📄 CSV Import Format

**Filename:** `soal_import.csv`

**Delimiter:** Semicolon (`;`)

**Columns Required:**
1. `content` - Question text
2. `answer` - Correct answer
3. `difficulty` - easy, medium, or hard
4. `topic_name` - Topic name (auto-created if doesn't exist)

**Example:**
```
content;answer;difficulty;topic_name
Berapa hasil dari 2 + 2?;4;easy;Penjumlahan Dasar
Jika x² + 2x + 1 = 0 maka x =;-1;medium;Persamaan Kuadrat
Tentukan invers dari matriks [[1,2],[3,4]];[[-2,1],[1.5,-0.5]];hard;Determinan dan Invers
```

---

## 🔌 Backend API Endpoints

All endpoints require admin login (`@admin_required`).

### 1. Get Topics for Materi
```
GET /api/topics/<materi_id>

Response:
[
  {"id": 1, "name": "Persamaan Linear", "description": "...", "question_count": 10},
  {"id": 2, "name": "Persamaan Kuadrat", "description": "...", "question_count": 10}
]
```

### 2. Get Statistics
```
GET /api/soal-stats/<materi_id>

Response:
{
  "total_questions": 30,
  "total_topics": 3,
  "easy": 10,
  "medium": 12,
  "hard": 8
}
```

### 3. Add Single Question
```
POST /admin/add_soal_materi

FormData:
- topic_id: 1
- content: "Soal pertanyaan"
- answer: "Jawaban"
- difficulty: "easy"

Response:
{"success": true, "message": "Soal berhasil ditambahkan"}
```

### 4. Bulk Import
```
POST /admin/bulk_import_soal

FormData:
- csv_file: <file>

Response:
{"success": true, "message": "Berhasil import 15 soal"}
```

---

## 🐛 Troubleshooting

### Problem: "Materi tidak ditemukan"
**Solution:** Ensure materis exist in `daftar_materi` table. Run seed script first.

### Problem: "Module 'csv' not found"
**Solution:** CSV module is built-in, shouldn't happen. Check Python installation.

### Problem: "Permission denied" on file upload
**Solution:** Ensure `/static/uploads/` directory exists and has write permissions.

### Problem: Topics not showing in dropdown
**Solution:** 
1. MySQL connection might be wrong
2. Check `.env` file has correct credentials
3. Verify `daftar_materi` table is not empty

### Problem: "CSRF token missing"
**Solution:** Admin panel should have CSRF token in page. Check HTML has:
```html
{% if request.form.get('csrf_token') %}
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
{% endif %}
```

---

## 📋 Database Verification

To verify setup, run these SQL queries in MySQL:

```sql
-- Check materis
SELECT * FROM daftar_materi;

-- Check topics
SELECT * FROM topics;

-- Count questions
SELECT COUNT(*) as total FROM questions;

-- Questions by difficulty
SELECT difficulty, COUNT(*) as count FROM questions GROUP BY difficulty;

-- Questions by topic
SELECT t.name as topic, COUNT(q.id) as question_count 
FROM topics t LEFT JOIN questions q ON t.id = q.topic_id 
GROUP BY t.id, t.name;
```

---

## 🎯 Next Steps

1. ✅ Run `python seed_soal_latihan.py` to populate initial data
2. ✅ Test admin panel at `/admin/add_soal_materi`
3. ✅ Add custom questions manually or via CSV
4. 📝 Create user exercise interface at `/user/latihan`
5. 📝 Connect to user progress tracking

---

## 📞 File References

| File | Purpose |
|------|---------|
| `seed_soal_latihan.py` | Auto-generate 80 questions |
| `Back_End/__init__.py` | API endpoints (lines 2335-2496) |
| `Front_End/templates/admin/add_soal_materi.html` | Admin UI panel |
| `PANDUAN_SOAL_LATIHAN.md` | Detailed technical documentation |
| `SETUP_SOAL_SISTEM.md` | This file |

---

**Created:** 2024
**Status:** Complete & Ready for Testing
