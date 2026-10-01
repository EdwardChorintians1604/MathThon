"""
MathThon Backend Entry Point
Inisialisasi aplikasi, mounting router API kurikulum, progress & gatekeeping.
"""
import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, jsonify
from flask_cors import CORS
from Back_End.core.config import settings
from Back_End.database.connection import get_engine, Base
from Back_End.api.routers import api_v2_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    
    # CORS
    CORS(app, origins=settings.ALLOWED_ORIGINS, supports_credentials=True)
    
    # Register LMS Routers (/api)
    app.register_blueprint(api_v2_bp, url_prefix="/api")
    
    @app.route("/")
    def health_check():
        return jsonify({
            "service": "MathThon LMS Backend",
            "version": "2.0.0",
            "status": "online",
            "endpoints": [
                "/api/courses",
                "/api/courses/syllabus",
                "/api/materials/<slug>",
                "/api/progress/validate_step",
                "/api/progress/status",
                "/api/users/login",
                "/api/users/profile"
            ]
        })

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 5001))
    print(f"🚀 MathThon LMS Backend running on http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=True)
