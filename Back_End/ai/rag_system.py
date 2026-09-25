"""
RAG SYSTEM (Retrieval-Augmented Generation)
=============================================
Sistem untuk retrieve dokumen relevan sebelum AI menjawab.
Mencegah halusinasi dengan grounding pada data riil.

Fitur:
- Vector embedding untuk documents
- Similarity search
- Multi-language support (Indonesian/English)
- Automatic document ingestion
- Query expansion & preprocessing
"""

import json
import logging
from typing import List, Dict, Optional, Tuple
from pathlib import Path

try:
    import chromadb
    from chromadb.config import Settings
    CHROMA_AVAILABLE = True
except ImportError:
    CHROMA_AVAILABLE = False
    logging.warning("ChromaDB tidak terinstall. Install: pip install chromadb")


logger = logging.getLogger(__name__)


class RAGSystem:
    """
    Sistem RAG untuk MathThon.
    Retrieve dokumen matematika relevan untuk memberikan context ke AI.
    """

    def __init__(self, collection_name: str = "mathmaticathon", persist_dir: str = None):
        """
        Initialize RAG System.

        Args:
            collection_name: Nama collection di ChromaDB
            persist_dir: Directory untuk persist data (jika None, gunakan in-memory)
        """
        if not CHROMA_AVAILABLE:
            raise ImportError(
                "ChromaDB tidak terinstall. Install dengan:\n"
                "pip install chromadb"
            )

        # Initialize ChromaDB client
        if persist_dir:
            self.client = chromadb.PersistentClient(path=persist_dir)
        else:
            self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}  # Cosine similarity untuk text
        )

        self.collection_name = collection_name
        self.persist_dir = persist_dir

        logger.info(f"✅ RAG System initialized (collection: {collection_name})")

    def ingest_documents(self, documents: List[Dict], batch_size: int = 100):
        """
        Ingest documents ke vector database.

        Args:
            documents: List of documents dengan format:
                {
                    "content": "Hukum Euler: e^(ix) = cos(x) + i*sin(x)",
                    "metadata": {
                        "type": "theorem",
                        "topic": "complex_analysis",
                        "difficulty": "intermediate"
                    }
                }
            batch_size: Batch size untuk ingestion

        Example:
            rag.ingest_documents([
                {
                    "content": "Teorema Pythagoras: a² + b² = c²",
                    "metadata": {"type": "theorem", "topic": "geometry"}
                },
                ...
            ])
        """
        if not documents:
            logger.warning("No documents to ingest")
            return

        total_ingested = 0

        # Process dalam batch
        for i in range(0, len(documents), batch_size):
            batch = documents[i : i + batch_size]

            # Prepare data untuk ChromaDB
            ids = []
            documents_text = []
            metadatas = []

            for idx, doc in enumerate(batch):
                doc_id = f"{self.collection_name}_{i + idx}"
                ids.append(doc_id)
                documents_text.append(doc.get("content", ""))
                metadatas.append(doc.get("metadata", {}))

            # Add ke collection
            try:
                self.collection.add(
                    ids=ids,
                    documents=documents_text,
                    metadatas=metadatas
                )
                total_ingested += len(batch)
                logger.info(f"✅ Ingested {total_ingested}/{len(documents)} documents")
            except Exception as e:
                logger.error(f"❌ Error ingesting batch: {e}")

        logger.info(f"✅ Total documents ingested: {total_ingested}")

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
        min_similarity: float = 0.15
    ) -> List[Dict]:
        """
        Retrieve dokumen relevan berdasarkan query.

        Args:
            query: User question/query
            top_k: Jumlah dokumen yang diambil
            min_similarity: Minimum similarity score (0-1)

        Returns:
            List of relevant documents dengan scores
        """
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k,
                include=["documents", "metadatas", "distances"]
            )

            if not results or not results["documents"]:
                logger.warning(f"No relevant documents found for: {query}")
                return []

            # Convert distances to similarity scores (cosine)
            documents = []
            for i, doc in enumerate(results["documents"][0]):
                distance = results["distances"][0][i]
                similarity = 1 - distance  # Convert distance to similarity

                if similarity >= min_similarity:
                    documents.append({
                        "content": doc,
                        "metadata": results["metadatas"][0][i],
                        "similarity": similarity,
                        "rank": i + 1
                    })

            logger.info(f"✅ Retrieved {len(documents)} relevant documents (query: {query[:50]})")
            return documents

        except Exception as e:
            logger.error(f"❌ Error retrieving documents: {e}")
            return []

    def query_with_context(self, user_query: str, top_k: int = 3) -> Tuple[str, List[str]]:
        """
        Query dengan context documents.

        Returns:
            (formatted_context: str, source_documents: List[str])
        """
        retrieved_docs = self.retrieve(user_query, top_k)

        if not retrieved_docs:
            return "", []

        # Format context untuk LLM
        context_text = "Berdasarkan dokumen yang relevan:\n\n"

        sources = []
        for idx, doc in enumerate(retrieved_docs, 1):
            context_text += f"{idx}. {doc['content']}\n"
            sources.append(f"[{idx}] Similarity: {doc['similarity']:.2%}")

        context_text += "\n---\n\n"

        return context_text, sources

    def load_from_csv(self, csv_path: str, content_column: str = "content"):
        """
        Load documents dari CSV file.

        CSV format:
        content,topic,difficulty
        "Teorema Pythagoras: a² + b² = c²",geometry,basic
        ...
        """
        import csv

        if not Path(csv_path).exists():
            logger.error(f"CSV file tidak ditemukan: {csv_path}")
            return 0

        documents = []
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    content = row.get(content_column, "")
                    if content:
                        metadata = {k: v for k, v in row.items() if k != content_column}
                        documents.append({
                            "content": content,
                            "metadata": metadata
                        })

            if documents:
                self.ingest_documents(documents)
                logger.info(f"✅ Loaded {len(documents)} documents dari CSV")
                return len(documents)

        except Exception as e:
            logger.error(f"❌ Error loading CSV: {e}")

        return 0

    def load_from_json(self, json_path: str):
        """
        Load documents dari JSON file.

        JSON format:
        [
            {
                "content": "...",
                "metadata": { "type": "theorem", ... }
            },
            ...
        ]
        """
        if not Path(json_path).exists():
            logger.error(f"JSON file tidak ditemukan: {json_path}")
            return 0

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                documents = json.load(f)

            if documents:
                self.ingest_documents(documents)
                logger.info(f"✅ Loaded {len(documents)} documents dari JSON")
                return len(documents)

        except Exception as e:
            logger.error(f"❌ Error loading JSON: {e}")

        return 0

    def get_collection_info(self) -> Dict:
        """Get info tentang collection"""
        count = self.collection.count()
        return {
            "collection_name": self.collection_name,
            "total_documents": count,
            "persist_dir": self.persist_dir,
        }

    def delete_collection(self):
        """Delete entire collection (careful!)"""
        try:
            self.client.delete_collection(name=self.collection_name)
            logger.warning(f"⚠️ Collection deleted: {self.collection_name}")
        except Exception as e:
            logger.error(f"❌ Error deleting collection: {e}")

    def export_documents(self, output_path: str):
        """Export all documents ke JSON file"""
        try:
            all_docs = self.collection.get()
            export_data = {
                "collection_name": self.collection_name,
                "total_documents": len(all_docs["ids"]),
                "documents": [
                    {
                        "id": doc_id,
                        "content": doc,
                        "metadata": metadata
                    }
                    for doc_id, doc, metadata in zip(
                        all_docs["ids"],
                        all_docs["documents"],
                        all_docs["metadatas"]
                    )
                ]
            }

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)

            logger.info(f"✅ Exported {len(all_docs['ids'])} documents to {output_path}")
        except Exception as e:
            logger.error(f"❌ Error exporting documents: {e}")


