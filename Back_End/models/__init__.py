from flask_sqlalchemy import SQLAlchemy
from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.config import Config
import logging

db = SQLAlchemy()

def init_db_schema(app):
    """Initialize database schema using raw MySQL queries (preserves existing logic)."""
    conn = None
    try:
        conn = get_db_connection(app)
        cursor = conn.cursor()
        
        tables = [
            """CREATE TABLE IF NOT EXISTS testimonials (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                user_name VARCHAR(255) NOT NULL, 
                message TEXT NOT NULL, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                born_place VARCHAR(255),
                username VARCHAR(255) NOT NULL UNIQUE,
                born_date DATE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                photo VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                google_sub VARCHAR(50) UNIQUE NULL
            )""",
            """CREATE TABLE IF NOT EXISTS daftar_materi (
                id INT AUTO_INCREMENT PRIMARY KEY,
                judul_materi VARCHAR(255) NOT NULL,
                deskripsi TEXT,
                status ENUM('active', 'inactive') DEFAULT 'active',
                rating INT DEFAULT 0,
                image_url VARCHAR(255) NULL,
                content LONGTEXT NULL,
                slug VARCHAR(255) UNIQUE NULL
            )""",
            """CREATE TABLE IF NOT EXISTS topics (
                id INT AUTO_INCREMENT PRIMARY KEY,
                materi_id INT NOT NULL,
                name VARCHAR(100) NOT NULL UNIQUE,
                description TEXT,
                FOREIGN KEY (materi_id) REFERENCES daftar_materi(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS questions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                topic_id INT NOT NULL,
                content TEXT NOT NULL,
                answer VARCHAR(255) NOT NULL,
                difficulty ENUM('easy', 'medium', 'hard') NOT NULL,
                FOREIGN KEY (topic_id) REFERENCES topics(id)
            )""",
            """CREATE TABLE IF NOT EXISTS user_progress (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                material_id INT NULL,
                topic_id INT NULL,
                status ENUM('Locked', 'In_Progress', 'Completed') DEFAULT 'Locked',
                score INT DEFAULT 0,
                current_stage INT DEFAULT 0,
                attempts_count INT DEFAULT 0,
                time_spent_seconds INT DEFAULT 0,
                completed_at DATETIME NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                correct_answers INT DEFAULT 0,
                questions_answered INT DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS user_analysis_results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                materi_id INT NOT NULL,
                score INT NOT NULL,
                total_questions INT NOT NULL,
                correct_answers INT NOT NULL,
                incorrect_answers INT NOT NULL, 
                completion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                feedback TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (materi_id) REFERENCES daftar_materi(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS password_reset_codes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL UNIQUE,
                code VARCHAR(10) NOT NULL,
                expires_at DATETIME NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                INDEX idx_user_id (user_id),
                INDEX idx_expires_at (expires_at)
            )""",
            """CREATE TABLE IF NOT EXISTS password_reset_tokens (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                token VARCHAR(255) NOT NULL UNIQUE,
                expires_at DATETIME NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS conversations (
                id VARCHAR(50) PRIMARY KEY,
                user_id INT NOT NULL,
                title VARCHAR(255) NOT NULL,
                is_pinned TINYINT(1) DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS chat_messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                conversation_id VARCHAR(50) NOT NULL,
                role ENUM('user', 'assistant') NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS feedback (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_name VARCHAR(255),
                comment TEXT,
                features TEXT,
                analysis_category VARCHAR(100),
                analysis_status VARCHAR(100),
                analysis_recommendation TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS user_activities (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                activity_type VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )""",
            """CREATE TABLE IF NOT EXISTS user_materi_progress (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                materi_slug VARCHAR(100) NOT NULL,
                checkpoint_stage INT DEFAULT 0,
                is_completed TINYINT(1) DEFAULT 0,
                time_spent_seconds INT DEFAULT 0,
                attempts_count INT DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                UNIQUE KEY uq_user_materi (user_id, materi_slug)
            )"""
        ]
        
        for table_sql in tables:
            cursor.execute(table_sql)
        
        conn.commit()
        logging.info("[DB] Schema initialized successfully.")
        
    except Exception as e:
        logging.error(f"[DB] Error initializing schema: {e}")
    finally:
        if conn:
            cursor.close()
            close_db_connection(conn)

# Re-export ORM models and schemas
from Back_End.models.domain import Course, Module, Material, UserProgress, User
from Back_End.models.schemas import ValidateStepRequest, ValidateStepResponse
