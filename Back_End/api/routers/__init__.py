"""
API Routers Package
Mengumpulkan router courses, progress, dan users ke dalam satu blueprint utama `/api`.
"""
from flask import Blueprint
from .courses import courses_router
from .progress import progress_router
from .users import users_router

api_v2_bp = Blueprint("api_v2", __name__)

# Daftarkan sub-router
api_v2_bp.register_blueprint(courses_router)
api_v2_bp.register_blueprint(progress_router)
api_v2_bp.register_blueprint(users_router)
