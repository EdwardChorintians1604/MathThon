from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

class Config:
    # Secret & Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    
    # MySQL Database Configuration
    # Mendukung input manual (MYSQL_HOST, MYSQL_PORT, dsb) atau satu DATABASE_URL (Service URI dari Aiven)
    DATABASE_URL = os.getenv('DATABASE_URL')
    if DATABASE_URL:
        from urllib.parse import urlparse, unquote
        parsed = urlparse(DATABASE_URL)
        MYSQL_USER = unquote(parsed.username or 'root')
        MYSQL_PASSWORD = unquote(parsed.password or '')
        MYSQL_HOST = parsed.hostname or 'localhost'
        MYSQL_PORT = parsed.port or 3306
        MYSQL_DB = (parsed.path or '/maththon_db').lstrip('/')
        
        # Format untuk SQLAlchemy dengan mysqlconnector
        clean_query = f"?{parsed.query}" if parsed.query else ""
        SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}{clean_query}"
    else:
        MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
        MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
        MYSQL_USER = os.getenv('MYSQL_USER', 'root')
        MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
        MYSQL_DB = os.getenv('MYSQL_DB', 'maththon_db')
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@"
            f"{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # AI/LLM
    OLLAMA_API_KEY = "http://localhost:11434/api/generate"
    MODEL_NAME = os.getenv('MODEL_NAME', 'phi4-mini:latest')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash')
    AI_SYSTEM_PROMPT = os.getenv("AI_SYSTEM_PROMPT", "Anda adalah asisten matematika yang membantu menyelesaikan soal secara langkah demi langkah.")
    
    # Email SMTP
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() in ('true', '1', 't')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    
    # Google OAuth
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    
    # Session Security
    SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV') == 'production'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Paths
    UPLOAD_FOLDER = 'uploads'
    
    # CORS
    _origins = os.getenv('ALLOWED_ORIGINS')
    ALLOWED_ORIGINS = [o.strip() for o in _origins.split(',') if o.strip()] if _origins else ['*']
    
    # Template/Static Folders
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(__file__), "../Front_End/templates")
    STATIC_FOLDER = os.path.join(os.path.dirname(__file__), "../Front_End/static")
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    
    CSV_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'Front_End', 'IndonesiaEduaction.csv')
