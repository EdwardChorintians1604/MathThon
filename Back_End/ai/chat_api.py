import os
import re
import logging
from flask import request, jsonify, current_app, session
from ..db.database_mysql import get_db_connection, close_db_connection
from .llm_client import LLMClient

# ✅ INTEGRASI SEMUA KOMPONEN CERDAS
from .rag_system import RAGSystem, create_system_prompt_with_rag_context
from .chat_memory_optimizer import ChatMemoryOptimizer

# ✅ HYBRID ENGINE: SymPy + LLM untuk mathematical accuracy
try:
    from .calculation_engine import HybridCalculationEngine
    HYBRID_ENGINE_AVAILABLE = True
except ImportError:
    HYBRID_ENGINE_AVAILABLE = False
    logging.warning("HybridCalculationEngine not available. Install sympy: pip install sympy")

# ✅ RAG SYSTEM: ChromaDB untuk grounding
try:
    # Cek apakah chromadb terinstal
    import chromadb
    CHROMA_AVAILABLE = True
except ImportError:
    CHROMA_AVAILABLE = False
    logging.warning("ChromaDB tidak terinstall. RAG system tidak akan aktif. Install: pip install chromadb")

logger = logging.getLogger(__name__)

# ✅ INISIALISASI KOMPONEN DI LEVEL GLOBAL (LEBIH EFISIEN)
# Pastikan path ini benar dan bisa ditulis oleh aplikasi
RAG_SYSTEM = RAGSystem(persist_dir="./chroma_db_prod") if CHROMA_AVAILABLE else None
MEMORY_OPTIMIZER = ChatMemoryOptimizer(max_context_messages=10, max_tokens=8000)
HYBRID_ENGINE = HybridCalculationEngine() if HYBRID_ENGINE_AVAILABLE else None


OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
MODEL_NAME     = os.getenv("MODEL_NAME",     "deepseek-r1:8b")
# ==============================================================================
# SYSTEM PROMPT  (raw string)
# ==============================================================================

SYSTEM_PROMPT = r"""
Kamu adalah MathThon AI, tutor matematika tingkat akademik yang ramah, analitis, mendalam, dan berakurasi sangat tinggi.
Tugas utamamu adalah membimbing pengguna memahami matematika secara menyeluruh dengan penjelasan logis, terstruktur, dan edukatif.

PRINSIP PENJELASAN MENDALAM:
1. STRUKTUR PENJELASAN RUNTUT:
   - Konsep & Rumus Kunci: Kenalkan rumus, aturan, atau teorema yang dipakai (misal: Aturan Rantai Turunan, Integral Parsial, Sifat Matriks).
   - Langkah demi Langkah (Step-by-Step): Jabarkan perhitungan secara terperinci dan jelas. Jangan melompati langkah krusial agar alur logika mudah dipahami.
   - Jawaban Akhir: Tuliskan hasil akhir secara tegas dan jelas.
   - Catatan / Tips Tambahan: Berikan wawasan konsep atau cara cepat mengecek kebenaran jawaban jika relevan.
2. RAMAH & MEMOTIVASI:
   - Berikan nada bicara tutor yang ramah, jelas, dan memotivasi. Jika pengguna menyapa atau bertanya konsep santai, responslah dengan hangat.
3. AKURASI TINGGI & TERMINOLOGI BAKU:
   - Matriks: Gunakan klasifikasi matematika murni (Matriks Persegi, Baris, Kolom, Identitas, Diagonal, Transpose, Simetris, Segitiga).
   - Trigonometri: Gunakan istilah baku (Sisi Depan, Sisi Samping, Sisi Miring / Hipotenusa).
   - Kalkulus: Pastikan aturan turunan dan integrasi dieksekusi dengan presisi tanpa kesalahan aljabar.
4. FORMATTING LATEX STANDAR KATEX:
   - Gunakan $...$ untuk matematika inline (misal $f'(x) = 3x^2$).
   - Gunakan $$...$$ untuk matematika blok/display (misal: $$f'(x) = 3x^2 + 4x - 5$$).
   - Matriks selalu gunakan \begin{pmatrix} ... \end{pmatrix} atau \begin{bmatrix} ... \end{bmatrix} dalam $$...$$.
"""

