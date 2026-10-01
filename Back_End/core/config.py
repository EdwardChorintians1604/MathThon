"""
Core Configuration Module
Menyediakan konfigurasi terpusat untuk security, database, LLM, dan environment.
"""
import os
from datetime import timedelta
from dotenv import load_dotenv
from Back_End.config import Config as BaseConfig

load_dotenv()

class AppConfig(BaseConfig):
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", BaseConfig.SECRET_KEY or "maththon_jwt_secret_2026")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", 24))
    
    # LLM / AI Tutor
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", BaseConfig.GEMINI_API_KEY)
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
    
    # Gatekeeping Settings
    STRICT_GATEKEEPING = os.getenv("STRICT_GATEKEEPING", "true").lower() in ("true", "1", "yes")

# Default singleton instance
settings = AppConfig()
