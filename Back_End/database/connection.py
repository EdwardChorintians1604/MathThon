"""
Database Connection & Session Management
Mendukung SQLAlchemy Session, Engine, dan koneksi MySQL mentah.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from Back_End.config import Config
import mysql.connector
import logging

logger = logging.getLogger(__name__)

# SQLAlchemy Base & Engine
Base = declarative_base()

_engine = None
_SessionFactory = None

def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(
            Config.SQLALCHEMY_DATABASE_URI,
            pool_recycle=3600,
            pool_pre_ping=True
        )
    return _engine

def get_db_session():
    """Mengembalikan scoped session SQLAlchemy."""
    global _SessionFactory
    if _SessionFactory is None:
        _SessionFactory = scoped_session(sessionmaker(bind=get_engine(), autocommit=False, autoflush=False))
    return _SessionFactory()

def get_raw_connection():
    """Koneksi langsung MySQL Connector."""
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