# ==============================================================================
# KONVERTER: LaTeX → Unicode
# ==============================================================================

# Tabel perintah LaTeX → simbol Unicode (urutan penting untuk penggantian)
LATEX_TO_UNICODE = [
    # Operator & relasi
    (r'\times',          '\u00d7'),
    (r'\cdot',           '\u00b7'),
    (r'\div',            '\u00f7'),
    (r'\pm',             '\u00b1'),
    (r'\mp',             '\u2213'),
    (r'\neq',            '\u2260'),
    (r'\ne',             '\u2260'),
    (r'\leq',            '\u2264'),
    (r'\le',             '\u2264'),
    (r'\geq',            '\u2265'),
    (r'\ge',             '\u2265'),
    (r'\approx',         '\u2248'),
    (r'\equiv',          '\u2261'),
    (r'\propto',         '\u221d'),
    # Konstanta & simbol
    (r'\pi',             '\u03c0'),
    (r'\infty',          '\u221e'),
    (r'\partial',        '\u2202'),
    (r'\nabla',          '\u2207'),
    (r'\angle',          '\u2220'),
    (r'\emptyset',       '\u2205'),
    (r'\varnothing',     '\u2205'),
    # Himpunan
    (r'\in',             '\u2208'),
    (r'\notin',          '\u2209'),
    (r'\subset',         '\u2282'),
    (r'\subseteq',       '\u2286'),
    (r'\cup',            '\u222a'),
    (r'\cap',            '\u2229'),
    # Kalkulus
    (r'\sum',            '\u2211'),
    (r'\prod',           '\u220f'),
    (r'\int',            '\u222b'),
    (r'\oint',           '\u222e'),
    # Logika & panah
    (r'\Rightarrow',     '\u21d2'),
    (r'\Leftarrow',      '\u21d0'),
    (r'\Leftrightarrow', '\u27fa'),
    (r'\rightarrow',     '\u2192'),
    (r'\leftarrow',      '\u2190'),
    (r'\leftrightarrow', '\u2194'),
    (r'\land',           '\u2227'),
    (r'\lor',            '\u2228'),
    (r'\neg',            '\u00ac'),
    (r'\forall',         '\u2200'),
    (r'\exists',         '\u2203'),
    # Huruf Yunani huruf kecil
    (r'\alpha',          '\u03b1'),
    (r'\beta',           '\u03b2'),
    (r'\gamma',          '\u03b3'),
    (r'\delta',          '\u03b4'),
    (r'\epsilon',        '\u03b5'),
    (r'\varepsilon',     '\u03b5'),
    (r'\zeta',           '\u03b6'),
    (r'\eta',            '\u03b7'),
    (r'\theta',          '\u03b8'),
    (r'\iota',           '\u03b9'),
    (r'\kappa',          '\u03ba'),
    (r'\lambda',         '\u03bb'),
    (r'\mu',             '\u03bc'),
    (r'\nu',             '\u03bd'),
    (r'\xi',             '\u03be'),
    (r'\rho',            '\u03c1'),
    (r'\sigma',          '\u03c3'),
    (r'\tau',            '\u03c4'),
    (r'\upsilon',        '\u03c5'),
    (r'\phi',            '\u03c6'),
    (r'\varphi',         '\u03c6'),
    (r'\chi',            '\u03c7'),
    (r'\psi',            '\u03c8'),
    (r'\omega',          '\u03c9'),
    # Huruf Yunani huruf besar
    (r'\Gamma',          '\u0393'),
    (r'\Delta',          '\u0394'),
    (r'\Theta',          '\u0398'),
    (r'\Lambda',         '\u039b'),
    (r'\Xi',             '\u039e'),
    (r'\Pi',             '\u03a0'),
    (r'\Sigma',          '\u03a3'),
    (r'\Upsilon',        '\u03a5'),
    (r'\Phi',            '\u03a6'),
    (r'\Psi',            '\u03a8'),
    (r'\Omega',          '\u03a9'),
]

