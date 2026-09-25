from flask import current_app, session
import mysql.connector
import logging

logger = logging.getLogger(__name__)

def get_db_connection(app):
    """Membuat koneksi ke database MySQL"""
    try:
        conn = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        return conn
    except mysql.connector.Error as e:
        logger.error(f"Error connecting to MySQL database: {e}")
        raise

def close_db_connection(conn):
    """Menutup koneksi database MySQL"""
    try:
        if conn:
            conn.close()
    except mysql.connector.Error as e:
        logger.error(f"Error closing MySQL connection: {e}")

def execute_query(conn, query, params=None):
    """Eksekusi query SELECT dengan error handling"""
    try:
        cursor = conn.cursor()
        if params is not None:
            cursor.execute(query, tuple(params)) # MySQL connector expects tuple for params
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except mysql.connector.Error as e:
        logger.error(f"Error executing SELECT query: {e}\nQuery: {query}\nParams: {params}")
        raise

def execute_insert(conn, query, params=None):
    """Eksekusi query INSERT/UPDATE/DELETE dan return lastrowid jika ada"""
    try:
        cursor = conn.cursor()
        if params is not None:
            cursor.execute(query, tuple(params)) # MySQL connector expects tuple for params
        else:
            cursor.execute(query)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id
    except mysql.connector.Error as e:
        conn.rollback()
        logger.error(f"Error executing insert/update: {e}\nQuery: {query}\nParams: {params}")
        raise