# ─────────────────────────────────────────────────────
# HELPER FUNCTION
# ─────────────────────────────────────────────────────

def create_system_prompt_with_rag_context(
    base_system_prompt: str,
    rag_context: str
) -> str:
    """
    Gabungkan system prompt dengan RAG context.
    HANYA gunakan template jika RAG benar-benar mengembalikan dokumen.
    Jika tidak ada dokumen, jangan sisipkan template apapun.
    """
    if not rag_context or rag_context.strip() == "":
        # ⛔ JANGAN sisipkan template konteks jika RAG kosong
        return base_system_prompt
    
    return f"""{base_system_prompt}

Gunakan informasi materi berikut sebagai referensi tambahan untuk menjawab pertanyaan pengguna:

{rag_context.strip()}"""


# ─────────────────────────────────────────────────────
# SAMPLE DATA
# ─────────────────────────────────────────────────────

SAMPLE_MATH_DOCUMENTS = [
    {
        "content": "Hukum Euler adalah identitas fundamental: e^(ix) = cos(x) + i*sin(x)",
        "metadata": {"type": "theorem", "topic": "complex_analysis", "difficulty": "intermediate"}
    },
    {
        "content": "Teorema Pythagoras: Dalam segitiga siku-siku, a² + b² = c², di mana c adalah hipotenusa.",
        "metadata": {"type": "theorem", "topic": "geometry", "difficulty": "basic"}
    },
    {
        "content": "Limit fundamental: lim(n→∞) (1 + 1/n)^n = e ≈ 2.71828",
        "metadata": {"type": "theorem", "topic": "calculus", "difficulty": "intermediate"}
    },
    {
        "content": "Integral dasar: ∫ x^n dx = (x^(n+1))/(n+1) + C, untuk n ≠ -1",
        "metadata": {"type": "formula", "topic": "calculus", "difficulty": "basic"}
    },
    {
        "content": "Logaritma natural: ln(e) = 1, ln(1) = 0, ln(a*b) = ln(a) + ln(b)",
        "metadata": {"type": "formula", "topic": "algebra", "difficulty": "basic"}
    },
]


# ─────────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("RAG SYSTEM - TEST")
    print("=" * 60)

    # Initialize
    rag = RAGSystem(collection_name="mathton_test", persist_dir=None)

    # Ingest sample documents
    print(f"\n1️⃣ Ingesting {len(SAMPLE_MATH_DOCUMENTS)} documents...")
    rag.ingest_documents(SAMPLE_MATH_DOCUMENTS)

    # Get collection info
    info = rag.get_collection_info()
    print(f"\n2️⃣ Collection Info: {info}")

    # Test retrieval
    test_queries = [
        "Apa itu Hukum Euler?",
        "Selesaikan integral",
        "Logaritma natural",
        "Teorema Pythagoras",
    ]

    print(f"\n3️⃣ Testing retrieval ({len(test_queries)} queries):")
    for query in test_queries:
        context, sources = rag.query_with_context(query, top_k=2)
        print(f"\n📌 Query: {query}")
        print(f"📖 Context:\n{context}")
        print(f"📍 Sources: {sources}")

    print("\n✅ Test selesai!")