# Peta superscript & subscript
_SUPERSCRIPT = {
    '0':'\u2070','1':'\u00b9','2':'\u00b2','3':'\u00b3','4':'\u2074','5':'\u2075',
    '6':'\u2076','7':'\u2077','8':'\u2078','9':'\u2079','n':'\u207f','+':'\u207a','-':'\u207b',
}
_SUBSCRIPT = {
    '0':'\u2080','1':'\u2081','2':'\u2082','3':'\u2083','4':'\u2084','5':'\u2085',
    '6':'\u2086','7':'\u2087','8':'\u2088','9':'\u2089','n':'\u2099',
}


def _find_braced(s: str, start: int):
    """
    Temukan pasangan kurung kurawal { } mulai dari posisi `start`.
    Mendukung kurung kurawal bersarang.
    Return (isi_dalam, posisi_setelah_kurung_tutup).
    """
    if start >= len(s) or s[start] != '{':
        return None, start
    depth = 0
    for i in range(start, len(s)):
        if   s[i] == '{': depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return s[start + 1:i], i + 1
    return None, start


def _to_superscript(s: str) -> str:
    return ''.join(_SUPERSCRIPT.get(c, c) for c in s)


def _to_subscript(s: str) -> str:
    return ''.join(_SUBSCRIPT.get(c, c) for c in s)


def latex_expr_to_unicode(expr: str) -> str:
    """
    Konversi satu ekspresi LaTeX menjadi representasi Unicode yang terbaca.

    Urutan konversi (PENTING):
    1. \\frac{num}{den}    -> num/den  (parser brace bersarang)
    2. \\sqrt[n]{x}        -> \u207f\u221a(x)
    3. \\sqrt{x}           -> \u221a(x)
    4. ^{...}              -> superscript Unicode
    5. _{...}              -> subscript Unicode
    6. \\circ              -> \u00b0
    7. Simbol dari LATEX_TO_UNICODE
    8. Hapus {} sisa
    9. Bersihkan spasi
    """
    if not expr:
        return expr

    # --- 1. \frac{num}{den} ---
    for _ in range(6):
        fracs = []
        i = 0
        while i < len(expr):
            m = re.search(r'\\frac', expr[i:])
            if not m:
                break
            pos = i + m.start()
            num, after_num = _find_braced(expr, pos + 5)
            if num is None:
                i = pos + 1
                continue
            den, after_den = _find_braced(expr, after_num)
            if den is None:
                i = pos + 1
                continue
            fracs.append((pos, after_den, num, den))
            i = after_den

        if not fracs:
            break

        for (start, end, num, den) in reversed(fracs):
            n = latex_expr_to_unicode(num.strip())
            d = latex_expr_to_unicode(den.strip())
            _clean = lambda s: bool(re.match(r'^[\w.\u00b1\u00d7\u00f7\u221a\u2070-\u2079\u207f\u207a\u207b\u00b7]+$', s))
            repl   = f'{n}/{d}' if (_clean(n) and _clean(d)) else f'({n})/({d})'
            expr   = expr[:start] + repl + expr[end:]

    # --- 2 & 3. \sqrt[n]{x} dan \sqrt{x} ---
    for _ in range(3):
        m = re.search(r'\\sqrt', expr)
        if not m:
            break
        pos = m.start()
        idx = pos + 5

        n_root = ''
        if idx < len(expr) and expr[idx] == '[':
            close = expr.find(']', idx)
            if close != -1:
                n_str  = expr[idx + 1:close]
                n_root = _to_superscript(n_str) if all(c in _SUPERSCRIPT for c in n_str) else n_str
                idx    = close + 1

        inner, after = _find_braced(expr, idx)
        if inner is None:
            break
        inner_u = latex_expr_to_unicode(inner.strip())
        expr    = expr[:pos] + f'{n_root}\u221a({inner_u})' + expr[after:]

    # --- 4. Pangkat ---
    def rep_pow(m):
        inner = m.group(1)
        return _to_superscript(inner) if all(c in _SUPERSCRIPT for c in inner) else f'^({inner})'

    expr = re.sub(r'\^\{([^{}]*)\}', rep_pow, expr)
    expr = re.sub(r'\^([0-9n])',     lambda m: _to_superscript(m.group(1)), expr)

    # --- 5. Subskrip ---
    def rep_sub(m):
        inner = m.group(1)
        return _to_subscript(inner) if all(c in _SUBSCRIPT for c in inner) else f'({inner})'

    expr = re.sub(r'_\{([^{}]*)\}', rep_sub, expr)
    expr = re.sub(r'_([0-9n])',     lambda m: _to_subscript(m.group(1)), expr)

    # --- 6. \circ -> degree ---
    expr = expr.replace(r'\circ', '\u00b0')

    # --- 7. Simbol dari tabel LATEX_TO_UNICODE ---
    for latex_cmd, unicode_sym in LATEX_TO_UNICODE:
        expr = re.sub(re.escape(latex_cmd) + r'(?=[^a-zA-Z]|$)', unicode_sym, expr)

    # --- 8. Hapus kurung kurawal ---
    expr = re.sub(r'[{}]', '', expr)

    # --- 9. Bersihkan spasi ---
    expr = re.sub(r'  +', ' ', expr)
    return expr.strip()


