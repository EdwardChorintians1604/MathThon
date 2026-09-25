from flask import Flask, render_template, request, jsonify
import json
import os 
from datetime import datetime

# Database Kasus (Case Base) - Expert Cases for Website Feedback
# Features (Ciri):
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

def submit_feedback_internal():
    try:
        data = request.get_json()
        user_features = data.get('features', [])
        user_comment = data.get('comment', '')
        user_name = data.get('name', 'Anonymous')

        best_match = None
        highest_similarity = 0

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
                'similarity': highest_similarity,
                'recommendation': best_match['rekomendasi'] if best_match else 'Terima kasih atas feedback Anda.'
            }
        }

        file_path = 'feedback_data.json'
        all_feedback = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    all_feedback = json.load(f)
                except:
                    all_feedback = []
        
        all_feedback.append(feedback_record)
        with open(file_path, 'w') as f:
            json.dump(all_feedback, f, indent=4)

        return jsonify({
            'success': True,
            'message': 'Feedback berhasil dianalisis',
            'analysis': feedback_record['analysis']
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Standalone run for testing only
if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/api/feedback/submit', methods=['POST'])
    def test_submit():
        return submit_feedback_internal()
        
    app.run(debug=True, port=5001)
