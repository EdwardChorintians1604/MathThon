import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Menggunakan variabel lingkungan untuk konfigurasi database agar lebih aman dan fleksibel
config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'maththon_db')
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Membuat tabel jika belum ada. Skema disesuaikan dengan models.py untuk konsistensi.
    # Menambahkan UNIQUE pada judul_materi untuk mencegah duplikasi.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daftar_materi (
            id INT AUTO_INCREMENT PRIMARY KEY,
            judul_materi VARCHAR(255) NOT NULL UNIQUE,
            deskripsi TEXT,
            status ENUM('active', 'inactive') DEFAULT 'active',
            rating INT DEFAULT 0,
            slug VARCHAR(255) UNIQUE
        )
    """)

    # Membuat tabel topics yang terkoneksi ke daftar_materi
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INT AUTO_INCREMENT PRIMARY KEY,
            materi_id INT NOT NULL,
            name VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            FOREIGN KEY (materi_id) REFERENCES daftar_materi(id) ON DELETE CASCADE
        )
    """)

    # Mendefinisikan data materi yang akan dimasukkan. Variabel 'data' sebelumnya tidak ada.
    # Menambahkan slug yang unik untuk setiap materi.
    data = [
        ('Fungsi Turunan', 'Materi tentang konsep turunan dalam kalkulus.', 'active', 5, 'fungsi-turunan'),
        ('Aljabar', 'Materi dasar-dasar aljabar, persamaan linear, dan kuadrat.', 'active', 4, 'aljabar'),
        ('Matriks', 'Materi tentang operasi matriks, determinan, dan invers.', 'active', 5, 'matriks'),
        ('Operasi Kabataku', 'Materi operasi dasar Kali, Bagi, Tambah, Kurang.', 'active', 5, 'operasi-kabataku'),
        ('Statistika', 'Materi tentang pengolahan dan penyajian data.', 'active', 4, 'statistika'),
        ('Trigonometri', 'Materi tentang sinus, cosinus, tangen, dan identitas trigonometri.', 'active', 4, 'trigonometri'),
        ('Kalkulus', 'Materi pengenalan limit, turunan, dan integral.', 'active', 5, 'kalkulus'),
        ('Peluang', 'Materi tentang konsep peluang dan kejadian.', 'inactive', 3, 'peluang')
    ]

    # Memasukkan data ke dalam tabel. Menggunakan INSERT IGNORE agar tidak error jika data sudah ada.
    cursor.executemany('''
    INSERT IGNORE INTO daftar_materi (judul_materi, deskripsi, status, rating, slug) 
    VALUES (%s, %s, %s, %s, %s)
    ''', data)

    conn.commit()

    print('✅ Database seeding for materials completed successfully!')

except mysql.connector.Error as err:
    print(f"❌ Database error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
