# Plan Strategy - MathThon AI Chatbot Fixes

Menganalisis dan memperbaiki 3 masalah utama chatbot AI (Verbosity/Pengulangan, Halusinasi Istilah "Adjungat"/"Opis", & Formatting LaTeX Patah di UI) sesuai dengan 4 langkah perbaikan teknis yang diminta.

## User Review Required

> [!IMPORTANT]
> **Perubahan Utama Backend & Prompt:**
> 1. **System Prompt**: Memasang aturan ketat fokus ke pertanyaan, memaksakan Glosarium Trigonometri Indonesia resmi (*Sisi Depan*, *Sisi Samping*, *Sisi Miring/Hipotenusa*), melarang keras istilah *opis*, *adjungat*, *sisi seni*, *sisi kiri*, dan membatasi agar tidak merangkum/mengulang percakapan terdahulu.
> 2. **Konfigurasi API Model**: Mengunci `temperature` ke `0.0` dan `top_p` ke `0.1` pada `LLMClient` (termasuk Gemini API GenerationConfig dan Ollama payload options).
> 3. **Context Window & Chat History**: Membatasi `max_context_messages` ke **4 pesan** (maksimal 2 turn percakapan terakhir) serta memperkuat sanitasi riwayat chat (`sanitize_chat_history` & `filter_messages`) untuk membuang kontaminasi jawaban lama.
> 4. **KaTeX Styling Reset**: Menambahkan CSS reset untuk `.katex-display` dan `.katex` di UI frontend agar rendering rumus tidak mengalami line-height aneh atau pembatas baris pecah.

---

## Proposed Changes

### Backend AI Module

#### [MODIFY] [llm_client.py](file:///e:/MathThon/Back_End/ai/llm_client.py)
- Memperbarui signature `generate()` dengan default `temperature=0.0` dan `top_p=0.1`.
- Memperbarui `GenerationConfig` pada Gemini API agar menggunakan `top_p=top_p` (menggantikan nilai hardcoded `0.8`).
- Mengirimkan `top_p` pada payload Ollama options.

#### [MODIFY] [chat_api.py](file:///e:/MathThon/Back_End/ai/chat_api.py)
- Mengganti `SYSTEM_PROMPT` dengan instruksi ketat sesuai glosarium baku Indonesia & aturan pemfokusan.
- Mengatur `MEMORY_OPTIMIZER = ChatMemoryOptimizer(max_context_messages=4)` untuk membatasi riwayat context hingga 2 turn terakhir.
- Memastikan pemanggilan `client.generate(...)` selalu menyertakan `temperature=0.0` dan `top_p=0.1`.

#### [MODIFY] [chat_memory_optimizer.py](file:///e:/MathThon/Back_End/ai/chat_memory_optimizer.py)
- Mengubah default `max_context_messages` menjadi `4`.
- Menambahkan istilah halusinasi (`"adjungat"`, `"opis"`, `"sisi seni"`, `"sisi kiri"`) ke daftar pola kontaminasi yang otomatis dibuang dari konteks memori.

---

### Frontend UI / Styling

#### [MODIFY] [ai_feature_user.html](file:///e:/MathThon/Front_End/templates/user/ai_feature_user.html)
- Menambahkan aturan CSS reset khusus KaTeX untuk `.msg-ai-content .katex-display` dan `.msg-ai-content .katex` agar `line-height` dan margin rumus LaTeX terlihat rapi dan tidak terdistorsi.

---

## Verification Plan

### Automated Tests / Verification Scripts
- Menjalankan tes `verify_halusinasi_fix.py` atau script pengujian backend untuk memverifikasi bahwa query trigonometri seperti $\sin(90^\circ)$ atau $\cos(30^\circ)$ memberikan respons langsung, presisi, tanpa kata "adjungat"/"opis", dan tidak mengulang topik lama.

### Manual Verification
- Uji coba pengiriman pertanyaan "Sin 90 nilainya berapa?" pada UI chatbot dan pastikan:
  1. Jawaban fokus hanya pada $\sin(90^\circ) = 1$.
  2. Istilah yang dipakai adalah Sisi Depan, Sisi Samping, Sisi Miring (tidak ada *adjungat*/*opis*).
  3. Formula LaTeX ter-render sempurna tanpa masalah CSS/line-height.
