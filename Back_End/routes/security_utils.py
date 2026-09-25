import os
import hashlib
import logging
import json # Tambahkan import json untuk serialisasi/deserialisasi data
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Manajemen Kunci Enkripsi ---
# Penting: Simpan file kunci ini di lokasi yang aman dan jangan pernah dimasukkan ke dalam version control (misal, tambahkan ke .gitignore)
KEY_FILE = 'secret.key'

def generate_key():
    """
    Menghasilkan kunci enkripsi baru dan menyimpannya ke dalam file.
    Fungsi ini hanya perlu dijalankan sekali saat setup awal.
    """
    if os.path.exists(KEY_FILE):
        logging.warning(f"File kunci '{KEY_FILE}' sudah ada. Tidak membuat kunci baru.")
        return
    
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    logging.info(f"Kunci enkripsi baru telah dibuat dan disimpan di '{KEY_FILE}'.")

def load_key():
    """
    Memuat kunci enkripsi dari file.
    """
    if not os.path.exists(KEY_FILE):
        logging.error(f"File kunci '{KEY_FILE}' tidak ditemukan. Jalankan generate_key() terlebih dahulu.")
        raise FileNotFoundError(f"File kunci '{KEY_FILE}' tidak ditemukan.")
    
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

# --- Fungsi Enkripsi & Dekripsi Data (Untuk Mitigasi Ransomware/Pencurian Data) ---

def encrypt_data(data: bytes) -> bytes:
    """
    Mengenkripsi data menggunakan kunci yang ada.
    :param data: Data dalam bentuk bytes yang akan dienkripsi.
    :return: Data terenkripsi dalam bentuk bytes.
    """
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data: bytes) -> bytes:
    """
    Mendekripsi data menggunakan kunci yang ada.
    :param encrypted_data: Data terenkripsi dalam bentuk bytes.
    :return: Data asli (plaintext) dalam bentuk bytes.
    """
    key = load_key()
    f = Fernet(key)
    try:
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data
    except Exception as e:
        logging.error(f"Gagal melakukan dekripsi. Data mungkin rusak atau kunci salah. Error: {e}")
        raise

# --- Fungsi untuk Enkripsi/Dekripsi Data yang Akan Dikirim ke/dari Frontend ---
# Data yang dikirim ke frontend biasanya dalam format JSON (string),
# jadi kita perlu mengkonversinya ke bytes sebelum enkripsi dan sebaliknya setelah dekripsi.

def encrypt_json_data(data: dict) -> bytes:
    """
    Mengenkripsi data dictionary (JSON) untuk pengiriman yang aman.
    :param data: Data dalam bentuk dictionary yang akan dienkripsi.
    :return: Data terenkripsi dalam bentuk bytes.
    """
    try:
        json_string = json.dumps(data)
        return encrypt_data(json_string.encode('utf-8'))
    except Exception as e:
        logging.error(f"Gagal mengonversi atau mengenkripsi data JSON: {e}")
        raise

def decrypt_json_data(encrypted_data: bytes) -> dict:
    """
    Mendekripsi data terenkripsi dan mengonversinya kembali ke dictionary (JSON).
    :param encrypted_data: Data terenkripsi dalam bentuk bytes.
    :return: Data asli dalam bentuk dictionary.
    """
    try:
        decrypted_bytes = decrypt_data(encrypted_data)
        json_string = decrypted_bytes.decode('utf-8')
        return json.loads(json_string)
    except Exception as e:
        logging.error(f"Gagal mendekripsi atau mengonversi data JSON: {e}")
        raise


# --- Pencegahan SQL Injection ---

