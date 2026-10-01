"""
Service: AI Tutor & Active Recall Scaffolding Validator
Memvalidasi jawaban multi-tahap, mendeteksi miskonsepsi matematika siswa,
dan memberikan petunjuk adaptif secara real-time via LLM (Gemini/Ollama)
atau Pedagogical Heuristic Fallback.
"""
import re
import logging
from typing import Dict, Any, Optional, Tuple
from Back_End.core.config import settings

logger = logging.getLogger(__name__)

# Katalog Soal Scaffolding Multi-Tahap per Modul/Materi
CHECKPOINT_CURRICULUM = {
    "integral": {
        "title": "Evaluasi & Akumulasi Integral",
        "steps": [
            {
                "step": 1,
                "question": "Diberikan $f(x) = 3x^2 + 4x$. Tentukan antiturunan suku pertama $\\int 3x^2\\,dx$ (abaikan konstanta $+C$ dulu).",
                "concept": "Aturan pangkat integral: int(a x^n dx) = a/(n+1) x^(n+1). Untuk 3x^2, n=2, sehingga 3/3 x^3 = x^3.",
                "valid_answers": ["x^3", "x**3", "1x^3", "1x**3", "x kubik"],
                "target_representation": "x^3"
            },
            {
                "step": 2,
                "question": "Sekarang tentukan antiturunan suku kedua $\\int 4x\\,dx$.",
                "concept": "Untuk 4x, n=1, sehingga 4/2 x^2 = 2x^2.",
                "valid_answers": ["2x^2", "2x**2", "2*x^2", "2*x**2"],
                "target_representation": "2x^2"
            },
            {
                "step": 3,
                "question": "Tuliskan bentuk umum antiturunan lengkap $F(x) = \\int (3x^2 + 4x)\\,dx$ beserta konstanta integrasinya.",
                "concept": "Gabungan antiturunan suku-suku ditambah C: x^3 + 2x^2 + C.",
                "valid_answers": ["x^3+2x^2+c", "x^3 + 2x^2 + c", "x**3+2x**2+c", "x^3 + 2x^2 + C"],
                "target_representation": "x^3 + 2x^2 + C"
            },
            {
                "step": 4,
                "question": "Hitung nilai integral tentu $\\int_{0}^{2} (3x^2 + 4x)\\,dx$. Berapakah angka pastinya?",
                "concept": "Substitusi batas atas F(2) - F(0): (2^3 + 2(2^2)) - 0 = (8 + 8) - 0 = 16.",
                "valid_answers": ["16", "16.0", "=16", "16 satuan luas"],
                "target_representation": "16"
            }
        ]
    },
    "limit": {
        "title": "Analisis Bentuk Tak Tentu Limit",
        "steps": [
            {
                "step": 1,
                "question": "Berapakah hasil jika kamu melakukan substitusi langsung $x = 2$ ke $\\frac{x^2 - 4}{x - 2}$?",
                "concept": "Substitusi langsung menghasilkan pembilang 2^2 - 4 = 0 dan penyebut 2 - 2 = 0, yaitu 0/0.",
                "valid_answers": ["0/0", "0 / 0", "tak tentu", "bentuk tak tentu", "nol per nol"],
                "target_representation": "0/0"
            },
            {
                "step": 2,
                "question": "Faktorkan bentuk selisih kuadrat pembilang: $x^2 - 4 = (...)(...)$?",
                "concept": "Faktorisasi selisih dua kuadrat a^2 - b^2 = (a-b)(a+b). Jadi x^2 - 4 = (x-2)(x+2).",
                "valid_answers": ["(x-2)(x+2)", "(x+2)(x-2)", "(x - 2)(x + 2)", "(x + 2)(x - 2)"],
                "target_representation": "(x-2)(x+2)"
            },
            {
                "step": 3,
                "question": "Setelah suku pembuat nol $(x-2)$ dicoret/dieliminasi, bentuk fungsi yang tersisa adalah?",
                "concept": "Membagi pembilang dan penyebut dengan (x-2) menyisakan (x+2).",
                "valid_answers": ["x+2", "x + 2", "(x+2)"],
                "target_representation": "x+2"
            },
            {
                "step": 4,
                "question": "Masukkan $x = 2$ ke bentuk sederhana tersebut. Berapakah nilai limit akhirnya?",
                "concept": "Substitusi x = 2 ke (x + 2) menghasilkan 2 + 2 = 4.",
                "valid_answers": ["4", "4.0", "=4"],
                "target_representation": "4"
            }
        ]
    },
    "fungsi_turunan": {
        "title": "Kalkulus Diferensial & Aturan Rantai",
        "steps": [
            {
                "step": 1,
                "question": "Tentukan turunan pertama dari $3x^2$ terhadap $x$.",
                "concept": "Aturan pangkat: d/dx(a x^n) = a*n x^(n-1). 3*2 x^(2-1) = 6x.",
                "valid_answers": ["6x", "6*x"],
                "target_representation": "6x"
            },
            {
                "step": 2,
                "question": "Tentukan turunan pertama dari $-4x$ terhadap $x$.",
                "concept": "Turunan dari ax adalah a. Jadi turunan -4x adalah -4.",
                "valid_answers": ["-4", "minus 4"],
                "target_representation": "-4"
            },
            {
                "step": 3,
                "question": "Gabungkan hasil keduanya untuk fungsi $f(x) = 3x^2 - 4x$. Tuliskan fungsi $f'(x)$.",
                "concept": "f'(x) = 6x - 4.",
                "valid_answers": ["6x-4", "6x - 4", "f'(x)=6x-4"],
                "target_representation": "6x - 4"
            },
            {
                "step": 4,
                "question": "Berapakah kemiringan (gradien) garis singgung kurva di titik $x = 3$?",
                "concept": "Substitusi x = 3 ke f'(x): 6(3) - 4 = 18 - 4 = 14.",
                "valid_answers": ["14", "14.0", "m=14"],
                "target_representation": "14"
            }
        ]
    },
    "operasi_kabataku": {
        "title": "Hierarki Operasi & Presedensi PEMDAS",
        "steps": [
            {
                "step": 1,
                "question": "Dalam ekspresi $8 + 2 \\times 5$, operasi manakah yang harus dikerjakan terlebih dahulu?",
                "concept": "Berdasarkan hierarki Ka-Ba-Ta-Ku (PEMDAS), perkalian memiliki prioritas lebih tinggi daripada penjumlahan.",
                "valid_answers": ["perkalian", "kali", "2*5", "2 x 5", "2x5", "perkalian 2x5"],
                "target_representation": "Perkalian (2 x 5)"
            },
            {
                "step": 2,
                "question": "Berapakah hasil dari $2 \\times 5$ tersebut?",
                "concept": "2 dikali 5 sama dengan 10.",
                "valid_answers": ["10", "10.0"],
                "target_representation": "10"
            },
            {
                "step": 3,
                "question": "Sekarang jumlahkan $8 + 10$. Berapakah hasil akhirnya?",
                "concept": "8 + 10 = 18.",
                "valid_answers": ["18", "18.0"],
                "target_representation": "18"
            },
            {
                "step": 4,
                "question": "Selesaikan ekspresi jebakan viral: $6 \\div 2(1 + 2)$. Tuliskan angka hasil akhirnya.",
                "concept": "1+2 = 3. Kemudian 6 : 2 * 3 dihitung dari kiri ke kanan: (6 : 2) * 3 = 3 * 3 = 9.",
                "valid_answers": ["9", "9.0"],
                "target_representation": "9"
            }
        ]
    },
    "aljabar": {
        "title": "Persamaan Linier Satu Variabel (PLSV)",
        "steps": [
            {
                "step": 1,
                "question": "Sederhanakan suku-suku sejenis pada persamaan: $3x + 5x = 24$. Berapakah koefisien $x$ di ruas kiri?",
                "concept": "3x + 5x = (3+5)x = 8x. Koefisiennya adalah 8.",
                "valid_answers": ["8", "8x", "delapan"],
                "target_representation": "8"
            },
            {
                "step": 2,
                "question": "Dari $8x = 24$, operasi apa yang harus dilakukan pada kedua ruas untuk mengisolasi variabel $x$?",
                "concept": "Membagi kedua ruas dengan angka 8.",
                "valid_answers": ["bagi 8", "pembagian", "dibagi 8", "bagi", "pembagian dengan 8"],
                "target_representation": "Dibagi dengan 8"
            },
            {
                "step": 3,
                "question": "Berapakah nilai $x$ dari $x = 24 / 8$?",
                "concept": "24 dibagi 8 sama dengan 3.",
                "valid_answers": ["3", "3.0", "x=3"],
                "target_representation": "3"
            },
            {
                "step": 4,
                "question": "Jika $x = 3$, berapakah nilai dari ekspresi $2x + 7$?",
                "concept": "2(3) + 7 = 6 + 7 = 13.",
                "valid_answers": ["13", "13.0"],
                "target_representation": "13"
            }
        ]
    },
    "matriks": {
        "title": "Operasi & Determinan Matriks 2x2",
        "steps": [
            {
                "step": 1,
                "question": "Diberikan matriks $A = \\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix}$. Tuliskan rumus determinan matriks $2 \\times 2$ untuk $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$.",
                "concept": "Determinan = perkalian diagonal utama dikurang perkalian diagonal samping: ad - bc.",
                "valid_answers": ["ad-bc", "ad - bc", "a*d - b*c", "ad-cb"],
                "target_representation": "ad - bc"
            },
            {
                "step": 2,
                "question": "Hitung hasil kali diagonal utama ($a \\times d$) pada matriks $A$.",
                "concept": "3 dikali 4 sama dengan 12.",
                "valid_answers": ["12", "12.0", "3*4=12"],
                "target_representation": "12"
            },
            {
                "step": 3,
                "question": "Hitung hasil kali diagonal samping ($b \\times c$) pada matriks $A$.",
                "concept": "2 dikali 1 sama dengan 2.",
                "valid_answers": ["2", "2.0", "2*1=2"],
                "target_representation": "2"
            },
            {
                "step": 4,
                "question": "Kurangkan $12 - 2$. Berapakah determinan matriks $A$ ($\det(A)$)?",
                "concept": "12 - 2 = 10.",
                "valid_answers": ["10", "10.0", "det(A)=10"],
                "target_representation": "10"
            }
        ]
    }
}

