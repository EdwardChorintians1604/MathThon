# 📋 IMPLEMENTATION GUIDE: MathThon AI Optimization

## ✅ TAHAP 1: KaTeX Rendering Optimization (PALING CEPAT)

### Apa yang Dilakukan:
- **Lazy Rendering**: Hanya render equations saat user scroll dekat
- **Batch Processing**: Process multiple equations efisien
- **Error Handling**: Fallback ke Unicode jika KaTeX gagal
- **Performance Monitoring**: Track rendering speed

### File yang Dibuat:
📄 `Front_End/static/js/katex-renderer-optimized.js`

### Cara Implementasi:

#### Step 1: Update template `ai_feature_user.html`
Tambahkan line ini di bagian `<head>` sebelum `</head>`:

```html
<!-- KaTeX Renderer Optimized -->
<script src="{{ url_for('static', filename='js/katex-renderer-optimized.js') }}"></script>
```

Pastikan urutan script:
```html
<!-- KaTeX library (harus duluan) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>

<!-- Marked untuk markdown (optional) -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

<!-- ✅ OPTIMIZED RENDERER (baru) -->
<script src="{{ url_for('static', filename='js/katex-renderer-optimized.js') }}"></script>
```

#### Step 2: Hapus atau comment out fungsi `renderMath()` lama
Di template yang sama, cari ini dalam tag `<script>`:
```javascript
// ── Math rendering ── 
function renderMath(el) {
  if (!el) return;
  if (typeof renderMathInElement !== 'undefined') {
    // ... old code ...
  }
}
```

Ganti dengan:
```javascript
// ✅ Sudah di-override oleh katex-renderer-optimized.js
// Fungsi lama dihapus atau di-comment
```

#### Step 3: Testing
Buka browser console (F12 → Console) dan test:
```javascript
// Test 1: Lihat stats
MathRendererDebug.getStats()

// Test 2: Force render semua
MathRendererDebug.renderAll()

// Test 3: Reset observer
MathRendererDebug.forceResetObserver()
```

Expected output:
```
✅ KaTeX Renderer Optimized loaded
```

---

## 🚀 TAHAP 2: System Prompt & Backend Integration

### Apa yang Dilakukan:
- Membuat system prompt yang **presisi & ketat** (anti-halusinasi)
- Implementasi context filtering (anti-poisoning)
- Konfigurasi model yang lebih baik

### File yang Perlu Diupdate:
📝 `Back_End/ai/chat_api.py` → System prompt yang lebih baik
📝 `Back_End/config.py` → Config untuk chat context

### Implementation Details: [Lihat TAHAP_2.md](./TAHAP_2.md)

---

## 🧠 TAHAP 3: Chat Memory Filtering & Context Optimization

### Apa yang Dilakukan:
- Filter pesan kasar/spam dari chat history
- Batasi context window (sliding window)
- Isolasi context antar conversation
- Cache response untuk query serupa

### File yang Dibuat:
📄 `Back_End/ai/chat_memory_optimizer.py`

### Fitur:
```python
from chat_memory_optimizer import ChatMemoryOptimizer

optimizer = ChatMemoryOptimizer(max_context_messages=5)

# Filter & optimize messages
optimized = optimizer.optimize_messages(
    messages=[...],
    max_tokens=2000
)

# Check untuk context poisoning
is_poisoned = optimizer.detect_poisoning(messages)
```

### Implementation Details: [Lihat TAHAP_3.md](./TAHAP_3.md)

---

## 🔍 TAHAP 4: RAG (Retrieval-Augmented Generation) Setup

### Apa yang Dilakukan:
- Buat vector database dari materi matematika
- Retrieve konteks relevan saat AI menjawab
- Prevent hallucination dengan grounding pada data riil

### File yang Dibuat:
📄 `Back_End/ai/rag_system.py` → RAG implementation
📄 `Back_End/ai/vector_db_manager.py` → Vector database manager

### Setup:
```bash
pip install chromadb
```

### Fitur:
```python
from rag_system import RAGSystem

rag = RAGSystem()

# Ingest materi
rag.ingest_documents([
    {"content": "Hukum Euler: e^(ix) = cos(x) + i*sin(x)", "metadata": {"type": "theorem"}},
    # ... more documents
])

# Query dengan RAG
context = rag.retrieve(query="Apa itu Hukum Euler?", top_k=3)
# context = ["e^(ix) = cos(x) + i*sin(x)", ...]

# Gunakan context dalam prompt
prompt = f"Berdasarkan: {context}\n\nUser: {user_query}"
```

### Implementation Details: [Lihat TAHAP_4.md](./TAHAP_4.md)

---

## ⚡ TAHAP 5: Hybrid Calculation Engine (SymPy + LLM)

### Apa yang Dilakukan:
- Routing: Chat biasa → LLM, Calculation → SymPy
- Solve equations dengan SymPy
- Verify output untuk akurasi
- Hybrid response: kombinasi symbolic + natural language

### File yang Dibuat:
📄 `Back_End/ai/calculation_engine.py` → Engine hybrid

### Setup:
```bash
pip install sympy
```

### Fitur:
```python
from calculation_engine import HybridCalculationEngine

engine = HybridCalculationEngine()

# Auto-detect jika query adalah calculation
result = engine.process(
    user_query="Selesaikan integral ∫ x² dx",
    use_llm_fallback=True
)

# Result = {
#   "type": "calculation",
#   "sympy_result": "x³/3 + C",
#   "explanation": "..."
# }
```

### Implementation Details: [Lihat TAHAP_5.md](./TAHAP_5.md)

---

## 📊 Summary Implementasi

| Tahap | Priority | Est. Time | Impact | Status |
|-------|----------|-----------|--------|--------|
| 1. KaTeX Optimization | 🔴 HIGH | 10 min | Tampilan rapi | ✅ Ready |
| 2. System Prompt | 🔴 HIGH | 15 min | Anti-halusinasi | 🔄 In-progress |
| 3. Memory Filtering | 🟡 MEDIUM | 30 min | Context clarity | 📋 Planned |
| 4. RAG Setup | 🟡 MEDIUM | 1 hour | Accuracy | 📋 Planned |
| 5. Hybrid Engine | 🟡 MEDIUM | 1.5 hours | Speed | 📋 Planned |

---

## 🔗 Quick Links
- [Tahap 1 Implementasi](#tahap-1-katex-rendering-optimization-paling-cepat)
- [Tahap 2: System Prompt](./TAHAP_2.md)
- [Tahap 3: Memory Filtering](./TAHAP_3.md)
- [Tahap 4: RAG Setup](./TAHAP_4.md)
- [Tahap 5: Hybrid Engine](./TAHAP_5.md)

---

## ✨ Monitoring & Testing

### Check KaTeX Performance:
```javascript
// Di browser console
MathRendererDebug.getStats()
// Output: { observedCount, queueLength, isRendering }
```

### Check System Prompt:
```bash
# Di terminal, test backend
curl -X POST http://localhost:5000/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Apa itu Hukum Euler?"}'
```

### Verify RAG:
```python
# Di Python shell
from rag_system import RAGSystem
rag = RAGSystem()
print(rag.retrieve("Hukum Euler", top_k=1))
```

---

## 📚 References
- KaTeX Docs: https://katex.org/
- ChromaDB: https://www.trychroma.com/
- SymPy: https://docs.sympy.org/
- Marked.js: https://marked.js.org/