def convert_aligned_block_to_unicode(block: str) -> str:
    """
    Konversi blok $$ \\begin{aligned} ... \\end{aligned} $$
    menjadi tabel teks Unicode yang terformat rapi dengan alignment kolom.
    """

    inner_m = re.search(r'\\begin\{aligned\}(.*?)\\end\{aligned\}', block, re.DOTALL)
    if not inner_m:
        stripped = re.sub(r'\$\$|\\begin\{[^}]+\}|\\end\{[^}]+\}', '', block)
        return latex_expr_to_unicode(stripped).strip()

    content = inner_m.group(1)

    # Pisahkan per baris
    raw_lines = re.split(r'\\\\', content)
    rows = []
    for raw in raw_lines:
        line = raw.strip()
        if not line:
            continue
        if '&' in line:
            parts = line.split('&', 1)
            lhs   = latex_expr_to_unicode(parts[0].strip())
            rhs_raw = parts[1].strip()
            rel_m = re.match(r'^(=|\\leq|\\geq|\\neq|\\approx|<|>)\s*(.*)', rhs_raw, re.DOTALL)
            if rel_m:
                op  = latex_expr_to_unicode(rel_m.group(1))
                val = latex_expr_to_unicode(rel_m.group(2).strip())
            else:
                op  = '='
                val = latex_expr_to_unicode(rhs_raw)
            rows.append((lhs, op, val))
        else:
            rows.append((latex_expr_to_unicode(line), '', ''))

    if not rows:
        return latex_expr_to_unicode(content)

    max_lhs = max(len(r[0]) for r in rows)
    lines_out = []
    for lhs, op, rhs in rows:
        if op:
            lines_out.append(f'  {lhs:<{max_lhs}}  {op}  {rhs}')
        else:
            lines_out.append(f'  {lhs}')

    return '\n'.join(lines_out)


def sanitize_chat_history(messages: list) -> list:
    """
    Sanitasi riwayat chat sebelum dikirim ke LLM.
    Menghapus pesan dengan pola kontaminasi (header looping, jawaban salah, istilah halusinasi)
    agar tidak mengkontaminasi konteks selanjutnya.
    """
    # Daftar kata kunci penolakan dari AI yang harus dibuang
    refusal_keywords = [
        "tidak dapat membantu dengan pertanyaan yang mencakup",
        "topik seksual atau kontroversial",
        "kebijakan keselamatan",
        "pelanggaran konten",
    ]
    
    # Pola header internal dan istilah halusinasi yang mungkin meracuni konteks (case-insensitive)
    contaminated_patterns = [
        "### jawaban benar",
        "### jawaban salah",
        "### pertanyaan ambigus",
        "### langkah penyelesaian",
        "### verifikasi",
        "### jawaban akhir",
        "pertanyaan anda mungkin maksudnya:",
        "contoh soal:",
        "sinyal",
        "sekawan",
        "opis",
        "adjungat",
        "sisi seni",
        "sisi senin",
        "sisi kiri",
        "sisi kawan",
        "sisi sahabat",
    ]
    
    cleaned = []
    for msg in messages:
        content = msg.get("content", "")
        if not content:
            continue
        content_lower = content.lower()
        
        # Skip refusal messages
        if any(kw in content_lower for kw in refusal_keywords):
            continue
            
        # Skip/filter contaminated assistant messages
        if msg.get("role") == "assistant":
            # Jika pesan asisten mengandung header tercemar atau istilah halusinasi, buang pesan tersebut dari konteks
            if any(pattern in content_lower for pattern in contaminated_patterns):
                continue
                
        cleaned.append(msg)
    return cleaned



