import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def check_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DB', 'maththon_db')
        )
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT COUNT(*) as count FROM topics")
        topics_count = cursor.fetchone()['count']
        print(f"Total Topics: {topics_count}")
        
        cursor.execute("SELECT COUNT(*) as count FROM questions")
        questions_count = cursor.fetchone()['count']
        print(f"Total Questions: {questions_count}")
        
        if topics_count == 0:
            print("Adding sample topics...")
            cursor.execute("INSERT INTO topics (name, description) VALUES ('Matriks', 'Pelajari operasi matriks, determinan, dan invers.')")
            cursor.execute("INSERT INTO topics (name, description) VALUES ('Operasi Kabataku', 'Latihan dasar penjumlahan, pengurangan, perkalian, dan pembagian.')")
            cursor.execute("INSERT INTO topics (name, description) VALUES ('Aljabar', 'Selesaikan persamaan linear dan kuadrat dengan mudah.')")
            conn.commit()
            
        if questions_count == 0:
            print("Adding sample questions...")
            # Sample questions for Matriks
            cursor.execute("SELECT id FROM topics WHERE name = 'Matriks'")
            matriks_id = cursor.fetchone()['id']
            cursor.execute("INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, 'Tentukan nilai determinan dari matriks [[2, 3], [1, 4]]', '5', 'easy')", (matriks_id,))
            cursor.execute("INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, 'Jika A = [[1, 2], [3, 4]] dan B = [[5, 6], [7, 8]], tentukan elemen baris 1 kolom 2 dari A + B', '8', 'easy')", (matriks_id,))
            
            # Sample questions for Kabataku
            cursor.execute("SELECT id FROM topics WHERE name = 'Operasi Kabataku'")
            kabataku_id = cursor.fetchone()['id']
            cursor.execute("INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, 'Selesaikan: $12 + 5 \\times 3$', '27', 'easy')", (kabataku_id,))
            cursor.execute("INSERT INTO questions (topic_id, content, answer, difficulty) VALUES (%s, 'Selesaikan: $(20 : 4) + (8 \times 2)$', '21', 'easy')", (kabataku_id,))
            
            conn.commit()
            print("Sample data added.")
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_db()
