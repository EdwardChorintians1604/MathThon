import os
import io
import json
import zipfile
import hashlib
import logging
from typing import Optional, Dict, Any, List, Tuple, Union
from datetime import datetime, timedelta
import pandas as pd
import mysql.connector
from flask import current_app
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.db.db_security_ai import (
    encrypt_bytes_aes256,
    decrypt_bytes_aes256,
    MAGIC_AES_HEADER,
    calculate_sha256_checksum,
    verify_backup_integrity,
    audit_database_integrity_and_credentials,
    analyze_query_sqli_ml,
    detect_audit_log_anomalies,
    analyze_query_cost_and_optimization,
    predict_caching_workload
)

logger = logging.getLogger(__name__)

# ==============================================================================
# PATHS & CONFIGURATION
# ==============================================================================
def get_backup_dir() -> str:
    """Mengembalikan path folder penyimpanan backup di root project secara aman."""
    try:
        from flask import current_app, has_app_context
        if has_app_context() and hasattr(current_app, 'root_path'):
            base_dir = os.path.dirname(current_app.root_path)
        else:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    except Exception:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    backup_dir = os.path.join(base_dir, 'backups', 'database')
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

def get_registry_file_path() -> str:
    return os.path.join(get_backup_dir(), 'backup_registry.json')

def get_config_file_path() -> str:
    return os.path.join(get_backup_dir(), 'backup_config.json')