def strip_leaked_headers(response: str) -> str:
    """
    Guardrail output: Hapus header/footer system prompt yang bocor ke respons AI.
    """
    if not response:
        return ""
    leaked = [
        "### KONTEKS DARI DATABASE MATERI",
        "### Jawaban Benar",
        "### CONTOH JAWABAN SALAH",
        "### CONTOH JAWABAN BENAR",
        "### Pertanyaan Ambigus",
        "### Langkah Penyelesaian",
        "### Verifikasi",
        "### Jawaban Akhir",
        "Pertanyaan Anda mungkin maksudnya:",
        "Gunakan konteks di atas sebagai sumber utama untuk menjawab pertanyaan.",
        "Jika jawaban tidak ditemukan dalam konteks, katakan dengan jelas.",
    ]
    for pattern in leaked:
        response = response.replace(pattern, "")
    response = re.sub(r'\n{3,}', '\n\n', response)
    return response.strip()


def enhance_ai_response(response: str) -> str:
    """
    Post-process respons AI untuk memastikan format LaTeX siap dirender dengan KaTeX di frontend.
    """
    if not response:
        return ""

    # Standardkan delimiter display math \[ ... \] ke $$ ... $$
    response = re.sub(r'\\\[\s*(.*?)\s*\\\]', r'$$\1$$', response, flags=re.DOTALL)
    
    # Standardkan delimiter inline math \( ... \) ke $ ... $
    response = re.sub(r'\\\(\s*(.*?)\s*\\\)', r'$\1$', response, flags=re.DOTALL)

    # Perbaiki penulisan \begin{aligned} atau \begin{pmatrix/bmatrix} tanpa $$ pembungkus
    response = re.sub(
        r'(?<!\$\$)\s*\\begin\{(aligned|pmatrix|bmatrix|vmatrix|matrix)\}(.*?)\\end\{\1\}\s*(?!\$\$)',
        r'\n$$\n\\begin{\1}\2\\end{\1}\n$$\n',
        response, flags=re.DOTALL
    )

    # Bersihkan baris kosong berlebihan (max 2 consecutive newlines)
    response = re.sub(r'\n{3,}', '\n\n', response)

    # Guardrail: hapus header system prompt yang bocor
    response = strip_leaked_headers(response)

    return response.strip()


# ==============================================================================
# HELPER: PREPROCESSING INPUT USER
# ==============================================================================

def preprocess_user_input(text: str) -> str:
    """Sanitize dan normalize input user."""
    if not text:
        return ""
    text = ' '.join(text.split())
    text = text.replace('<', '<').replace('>', '>')
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    return text.strip()


# ==============================================================================
# ROUTE HANDLER
# ==============================================================================

