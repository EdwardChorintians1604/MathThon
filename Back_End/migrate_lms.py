import os
import mysql.connector
from Back_End.config import Config

def migrate_lms_schema():
    conn = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
    cursor = conn.cursor()

    print("[MIGRATION] Creating LMS schema...")

    # 1. Tabel Courses (VARCHAR 100 for slugs to satisfy InnoDB 767-byte limit)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(191) NOT NULL,
            slug VARCHAR(100) UNIQUE NOT NULL,
            description TEXT,
            order_index INT DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """)
    print("[MIGRATION] 'courses' table checked/created.")

    # 2. Tabel Modules
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS modules (
            id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT NOT NULL,
            title VARCHAR(191) NOT NULL,
            slug VARCHAR(100) UNIQUE NOT NULL,
            description TEXT,
            icon VARCHAR(100) DEFAULT 'bi-journal-bookmark-fill',
            order_index INT DEFAULT 1,
            prerequisite_module_id INT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
            FOREIGN KEY (prerequisite_module_id) REFERENCES modules(id) ON DELETE SET NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """)
    print("[MIGRATION] 'modules' table checked/created.")

    # 3. Tabel Materials (Sub-bab)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INT AUTO_INCREMENT PRIMARY KEY,
            module_id INT NOT NULL,
            chapter_number INT NOT NULL,
            title VARCHAR(191) NOT NULL,
            slug VARCHAR(100) NOT NULL,
            content_type ENUM('reading', 'exercise', 'sandbox', 'checkpoint') DEFAULT 'reading',
            is_checkpoint TINYINT(1) DEFAULT 0,
            prerequisite_id INT NULL,
            order_index INT DEFAULT 1,
            anchor_id VARCHAR(50) DEFAULT 'bab1',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (module_id) REFERENCES modules(id) ON DELETE CASCADE,
            FOREIGN KEY (prerequisite_id) REFERENCES materials(id) ON DELETE SET NULL,
            UNIQUE KEY uq_module_slug (module_id, slug)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """)
    print("[MIGRATION] 'materials' table checked/created.")

    # 4. Tabel user_progress
    cursor.execute("SHOW TABLES LIKE 'user_progress'")
    has_user_progress = cursor.fetchone()

    if not has_user_progress:
        cursor.execute("""
            CREATE TABLE user_progress (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                material_id INT NOT NULL,
                status ENUM('Locked', 'In_Progress', 'Completed') DEFAULT 'Locked',
                score INT DEFAULT 0,
                current_stage INT DEFAULT 0,
                attempts_count INT DEFAULT 0,
                time_spent_seconds INT DEFAULT 0,
                completed_at DATETIME NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE,
                UNIQUE KEY uq_user_material (user_id, material_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """)
        print("[MIGRATION] 'user_progress' table created from scratch.")
    else:
        def add_column_if_missing(col_name, col_def):
            cursor.execute(f"SHOW COLUMNS FROM user_progress LIKE '{col_name}'")
            if not cursor.fetchone():
                cursor.execute(f"ALTER TABLE user_progress ADD COLUMN {col_name} {col_def}")
                print(f"[MIGRATION] Added column '{col_name}' to user_progress.")

        # Modifikasi topic_id agar NULLable jika ada
        cursor.execute("SHOW COLUMNS FROM user_progress LIKE 'topic_id'")
        if cursor.fetchone():
            try:
                cursor.execute("ALTER TABLE user_progress MODIFY topic_id INT NULL")
                print("[MIGRATION] Modified topic_id to be NULLable.")
            except Exception as e:
                print(f"[MIGRATION Note] Could not modify topic_id: {e}")

        add_column_if_missing("material_id", "INT NULL")
        add_column_if_missing("status", "ENUM('Locked', 'In_Progress', 'Completed') DEFAULT 'Locked'")
        add_column_if_missing("score", "INT DEFAULT 0")
        add_column_if_missing("current_stage", "INT DEFAULT 0")
        add_column_if_missing("attempts_count", "INT DEFAULT 0")
        add_column_if_missing("time_spent_seconds", "INT DEFAULT 0")
        add_column_if_missing("completed_at", "DATETIME NULL")
        add_column_if_missing("last_updated", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")

        # Cek index uq_user_material
        try:
            cursor.execute("CREATE INDEX idx_user_material ON user_progress (user_id, material_id)")
            print("[MIGRATION] Created index idx_user_material on user_progress.")
        except Exception:
            pass

    conn.commit()
    conn.close()
    print("[MIGRATION] Schema successfully migrated!")

if __name__ == "__main__":
    migrate_lms_schema()
