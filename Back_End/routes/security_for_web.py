import cryptography
import os
import hashlib
import logging
import json
from cryptography.fernet import Fernet
from flask import request, redirect, url_for, session, flash
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Manajemen Kunci Enkripsi ---
KEY_FILE = 'secret.key'

def generate_key():
    """
    Menghasilkan kunci enkripsi baru dan menyimpannya ke dalam file.
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
    """
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data: bytes) -> bytes:
    """
    Mendekripsi data menggunakan kunci yang ada.
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

def encrypt_json_data(data: dict) -> bytes:
    """
    Mengenkripsi data dictionary (JSON) untuk pengiriman yang aman.
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
    """
    try:
        decrypted_bytes = decrypt_data(encrypted_data)
        json_string = decrypted_bytes.decode('utf-8')
        return json.loads(json_string)
    except Exception as e:
        logging.error(f"Gagal mendekripsi atau mengonversi data JSON: {e}")
        raise

# --- File Integrity Monitoring (Deteksi Perubahan Akibat Ransomware) ---

def calculate_hash(filepath: str) -> str:
    """Menghitung hash SHA-256 dari sebuah file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        logging.warning(f"File tidak ditemukan saat menghitung hash: {filepath}")
        return ""

# --- Decorator untuk otentikasi dan otorisasi ---
def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session and 'admin_logged_in' not in session:
                flash('Anda harus login untuk mengakses halaman ini.', 'warning')
                return redirect(url_for('auth.login_user')) # Atau login_admin tergantung konteks
            
            if role == 'admin' and 'admin_logged_in' not in session:
                flash('Anda tidak memiliki izin untuk mengakses halaman ini.', 'danger')
                return redirect(url_for('main.home')) # Redirect ke halaman utama atau halaman error
            
            if role == 'user' and 'user_id' not in session:
                flash('Anda harus login sebagai pengguna untuk mengakses halaman ini.', 'warning')
                return redirect(url_for('auth.login_user'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Anda harus login sebagai administrator untuk mengakses halaman ini.', 'danger')
            return redirect(url_for('admin.login_admin'))
        return f(*args, **kwargs)
    return decorated_function

def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Anda harus login sebagai pengguna untuk mengakses halaman ini.', 'warning')
            return redirect(url_for('auth.login_user'))
        return f(*args, **kwargs)
    return decorated_function

if __name__ == '__main__':
    print("Contoh penggunaan fungsi keamanan:")
    generate_key()
    
    original_data = b"Data sensitif untuk dienkripsi."
    encrypted = encrypt_data(original_data)
    decrypted = decrypt_data(encrypted)
    print(f"Original: {original_data.decode()}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted.decode()}")

    json_data = {"key": "value", "number": 123}
    encrypted_json = encrypt_json_data(json_data)
    decrypted_json = decrypt_json_data(encrypted_json)
    print(f"Original JSON: {json_data}")
    print(f"Encrypted JSON: {encrypted_json}")
    print(f"Decrypted JSON: {decrypted_json}")

    # Untuk demo calculate_hash, Anda bisa membuat file dummy
    dummy_file_path = "dummy_file.txt"
    with open(dummy_file_path, "w") as f:
        f.write("Ini adalah konten file dummy.")
    
    initial_hash = calculate_hash(dummy_file_path)
    print(f"Hash awal '{dummy_file_path}': {initial_hash}")
    
    # Simulasikan perubahan file
    with open(dummy_file_path, "a") as f:
        f.write("Konten tambahan.")
    
    new_hash = calculate_hash(dummy_file_path)
    print(f"Hash baru '{dummy_file_path}': {new_hash}")
    
    if initial_hash != new_hash:
        print("Deteksi perubahan file: Hash berubah!")
    
    os.remove(dummy_file_path) # Bersihkan file dummy
