#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk Generate Soal Latihan Otomatis
Script ini membuat banyak soal untuk setiap materi/topik yang tersedia
"""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Back_End')))

load_dotenv()

# Database Connection Config
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'maththon_db')
}

# Data Soal untuk Setiap Materi
SOAL_DATA = {
    'Aljabar': {
        'description': 'Topik tentang persamaan dan fungsi aljabar',
        'topics': {
            'Persamaan Linear': [
                ('Jika x + 5 = 12, berapa nilai x?', '7', 'easy'),
                ('Selesaikan: 2x - 3 = 9', '6', 'easy'),
                ('Jika 3x = 15, berapa nilai x?', '5', 'easy'),
                ('Selesaikan: x + 8 = 20', '12', 'easy'),
                ('Jika 4x - 2 = 10, berapa x?', '3', 'medium'),
                ('Selesaikan: 5x + 3 = 28', '5', 'medium'),
                ('Jika 2x - 7 = x + 5, berapa x?', '12', 'medium'),
                ('Selesaikan: 3(x - 2) = 12', '6', 'medium'),
                ('Jika (x + 3)/2 = 7, berapa x?', '11', 'medium'),
                ('Selesaikan: 2x/3 + 4 = 10', '9', 'hard'),
            ],
            'Persamaan Kuadrat': [
                ('Faktorkan: x² + 5x + 6', '(x+2)(x+3)', 'easy'),
                ('Berapa akar dari x² = 16?', '4 atau -4', 'easy'),
                ('Faktorkan: x² - 9', '(x+3)(x-3)', 'easy'),
                ('Jika x² + 2x - 8 = 0, berapa x?', '2 atau -4', 'medium'),
                ('Selesaikan: x² - 5x + 6 = 0', '2 atau 3', 'medium'),
                ('Berapa diskriminan dari x² + 2x + 1?', '0', 'medium'),
                ('Jika x² - 7x + 12 = 0, berapa akar-akarnya?', '3 atau 4', 'medium'),
                ('Faktorkan: 2x² + 7x + 3', '(2x+1)(x+3)', 'hard'),
                ('Selesaikan: x² + 4x - 5 = 0', '1 atau -5', 'hard'),
                ('Jika x² - 10x + 24 = 0, berapa x?', '4 atau 6', 'hard'),
            ],
            'Fungsi dan Grafik': [
                ('Jika f(x) = 2x + 3, berapa f(2)?', '7', 'easy'),
                ('Jika f(x) = x², berapa f(3)?', '9', 'easy'),
                ('Jika f(x) = 3x - 1, berapa f(0)?', '-1', 'easy'),
                ('Jika g(x) = x + 4, berapa g(5)?', '9', 'medium'),
                ('Berapa slope dari y = 2x + 5?', '2', 'medium'),
                ('Jika f(x) = x² + 2x + 1, berapa f(-1)?', '0', 'medium'),
                ('Berapa intercept y dari x² + 3x + 2?', '2', 'medium'),
                ('Jika f(x) = (x+1)/(x-1), berapa f(2)?', '3', 'hard'),
                ('Berapa domain dari f(x) = 1/(x-3)?', 'Semua real kecuali 3', 'hard'),
                ('Jika f(x) = √(x-2), berapa domain-nya?', 'x ≥ 2', 'hard'),
            ],
        }
    },
    'Matriks': {
        'description': 'Topik tentang matriks dan operasinya',
        'topics': {
            'Operasi Matriks': [
                ('Jika A = [1 2; 3 4], berapa determinan A?', '-2', 'easy'),
                ('Berapa hasil 2 × [1 2; 3 4]?', '[2 4; 6 8]', 'easy'),
                ('Jika A = [1 0; 0 1], apa nama matriks ini?', 'Matriks Identitas', 'easy'),
                ('Berapa transpose dari [1 2 3]?', '[1; 2; 3]', 'medium'),
                ('Jika A + B = [3 4; 7 8] dan A = [1 2; 3 4], berapa B?', '[2 2; 4 4]', 'medium'),
                ('Jika matriks 3×3, berapa elemen maksimal?', '9', 'medium'),
                ('Jika A = [2 3; 1 4], berapa trace A?', '6', 'medium'),
                ('Berapa hasil [1 2] × [3; 4]?', '11', 'hard'),
                ('Jika A⁻¹ adalah invers A, apa A × A⁻¹?', 'I (Matriks Identitas)', 'hard'),
                ('Jika |A| = 0, apa karakteristik matriks A?', 'Singular', 'hard'),
            ],
            'Determinan dan Invers': [
                ('Jika A = [1 2; 3 4], berapa det(A)?', '-2', 'easy'),
                ('Jika A = [a b; c d], berapa det(A)?', 'ad - bc', 'medium'),
                ('Matriks kapan tidak punya invers?', 'Ketika determinan = 0', 'medium'),
                ('Jika det(A) = 5, berapa det(2A) untuk matriks 2×2?', '20', 'medium'),
                ('Jika A⁻¹ = [1 2; 3 4], berapa det(A⁻¹)?', '1/det(A)', 'hard'),
                ('Jika A = [2 3; 1 5], hitung invers A', '[5/7 -3/7; -1/7 2/7]', 'hard'),
                ('Untuk matriks 3×3, jumlah minor yang ada?', '9', 'hard'),
                ('Jika AB = I, apa hubungan A dan B?', 'A dan B saling invers', 'hard'),
                ('Berapa det(A) jika baris 1 = baris 2?', '0', 'hard'),
                ('Jika det(A) = 3 dan det(B) = 4, berapa det(AB)?', '12', 'hard'),
            ],
        }
    },
    'Operasi Kabataku': {
        'description': 'Topik tentang operasi aritmatika dasar',
        'topics': {
            'Penjumlahan dan Pengurangan': [
                ('Berapa 5 + 3?', '8', 'easy'),
                ('Berapa 10 - 4?', '6', 'easy'),
                ('Berapa 15 + 8?', '23', 'easy'),
                ('Berapa 20 - 7?', '13', 'easy'),
                ('Berapa 25 + 18?', '43', 'medium'),
                ('Berapa 100 - 35?', '65', 'medium'),
                ('Berapa -5 + 10?', '5', 'medium'),
                ('Berapa -8 - 3?', '-11', 'medium'),
                ('Berapa 150 + (-50)?', '100', 'hard'),
                ('Berapa -20 - (-5)?', '-15', 'hard'),
            ],
            'Perkalian dan Pembagian': [
                ('Berapa 3 × 4?', '12', 'easy'),
                ('Berapa 12 ÷ 3?', '4', 'easy'),
                ('Berapa 5 × 6?', '30', 'easy'),
                ('Berapa 20 ÷ 4?', '5', 'easy'),
                ('Berapa 7 × 8?', '56', 'medium'),
                ('Berapa 72 ÷ 8?', '9', 'medium'),
                ('Berapa (-3) × 4?', '-12', 'medium'),
                ('Berapa 25 ÷ (-5)?', '-5', 'medium'),
                ('Berapa (-6) × (-7)?', '42', 'hard'),
                ('Berapa (-48) ÷ (-6)?', '8', 'hard'),
            ],
            'Operasi Campuran': [
                ('Berapa 2 + 3 × 4?', '14', 'medium'),
                ('Berapa (2 + 3) × 4?', '20', 'medium'),
                ('Berapa 10 - 2 + 3?', '11', 'medium'),
                ('Berapa 20 ÷ 4 + 2?', '7', 'medium'),
                ('Berapa 5 × 2 - 3?', '7', 'medium'),
                ('Berapa (10 + 5) × 2?', '30', 'hard'),
                ('Berapa 100 ÷ 5 × 2?', '40', 'hard'),
                ('Berapa 2³ + 2²?', '12', 'hard'),
                ('Berapa √16 + 3²?', '13', 'hard'),
                ('Berapa 3² × 2 - 10?', '8', 'hard'),
            ],
        }
    },
    'Statistika': {
        'description': 'Topik tentang pengumpulan, analisis, interpretasi, presentasi, dan organisasi data',
        'topics': {
            'Ukuran Pemusatan Data': [
                ('Hitung mean dari data: 2, 4, 6, 8, 10', '6', 'easy'),
                ('Tentukan median dari data: 3, 5, 7, 9, 11', '7', 'easy'),
                ('Tentukan modus dari data: 2, 3, 3, 4, 5', '3', 'easy'),
                ('Hitung mean dari data: 10, 20, 30, 40', '25', 'medium'),
                ('Median dari data: 4, 1, 7, 9, 2, 5 is?', '4.5', 'medium'),
                ('Jika rata-rata 5 bilangan adalah 10, berapa jumlahnya?', '50', 'medium'),
                ('Data: 2, x, 6, 8. Jika mean=5, berapa x?', '4', 'medium'),
                ('Tentukan modus dari data: 1, 2, 2, 3, 3, 3, 4', '3', 'easy'),
                ('Mean dari 5, 7, 9, x adalah 8. Berapa x?', '11', 'hard'),
                ('Median dari 10, 20, x, 40, 50 adalah 30. Berapa x?', '30', 'hard'),
            ],
            'Penyajian Data': [
                ('Apa jenis diagram untuk persentase?', 'Pie Chart', 'easy'),
                ('Diagram batang digunakan untuk?', 'Membandingkan kategori', 'easy'),
                ('Histogram digunakan untuk data?', 'Kontinu', 'medium'),
                ('Apa itu ogive?', 'Grafik frekuensi kumulatif', 'medium'),
                ('Scatter plot menunjukkan?', 'Hubungan dua variabel', 'medium'),
                ('Box plot menunjukkan?', 'Distribusi data (kuartil)', 'hard'),
                ('Apa sumbu x pada histogram?', 'Interval kelas', 'medium'),
                ('Apa sumbu y pada histogram?', 'Frekuensi', 'easy'),
                ('Diagram garis cocok untuk?', 'Data time series', 'easy'),
                ('Stem-and-leaf plot menampilkan?', 'Data asli', 'medium'),
            ]
        }
    },
    'Trigonometri': {
        'description': 'Topik tentang sudut dan fungsi trigonometri',
        'topics': {
            'Perbandingan Trigonometri': [
                ('Sin 30 derajat adalah?', '0.5', 'easy'),
                ('Cos 60 derajat adalah?', '0.5', 'easy'),
                ('Tan 45 derajat adalah?', '1', 'easy'),
                ('Sin 90 derajat adalah?', '1', 'easy'),
                ('Cos 0 derajat adalah?', '1', 'easy'),
                ('Sin 45 derajat adalah?', '1/√2 atau 0.707', 'medium'),
                ('Cos 45 derajat adalah?', '1/√2 atau 0.707', 'medium'),
                ('Tan 60 derajat adalah?', '√3', 'medium'),
                ('Sin 60 derajat adalah?', '√3/2', 'medium'),
                ('Tan 30 derajat adalah?', '1/√3', 'medium'),
            ],
            'Identitas Trigonometri': [
                ('sin²x + cos²x = ?', '1', 'easy'),
                ('tan x = ?', 'sin x / cos x', 'easy'),
                ('1 + tan²x = ?', 'sec²x', 'medium'),
                ('1 + cot²x = ?', 'csc²x', 'medium'),
                ('sin(2x) = ?', '2 sin x cos x', 'hard'),
                ('cos(2x) = ?', 'cos²x - sin²x', 'hard'),
                ('sin(-x) = ?', '-sin x', 'medium'),
                ('cos(-x) = ?', 'cos x', 'medium'),
                ('sin(90 - x) = ?', 'cos x', 'medium'),
                ('cos(90 - x) = ?', 'sin x', 'medium'),
            ]
        }
    },
    'Kalkulus': {
        'description': 'Topik tentang limit, turunan, dan integral',
        'topics': {
            'Limit Fungsi': [
                ('Limit x->2 dari 2x+1', '5', 'easy'),
                ('Limit x->3 dari x^2', '9', 'easy'),
                ('Limit x->0 dari sin(x)/x', '1', 'medium'),
                ('Limit x->inf dari 1/x', '0', 'medium'),
                ('Limit x->1 dari (x^2-1)/(x-1)', '2', 'medium'),
                ('Limit x->2 dari (x^2-4)/(x-2)', '4', 'medium'),
                ('Limit x->0 dari (1-cos x)/x', '0', 'hard'),
                ('Limit x->inf dari (2x+1)/(x-3)', '2', 'hard'),
                ('Limit x->0 dari tan(x)/x', '1', 'medium'),
                ('Limit x->3 dari 3x-5', '4', 'easy'),
            ],
            'Turunan Dasar': [
                ('Turunan dari x^2', '2x', 'easy'),
                ('Turunan dari 5x', '5', 'easy'),
                ('Turunan dari sin(x)', 'cos(x)', 'medium'),
                ('Turunan dari cos(x)', '-sin(x)', 'medium'),
                ('Turunan dari e^x', 'e^x', 'medium'),
                ('Turunan dari ln(x)', '1/x', 'medium'),
                ('Turunan dari x^3', '3x^2', 'easy'),
                ('Turunan dari konstanta 10', '0', 'easy'),
                ('Turunan dari x^n', 'nx^(n-1)', 'medium'),
                ('Turunan dari 1/x', '-1/x^2', 'hard'),
            ]
        }
    },
}

def connect_db():
    """Koneksi ke database"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print(f"✓ Berhasil terhubung ke database: {DB_CONFIG['database']}")
        return conn
    except Error as err:
        print(f"✗ Error koneksi database: {err}")
        return None

