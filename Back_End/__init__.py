from flask import Flask, session, g, url_for, request, abort, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_limiter import Limiter
from dotenv import load_dotenv
import os
import logging
import time

load_dotenv()

# Imports
from Back_End.config import Config
from Back_End.models import db, init_db_schema
from Back_End.routes.utils import *
from Back_End.bug_and_crime_detection.bug_and_crime_detection import limiter, init_security_logging, security_middleware
from Back_End.routes.security_for_web import login_required, admin_required, user_required, generate_key
from Back_End.db.database_mysql import close_db_connection

# Global
db = SQLAlchemy()
csrf = CSRFProtect()
# Removed redundant limiter - using imported one from security module

def create_app(test_config=None):
    app = Flask(__name__, template_folder=Config.TEMPLATE_FOLDER, static_folder=Config.STATIC_FOLDER)
    
    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_object(Config)
    
    # Extensions
    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)
    
    # CORS
    CORS(app, origins=Config.ALLOWED_ORIGINS, supports_credentials=True)
    
    # Security init
    init_security_logging()
    generate_key()
    
    # Middleware & Error Handlers
    @app.before_request
    def before_request_timer():
        g.start_time = time.perf_counter()
        if not request.path.startswith('/static'):
            return security_middleware()

    @app.after_request
    def after_request_logger(response):
        # Tambahkan security headers
        h = response.headers
        h['X-Frame-Options'] = 'DENY'
        h['X-Content-Type-Options'] = 'nosniff'
        h['X-XSS-Protection'] = '1; mode=block'
        h['Referrer-Policy'] = 'strict-origin-when-cross-origin'

        # Log performa request (kecuali static files)
        if not request.path.startswith('/static'):
            elapsed_ms = (time.perf_counter() - g.get('start_time', time.perf_counter())) * 1000
            size_bytes  = response.calculate_content_length() or 0
            level = logging.WARNING if (elapsed_ms > 3000 or response.status_code >= 500) else logging.INFO
            logging.log(
                level,
                '%s %s → %d | %.0f ms | %d bytes',
                request.method, request.path,
                response.status_code, elapsed_ms, size_bytes
            )
        return response
    
    @app.errorhandler(429)
    def ratelimit_handler(e):
        if '/api/' in request.path:
            return jsonify({"success": False, "error": "Rate limited"}), 429
        return render_template("error_security.html", title="Rate Limited", code=429, message=str(e)), 429
    
    @app.errorhandler(403)
    def forbidden_handler(e):
        return render_template("error_security.html", title="Access Denied", code=403, message=str(e)), 403
    
    @app.context_processor
    def inject_user():
        class UserContext:
            def __init__(self, user_id):
                self.id = user_id
                self.is_authenticated = bool(user_id)
        user_id = session.get('user_id')
        from flask_wtf.csrf import generate_csrf
        return dict(current_user=UserContext(user_id), csrf_token=generate_csrf)
    
    @app.teardown_appcontext
    def close_conn(e):
        conn = g.pop('db_conn', None)
        if conn:
            close_db_connection(conn)
    
    with app.app_context():
        init_db_schema(app)
    
    # Register ALL Blueprints
    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    
    from .routes.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from .routes.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from .routes.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from .routes.latihan import latihan_bp # Handles /user/latihan/<topic_id>
    app.register_blueprint(latihan_bp, url_prefix='/user/latihan')
    
    from .routes.materi import materi_bp
    app.register_blueprint(materi_bp, url_prefix='/user/materi')
    
    from .routes.ai import ai_bp
    app.register_blueprint(ai_bp, url_prefix='/api/ai')
    
    from .routes.feedback import feedback_bp
    app.register_blueprint(feedback_bp, url_prefix='/api/feedback')

    # Legacy aliases REMOVED - use proper url_for('auth.login_user') etc.
    
    # Existing external registers (keep for compatibility)
    try:
        from .progres_user import register_progres_routes
        register_progres_routes(app)
    except:
        pass
    
    # Tidak perlu mendaftarkan blueprint eksternal MathThon_Math_Lesson, karena folder ini tidak digunakan.
    # --- Compatibility Layer (Jalur Darurat) ---
    # Ini membuat template yang memanggil 'register_user' tetap jalan
    # dengan me-redirect ke 'auth.register_user'
    @app.route('/legacy_register')
    def register_user():
        return redirect(url_for('auth.register_user'))

    @app.route('/legacy_login')
    def login_user():
        return redirect(url_for('auth.login_user'))

    # Compatibility untuk template yang memanggil 'materi_user_page'
    @app.route('/legacy_materi_user', endpoint='materi_user_page')
    def legacy_materi_user_redirect():
        return redirect(url_for('materi.materi_user'))
    # -------------------------------------------
    
    logging.info("🚀 Back_End refactored! All blueprints registered. Run with: flask --app Back_End.__init__:create_app() run")
    return app
