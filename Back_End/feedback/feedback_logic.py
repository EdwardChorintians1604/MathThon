from flask import current_app
import json
import os
from datetime import datetime

# Database Kasus (Case Base) - Expert Cases for Website Feedback
# Features List:
# F1: Visual desain estetik/premium
# F2: Navigasi antar menu membingungkan
# F3: Kecepatan loading halaman sangat baik
# F4: Performa berat/lag ketika load grafik/chart
# F5: Materi edukasi sangat lengkap dan membantu
# F6: Penjelasan teori matematika terlalu rumit/sulit dipahami
# F7: Terjadi error saat interaksi (button tidak merespon)
# F8: Sidenav/Sidebar sulit dibuka di perangkat mobile
# F9: Animasi dan transisi halaman sangat halus
# F10: Kurangnya contoh soal berbasis kasus nyata
# F11: Fitur kalkulator tidak memberikan hasil akurat
# F12: Kontras warna dan ukuran font sulit dibaca

EXPERT_FEEDBACK_CASES = [
    {
        'id': 'CAT_UI_POS',
        'category': 'Desain & UI',
        'ciri': ['F1', 'F9'],
        'status': 'Sangat Positif',
        'rekomendasi': 'Estetika visual sudah sangat baik. Pertahankan penggunaan transisi halus dan tingkatkan micro-interactions.'
    },
    {
        'id': 'CAT_UI_NEG',
        'category': 'Desain & UI',
        'ciri': ['F2', 'F12'],
        'status': 'Perlu Perbaikan UX',
        'rekomendasi': 'Evaluasi hirarki informasi. Perbaiki kontras warna teks dan sederhanakan alur navigasi agar lebih intuitif.'
    },
    {
        'id': 'CAT_PERF_POS',
        'category': 'Performa',
        'ciri': ['F3'],
        'status': 'Sangat Baik',
        'rekomendasi': 'Kecepatan akses optimal. Pastikan optimasi server tetap stabil seiring bertambahnya trafik.'
    },
    {
        'id': 'CAT_PERF_NEG',
        'category': 'Performa',
        'ciri': ['F4'],
        'status': 'Isu Optimasi',
        'rekomendasi': 'Optimasi rendering Chart.js. Gunakan data lazy loading atau kurangi kompleksitas visual pada grafik berat.'
    },
    {
        'id': 'CAT_CONTENT_POS',
        'category': 'Konten Materi',
        'ciri': ['F5'],
        'status': 'Berkualitas',
        'rekomendasi': 'Konten sudah komprehensif. Tambahkan fitur bookmark materi untuk kemudahan akses kembali.'
    },
    {
        'id': 'CAT_CONTENT_NEG',
        'category': 'Konten Materi',
        'ciri': ['F6', 'F10'],
        'status': 'Perlu Penyederhanaan',
        'rekomendasi': 'Gunakan bahasa yang lebih ramah pemula (ELI5). Tambahkan lebih banyak studi kasus dunia nyata.'
    },
    {
        'id': 'CAT_TECH_BUG',
        'category': 'Teknis & Bug',
        'ciri': ['F7', 'F11'],
        'status': 'Kritis',
        'rekomendasi': 'Lakukan debugging pada function JavaScript terkait. Unit testing diperlukan untuk fitur kalkulator.'
    },
    {
        'id': 'CAT_MOBILE_ISSUE',
        'category': 'Responsivitas',
        'ciri': ['F8'],
        'status': 'Isu Mobile',
        'rekomendasi': 'Perbaiki z-index sidenav dan sensitivitas touch event pada perangkat Android/iOS.'
    }
]

def calculate_similarity(target_case, source_case):
    if not source_case:
        return 0
    matches = 0
    for feature in source_case:
        if feature in target_case:
            matches += 1
    return matches / len(source_case) if len(source_case) > 0 else 0
    
def analyze_and_save_feedback(feedback_data):
    """
    Menganalisis feedback pengguna menggunakan CBR, menyimpannya ke file JSON,
    dan mengembalikan hasil analisis.
    """
    user_features = feedback_data.get('features', [])
    user_comment = feedback_data.get('comment', '')
    user_name = feedback_data.get('name', 'Anonymous')

    best_match = None
    highest_similarity = 0

    # Phase: RETRIEVE
    for case in EXPERT_FEEDBACK_CASES:
        sim = calculate_similarity(user_features, case['ciri'])
        if sim > highest_similarity:
            highest_similarity = sim
            best_match = case

    feedback_record = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'user': user_name,
        'features': user_features,
        'comment': user_comment,
        'analysis': {
            'category': best_match['category'] if best_match else 'General',
            'status': best_match['status'] if best_match else 'Neutral',
            'similarity': f"{highest_similarity:.2%}",
            'recommendation': best_match['rekomendasi'] if best_match else 'Terima kasih atas feedback Anda. Kami akan meninjau saran Anda.'
        }
    }

    # Gunakan path absolut yang aman. current_app.root_path menunjuk ke folder 'Back_End'
    # Kita simpan feedback_data.json di root project (sejajar dengan app.py)
    base_dir = os.path.dirname(current_app.root_path) # Naik satu level dari Back_End
    file_path = os.path.join(base_dir, 'feedback_data.json')
    
    all_feedback = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                all_feedback = json.load(f)
        except Exception:
            all_feedback = [] # Buat list baru jika file error/kosong
    
    all_feedback.insert(0, feedback_record) # Tambahkan feedback baru di paling atas
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_feedback, f, indent=4)

    return feedback_record['analysis']

def get_all_feedback():
    """Membaca semua data feedback dari file JSON."""
    base_dir = os.path.dirname(current_app.root_path)
    file_path = os.path.join(base_dir, 'feedback_data.json')
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []
