"""
Core Security Module
Mendukung pembuatan & validasi JWT Token, hashing password, serta middleware autentikasi.
"""
import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify, session, g
import logging
from Back_End.core.config import settings

logger = logging.getLogger(__name__)

def create_access_token(payload: dict, expires_delta: timedelta = None) -> str:
    """Membuat JWT token dengan masa kedaluwarsa terukur."""
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(hours=settings.JWT_EXPIRATION_HOURS)
    
    to_encode.update({
        "exp": expire,
        "iat": now,
        "iss": "maththon-lms"
    })
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """Mendekode dan memvalidasi JWT token."""
    try:
        decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM], issuer="maththon-lms")
        return decoded
    except jwt.ExpiredSignatureError:
        logger.warning("[Security] JWT Token has expired.")
        return None
    except jwt.InvalidTokenError as e:
        logger.warning(f"[Security] Invalid JWT Token: {e}")
        return None

def get_current_user_id() -> int:
    """
    Mengambil user_id aktif dari header Authorization: Bearer <token>
    atau fallback ke session['user_id'] (session Flask).
    """
    # 1. Cek Authorization Header
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        decoded = decode_access_token(token)
        if decoded and "sub" in decoded:
            try:
                return int(decoded["sub"])
            except (ValueError, TypeError):
                return None

    # 2. Cek Session Flask (web user)
    if session.get("user_id"):
        return session.get("user_id")

    return None

def auth_required(f):
    """
    Decorator untuk mengamankan route API. Menerima JWT Bearer Token
    maupun Session cookie aktif.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({
                "status": "error",
                "error": "Unauthorized",
                "message": "Autentikasi diperlukan. Sertakan JWT Bearer token atau login terlebih dahulu."
            }), 401
        g.user_id = user_id
        return f(*args, **kwargs)
    return decorated