def get_default_config() -> dict:
    return {
        'auto_backup_enabled': True,
        'interval_type': 'daily',  # 'hourly', 'daily', 'weekly'
        'interval_hours': 24,
        'format': 'zip',           # 'sql' or 'zip'
        'retention_count': 10,     # Simpan maksimal 10 file backup terakhir
        'last_backup_time': None,
        'next_backup_time': (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    }

def load_backup_config() -> dict:
    cfg_file = get_config_file_path()
    if os.path.exists(cfg_file):
        try:
            with open(cfg_file, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
                default = get_default_config()
                default.update(cfg)
                return default
        except Exception as e:
            logger.warning(f"Error loading backup_config.json: {e}")
    default = get_default_config()
    save_backup_config(default)
    return default

def save_backup_config(config: dict):
    cfg_file = get_config_file_path()
    try:
        with open(cfg_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        logger.error(f"Error saving backup_config.json: {e}")

def load_backup_registry() -> list:
    reg_file = get_registry_file_path()
    if os.path.exists(reg_file):
        try:
            with open(reg_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Error loading backup_registry.json: {e}")
    return []

def save_backup_registry(registry: list):
    reg_file = get_registry_file_path()
    try:
        with open(reg_file, 'w', encoding='utf-8') as f:
            json.dump(registry, f, indent=4)
    except Exception as e:
        logger.error(f"Error saving backup_registry.json: {e}")

def format_file_size(bytes_size: int) -> str:
    """Format bytes ke satuan yang nyaman dibaca (B, KB, MB, GB)."""
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.1f} KB"
    elif bytes_size < 1024 * 1024 * 1024:
        return f"{bytes_size / (1024 * 1024):.2f} MB"
    else:
        return f"{bytes_size / (1024 * 1024 * 1024):.2f} GB"

# ==============================================================================
# DATABASE HEALTH & TABLE OVERVIEW
# ==============================================================================
def get_database_overview(app) -> dict:
    """
    Mengambil data komprehensif kesehatan database:
    - Ukuran database total (data + indeks)
    - Versi MySQL & host
    - Daftar seluruh tabel dengan jumlah baris dan ukuran masing-masing
    """
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor(dictionary=True)

        db_name = app.config.get('MYSQL_DB', 'maththon_db')
        host = app.config.get('MYSQL_HOST', 'localhost')
        port = app.config.get('MYSQL_PORT', 3306)

        # 1. Versi MySQL
        cursor.execute("SELECT VERSION() AS ver")
        version_row = cursor.fetchone()
        db_version = version_row['ver'] if version_row else 'Unknown'

        # 2. Ambil informasi seluruh tabel dari information_schema
        query_tables = """
            SELECT 
                TABLE_NAME AS table_name,
                ENGINE AS engine,
                TABLE_ROWS AS table_rows,
                DATA_LENGTH AS data_length,
                INDEX_LENGTH AS index_length,
                (DATA_LENGTH + INDEX_LENGTH) AS total_size,
                AUTO_INCREMENT AS auto_increment,
                TABLE_COLLATION AS collation,
                CREATE_TIME AS create_time,
                UPDATE_TIME AS update_time
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = %s
            ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC, TABLE_NAME ASC
        """
        cursor.execute(query_tables, (db_name,))
        raw_tables = cursor.fetchall()

        total_bytes = 0
        total_rows = 0
        tables_info = []

        for row in raw_tables:
            size_bytes = int(row['total_size'] or 0)
            row_count = int(row['table_rows'] or 0)
            total_bytes += size_bytes
            total_rows += row_count

            tables_info.append({
                'name': row['table_name'],
                'engine': row['engine'] or 'InnoDB',
                'rows': row_count,
                'data_size_formatted': format_file_size(row['data_length'] or 0),
                'index_size_formatted': format_file_size(row['index_length'] or 0),
                'total_size_bytes': size_bytes,
                'total_size_formatted': format_file_size(size_bytes),
                'collation': row['collation'] or 'utf8mb4_general_ci',
                'updated_at': str(row['update_time'] or row['create_time'] or '-')
            })

        close_db_connection(conn)

        return {
            'connected': True,
            'database_name': db_name,
            'host': f"{host}:{port}",
            'version': db_version,
            'total_tables': len(tables_info),
            'total_rows': total_rows,
            'total_size_bytes': total_bytes,
            'total_size_formatted': format_file_size(total_bytes),
            'tables': tables_info
        }
    except Exception as e:
        logger.error(f"Error in get_database_overview: {e}")
        if conn:
            close_db_connection(conn)
        return {
            'connected': False,
            'error': str(e),
            'database_name': app.config.get('MYSQL_DB', 'maththon_db'),
            'host': app.config.get('MYSQL_HOST', 'localhost'),
            'version': 'N/A',
            'total_tables': 0,
            'total_rows': 0,
            'total_size_bytes': 0,
            'total_size_formatted': '0 B',
            'tables': []
        }

def optimize_single_table(app, table_name: str) -> dict:
    """Menjalankan OPTIMIZE TABLE dan ANALYZE TABLE untuk satu tabel."""
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"OPTIMIZE TABLE `{table_name}`")
        opt_res = cursor.fetchall()
        cursor.execute(f"ANALYZE TABLE `{table_name}`")
        ana_res = cursor.fetchall()
        close_db_connection(conn)
        return {'success': True, 'table': table_name, 'message': f"Tabel `{table_name}` berhasil dioptimasi & dianalisis."}
    except Exception as e:
        logger.error(f"Error optimizing table {table_name}: {e}")
        if conn:
            close_db_connection(conn)
        return {'success': False, 'table': table_name, 'error': str(e)}

def optimize_all_database_tables(app) -> dict:
    """Mengoptimasi seluruh tabel dalam database."""
    conn = None
    try:
        overview = get_database_overview(app)
        if not overview['connected']:
            return {'success': False, 'error': 'Database tidak terhubung'}

        conn = get_db_connection(app)
        cursor = conn.cursor()
        optimized = []
        for t in overview['tables']:
            tname = t['name']
            try:
                cursor.execute(f"OPTIMIZE TABLE `{tname}`")
                cursor.fetchall()
                optimized.append(tname)
            except Exception as opt_err:
                logger.warning(f"Failed to optimize {tname}: {opt_err}")

        close_db_connection(conn)
        return {'success': True, 'count': len(optimized), 'tables': optimized}
    except Exception as e:
        logger.error(f"Error optimizing all tables: {e}")
        if conn:
            close_db_connection(conn)
        return {'success': False, 'error': str(e)}

# ==============================================================================
# ROBUST SQL DUMP GENERATOR (FULL BACKUP ENGINE)
# ==============================================================================
def escape_sql_value(val) -> str:
    """Escaping data Python ke literal SQL yang aman dan valid."""
    if val is None:
        return "NULL"
    elif isinstance(val, (int, float)):
        return str(val)
    elif isinstance(val, bool):
        return "1" if val else "0"
    elif isinstance(val, (datetime, pd.Timestamp)):
        return f"'{val.strftime('%Y-%m-%d %H:%M:%S')}'"
    elif isinstance(val, bytes):
        return f"X'{val.hex()}'"
    else:
        # String escaping untuk MySQL
        s = str(val)
        s = s.replace('\\', '\\\\')
        s = s.replace("'", "''")
        s = s.replace('\0', '\\0')
        s = s.replace('\n', '\\n')
        s = s.replace('\r', '\\r')
        return f"'{s}'"

def generate_full_sql_dump(app, target_tables=None, include_data=True) -> str:
    """
    Menghasilkan script SQL Dump utuh, standar MySQL yang siap direstore:
    - Nonaktifkan Foreign Key Checks sementara
    - DROP TABLE IF EXISTS
    - CREATE TABLE lengkap
    - INSERT INTO dengan batch chunking
    """
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor()

        db_name = app.config.get('MYSQL_DB', 'maththon_db')

        # Dapatkan daftar seluruh tabel
        if not target_tables:
            cursor.execute("SHOW TABLES")
            target_tables = [t[0] for t in cursor.fetchall()]

        timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output_lines = [
            "-- -------------------------------------------------------------",
            f"-- MathThon Enterprise Database Backup Dump",
            f"-- Database   : {db_name}",
            f"-- Dibuat Pada: {timestamp_str}",
            f"-- Total Tabel: {len(target_tables)}",
            "-- -------------------------------------------------------------",
            "",
            "/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;",
            "/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;",
            "/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;",
            "/*!40101 SET NAMES utf8mb4 */;",
            "/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;",
            "/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;",
            "/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;",
            "/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;",
            ""
        ]

        for table in target_tables:
            output_lines.append(f"-- =============================================================")
            output_lines.append(f"-- Struktur Tabel `{table}`")
            output_lines.append(f"-- =============================================================")
            output_lines.append(f"DROP TABLE IF EXISTS `{table}`;")

            cursor.execute(f"SHOW CREATE TABLE `{table}`")
            create_stmt = cursor.fetchone()[1]
            output_lines.append(f"{create_stmt};")
            output_lines.append("")

            if include_data:
                cursor.execute(f"SELECT * FROM `{table}`")
                rows = cursor.fetchall()
                if rows:
                    output_lines.append(f"-- Data untuk tabel `{table}` ({len(rows)} baris)")
                    output_lines.append(f"/*!40000 ALTER TABLE `{table}` DISABLE KEYS */;")

                    # Ambil nama kolom
                    cursor.execute(f"SHOW COLUMNS FROM `{table}`")
                    cols = [f"`{c[0]}`" for c in cursor.fetchall()]
                    cols_str = ", ".join(cols)

                    # Batch INSERT (maksimal 200 baris per statement INSERT)
                    chunk_size = 200
                    for i in range(0, len(rows), chunk_size):
                        chunk = rows[i:i + chunk_size]
                        val_rows = []
                        for row in chunk:
                            formatted_vals = [escape_sql_value(v) for v in row]
                            val_rows.append(f"({', '.join(formatted_vals)})")
                        insert_stmt = f"INSERT INTO `{table}` ({cols_str}) VALUES\n" + ",\n".join(val_rows) + ";"
                        output_lines.append(insert_stmt)

                    output_lines.append(f"/*!40000 ALTER TABLE `{table}` ENABLE KEYS */;")
                    output_lines.append("")

        output_lines.extend([
            "-- -------------------------------------------------------------",
            "-- Pulihkan Konfigurasi Semula",
            "-- -------------------------------------------------------------",
            "/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;",
            "/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;",
            "/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;",
            "/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;",
            "/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;",
            "/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;",
            "/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;",
            "",
            f"-- Dump Selesai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ])

        close_db_connection(conn)
        return "\n".join(output_lines)
    except Exception as e:
        logger.error(f"Error generating SQL dump: {e}")
        if conn:
            close_db_connection(conn)
        raise

# ==============================================================================
# MULTI-TABLE EXCEL & CSV EXPORT
# ==============================================================================
def generate_multi_table_excel_bytes(app) -> io.BytesIO:
    """Mengekspor seluruh tabel database ke berkas Excel tunggal dengan multi-sheet."""
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Summary Sheet
            summary_data = []
            for t in tables:
                df = pd.read_sql(f"SELECT * FROM `{t}`", conn)
                # Batasi nama sheet maksimal 31 karakter (batasan Excel)
                sheet_title = t[:31]
                df.to_excel(writer, sheet_name=sheet_title, index=False)
                summary_data.append({'Tabel': t, 'Jumlah Baris': len(df), 'Sheet Name': sheet_title})

            df_summary = pd.DataFrame(summary_data)
            df_summary.to_excel(writer, sheet_name='_RINGKASAN_DATABASE', index=False)

        output.seek(0)
        close_db_connection(conn)
        return output
    except Exception as e:
        logger.error(f"Error exporting multi-table Excel: {e}")
        if conn:
            close_db_connection(conn)
        raise

def generate_multi_table_csv_zip_bytes(app) -> io.BytesIO:
    """Mengekspor seluruh tabel database sebagai kumpulan CSV dalam satu arsip ZIP."""
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for t in tables:
                df = pd.read_sql(f"SELECT * FROM `{t}`", conn)
                csv_bytes = df.to_csv(index=False).encode('utf-8-sig') # UTF-8 with BOM
                zip_file.writestr(f"{t}.csv", csv_bytes)

        zip_buffer.seek(0)
        close_db_connection(conn)
        return zip_buffer
    except Exception as e:
        logger.error(f"Error exporting multi-table CSV zip: {e}")
        if conn:
            close_db_connection(conn)
        raise

# ==============================================================================
# PERIODIC & SCHEDULED BACKUP ENGINE
# ==============================================================================
def create_backup_snapshot(app, backup_type: str = 'manual', backup_format: str = 'zip', encrypt_aes: bool = False, passphrase: Optional[str] = None) -> dict:
    """
    Membuat file snapshot backup fisik di folder backups/database/
    Mendukung:
    - Format ZIP terkompresi (.sql.zip)
    - Format SQL mentah (.sql)
    - Enkripsi AES-256 (Data-at-Rest) (.sql.aes atau .zip.aes)
    - Penghitungan otomatis SHA-256 Checksum untuk jaminan integritas
    - Pencatatan di backup_registry.json serta penegakan retention policy.
    """
    backup_dir = get_backup_dir()
    now = datetime.now()
    timestamp_slug = now.strftime("%Y%m%d_%H%M%S")
    db_name = app.config.get('MYSQL_DB', 'maththon_db')

    # Buat konten SQL dump
    sql_content = generate_full_sql_dump(app, include_data=True)
    sql_bytes = sql_content.encode('utf-8')

    is_aes = encrypt_aes or backup_format in {'aes', 'zip.aes', 'sql.aes'}

    if backup_format in {'zip', 'zip.aes'}:
        # Buat ZIP buffer di memori
        zip_buf = io.BytesIO()
        sql_inner_name = f"backup_{db_name}_{timestamp_slug}_{backup_type}.sql"
        with zipfile.ZipFile(zip_buf, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(sql_inner_name, sql_bytes)
        raw_bytes = zip_buf.getvalue()

        if is_aes:
            filename = f"backup_{db_name}_{timestamp_slug}_{backup_type}.zip.aes"
            file_path = os.path.join(backup_dir, filename)
            encrypted_payload = encrypt_bytes_aes256(raw_bytes, passphrase=passphrase)
            with open(file_path, 'wb') as f:
                f.write(encrypted_payload)
        else:
            filename = f"backup_{db_name}_{timestamp_slug}_{backup_type}.sql.zip"
            file_path = os.path.join(backup_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(raw_bytes)
    else: # sql
        if is_aes:
            filename = f"backup_{db_name}_{timestamp_slug}_{backup_type}.sql.aes"
            file_path = os.path.join(backup_dir, filename)
            encrypted_payload = encrypt_bytes_aes256(sql_bytes, passphrase=passphrase)
            with open(file_path, 'wb') as f:
                f.write(encrypted_payload)
        else:
            filename = f"backup_{db_name}_{timestamp_slug}_{backup_type}.sql"
            file_path = os.path.join(backup_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(sql_content)

    file_size = os.path.getsize(file_path)

    # Hitung SHA256 checksum untuk verifikasi integritas
    checksum = calculate_sha256_checksum(file_path)

    record = {
        'id': f"bkp_{timestamp_slug}",
        'filename': filename,
        'format': 'zip.aes' if (backup_format in {'zip', 'zip.aes'} and is_aes) else ('sql.aes' if is_aes else backup_format),
        'type': backup_type, # 'manual', 'scheduled_daily', 'scheduled_weekly'
        'created_at': now.strftime("%Y-%m-%d %H:%M:%S"),
        'size_bytes': file_size,
        'size_formatted': format_file_size(file_size),
        'checksum': checksum,
        'is_encrypted': is_aes,
        'encryption': 'AES-256-CBC (PBKDF2)' if is_aes else 'None',
        'status': 'Tersedia'
    }

    # Simpan ke registry
    registry = load_backup_registry()
    registry.insert(0, record)

    # Terapkan Retention Policy (hapus backup tertua jika melebihi batas)
    config = load_backup_config()
    max_retention = int(config.get('retention_count', 10))

    if len(registry) > max_retention:
        to_purge = registry[max_retention:]
        registry = registry[:max_retention]
        for p in to_purge:
            purge_path = os.path.join(backup_dir, p['filename'])
            if os.path.exists(purge_path):
                try:
                    os.remove(purge_path)
                    logger.info(f"Purged old backup: {p['filename']}")
                except Exception as pe:
                    logger.warning(f"Failed to purge {p['filename']}: {pe}")

    save_backup_registry(registry)

    # Perbarui jadwal berikutnya di konfigurasi
    config['last_backup_time'] = record['created_at']
    interval_hours = int(config.get('interval_hours', 24))
    next_time = now + timedelta(hours=interval_hours)
    config['next_backup_time'] = next_time.strftime("%Y-%m-%d %H:%M:%S")
    save_backup_config(config)

    return record

def delete_backup_file(filename: str) -> bool:
    """Menghapus arsip backup tertentu dari folder dan registry."""
    backup_dir = get_backup_dir()
    file_path = os.path.join(backup_dir, filename)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f"Error removing backup file {file_path}: {e}")
            return False

    registry = load_backup_registry()
    new_reg = [r for r in registry if r.get('filename') != filename]
    save_backup_registry(new_reg)
    return True

def restore_database_from_file_content(app, sql_content: str) -> dict:
    """
    Memulihkan database dari teks script SQL dump:
    - Mengeksekusi seluruh statement SQL dengan proteksi foreign key
    """
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor()

        # Matikan pengecekan constraint sementara
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cursor.execute("SET UNIQUE_CHECKS = 0;")

        # Pisahkan statement dengan pembagi titik koma yang aman
        statements = []
        current_stmt = []
        in_string = False
        escape = False

        for line in sql_content.splitlines():
            line_str = line.strip()
            if not in_string and (line_str.startswith('--') or line_str.startswith('/*') or not line_str):
                continue

            current_stmt.append(line)
            if line_str.endswith(';'):
                statements.append("\n".join(current_stmt))
                current_stmt = []

        executed_count = 0
        for stmt in statements:
            cleaned = stmt.strip()
            if cleaned and not cleaned.startswith('--'):
                try:
                    cursor.execute(cleaned)
                    executed_count += 1
                except Exception as stmt_err:
                    logger.warning(f"Notice during restore stmt: {stmt_err}")

        conn.commit()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        cursor.execute("SET UNIQUE_CHECKS = 1;")
        close_db_connection(conn)

        return {'success': True, 'statements_executed': executed_count}
    except Exception as e:
        logger.error(f"Error restoring database: {e}")
        if conn:
            try:
                conn.rollback()
                cursor = conn.cursor()
                cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
                close_db_connection(conn)
            except:
                pass
        return {'success': False, 'error': str(e)}

def restore_database_from_archive(app, filename: str, passphrase: Optional[str] = None) -> dict:
    """Memulihkan database langsung dari berkas snapshot di folder backups, mendukung berkas terenkripsi AES-256."""
    backup_dir = get_backup_dir()
    file_path = os.path.join(backup_dir, filename)

    if not os.path.exists(file_path):
        return {'success': False, 'error': 'Berkas backup tidak ditemukan di server.'}

    with open(file_path, 'rb') as f:
        file_bytes = f.read()

    # Periksa apakah terenkripsi AES-256 (ekstensi .aes atau header MAGIC_AES_HEADER)
    if filename.endswith('.aes') or file_bytes.startswith(MAGIC_AES_HEADER):
        try:
            file_bytes = decrypt_bytes_aes256(file_bytes, passphrase=passphrase)
        except Exception as dec_err:
            logger.error(f"Failed to decrypt AES-256 backup {filename}: {dec_err}")
            return {'success': False, 'error': f"Gagal mendekripsi berkas AES-256: {dec_err}. Pastikan passphrase enkripsi benar."}

    # Jika berkas merupakan arsip ZIP
    if filename.endswith('.zip') or filename.endswith('.zip.aes') or file_bytes.startswith(b'PK\x03\x04'):
        try:
            with zipfile.ZipFile(io.BytesIO(file_bytes), 'r') as zf:
                sql_names = [n for n in zf.namelist() if n.endswith('.sql')]
                if not sql_names:
                    return {'success': False, 'error': 'Arsip ZIP tidak berisi berkas .sql'}
                sql_content = zf.read(sql_names[0]).decode('utf-8', errors='replace')
        except Exception as zerr:
            return {'success': False, 'error': f"Gagal membaca arsip ZIP: {zerr}"}
    else:
        sql_content = file_bytes.decode('utf-8', errors='replace')

    return restore_database_from_file_content(app, sql_content)

def check_and_run_scheduled_backup_if_due(app):
    """
    Pengecekan periodik otomatis: dipanggil saat admin mengakses modul database.
    Jika jadwal otomatis aktif dan waktu saat ini telah melewati next_backup_time,
    buat snapshot backup otomatis secara instan.
    """
    try:
        config = load_backup_config()
        if not config.get('auto_backup_enabled'):
            return None

        next_time_str = config.get('next_backup_time')
        if not next_time_str:
            return None

        next_time = datetime.strptime(next_time_str, "%Y-%m-%d %H:%M:%S")
        if datetime.now() >= next_time:
            interval_type = config.get('interval_type', 'daily')
            record = create_backup_snapshot(app, backup_type=f"scheduled_{interval_type}", backup_format=config.get('format', 'zip'))
            logger.info(f"Auto periodic backup executed successfully: {record['filename']}")
            return record
    except Exception as e:
        logger.error(f"Error checking scheduled backup: {e}")
    return None
