"""
CHAT MEMORY OPTIMIZER
======================
Optimasi riwayat chat untuk mencegah context poisoning dan meningkatkan efisiensi.

Fitur:
- Filter pesan spam/kasar sebelum dikirim ke LLM
- Sliding window context (hanya N pesan terbaru)
- Deteksi poisoning (conversation yang rusak)
- Token counting & optimization
- Response caching untuk query serupa
"""

import re
import hashlib
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class ChatMessage:
    """Representasi satu pesan chat"""
    role: str  # 'user' atau 'assistant'
    content: str
    timestamp: Optional[datetime] = None
    is_valid: bool = True
    reason_invalid: Optional[str] = None

    def to_dict(self):
        return {
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
        }


class ChatMemoryOptimizer:
    """
    Optimasi chat memory dengan filtering dan context windowing.
    """

    def __init__(self, max_context_messages: int = 10, max_tokens: int = 8000):
        """
        Args:
            max_context_messages: Berapa banyak pesan terakhir yang dikirim ke LLM (10 = 5 turn Q&A)
            max_tokens: Maksimal tokens untuk context window
        """
        self.max_context_messages = max_context_messages
        self.max_tokens = max_tokens
        self.response_cache: Dict[str, str] = {}  # Cache untuk query serupa
        self.offensive_keywords = self._load_offensive_keywords()
        self.last_context_hash = None

    def _load_offensive_keywords(self) -> List[str]:
        """Load daftar kata-kata yang dianggap offensive/spam"""
        # Daftar kata-kata yang akan difilter (sesuaikan dengan kebutuhan)
        return [
            'bego', 'goblok', 'idiot', 'tolol', 'bangsat',
            'anjing', 'bitch', 'fuck', 'shit', 'asshole',
            # Tambahkan lebih banyak sesuai kebutuhan
        ]

    def detect_offensive_language(self, text: str) -> Tuple[bool, Optional[str]]:
        """
        Deteksi pesan yang mengandung bahasa kasar.

        Returns:
            (is_offensive: bool, keyword_found: Optional[str])
        """
        text_lower = text.lower()

        for keyword in self.offensive_keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', text_lower):
                return True, keyword

        return False, None

    def detect_poisoning(self, messages: List[Dict]) -> bool:
        """
        Deteksi apakah chat history terkontaminasi dengan pesan kasar/spam
        yang bisa mempengaruhi respons AI.

        Indikator:
        - Banyak pesan offensive dari user
        - Pola pertanyaan yang tidak logis (sering berulang)
        - Kontradiksi dalam context
        """
        if len(messages) < 2:
            return False

        # Count offensive messages
        offensive_count = 0
        for msg in messages:
            if msg.get('role') == 'user':
                is_offensive, _ = self.detect_offensive_language(msg.get('content', ''))
                if is_offensive:
                    offensive_count += 1

        # Jika > 30% pesan user adalah offensive, dianggap poisoned
        user_messages = [m for m in messages if m.get('role') == 'user']
        if user_messages:
            offensive_ratio = offensive_count / len(user_messages)
            if offensive_ratio > 0.3:
                return True

        return False

    def filter_messages(self, messages: List[Dict]) -> List[Dict]:
        """
        Filter pesan yang offensive/invalid serta pesan assistant yang terkontaminasi halusinasi.

        - Hapus pesan user yang mengandung bahasa kasar
        - Hapus pesan AI yang mengandung istilah halusinasi (Sekawan, Sinyal, opis, adjungat, dll)
        - Kembalikan list yang sudah difilter
        """
        filtered = []
        contaminated_patterns = [
            "### jawaban benar", "### jawaban salah", "### pertanyaan ambigus",
            "### langkah penyelesaian", "### verifikasi", "### jawaban akhir",
            "pertanyaan anda mungkin maksudnya:", "contoh soal:",
            "sinyal", "sekawan", "opis", "adjungat", "sisi seni", "sisi senin", "sisi kiri", "sisi kawan",
            "matriks satu baris", "matriks dua baris", "matriks 1 dimensi", "matriks dua dimensi", "matriks 2 dimensi", "matriks 3 dimensi", "1d array", "2d array"
        ]

        for msg in messages:
            role = msg.get('role', 'user')
            content = msg.get('content', '')
            content_lower = content.lower()

            # Filter assistant messages with contaminated content
            if role == 'assistant':
                if any(p in content_lower for p in contaminated_patterns):
                    print(f"⚠️ Filtered contaminated assistant message")
                    continue
                filtered.append(msg)
                continue

            # User messages: check offensive language
            is_offensive, keyword = self.detect_offensive_language(content)

            if is_offensive:
                # Log tapi jangan tambahkan ke context
                print(f"⚠️ Filtered offensive message (keyword: {keyword})")
                continue

            filtered.append(msg)

        return filtered

    def estimate_tokens(self, text: str) -> int:
        """
        Estimasi jumlah tokens untuk teks.
        Rough estimate: ~1 token per 4 karakter (untuk LLM seperti GPT/Gemini)
        """
        return len(text) // 4

    def sliding_window_context(self, messages: List[Dict], include_system: bool = False) -> List[Dict]:
        """
        Ambil N pesan terbaru dari chat history (sliding window).

        Args:
            messages: List of all messages
            include_system: Jika True, include system message pertama kali

        Returns:
            List dengan max_context_messages pesan terakhir
        """
        # Filter terlebih dahulu
        filtered = self.filter_messages(messages)

        # Ambil yang paling recent
        window = filtered[-self.max_context_messages:] if filtered else []

        # Jika ada system message, letakkan di awal
        if include_system and filtered and filtered[0].get('role') == 'system':
            system_msg = filtered[0]
            window = [system_msg] + [m for m in window if m.get('role') != 'system']

        return window

    def optimize_context_by_tokens(self, messages: List[Dict]) -> List[Dict]:
        """
        Optimasi context berdasarkan token limit, bukan jumlah pesan.

        Strategy:
        1. Filter offensive messages
        2. Ambil pesan terbaru sampai token limit
        3. Pastikan setiap Q&A pair lengkap (user + assistant)
        """
        filtered = self.filter_messages(messages)

        optimized = []
        total_tokens = 0

        # Proses dari belakang (pesan paling recent)
        for msg in reversed(filtered):
            msg_tokens = self.estimate_tokens(msg.get('content', ''))

            if total_tokens + msg_tokens > self.max_tokens:
                break

            optimized.insert(0, msg)
            total_tokens += msg_tokens

        return optimized

    def get_context_hash(self, messages: List[Dict]) -> str:
        """
        Generate hash dari context untuk detect perubahan.
        Berguna untuk cache invalidation.
        """
        content = '|'.join([m.get('content', '') for m in messages])
        return hashlib.md5(content.encode()).hexdigest()

    def cache_response(self, query: str, response: str):
        """Cache response untuk query tertentu"""
        query_hash = hashlib.md5(query.encode()).hexdigest()
        self.response_cache[query_hash] = response

    def get_cached_response(self, query: str) -> Optional[str]:
        """
        Ambil cached response jika ada query serupa.
        Mengurangi API calls dan mempercepat response.
        """
        query_hash = hashlib.md5(query.encode()).hexdigest()
        return self.response_cache.get(query_hash)

    def should_invalidate_cache(self, current_context_hash: str) -> bool:
        """Detect apakah cache harus di-reset"""
        if self.last_context_hash is None:
            self.last_context_hash = current_context_hash
            return False

        if current_context_hash != self.last_context_hash:
            self.last_context_hash = current_context_hash
            return True

        return False

    def optimize_messages(
        self,
        messages: List[Dict],
        strategy: str = 'sliding_window'  # 'sliding_window' atau 'token_limit'
    ) -> List[Dict]:
        """
        Main optimization function.

        Args:
            messages: Raw chat history
            strategy: Strategi optimasi

        Returns:
            Optimized messages ready to send to LLM
        """
        if strategy == 'token_limit':
            return self.optimize_context_by_tokens(messages)
        else:
            return self.sliding_window_context(messages)

    def prepare_for_llm(
        self,
        messages: List[Dict],
        system_prompt: Optional[str] = None
    ) -> List[Dict]:
        """
        Siapkan messages untuk dikirim ke LLM.

        Proses:
        1. Filter offensive messages
        2. Apply sliding window
        3. Tambah system prompt di awal
        4. Return final list
        """
        optimized = self.optimize_messages(messages)

        # Tambah system prompt jika ada
        if system_prompt:
            # Check apakah sudah ada system message
            if optimized and optimized[0].get('role') == 'system':
                optimized[0]['content'] = system_prompt
            else:
                optimized.insert(0, {'role': 'system', 'content': system_prompt})

        return optimized

    def get_stats(self) -> Dict:
        """Get statistik optimization"""
        return {
            'cache_size': len(self.response_cache),
            'max_context_messages': self.max_context_messages,
            'max_tokens': self.max_tokens,
            'last_context_hash': self.last_context_hash,
        }

    def debug_analyze_messages(self, messages: List[Dict]) -> Dict:
        """
        Analisis detail untuk debugging.
        """
        offensive_count = 0
        user_count = 0
        assistant_count = 0
        total_tokens = 0

        for msg in messages:
            role = msg.get('role', 'user')
            content = msg.get('content', '')

            if role == 'user':
                user_count += 1
                is_offensive, keyword = self.detect_offensive_language(content)
                if is_offensive:
                    offensive_count += 1

            elif role == 'assistant':
                assistant_count += 1

            total_tokens += self.estimate_tokens(content)

        return {
            'total_messages': len(messages),
            'user_messages': user_count,
            'assistant_messages': assistant_count,
            'offensive_count': offensive_count,
            'offensive_ratio': offensive_count / user_count if user_count > 0 else 0,
            'total_tokens': total_tokens,
            'is_poisoned': self.detect_poisoning(messages),
            'recommendation': self._get_recommendation(offensive_count, user_count, total_tokens)
        }

    def _get_recommendation(self, offensive_count: int, user_count: int, total_tokens: int) -> str:
        """Get rekomendasi berdasarkan analisis"""
        if offensive_count > 0:
            return f"⚠️ {offensive_count} pesan offensive terdeteksi. Filter sebelum kirim ke LLM."

        if total_tokens > self.max_tokens:
            return f"⚠️ Token ({total_tokens}) melebihi limit ({self.max_tokens}). Kurangi context window."

        return "✅ Context history dalam kondisi baik. Siap untuk LLM."