def get_or_create_materi(conn, judul_materi, deskripsi):
    """Dapatkan atau buat materi baru"""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM daftar_materi WHERE judul_materi = %s", (judul_materi,))
        result = cursor.fetchone()
        
        if result:
            return result[0]
        
        # Create new materi
        cursor.execute(
            "INSERT INTO daftar_materi (judul_materi, deskripsi, status) VALUES (%s, %s, %s)",
            (judul_materi, deskripsi, 'active')
        )
        conn.commit()
        print(f"  ✓ Materi '{judul_materi}' dibuat")
        return cursor.lastrowid
    except Error as err:
        print(f"  ✗ Error mendapatkan/membuat materi: {err}")
        return None
    finally:
        cursor.close()

def get_or_create_topic(conn, materi_id, topic_name, description):
    """Dapatkan atau buat topic baru"""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM topics WHERE name = %s AND materi_id = %s", (topic_name, materi_id))
        result = cursor.fetchone()
        
        if result:
            return result[0]
        
        # Create new topic
        cursor.execute(
            "INSERT INTO topics (materi_id, name, description) VALUES (%s, %s, %s)",
            (materi_id, topic_name, description)
        )
        conn.commit()
        print(f"    ✓ Topic '{topic_name}' dibuat")
        return cursor.lastrowid
    except Error as err:
        print(f"    ✗ Error mendapatkan/membuat topic: {err}")
        return None
    finally:
        cursor.close()

