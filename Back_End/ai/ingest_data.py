import sys
import os
import logging

# Tambahkan root project ke path agar bisa import module dari Back_End
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Back_End.db.database_mysql import get_db_connection, close_db_connection
from Back_End.ai.rag_system import RAGSystem

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingest_materi_from_mysql_to_rag():
    """
    Mengambil semua materi dari tabel 'daftar_materi' di MySQL
    dan memasukkannya (ingest) ke dalam database vektor ChromaDB untuk RAG.
    """
    from Back_End import create_app
    app = create_app()
    conn = None
    try:
        # Inisialisasi RAG System, pastikan persist_dir sama dengan di chat_api.py
        rag = RAGSystem(persist_dir="./chroma_db_prod")
        
        # Koneksi ke database MySQL
        with app.app_context():
            conn = get_db_connection(app)
            if not conn:
                logging.error("Tidak bisa terhubung ke database MySQL.")
                return
                
            cursor = conn.cursor(dictionary=True)
        
        # Ambil semua materi yang memiliki konten
        cursor.execute("SELECT id, judul_materi, content, slug FROM daftar_materi WHERE content IS NOT NULL AND content != ''")
        materis = cursor.fetchall()
        
        if not materis:
            logging.warning("Tidak ada materi di tabel 'daftar_materi' yang bisa di-ingest.")
            return

        documents_to_ingest = []
        for materi in materis:
            # Gabungkan judul dan konten untuk konteks yang lebih kaya
            full_content = f"Judul Materi: {materi['judul_materi']}\n\n{materi['content']}"
            documents_to_ingest.append({
                "content": full_content,
                "metadata": {
                    "source": "mysql_daftar_materi",
                    "materi_id": materi['id'],
                    "slug": materi['slug']
                }
            })
        
        logging.info(f"Menyiapkan {len(documents_to_ingest)} dokumen untuk di-ingest ke RAG...")
        rag.ingest_documents(documents_to_ingest)
        
        logging.info(f"✅ Ingest {len(documents_to_ingest)} materi ke RAG selesai.")
        
    except Exception as e:
        logging.error(f"❌ Gagal melakukan ingest ke RAG: {e}", exc_info=True)
    finally:
        if conn:
            close_db_connection(conn)

if __name__ == "__main__":
    ingest_materi_from_mysql_to_rag()