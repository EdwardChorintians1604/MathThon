import os
import logging
import mysql.connector
from flask import render_template, session, redirect, url_for, current_app
from .db.database_mysql import get_db_connection, close_db_connection
from .security_for_web import user_required

logger = logging.getLogger(__name__)

def register_progres_routes(app):
    """
    Daftarkan route /user/progres_user dengan endpoint 'progres_user'.
    Menggunakan app.add_url_rule sehingga url_for('progres_user') valid.
    """
    @app.route("/user/progres_user", methods=["GET", "POST"])
    @user_required
    def progres_user_view():
        conn = None
        cursor = None
        user = None
        photo_url = url_for("static", filename="uploads/default.jpg")

        # pastikan login
        user_id = session.get("user_id")
        if not user_id:
            return redirect(url_for("auth.login_user"))
        try:
            conn = get_db_connection(current_app)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name, username, photo FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            cursor.close()
            cursor = None

            if user:
                user["name"] = str(user.get("name") or "")
                user["username"] = str(user.get("username") or "")
                photo_path = user.get("photo") or "uploads/default.jpg"
                photo_url = url_for("static", filename=photo_path)
            else:
                user = {"name": session.get("username", "User"), "username": session.get("username", "")}

        except mysql.connector.Error:
            logger.exception("Error loading progres_user")
            user = {"name": session.get("username", "User"), "username": session.get("username", "")}
        finally:
            try:
                if cursor:
                    cursor.close()
            except Exception:
                pass
            if conn:
                close_db_connection(conn)

        return render_template("user/progres_user.html", users=user, photo_url=photo_url)