class AITutorService:
    @staticmethod
    def normalize_str(s: str) -> str:
        """Membersihkan dan menormalisasi string input user untuk perbandingan."""
        if not s:
            return ""
        s = s.strip().lower()
        # Hilangkan spasi berlebih
        s = re.sub(r'\s+', ' ', s)
        # Hilangkan tanda '=' di awal
        s = re.sub(r'^[=\s]+', '', s)
        return s

    @classmethod
    def validate_step(cls, module_key: str, step_index: int, user_answer: str) -> Tuple[bool, bool, Dict[str, Any]]:
        """
        Validasi jawaban untuk step tertentu.
        Return: (is_correct, is_final_step, step_info_dict)
        """
        curriculum = CHECKPOINT_CURRICULUM.get(module_key)
        if not curriculum:
            # Fallback untuk modul dinamis
            curriculum = CHECKPOINT_CURRICULUM.get("integral")

        steps = curriculum["steps"]
        step_idx = max(0, min(step_index - 1, len(steps) - 1))
        current_step = steps[step_idx]
        total_steps = len(steps)
        is_final = (step_index >= total_steps)

        norm_user = cls.normalize_str(user_answer)
        valid_norms = [cls.normalize_str(ans) for ans in current_step["valid_answers"]]

        # Cek kesesuaian jawaban (exact match atau contains)
        is_correct = False
        if norm_user in valid_norms:
            is_correct = True
        else:
            for vn in valid_norms:
                if vn == norm_user or (len(vn) > 3 and vn in norm_user):
                    is_correct = True
                    break

        return is_correct, is_final, current_step

    @classmethod
    def generate_socratic_hint(cls, module_key: str, step_index: int, user_input: str, step_info: dict) -> str:
        """
        Memanggil pipeline RAG / LLM (Gemini/Ollama) untuk menghasilkan petunjuk Socratic
        adaptif secara real-time. Jika offline/rate limit, fallback ke Pedagogical Heuristic.
        """
        question = step_info.get("question", "")
        concept = step_info.get("concept", "")

        # 1. Coba panggil LLMClient (Gemini / Ollama)
        try:
            from Back_End.ai.llm_client import LLMClient
            client = LLMClient(provider="gemini")
            prompt = (
                f"Kamu adalah AI Tutor Matematika MathThon yang ramah, ringkas, dan fokus pada metode Socratic.\n"
                f"Modul Materi: {module_key}\n"
                f"Tahap Soal Ke-{step_index}: {question}\n"
                f"Konsep/Kunci: {concept}\n"
                f"Jawaban Siswa yang Keliru: '{user_input}'\n\n"
                f"INSTRUKSI:\n"
                f"1. Analisis letak kekeliruan logika pemikiran siswa (maksimal 2-3 kalimat hangat).\n"
                f"2. Berikan petunjuk arah pemikiran atau aturan aljabar/kalkulus yang terlupakan.\n"
                f"3. DILARANG KERAS memberikan angka jawaban akhir secara langsung!\n"
                f"Gunakan bahasa Indonesia yang ramah dan memotivasi."
            )
            response = client.generate(prompt)
            if response and len(response.strip()) > 10:
                return response.strip()
        except Exception as e:
            logger.warning(f"[AI Tutor LLM Fallback]: {e}")

        # 2. Pedagogical Heuristic Fallback (Real-time and guaranteed reliable)
        return cls._heuristic_fallback_hint(module_key, step_index, user_input, concept)

    @classmethod
    def _heuristic_fallback_hint(cls, module_key: str, step_index: int, user_input: str, concept: str) -> str:
        """Fallback heuristik pedagogis jika koneksi LLM mengalami kendala."""
        inp = str(user_input).lower().strip()
        
        if "integral" in module_key:
            if "^" not in inp and "**" not in inp and step_index <= 3:
                return "Perhatikan aturan pangkat integral: saat mengintegralkan x^n, pangkat baru menjadi n+1, lalu bagi koefisien depan dengan pangkat baru tersebut. Jangan lupa menuliskan variabel x dan pangkatnya!"
            elif "c" not in inp and step_index == 3:
                return "Hampir benar! Ingat bahwa ini adalah integral tak tentu. Suku apa yang selalu harus ditambahkan di akhir untuk mewakili sembarang konstanta?"
            elif step_index == 4:
                return f"Tinjau kembali substitusi batas atas dan batas bawah: F(2) - F(0). Hitung 2³ terlebih dahulu, lalu tambahkan dengan 2(2²). Hasilnya adalah bilangan bulat positif."

        elif "limit" in module_key:
            if step_index == 1:
                return "Jika kamu langsung memasukkan nilai x ke pembilang dan penyebut, kamu akan mendapatkan bentuk pembagian khusus yang dinamakan 'bentuk tak tentu'. Coba periksa kembali."
            elif step_index == 2:
                return "Gunakan rumus selisih dua kuadrat: a² - b² = (a - b)(a + b). Ingat bahwa angka 4 dapat dituliskan sebagai 2²."
            elif step_index == 4:
                return "Setelah mencoret faktor (x - 2), masukkan x = 2 ke dalam ekspresi yang tersisa (x + 2). Berapakah 2 + 2?"

        elif "fungsi_turunan" in module_key:
            if step_index == 1:
                return "Pada turunan (diferensial), kalikan pangkat lama dengan koefisien di depan, lalu kurangi pangkat x dengan 1: d/dx(3x²) = (3 * 2)x^(2-1)."
            elif step_index == 4:
                return "Ganti nilai x pada gradien f'(x) = 6x - 4 dengan angka 3: hitunglah 6(3) - 4."

        elif "operasi_kabataku" in module_key:
            if "tambah" in inp or "8+2" in inp:
                return "Hati-hati dengan jebakan urutan! Operasi perkalian dan pembagian (Ka-Ba) harus diselesaikan lebih dulu daripada penjumlahan dan pengurangan (Ta-Ku)."
            elif step_index == 4:
                return "Selesaikan tanda kurung (1 + 2 = 3) terlebih dahulu. Kemudian, karena pembagian dan perkalian memiliki derajat yang sama, kerjakan secara berurutan dari kiri ke kanan: 6 dibagi 2, lalu hasilnya dikali 3."

        return f"Tinjau kembali konsep ini: {concept}. Periksa langkah aljabar dan tanda operasimu secara teliti."