def how_to_prevent_sql_injection():
    """
    Fungsi ini bersifat informatif untuk menunjukkan cara mencegah SQL Injection.
    Pencegahan SQL Injection TIDAK menggunakan enkripsi, melainkan 'parameterized queries'.
    
    File Anda `Back_End/db/database.py` sudah menggunakan pendekatan yang benar.
    """
    print("--- Panduan Pencegahan SQL Injection ---")
    print("Cara terbaik untuk mencegah SQL Injection adalah dengan TIDAK pernah menggunakan f-string atau format string untuk memasukkan data ke dalam query.")
    print("\n❌ CONTOH YANG SALAH (Rentan):")
    user_input = "1; DROP TABLE users"
    # Query ini sangat berbahaya karena input pengguna langsung dimasukkan ke string query.
    wrong_query = f"SELECT * FROM users WHERE id = {user_input}"
    print(f"   {wrong_query}")
    
    print("\n✅ CONTOH YANG BENAR (Aman):")
    print("   Gunakan placeholder '?' dan teruskan nilai sebagai parameter kedua dalam bentuk tuple.")
    correct_query = "SELECT * FROM users WHERE username = ?"
    params = ('admin',)
    print(f"   Query: {correct_query}")
    print(f"   Parameter: {params}")
    print("\nDriver database (seperti sqlite3) akan secara aman menangani input, memisahkannya dari perintah SQL itu sendiri.")
    print("Lihat fungsi `execute_query` dan `execute_insert` di `database.py` untuk implementasi yang sudah aman.")


# --- File Integrity Monitoring (Deteksi Perubahan Akibat Ransomware) ---

def calculate_hash(filepath: str) -> str:
    """Menghitung hash SHA-256 dari sebuah file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Baca file dalam chunk untuk efisiensi memori
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        logging.warning(f"File tidak ditemukan saat menghitung hash: {filepath}")
        return ""

if __name__ == '__main__':
    # Contoh penggunaan:
    
    # 1. Hasilkan kunci saat pertama kali setup (cukup sekali)
    print("Langkah 1: Menghasilkan kunci enkripsi jika belum ada...")
    generate_key()
    print("-" * 20)
    
    # 2. Panduan pencegahan SQL Injection
    how_to_prevent_sql_injection()
    print("-" * 20)

    # 3. Contoh enkripsi dan dekripsi data
    print("\nLangkah 3: Contoh Enkripsi/Dekripsi")
    original_text = b"Ini adalah data rahasia yang akan kita amankan."
    encrypted = encrypt_data(original_text)
    decrypted = decrypt_data(encrypted)
    
    print(f"Data Asli    : {original_text.decode()}")
    print(f"Data Terenkripsi: {encrypted}")
    print(f"Data Terdekripsi: {decrypted.decode()}")
    assert original_text == decrypted
    print("✅ Enkripsi dan Dekripsi berhasil!")
    print("-" * 20)

    # 4. Contoh monitoring integritas file
    print("\nLangkah 4: Contoh Monitoring Integritas File")
    # Kita akan coba hitung hash dari file home.html
    file_to_monitor = r'f:\MathThon\Front_End\templates\home.html'
    if os.path.exists(file_to_monitor):
        initial_hash = calculate_hash(file_to_monitor)
        print(f"Hash awal dari '{os.path.basename(file_to_monitor)}': {initial_hash}")
        # Anda bisa menyimpan hash ini di database/file terpisah yang aman.
        # Kemudian, jalankan fungsi calculate_hash() secara berkala dan bandingkan hasilnya.
        # Jika hash berubah, berarti file telah dimodifikasi.
    else:
        print(f"File '{file_to_monitor}' tidak ditemukan untuk demo hash.")

    # 5. Contoh enkripsi/dekripsi data JSON untuk frontend
    print("\nLangkah 5: Contoh Enkripsi/Dekripsi Data JSON untuk Frontend")
    original_json = {"user_id": 123, "username": "john_doe", "role": "admin"}
    encrypted_json = encrypt_json_data(original_json)
    decrypted_json = decrypt_json_data(encrypted_json)

    print(f"Original JSON    : {original_json}")
    print(f"Encrypted JSON   : {encrypted_json}")
    print(f"Decrypted JSON   : {decrypted_json}")
    assert original_json == decrypted_json
    print("✅ Enkripsi dan Dekripsi JSON berhasil!")