def create_questions(conn, topic_id, questions_list):
    """Buat banyak soal untuk topic tertentu"""
    cursor = conn.cursor()
    added = 0
    
    try:
        for content, answer, difficulty in questions_list:
            # Check if question already exists
            cursor.execute(
                "SELECT id FROM questions WHERE topic_id = %s AND content = %s",
                (topic_id, content)
            )
            
            if not cursor.fetchone():  # Jika belum ada
                cursor.execute(
                    "INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, %s, %s, %s)",
                    (topic_id, content, answer, difficulty)
                )
                added += 1
        
        conn.commit()
        print(f"      ✓ Ditambahkan {added} soal baru")
        return added
    except Error as err:
        print(f"      ✗ Error membuat soal: {err}")
        return 0
    finally:
        cursor.close()

def seed_soal_database(conn):
    """Main function untuk seed database dengan soal-soal"""
    print("\n" + "="*60)
    print("MEMULAI SEED SOAL LATIHAN KE DATABASE")
    print("="*60 + "\n")
    
    total_materis = 0
    total_topics = 0
    total_soals = 0
    
    for materi_name, materi_content in SOAL_DATA.items():
        print(f"\n[{materi_name.upper()}]")
        
        # Create or get materi
        materi_id = get_or_create_materi(conn, materi_name, materi_content['description'])
        if materi_id:
            total_materis += 1
            
            # Create topics and questions
            for topic_name, questions_list in materi_content['topics'].items():
                print(f"  └─ {topic_name}")
                
                topic_id = get_or_create_topic(conn, materi_id, topic_name, f"Topik {topic_name} dalam {materi_name}")
                if topic_id:
                    total_topics += 1
                    soals_added = create_questions(conn, topic_id, questions_list)
                    total_soals += soals_added
    
    print("\n" + "="*60)
    print("RINGKASAN SEED")
    print("="*60)
    print(f"Total Materi:  {total_materis}")
    print(f"Total Topics:  {total_topics}")
    print(f"Total Soal:    {total_soals}")
    print("="*60 + "\n")

