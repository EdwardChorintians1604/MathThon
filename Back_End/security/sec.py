#!/usr/bin/env python3
"""
sec.py
Simple Flask-based API providing:
 - File upload + heuristic ransomware/malware detection
 - Basic cryptography utilities (Fernet encryption/decryption, HMAC)
 - Lightweight persistence to MySQL (scan records)

Notes:
 - Requires: Flask, python-dotenv, cryptography, mysql-connector-python
 - Install: pip install flask python-dotenv cryptography mysql-connector-python
 - Configure environment variables in a .env file: 
     MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
     FERNET_KEY (optional; will be generated and printed on first run)
     HMAC_SECRET (optional)

This is a starter implementation focusing on safety and explainability: rule-based
heuristics (entropy, suspicious extensions, suspicious strings) and placeholders
for a machine-learning model if you want to plug one later.

"""

from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
import mysql.connector
import hashlib
import base64
import secrets
import hmac
import logging
import time
import math
import tempfile
from cryptography.fernet import Fernet, InvalidToken

# ---- Configuration & startup ----
load_dotenv()

UPLOAD_DIR = os.getenv('UPLOAD_DIR', './uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

MYSQL_CONFIG = {
    'host': os.getenv('MYSQL_HOST', '127.0.0.1'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DB', 'secdb'),
}

FERNET_KEY = os.getenv('FERNET_KEY')
if not FERNET_KEY:
    # generate and print so operator can persist it
    FERNET_KEY = Fernet.generate_key().decode()
    print('Generated FERNET_KEY (save this to .env):', FERNET_KEY)

HMAC_SECRET = os.getenv('HMAC_SECRET') or secrets.token_hex(32)

# App & logging
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # limit uploads to 50 MB
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sec')

fernet = Fernet(FERNET_KEY.encode())

# ---- Database helpers ----

def get_db_conn():
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
    except Exception as e:
        logger.exception('MySQL connection failed')
        raise
    return conn


def init_db():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS scans (
        id INT AUTO_INCREMENT PRIMARY KEY,
        filename VARCHAR(255),
        sha256 VARCHAR(128),
        filesize BIGINT,
        entropy FLOAT,
        verdict VARCHAR(64),
        meta JSON,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    ''')
    conn.commit()
    cur.close()
    conn.close()

# Try to create table on startup; ignore errors but warn
try:
    init_db()
except Exception as e:
    logger.warning('Failed to initialize DB: %s', e)

# ---- Utility functions ----

def sha256_of_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def file_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    freq = [0] * 256
    for byte in data:
        freq[byte] += 1
    entropy = 0.0
    length = len(data)
    for f in freq:
        if f:
            p = f / length
            entropy -= p * math.log2(p)
    return entropy


def extract_ascii_strings(data: bytes, min_len=4):
    # simple strings extractor
    out = []
    current = []
    for b in data:
        if 32 <= b < 127:
            current.append(chr(b))
        else:
            if len(current) >= min_len:
                out.append(''.join(current))
            current = []
    if len(current) >= min_len:
        out.append(''.join(current))
    return out


def is_suspicious_extension(filename: str) -> bool:
    ext = os.path.splitext(filename)[1].lower()
    suspicious_exts = {'.exe', '.dll', '.scr', '.js', '.vbs', '.ps1', '.jar', '.bat', '.cmd', '.com', '.sys'}
    return ext in suspicious_exts


def simple_heuristic_detection(filename: str, data: bytes) -> (str, dict):
    """Return (verdict, meta)
    verdict: 'clean' | 'suspicious' | 'malicious'
    meta: dictionary with metrics
    """
    meta = {}
    sha256 = sha256_of_bytes(data)
    entropy = file_entropy(data)
    strings = extract_ascii_strings(data, min_len=4)
    filesize = len(data)

    meta['sha256'] = sha256
    meta['filesize'] = filesize
    meta['entropy'] = entropy
    meta['strings_sample'] = strings[:20]

    score = 0

    # High entropy often indicates encrypted/compressed content (ransomware payloads may be packed/encrypted)
    if entropy >= 7.5:
        score += 2
        meta['reason_entropy'] = 'high'
    elif entropy >= 6.5:
        score += 1
        meta['reason_entropy'] = 'medium'

    # Suspicious extension
    if is_suspicious_extension(filename):
        score += 2
        meta['reason_extension'] = True

    # Suspicious strings (rudimentary)
    suspicious_keywords = ['ransom', 'decrypt', 'payment', 'bitcoin', 'btc', 'wallet', 'tor', 'contact', 'key', 'decrypt_my_files']
    found_keywords = [kw for kw in suspicious_keywords if any(kw in s.lower() for s in strings)]
    if found_keywords:
        score += 3
        meta['found_keywords'] = found_keywords

    # Presence of many .onion or tor addresses
    onion_like = [s for s in strings if '.onion' in s.lower() or (len(s) >= 16 and s.endswith('.onion'))]
    if onion_like:
        score += 2
        meta['onion_examples'] = onion_like[:5]

    # very small or empty files are likely not malware
    if filesize == 0:
        score = max(0, score - 2)

    # Heuristic to convert score to verdict
    if score >= 5:
        verdict = 'malicious'
    elif score >= 3:
        verdict = 'suspicious'
    else:
        verdict = 'clean'

    meta['heuristic_score'] = score
    return verdict, meta

# ---- API endpoints ----

@app.route('/')
def index():
    return jsonify({
        'service': 'sec.py - malware/ransomware detector + cryptography',
        'version': '0.1',
        'endpoints': [
            '/api/scan (POST: file upload)',
            '/api/scan/<sha256> (GET: scan result)',
            '/api/report (GET: recent scan records)',
            '/api/crypt/encrypt (POST: json {"data":"..."})',
            '/api/crypt/decrypt (POST: json {"token":"..."})',
            '/api/crypt/hmac (POST: json {"data":"..."})'
        ]
    })

@app.route('/api/scan', methods=['POST'])
def api_scan():
    # Accept file via multipart/form-data with key 'file'
    if 'file' not in request.files:
        return jsonify({'error': 'no file part'}), 400
    f = request.files['file']
    if f.filename == '':
        return jsonify({'error': 'no filename provided'}), 400

    filename = os.path.basename(f.filename)

    # Read into memory (guarded by MAX_CONTENT_LENGTH)
    data = f.read()
    # Basic scan
    verdict, meta = simple_heuristic_detection(filename, data)

    # Persist file to upload dir (but mark quarantined filename if malicious)
    safe_name = f"{int(time.time())}_{secrets.token_hex(8)}_{filename}"
    path = os.path.join(UPLOAD_DIR, safe_name)
    with open(path, 'wb') as wf:
        wf.write(data)

    # Store record in DB if possible
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        insert_sql = "INSERT INTO scans (filename, sha256, filesize, entropy, verdict, meta) VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(insert_sql, (filename, meta.get('sha256'), meta.get('filesize'), meta.get('entropy'), verdict, json_safe(meta)))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.warning('Failed to write scan record to DB: %s', e)

    response = {
        'filename': filename,
        'stored_as': safe_name,
        'verdict': verdict,
        'meta': meta
    }
    return jsonify(response)


def json_safe(obj):
    # convert Python types into JSON-serializable ones (very small helper)
    import json
    try:
        return json.dumps(obj, default=str)
    except Exception:
        return json.dumps(str(obj))


@app.route('/api/scan/<sha256>', methods=['GET'])
def get_scan(sha256):
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, filename, sha256, filesize, entropy, verdict, meta, created_at FROM scans WHERE sha256=%s LIMIT 1', (sha256,))
        row = cur.fetchone()
        cur.close()
        conn.close()
    except Exception as e:
        logger.warning('DB query failed: %s', e)
        row = None

    if not row:
        return jsonify({'error': 'not found'}), 404
    id_, filename, sha, filesize, entropy, verdict, meta_json, created_at = row
    import json
    try:
        meta = json.loads(meta_json)
    except Exception:
        meta = meta_json
    return jsonify({
        'id': id_, 'filename': filename, 'sha256': sha, 'filesize': filesize,
        'entropy': entropy, 'verdict': verdict, 'meta': meta, 'created_at': str(created_at)
    })


@app.route('/api/report', methods=['GET'])
def report():
    limit = int(request.args.get('limit', 20))
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, filename, sha256, filesize, entropy, verdict, created_at FROM scans ORDER BY created_at DESC LIMIT %s', (limit,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        logger.warning('DB query failed: %s', e)
        return jsonify({'error': 'db error', 'detail': str(e)}), 500

    out = []
    for r in rows:
        out.append({
            'id': r[0], 'filename': r[1], 'sha256': r[2], 'filesize': r[3], 'entropy': float(r[4] or 0), 'verdict': r[5], 'created_at': str(r[6])
        })
    return jsonify({'count': len(out), 'results': out})

# ---- Cryptography endpoints ----

@app.route('/api/crypt/encrypt', methods=['POST'])
def crypt_encrypt():
    payload = request.get_json(force=True, silent=True)
    if not payload or 'data' not in payload:
        return jsonify({'error': 'missing data'}), 400
    data = payload['data']
    if isinstance(data, str):
        data = data.encode()
    token = fernet.encrypt(data)
    return jsonify({'token': token.decode()})


@app.route('/api/crypt/decrypt', methods=['POST'])
def crypt_decrypt():
    payload = request.get_json(force=True, silent=True)
    if not payload or 'token' not in payload:
        return jsonify({'error': 'missing token'}), 400
    token = payload['token']
    try:
        plain = fernet.decrypt(token.encode())
    except InvalidToken:
        return jsonify({'error': 'invalid token'}), 400
    return jsonify({'data': plain.decode(errors='replace')})


@app.route('/api/crypt/hmac', methods=['POST'])
def crypt_hmac():
    payload = request.get_json(force=True, silent=True)
    if not payload or 'data' not in payload:
        return jsonify({'error': 'missing data'}), 400
    data = payload['data']
    if isinstance(data, str):
        data_bytes = data.encode()
    else:
        import json
        data_bytes = json.dumps(data, default=str).encode()
    digest = hmac.new(HMAC_SECRET.encode(), data_bytes, hashlib.sha256).hexdigest()
    return jsonify({'hmac': digest})

# ---- Utility: serve uploaded files (admin only) ----
@app.route('/uploads/<path:filename>', methods=['GET'])
def serve_upload(filename):
    # In production protect this with authentication!
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)

# ---- Run ----
if __name__ == '__main__':
    # Simple development server. For production use Gunicorn / uWSGI behind a reverse proxy.
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