# ─────────────────────────────────────────────────────
# INTEGRATION HELPER
# ─────────────────────────────────────────────────────

def optimize_before_api_call(
    messages: List[Dict],
    system_prompt: str,
    optimizer: Optional[ChatMemoryOptimizer] = None
) -> List[Dict]:
    """
    Helper function untuk optimize messages sebelum dikirim ke LLM API.

    Usage di chat_api.py:
    ```python
    optimized_msgs = optimize_before_api_call(
        messages=chat_history,
        system_prompt=SYSTEM_PROMPT,
        optimizer=chat_optimizer
    )
    response = llm_client.generate(messages=optimized_msgs)
    ```
    """
    if optimizer is None:
        optimizer = ChatMemoryOptimizer()

    return optimizer.prepare_for_llm(messages, system_prompt)


# ─────────────────────────────────────────────────────
# CONTOH PENGGUNAAN
# ─────────────────────────────────────────────────────

if __name__ == '__main__':
    # Test
    optimizer = ChatMemoryOptimizer(max_context_messages=5)

    # Sample messages dengan offensive content
    test_messages = [
        {'role': 'system', 'content': 'Anda adalah tutor matematika'},
        {'role': 'user', 'content': 'Halo, bisa bantu saya?'},
        {'role': 'assistant', 'content': 'Tentu! Apa soal Anda?'},
        {'role': 'user', 'content': 'Kamu bego!'},  # Offensive
        {'role': 'user', 'content': 'Sebenarnya, selesaikan integral ∫ x² dx'},
        {'role': 'assistant', 'content': 'Hasil: x³/3 + C'},
    ]

    print("=" * 60)
    print("CHAT MEMORY OPTIMIZER - TEST")
    print("=" * 60)

    # Test 1: Detect poisoning
    is_poisoned = optimizer.detect_poisoning(test_messages)
    print(f"\n1️⃣ Is Poisoned: {is_poisoned}")

    # Test 2: Filter messages
    filtered = optimizer.filter_messages(test_messages)
    print(f"\n2️⃣ Filtered Messages ({len(filtered)}):")
    for msg in filtered:
        print(f"   {msg['role']}: {msg['content'][:50]}...")

    # Test 3: Optimize context
    optimized = optimizer.optimize_messages(test_messages)
    print(f"\n3️⃣ Optimized Context ({len(optimized)} messages):")
    for msg in optimized:
        print(f"   {msg['role']}: {msg['content'][:50]}...")

    # Test 4: Analyze
    analysis = optimizer.debug_analyze_messages(test_messages)
    print(f"\n4️⃣ Analysis:")
    for key, val in analysis.items():
        print(f"   {key}: {val}")

    print("\n✅ Test selesai!")