def chat():
    try:
        data            = request.get_json(force=True)
        user_message    = data.get("message", "").strip()
        conversation_id = data.get("conversation_id")
        user_id         = session.get("user_id")
        use_rag         = data.get("use_rag", True) # Opsi untuk mengaktifkan/menonaktifkan RAG dari frontend
        conversation_history = []

        if not user_message:
            return jsonify({"error": "Pesan tidak boleh kosong"}), 400

        user_message = preprocess_user_input(user_message)

        # --- Simpan pesan user ke DB ---
        conn = cursor = None
        if conversation_id and user_id:
            try:
                conn   = get_db_connection(current_app)
                cursor = conn.cursor(dictionary=True)
                cursor.execute(
                    "SELECT id FROM conversations WHERE id = %s AND user_id = %s",
                    (conversation_id, user_id)
                )
                if cursor.fetchone():
                    cursor.execute(
                        """
                        SELECT role, content FROM (
                            SELECT id, role, content
                            FROM chat_messages
                            WHERE conversation_id = %s
                            ORDER BY id DESC
                            LIMIT 20
                        ) recent_messages
                        ORDER BY id ASC
                        """,
                        (conversation_id,)
                    ) # Ambil riwayat mentah dari DB
                    db_history = cursor.fetchall()
                    cursor.execute(
                        "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                        (conversation_id, 'user', user_message)
                    )
                    conn.commit()
                    
                    # Proses riwayat dengan Memory Optimizer untuk memfilter konten kasar
                    conversation_history = MEMORY_OPTIMIZER.optimize_messages(db_history)
                    
                    # Sanitasi kontaminasi looping header (Jawaban Benar, dll)
                    conversation_history = sanitize_chat_history(conversation_history)
                else:
                    conversation_id = None
            except Exception as e:
                current_app.logger.error(f"Error saving user message: {e}")
                conversation_id = None
            finally:
                if cursor: cursor.close()
                if conn:   close_db_connection(conn)

        # --- HYBRID ENGINE: Try SymPy first for math problems ---
        ai_reply = None
        calculation_used = False
        sources = []

        if HYBRID_ENGINE:
            try:
                engine_result = HYBRID_ENGINE.process(user_message, use_llm_fallback=True)
                
                # If SymPy succeeded, use calculation result
                if engine_result.get("used_sympy"):
                    calculation_used = True
                    logger.info(f"SymPy solved {engine_result.get('type')} query")
                    
                    # Build result string from SymPy
                    sympy_output = _format_sympy_output(engine_result)
                    
                    # Kirim ke LLM HANYA untuk penjelasan, bukan perhitungan ulang
                    explanation_system_prompt = SYSTEM_PROMPT + "\n\n[PENTING: Anda diberi hasil perhitungan yang sudah akurat dari mesin simbolik. Tugas Anda HANYA menjelaskan langkah-langkahnya dalam bahasa yang mudah dimengerti, BUKAN menghitung ulang.]"
                    client = LLMClient(provider="gemini")
                    explanation_prompt = f"Hasil perhitungan SymPy:\n{sympy_output}\n\nPengguna bertanya: {user_message}\n\nJelaskan hasil ini dengan narasi yang jelas dan mudah dipahami."
                    
                    messages = [
                        {"role": "system", "content": explanation_system_prompt},
                        *conversation_history,
                        {"role": "user", "content": explanation_prompt},
                    ]
                    ai_reply = client.generate(
                        messages=messages, 
                        temperature=0.3, 
                        top_p=0.95, 
                        max_output_tokens=8192
                    ).strip()
                    
                    # Prepend SymPy result to explanation
                    ai_reply = f"{sympy_output}\n\n**Penjelasan:**\n{ai_reply}"
                    
            except Exception as e:
                logger.warning(f"Hybrid engine error (fallback to pure LLM): {e}")
                ai_reply = None  # Will fallback to pure LLM below

        # --- Fallback: Pure LLM untuk non-math atau jika hybrid gagal ---
        if not ai_reply:
            logger.info("Using pure LLM (with RAG)")
            
            # Gunakan RAG untuk mengambil konteks dari materi yang sudah divalidasi
            rag_context, sources = "", []
            # [DIAGNOSTIC] Menonaktifkan RAG sementara untuk menguji teori context poisoning
            if RAG_SYSTEM and False: # use_rag:
                rag_context, sources = RAG_SYSTEM.query_with_context(user_message, top_k=3)
            
            system_prompt_with_context = create_system_prompt_with_rag_context(
                base_system_prompt=SYSTEM_PROMPT,
                rag_context=rag_context
            )

            client   = LLMClient(provider="gemini")
            
            # Middleware: bungkus input user agar AI fokus pada soal pengguna
            formatted_user_input = process_user_query(user_message)
            
            messages = [
                {"role": "system", "content": system_prompt_with_context},
                *conversation_history,
                {"role": "user",   "content": formatted_user_input},
            ]
            
            ai_reply = client.generate(
                messages=messages, 
                temperature=0.3, 
                top_p=0.95,
                max_output_tokens=8192
            ).strip()

        if not ai_reply:
            ai_reply = "(AI tidak memberikan jawaban)"
        else:
            # Konversi semua LaTeX ke Unicode sebelum dikirim ke frontend (hanya jika tidak dari SymPy)
            if not calculation_used: # Jika bukan dari SymPy
                ai_reply = enhance_ai_response(ai_reply)
            
            # Tambahkan sumber jika RAG menemukan sesuatu
            if sources:
                ai_reply += "\n\n---\n*Jawaban didasarkan pada materi yang relevan dari database.*"

        # --- Simpan balasan AI ke DB ---
        if conversation_id and user_id:
            conn = cursor = None
            try:
                conn   = get_db_connection(current_app)
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                    (conversation_id, 'assistant', ai_reply)
                )
                conn.commit()
            except Exception as e:
                current_app.logger.error(f"Error saving AI reply: {e}")
            finally:
                if cursor: cursor.close()
                if conn:   close_db_connection(conn)

        # Kembalikan 'reply' DAN 'response' agar kompatibel dengan semua versi frontend
        return jsonify({"reply": ai_reply, "response": ai_reply})

    except Exception as e:
        current_app.logger.error(f"Internal error in chat(): {e}")
        return jsonify({"error": "Terjadi kesalahan internal", "detail": str(e)}), 500


