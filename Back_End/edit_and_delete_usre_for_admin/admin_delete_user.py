from flask import redirect, url_for, flash
from Back_End.db.database_mysql import get_db_connection, close_db_connection, execute_query
import mysql.connector
import logging

def delete_user_by_admin(app, user_id):
    """Menghapus user berdasarkan ID."""
    conn = None
    try:
        conn = get_db_connection(app)
        execute_query(conn, "DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        flash("Pengguna berhasil dihapus.", "success")
    except mysql.connector.Error as err:
        logging.error(f"Error deleting user by admin: {err}")
        flash("Terjadi kesalahan saat menghapus pengguna.", "danger")
    finally:
        if conn:
            close_db_connection(conn)
    return redirect(url_for('manage_users'))