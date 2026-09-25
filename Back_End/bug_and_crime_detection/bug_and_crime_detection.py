import re
import json
import os
import time
import logging
from flask import request, jsonify, abort
from datetime import datetime
import bleach

# Opsional: deteksi MIME dari isi file (pip install python-magic; di Windows mungkin perlu python-magic-bin)
try:
    import magic
    if not callable(getattr(magic, "from_buffer", None)):
        magic = None
except (ImportError, OSError):
    magic = None

# Opsional: scan malware dengan ClamAV (pip install pyclamd; butuh daemon clamd)
try:
    import pyclamd
except (ImportError, OSError):
    pyclamd = None
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Path log keamanan
SECURITY_LOG_PATH = 'security_logs.json'
SECURITY_TEXT_LOG = 'security.log'

# Konfigurasi File
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_MIME = ["image/png", "image/jpeg", "application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]

# Pola deteksi SQL Injection (RegEx) - Diperluas
SQLI_PATTERNS = [
    r"(?i)union.*select",
    r"(?i)select.*from",
    r"(?i)insert.*into",
    r"(?i)delete.*from",
    r"(?i)drop.*table",
    r"(?i)truncate.*table",
    r"(?i)update.*set",
    r"(?i)sleep\(",
    r"(?i)benchmark\(",
    r"(?i)waitfor.*delay",
    r"' OR '1'='1",
    r'" OR "1"="1',
    r";--",
    r"\/\*.*?\*\/",
    r"\bOR\b.*\d+=\d+",
    r"\bAND\b.*\d+=\d+",
    r"'\s*--",
    r"\"\s*--",
    r"admin'\s*--",
    r"'\s*OR\s*TRUE\s*--",
    r"'\s*OR\s*1=1\s*#"
]

# Initialize Limiter (will be connected in create_app)
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def init_security_logging():
    """Mengatur logging ke file text untuk audit internal"""
    logging.basicConfig(
        filename=SECURITY_TEXT_LOG,
        level=logging.WARNING,
        format="%(asctime)s | %(levelname)s | %(ip)s | %(path)s | %(message)s"
    )

def log_incident(attack_type, severity, details):
    """Mencatat insiden keamanan ke file JSON untuk Dashboard Admin dan file text"""
    incident = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'ip': request.remote_addr,
        'path': request.path,
        'method': request.method,
        'attack_type': attack_type,
        'severity': severity,
        'details': details,
        'user_agent': request.headers.get('User-Agent', 'Unknown')
    }
    
    # Log ke JSON (untuk Dashboard)
    logs = []
    if os.path.exists(SECURITY_LOG_PATH):
        try:
            with open(SECURITY_LOG_PATH, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
                logs = loaded if isinstance(loaded, list) else []
        except (json.JSONDecodeError, OSError):
            logs = []

    logs.append(incident)
    logs = logs[-1000:]  # Simpan 1000 terakhir

    try:
        with open(SECURITY_LOG_PATH, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=4)
    except OSError:
        pass  # Jangan gagalkan request jika log file tidak bisa ditulis

    # Log ke file text (untuk audit)
    extra = {'ip': request.remote_addr, 'path': request.path}
    logger = logging.getLogger(__name__)
    if severity == "CRITICAL":
        logger.critical(f"{attack_type}: {details}", extra=extra)
    else:
        logger.warning(f"{attack_type}: {details}", extra=extra)

def detect_sqli():
    """Mendeteksi pola SQL Injection pada query string, form data, dan JSON"""
    data_to_check = []
    if request.args:
        data_to_check.extend(request.args.values())
    if request.form:
        data_to_check.extend(request.form.values())
    if request.is_json:
        try:
            json_data = request.get_json()
            if isinstance(json_data, dict):
                data_to_check.extend(map(str, json_data.values()))
        except:
            pass

    for val in data_to_check:
        raw_val = str(val)
        cleaned_val = bleach.clean(raw_val)
        for pattern in SQLI_PATTERNS:
            if re.search(pattern, raw_val):  # Scan raw value untuk deteksi akurat
                # Log payload yang sudah disanitasi agar tidak menulis ulang payload berbahaya ke log
                log_incident("SQL Injection", "CRITICAL", f"Pattern matched in: {cleaned_val[:50]}...")
                return True
    return False

def validate_file_safety(file):
    """Validasi file upload menggunakan Magic Numbers dan ukuran file"""
    if not file:
        return True

    # Cek ukuran file
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    
    if size > MAX_FILE_SIZE:
        log_incident("Large File Upload", "HIGH", f"Size: {size} bytes")
        return False

    # Validasi MIME type berbasis konten (bukan cuma ekstensi)
    if magic:
        try:
            mime = magic.from_buffer(file.read(2048), mime=True)
            file.seek(0) # Reset pointer
            
            if mime not in ALLOWED_MIME:
                log_incident("Restricted File Type", "CRITICAL", f"MIME blocked: {mime}")
                return False
        except Exception as e:
            log_incident("File Scan Error", "HIGH", str(e))
            # Non-blocking if magic fails
    else:
        # Fallback ke ekstensi jika magic tidak tersedia
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png', '.pdf', '.docx']:
            log_incident("Restricted Extension", "CRITICAL", f"Extension blocked: {ext}")
            return False

    # Malware scan (jika ClamAV aktif)
    if pyclamd:
        try:
            cd = pyclamd.ClamdUnixSocket()
            scan = cd.scan_stream(file.read())
            file.seek(0)
            if scan:
                log_incident("Malware Detected", "CRITICAL", str(scan))
                return False
        except:
            pass # ClamAV not running

    return True

def security_middleware():
    """Saring setiap request untuk aktivitas berbahaya"""
    if request.path.startswith('/static'):
        return None

    # 1. Deteksi SQL Injection
    if detect_sqli():
        abort(403, description="Akses diblokir: Aktivitas mencurigakan terdeteksi oleh sistem MathThon.")

    # 2. XSS Protection Headers
    # Headers akan diatur di after_request di __init__.py

    return None

def get_security_summary():
    """Ringkasan statistik untuk dashboard admin"""
    if not os.path.exists(SECURITY_LOG_PATH):
        return {'total': 0, 'critical': 0, 'by_type': {}}
        
    try:
        with open(SECURITY_LOG_PATH, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {'total': 0, 'critical': 0, 'by_type': {}}

    if not isinstance(logs, list):
        logs = []

    summary = {
        'total': len(logs),
        'critical': sum(1 for l in logs if isinstance(l, dict) and l.get('severity') == 'CRITICAL'),
        'by_type': {}
    }

    for l in logs:
        if not isinstance(l, dict):
            continue
        t = l.get('attack_type', 'Unknown')
        summary['by_type'][t] = summary['by_type'].get(t, 0) + 1

    return summary