def get_statistics(conn):
    """Tampilkan statistik database"""
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) FROM daftar_materi")
        materi_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM topics")
        topic_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM questions")
        question_count = cursor.fetchone()[0]
        
        print("\n" + "="*60)
        print("STATISTIK DATABASE SOAL LATIHAN")
        print("="*60)
        print(f"Total Materi:     {materi_count}")
        print(f"Total Topics:     {topic_count}")
        print(f"Total Soal:       {question_count}")
        
        # Detail per materi
        print("\nDETAIL PER MATERI:")
        cursor.execute("SELECT id, judul_materi FROM daftar_materi")
        materis = cursor.fetchall()
        
        for (m_id, m_name) in materis:
            cursor.execute("SELECT COUNT(*) FROM topics WHERE materi_id = %s", (m_id,))
            topics_count = cursor.fetchone()[0]
            
            cursor.execute("""
                SELECT COUNT(q.id) FROM questions q
                JOIN topics t ON q.topic_id = t.id
                WHERE t.materi_id = %s
            """, (m_id,))
            questions_count = cursor.fetchone()[0]
            
            print(f"  • {m_name}: {topics_count} topics, {questions_count} soal")
        
        print("="*60 + "\n")
        
    except Error as err:
        print(f"Error mengambil statistik: {err}")
    finally:
        cursor.close()

if __name__ == "__main__":
    conn = connect_db()
    
    if conn:
        try:
            seed_soal_database(conn)
            get_statistics(conn)
            
            print("✓ Seed database berhasil dilakukan!")
            print("  User sekarang bisa mengakses latihan soal dengan banyak variasi")
            
        except Exception as e:
            print(f"✗ Error: {e}")
        finally:
            conn.close()
    else:
        print("✗ Gagal terhubung ke database")
