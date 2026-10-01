"""
Router: Users & Authentication API
Menyediakan endpoint login (JWT Token), registrasi, dan profil pengguna.
"""
from flask import Blueprint, jsonify, request, session, g
from Back_End.core.security import create_access_token, auth_required, get_current_user_id
from Back_End.database.connection import get_db_session
from Back_End.models.domain import User
from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

users_router = Blueprint("users_router", __name__)

@users_router.route("/users/login", methods=["POST"])
def api_login():
    """Endpoint login untuk SPA atau Mobile Client menghasilkan JWT Token."""
    data = request.get_json() or {}
    identifier = data.get("username_or_email", "").strip()
    password = data.get("password", "")

    if not identifier or not password:
        return jsonify({
            "status": "error",
            "message": "Username/Email dan password wajib diisi."
        }), 400

    db_session = get_db_session()
    user = db_session.query(User).filter(
        (User.username == identifier) | (User.email == identifier)
    ).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({
            "status": "error",
            "message": "Kredensial tidak valid. Periksa username dan password Anda."
        }), 401

    # Generate JWT token
    token = create_access_token({
        "sub": str(user.id),
        "username": user.username,
        "email": user.email
    })

    # Simpan juga di session Flask untuk sinkronisasi web browser
    session["user_id"] = user.id

    return jsonify({
        "status": "success",
        "access_token": token,
        "token_type": "bearer",
        "user": user.to_dict()
    }), 200

@users_router.route("/users/profile", methods=["GET"])
def api_profile():
    """Mengambil profil user saat ini (via JWT atau session)."""
    user_id = get_current_user_id() or session.get("user_id")
    if not user_id:
        return jsonify({"status": "error", "message": "Belum terautentikasi"}), 401

    db_session = get_db_session()
    user = db_session.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({"status": "error", "message": "Pengguna tidak ditemukan"}), 404

    return jsonify({
        "status": "success",
        "data": user.to_dict()
    }), 200
