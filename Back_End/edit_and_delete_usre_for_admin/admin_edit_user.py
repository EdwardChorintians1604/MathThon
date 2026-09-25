from flask import render_template, request, redirect, url_for, flash
from Back_End.db.database_mysql import get_db_connection, close_db_connection
import mysql.connector
import logging

def edit_user_form(app, user_id):
    """Menampilkan form untuk mengedit data user."""
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, username, email, born_place, born_date FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        if not user:
            flash("Pengguna tidak ditemukan.", "danger")
            return redirect(url_for('manage_users'))
        return render_template("admin/edit_user.html", user=user)
    except mysql.connector.Error as err:
        logging.error(f"Error fetching user for edit: {err}")
        flash("Gagal memuat data pengguna.", "danger")
        return redirect(url_for('manage_users'))
    finally:
        if conn:
            close_db_connection(conn)

def update_user_by_admin(app, user_id):
    """Memproses update data user dari form admin."""
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        born_place = request.form.get("born_place")
        born_date = request.form.get("born_date")

        conn = None
        try:
            conn = get_db_connection(app)
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name = %s, username = %s, email = %s, born_place = %s, born_date = %s WHERE id = %s",
                           (name, username, email, born_place, born_date, user_id))
            conn.commit()
            cursor.close()
            flash("Data pengguna berhasil diperbarui!", "success")
            return redirect(url_for('manage_users'))
        except mysql.connector.Error as err:
            logging.error(f"Error updating user by admin: {err}")
            flash(f"Terjadi kesalahan saat memperbarui data: {err}", "danger")
            return redirect(url_for('edit_user_form', user_id=user_id))
        finally:
            if conn:
                close_db_connection(conn)