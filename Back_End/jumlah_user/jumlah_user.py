import logging
import mysql.connector
from ..db.database_mysql import get_db_connection, close_db_connection

def get_user_statistics(app):
    """
    Mengambil statistik jumlah user dan interaksi dari database MySQL.
    """
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor(dictionary=True)
        
        # Hitung Total User
        cursor.execute("SELECT COUNT(*) as total FROM users")
        user_count = cursor.fetchone()['total']
        
        # Hitung Total Feedback/Interaksi
        cursor.execute("SELECT COUNT(*) as total FROM chat_messages")
        chat_count = cursor.fetchone()['total']
        
        cursor.close()
        return {
            'user_count': user_count,
            'chat_count': chat_count
        }
    except mysql.connector.Error as err:
        logging.error(f"Gagal mengambil statistik user: {err}")
        # Jika satu query gagal, biarkan yang lain tetap bekerja jika memungkinkan
        if 'user_count' not in locals(): user_count = 0
        if 'chat_count' not in locals(): chat_count = 0
        return {
            'user_count': user_count,
            'chat_count': chat_count
        }
    finally:
        if conn:
            close_db_connection(conn)