def _format_sympy_output(engine_result: dict) -> str:
    """Format SymPy calculation result untuk display"""
    result_type = engine_result.get("type", "unknown")
    
    if result_type == "solve":
        solutions = engine_result.get("solutions_latex", [])
        solutions_text = " atau ".join([f"$${sol}$$" for sol in solutions])
        return f"**Solusi:**\n\n{solutions_text}"
    
    elif result_type == "integration":
        result_latex = engine_result.get("result_latex", "")
        original = engine_result.get("original", "")
        return f"**Integral:**\n\n$$\\int {original} \\, dx = {result_latex} + C$$"
    
    elif result_type == "derivation":
        result_latex = engine_result.get("result_latex", "")
        original = engine_result.get("original", "")
        return f"**Turunan:**\n\n$$\\frac{{d}}{{dx}} \\left( {original} \\right) = {result_latex}$$"
    
    elif result_type == "simplify":
        simplified = engine_result.get("simplified_latex", "")
        original = engine_result.get("original", "")
        return f"**Penyederhanaan:**\n\nDari: ${original}$\n\nMenjadi: ${simplified}$"
    
    elif result_type == "expand":
        expanded = engine_result.get("expanded_latex", "")
        original = engine_result.get("original", "")
        return f"**Pengembangan:**\n\n${original}$ \u2192 ${expanded}$"
    
    return ""


# ==============================================================================
# PROMPT WRAPPER — Middleware untuk memformat input user
# ==============================================================================

def process_user_query(user_input: str) -> str:
    """
    Sanitasi dasar input pengguna tanpa menyuntikkan teks/contoh kaku.
    """
    return user_input.strip()


def chat_ai_logic(data: dict) -> dict:
    """
    Fungsi wrapper yang dipanggil oleh ai_routes.py (blueprint lama).
    Menggunakan logika yang sama dengan chat() tapi tanpa request context.
    """
    user_message = (data.get('message') or '').strip()
    if not user_message:
        return {'error': 'Pesan tidak boleh kosong'}

    user_message = preprocess_user_input(user_message)

    system_content = SYSTEM_PROMPT
    table = current_app.config.get('TABLE')
    if table:
        system_content += f'\n\n---\n\nTabel Referensi:\n{table}'

    try:
        client = LLMClient(provider='gemini')
        
        # Gunakan middleware wrapper untuk memformat input user
        formatted_user_input = process_user_query(user_message)
        
        messages = [
            {'role': 'system', 'content': system_content},
            {'role': 'user',   'content': formatted_user_input},
        ]
        ai_reply = client.generate(messages=messages, temperature=0.3, top_p=0.95, max_output_tokens=8192).strip()
        if not ai_reply:
            ai_reply = '(AI tidak memberikan jawaban)'
        else:
            ai_reply = enhance_ai_response(ai_reply)
        return {'response': ai_reply, 'reply': ai_reply}
    except Exception as e:
        current_app.logger.error(f'chat_ai_logic error: {e}')
        return {'error': str(e)}

