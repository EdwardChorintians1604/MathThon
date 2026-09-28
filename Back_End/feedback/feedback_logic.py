from flask import current_app
import json
import os
import re
import uuid
from collections import Counter
from datetime import datetime

# ==============================================================================
# 1. FORMAL FEATURE REGISTRY & DOMAIN DICTIONARY
# ==============================================================================
FEATURE_DEFINITIONS = {
    'F1': {
        'name': 'Visual UI Premium',
        'category': 'Desain & UI',
        'polarity': 'positive',
        'weight': 1.0,
        'icon': 'bi-brush',
        'badge_class': 'badge-success'
    },
    'F2': {
        'name': 'Navigasi Membingungkan',
        'category': 'Desain & UI',
        'polarity': 'negative',
        'weight': 1.3,
        'icon': 'bi-signpost-split',
        'badge_class': 'badge-warning'
    },
    'F3': {
        'name': 'Loading Sangat Cepat',
        'category': 'Performa',
        'polarity': 'positive',
        'weight': 1.0,
        'icon': 'bi-lightning-charge',
        'badge_class': 'badge-success'
    },
    'F4': {
        'name': 'Grafik Lag / Berat',
        'category': 'Performa',
        'polarity': 'negative',
        'weight': 1.5,
        'icon': 'bi-graph-down',
        'badge_class': 'badge-danger'
    },
    'F5': {
        'name': 'Materi Edukasi Lengkap',
        'category': 'Konten Materi',
        'polarity': 'positive',
        'weight': 1.0,
        'icon': 'bi-journal-check',
        'badge_class': 'badge-success'
    },
    'F6': {
        'name': 'Teori Terlalu Rumit',
        'category': 'Konten Materi',
        'polarity': 'negative',
        'weight': 1.2,
        'icon': 'bi-brain',
        'badge_class': 'badge-warning'
    },
    'F7': {
        'name': 'Error / Bug Interaksi',
        'category': 'Teknis & Bug',
        'polarity': 'critical',
        'weight': 2.0,
        'icon': 'bi-bug',
        'badge_class': 'badge-danger'
    },
    'F8': {
        'name': 'Sidenav Mobile Macet',
        'category': 'Responsivitas',
        'polarity': 'negative',
        'weight': 1.3,
        'icon': 'bi-phone',
        'badge_class': 'badge-warning'
    },
    'F9': {
        'name': 'Animasi & Transisi Halus',
        'category': 'Desain & UI',
        'polarity': 'positive',
        'weight': 1.0,
        'icon': 'bi-stars',
        'badge_class': 'badge-success'
    },
    'F10': {
        'name': 'Kurang Contoh Kasus Nyata',
        'category': 'Konten Materi',
        'polarity': 'negative',
        'weight': 1.1,
        'icon': 'bi-lightbulb',
        'badge_class': 'badge-warning'
    },
    'F11': {
        'name': 'Kalkulator Tidak Akurat',
        'category': 'Teknis & Bug',
        'polarity': 'critical',
        'weight': 2.0,
        'icon': 'bi-calculator',
        'badge_class': 'badge-danger'
    },
    'F12': {
        'name': 'Font / Kontras Sulit Dibaca',
        'category': 'Desain & UI',
        'polarity': 'negative',
        'weight': 1.2,
        'icon': 'bi-eye-slash',
        'badge_class': 'badge-warning'
    }
}

# ==============================================================================
# 2. CASE BASE (EXPERT KNOWLEDGE REPOSITORY)
# ==============================================================================
EXPERT_FEEDBACK_CASES = [
    {
        'id': 'CAT_TECH_CRITICAL',
        'category': 'Teknis & Bug',
        'ciri': ['F7', 'F11'],
        'status': 'Kritis',
        'default_priority': 'kritis',
        'target_polarity': 'critical',
        'keywords': ['bug', 'error', 'rusak', 'kalkulator', 'salah', 'crash', 'keamanan', 'celah', 'hacker', 'serangan', 'tombol', 'respon'],
        'rekomendasi': 'Lakukan debugging pada function JavaScript dan kalkulator matematika. Terapkan automated testing serta audit integritas server.'
    },
    {
        'id': 'CAT_PERF_LAG',
        'category': 'Performa',
        'ciri': ['F4'],
        'status': 'Isu Optimasi',
        'default_priority': 'tinggi',
        'target_polarity': 'negative',
        'keywords': ['lag', 'berat', 'lemot', 'lambat', 'grafik', 'chart', 'fps', 'rendering', 'beban', 'memory'],
        'rekomendasi': 'Optimasi rendering Chart.js, terapkan data lazy loading atau debouncing, dan kurangi kompleksitas kalkulasi visual saat load grafik.'
    },
    {
        'id': 'CAT_PERF_POS',
        'category': 'Performa',
        'ciri': ['F3'],
        'status': 'Sangat Baik',
        'default_priority': 'rendah',
        'target_polarity': 'positive',
        'keywords': ['cepat', 'kencang', 'lancar', 'ngebut', 'responsif', 'stabil', 'ringan'],
        'rekomendasi': 'Kecepatan respon sistem sudah optimal. Pertahankan konfigurasi browser caching, Gzip compression, dan monitoring CDN.'
    },
    {
        'id': 'CAT_UI_NEG',
        'category': 'Desain & UI',
        'ciri': ['F2', 'F12'],
        'status': 'Perlu Perbaikan UX',
        'default_priority': 'normal',
        'target_polarity': 'negative',
        'keywords': ['navigasi', 'bingung', 'font', 'warna', 'kontras', 'buruk', 'tulisan', 'gelap', 'sulit', 'baca', 'desain', 'tampilan', 'layout'],
        'rekomendasi': 'Evaluasi hierarki visual. Perbaiki rasio kontras warna font sesuai pedoman WCAG AA dan sederhanakan breadcrumb navigasi menu.'
    },
    {
        'id': 'CAT_UI_POS',
        'category': 'Desain & UI',
        'ciri': ['F1', 'F9'],
        'status': 'Sangat Positif',
        'default_priority': 'rendah',
        'target_polarity': 'positive',
        'keywords': ['estetik', 'premium', 'indah', 'bagus', 'keren', 'cantik', 'animasi', 'halus', 'modern', 'elegan', 'rapi'],
        'rekomendasi': 'Estetika visual dan animasi dinilai memuaskan. Pertahankan konsistensi design token dan kembangkan micro-interactions yang interaktif.'
    },
    {
        'id': 'CAT_CONTENT_NEG',
        'category': 'Konten Materi',
        'ciri': ['F6', 'F10'],
        'status': 'Perlu Penyederhanaan',
        'default_priority': 'normal',
        'target_polarity': 'negative',
        'keywords': ['rumit', 'sulit', 'susah', 'teori', 'contoh', 'nyata', 'industri', 'pusing', 'penjelasan', 'aplikasi', 'kurikulum'],
        'rekomendasi': 'Sederhanakan pemaparan rumus dengan pendekatan kontekstual (ELI5). Tambahkan lebih banyak simulasi kasus nyata di industri.'
    },
    {
        'id': 'CAT_CONTENT_POS',
        'category': 'Konten Materi',
        'ciri': ['F5'],
        'status': 'Berkualitas',
        'default_priority': 'rendah',
        'target_polarity': 'positive',
        'keywords': ['lengkap', 'jelas', 'membantu', 'paham', 'komprehensif', 'bagus', 'terstruktur', 'edukatif'],
        'rekomendasi': 'Materi kurikulum sudah komprehensif. Tambahkan fitur bookmark materi dan latihan soal berjenjang adaptif.'
    },
    {
        'id': 'CAT_MOBILE_ISSUE',
        'category': 'Responsivitas',
        'ciri': ['F8'],
        'status': 'Isu Mobile',
        'default_priority': 'tinggi',
        'target_polarity': 'negative',
        'keywords': ['mobile', 'hp', 'smartphone', 'layar', 'sidenav', 'sidebar', 'sentuh', 'touch', 'responsif', 'geser', 'android', 'ios'],
        'rekomendasi': 'Perbaiki z-index sidenav overlay, sesuaikan touch target button, dan uji kompatibilitas responsive di berbagai resolusi layar HP.'
    }
]

# ==============================================================================
# 3. INDONESIAN LEXICON & NLP SENTIMENT HEURISTICS
# ==============================================================================
POSITIVE_LEXICON = {
    'bagus', 'keren', 'mantap', 'hebat', 'cepat', 'lancar', 'membantu', 'suka',
    'estetik', 'optimal', 'rapi', 'lengkap', 'puas', 'halus', 'elegan', 'jelas',
    'mudah', 'terima', 'kasih', 'indah', 'top', 'sempurna', 'terbaik', 'senang'
}

NEGATIVE_LEXICON = {
    'bug', 'error', 'rusak', 'gagal', 'salah', 'lag', 'lemot', 'lambat', 'jelek',
    'buruk', 'hancur', 'celah', 'keamanan', 'serangan', 'membingungkan', 'sulit',
    'susah', 'perbaiki', 'tolong', 'tidak', 'kurang', 'berat', 'macet', 'pusing',
    'kecewa', 'bermasalah', 'crash', 'buntu', 'hang', 'ngelag', 'rumit'
}

CRITICAL_LEXICON = {
    'bug', 'error', 'kritis', 'keamanan', 'celah', 'hacker', 'serangan',
    'hancur', 'rusak', 'crash', 'fatal', 'kebobolan'
}

def analyze_text_sentiment(text: str):
    """
    Menganalisis sentimen teks berbahasa Indonesia dengan heuristik leksikon,
    deteksi kata negasi, serta kata pemicu kritis.
    """
    if not text or not text.strip():
        return {'score': 0.0, 'sentiment': 'Netral', 'has_critical': False}

    words = re.findall(r'\b[a-zA-Z0-9_-]+\b', text.lower())
    if not words:
        return {'score': 0.0, 'sentiment': 'Netral', 'has_critical': False}

    pos_count = 0
    neg_count = 0
    has_critical = False

    negation_active = False
    negation_window = 0

    for word in words:
        if word in {'tidak', 'bukan', 'kurang', 'belum', 'jangan', 'tanpa'}:
            negation_active = True
            negation_window = 3
            continue

        is_pos = word in POSITIVE_LEXICON
        is_neg = word in NEGATIVE_LEXICON
        if word in CRITICAL_LEXICON:
            has_critical = True

        if negation_active and negation_window > 0:
            negation_window -= 1
            if is_pos:
                neg_count += 1.5
            elif is_neg:
                pos_count += 0.8
            continue
        else:
            negation_active = False

        if is_pos:
            pos_count += 1
        if is_neg:
            neg_count += 1.2

    total_hits = pos_count + neg_count
    if total_hits == 0:
        score = 0.0
    else:
        score = (pos_count - neg_count) / max(1.0, total_hits)

    if has_critical or score <= -0.25:
        sentiment = 'Kritis / Negatif' if has_critical else 'Negatif'
    elif score >= 0.25:
        sentiment = 'Positif'
    else:
        sentiment = 'Netral'

    return {
        'score': round(score, 2),
        'sentiment': sentiment,
        'has_critical': has_critical,
        'words': set(words)
    }

# ==============================================================================
# 4. HYBRID CBR SIMILARITY ALGORITHM (WEIGHTED SØRENSEN-DICE + TEXT AFFINITY)
# ==============================================================================
def calculate_feature_dice(user_features: list, case_features: list) -> float:
    """
    Menghitung weighted Sørensen-Dice similarity antar himpunan fitur.
    Mencegah bias 100% pada case berskala kecil saat input user kompleks.
    """
    if not case_features and not user_features:
        return 0.0
    if not case_features or not user_features:
        return 0.0

    user_set = set(user_features)
    case_set = set(case_features)

    intersection = user_set.intersection(case_set)
    if not intersection:
        return 0.0

    inter_weight = sum(FEATURE_DEFINITIONS.get(f, {}).get('weight', 1.0) for f in intersection)
    user_weight = sum(FEATURE_DEFINITIONS.get(f, {}).get('weight', 1.0) for f in user_set)
    case_weight = sum(FEATURE_DEFINITIONS.get(f, {}).get('weight', 1.0) for f in case_set)

    denominator = user_weight + case_weight
    if denominator <= 0:
        return 0.0

    return (2.0 * inter_weight) / denominator

def calculate_text_similarity(comment_words: set, case: dict) -> float:
    """
    Menghitung kemiripan kata kunci komentar dengan case base.
    """
    if not comment_words or not case.get('keywords'):
        return 0.0

    case_keywords = set(case['keywords'])
    matches = comment_words.intersection(case_keywords)
    if not matches:
        return 0.0

    # Normalisasi berbasis akar kata agar komentar pendek bernas tetap bernilai tinggi
    matched_score = len(matches) / max(1.5, (len(case_keywords) ** 0.5))
    return min(1.0, matched_score)

def evaluate_cbr_cases(user_features: list, user_comment: str):
    """
    Eksekusi CBR Retrieve & Revise dengan algoritma Hybrid:
    - Weighted Feature Matching
    - Semantic Text Keyword Matching
    - Polarity Alignment Penalty/Boost
    """
    text_eval = analyze_text_sentiment(user_comment)
    comment_words = text_eval['words'] if 'words' in text_eval else set()

    best_match = None
    highest_similarity = -1.0

    has_features = bool(user_features)
    has_comment = bool(user_comment and user_comment.strip())

    for case in EXPERT_FEEDBACK_CASES:
        sim_features = calculate_feature_dice(user_features, case['ciri'])
        sim_text = calculate_text_similarity(comment_words, case)

        # Bobot perpaduan fitur dan teks
        if has_features and has_comment:
            sim_score = (0.65 * sim_features) + (0.35 * sim_text)
        elif has_features:
            sim_score = sim_features
        elif has_comment:
            sim_score = sim_text
        else:
            sim_score = 0.0

        # Penyesuaian polaritas (Penalti & Boost):
        # Jika user mengeluhkan bug/isu kritis tapi case ini statusnya 'Sangat Baik' / Positif,
        # beri penalti agar tidak salah diagnosis.
        if (text_eval['has_critical'] or text_eval['sentiment'] in {'Negatif', 'Kritis / Negatif'}) and case['target_polarity'] == 'positive':
            sim_score *= 0.15
        elif text_eval['sentiment'] == 'Positif' and case['target_polarity'] in {'negative', 'critical'}:
            sim_score *= 0.25

        # Boost khusus jika user memilih F7/F11 dan case ini menangani Teknis & Bug
        if any(f in {'F7', 'F11'} for f in user_features) and case['category'] == 'Teknis & Bug':
            sim_score = min(1.0, sim_score + 0.20)

        if sim_score > highest_similarity:
            highest_similarity = sim_score
            best_match = case

    # Fallback jika tidak ada kesamaan fitur maupun komentar
    if highest_similarity <= 0.0 or best_match is None:
        highest_similarity = 0.0
        best_match = {
            'id': 'CAT_GENERAL',
            'category': 'General',
            'status': 'Neutral',
            'default_priority': 'normal',
            'target_polarity': 'neutral',
            'rekomendasi': 'Terima kasih atas feedback Anda. Tim MathThon akan meninjau saran Anda secara berkala.'
        }

    # Tentukan prioritas cerdas
    calculated_priority = best_match.get('default_priority', 'normal')
    if text_eval['has_critical'] or any(f in {'F7', 'F11'} for f in user_features):
        calculated_priority = 'kritis'
    elif any(f in {'F4', 'F8'} for f in user_features) or text_eval['sentiment'] == 'Negatif':
        if calculated_priority not in {'kritis'}:
            calculated_priority = 'tinggi'

    return {
        'best_case': best_match,
        'similarity': highest_similarity,
        'sentiment': text_eval['sentiment'],
        'sentiment_score': text_eval['score'],
        'priority': calculated_priority
    }

# ==============================================================================
# 5. DATA PERSISTENCE & WORKFLOW MANAGEMENT
# ==============================================================================
def get_feedback_file_path() -> str:
    """Mengembalikan path absolut feedback_data.json."""
    base_dir = os.path.dirname(current_app.root_path)
    return os.path.join(base_dir, 'feedback_data.json')

def enrich_feature_metadata(feature_codes: list) -> list:
    """Mengubah kode fitur mentah (F1, F2) menjadi objek terstruktur yang kaya UI."""
    enriched = []
    for code in feature_codes:
        meta = FEATURE_DEFINITIONS.get(code)
        if meta:
            enriched.append({
                'code': code,
                'name': meta['name'],
                'category': meta['category'],
                'polarity': meta['polarity'],
                'icon': meta['icon'],
                'badge_class': meta['badge_class']
            })
        else:
            enriched.append({
                'code': code,
                'name': code,
                'category': 'Lainnya',
                'polarity': 'neutral',
                'icon': 'bi-tag',
                'badge_class': 'badge-secondary'
            })
    return enriched

def analyze_and_save_feedback(feedback_data: dict) -> dict:
    """
    Menganalisis feedback baru menggunakan CBR & NLP yang telah disempurnakan,
    kemudian menyimpannya ke feedback_data.json.
    """
    user_features = feedback_data.get('features', [])
    user_comment = feedback_data.get('comment', '').strip()
    user_name = feedback_data.get('name', '').strip() or 'Anonymous'

    cbr_result = evaluate_cbr_cases(user_features, user_comment)
    best_case = cbr_result['best_case']

    feedback_record = {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'user': user_name,
        'features': user_features,
        'comment': user_comment,
        'analysis': {
            'category': best_case['category'],
            'status': best_case['status'],
            'similarity': f"{cbr_result['similarity']:.2%}",
            'similarity_raw': round(cbr_result['similarity'], 4),
            'sentiment': cbr_result['sentiment'],
            'matched_case_id': best_case.get('id', 'CAT_GENERAL'),
            'recommendation': best_case.get('rekomendasi', '')
        },
        'workflow': {
            'status': 'baru',
            'priority': cbr_result['priority'],
            'admin_response': '',
            'action_plan': '',
            'updated_at': None,
            'updated_by': None
        }
    }

    file_path = get_feedback_file_path()
    all_feedback = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                all_feedback = json.load(f)
        except Exception:
            all_feedback = []

    all_feedback.insert(0, feedback_record)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_feedback, f, indent=4)

    return feedback_record['analysis']

def get_all_feedback(with_feature_meta: bool = True) -> list:
    """
    Membaca semua data feedback dari file JSON dengan migrasi ringan,
    serta memperkaya data fitur jika with_feature_meta=True.
    """
    file_path = get_feedback_file_path()
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            records = json.load(f)
        except json.JSONDecodeError:
            return []

    changed = False
    for record in records:
        if not record.get('id'):
            record['id'] = str(uuid.uuid4())
            changed = True
        if not record.get('workflow'):
            record['workflow'] = {
                'status': 'baru',
                'priority': 'normal',
                'admin_response': '',
                'action_plan': '',
                'updated_at': None,
                'updated_by': None
            }
            changed = True
        # Pastikan field analysis memiliki sentiment
        analysis = record.setdefault('analysis', {})
        if 'sentiment' not in analysis:
            comment_text = record.get('comment', '')
            analysis['sentiment'] = analyze_text_sentiment(comment_text)['sentiment']
            changed = True

        if with_feature_meta:
            record['feature_details'] = enrich_feature_metadata(record.get('features', []))

    if changed:
        with open(file_path, 'w', encoding='utf-8') as out:
            json.dump(records, out, indent=4)

    return records

def update_feedback_workflow(feedback_id: str, updates: dict, admin_user: str = 'Administrator') -> dict | None:
    """Menyimpan keputusan tindak lanjut admin untuk feedback tertentu."""
    records = get_all_feedback(with_feature_meta=False)
    allowed_statuses = {'baru', 'ditinjau', 'direncanakan', 'dikerjakan', 'selesai', 'ditutup'}
    allowed_priorities = {'rendah', 'normal', 'tinggi', 'kritis'}

    for record in records:
        if record.get('id') != feedback_id:
            continue

        workflow = record.setdefault('workflow', {})
        status = updates.get('status', workflow.get('status', 'baru'))
        priority = updates.get('priority', workflow.get('priority', 'normal'))

        if status not in allowed_statuses or priority not in allowed_priorities:
            raise ValueError('Status atau prioritas tidak valid.')

        workflow.update({
            'status': status,
            'priority': priority,
            'admin_response': str(updates.get('admin_response', workflow.get('admin_response', ''))).strip()[:3000],
            'action_plan': str(updates.get('action_plan', workflow.get('action_plan', ''))).strip()[:3000],
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_by': admin_user
        })

        file_path = get_feedback_file_path()
        with open(file_path, 'w', encoding='utf-8') as out:
            json.dump(records, out, indent=4)

        record['feature_details'] = enrich_feature_metadata(record.get('features', []))
        return record

    return None

def delete_feedback(feedback_id: str) -> bool:
    """Menghapus feedback berdasarkan ID."""
    records = get_all_feedback(with_feature_meta=False)
    initial_len = len(records)
    records = [r for r in records if r.get('id') != feedback_id]

    if len(records) == initial_len:
        return False

    file_path = get_feedback_file_path()
    with open(file_path, 'w', encoding='utf-8') as out:
        json.dump(records, out, indent=4)

    return True

def reanalyze_all_feedback() -> int:
    """
    Menjalankan ulang seluruh algoritma CBR & NLP yang telah disempurnakan
    ke semua feedback di database, memperbaiki anomali klasifikasi lama.
    """
    records = get_all_feedback(with_feature_meta=False)
    count = 0

    for record in records:
        user_features = record.get('features', [])
        user_comment = record.get('comment', '')

        cbr_res = evaluate_cbr_cases(user_features, user_comment)
        best_case = cbr_res['best_case']

        record['analysis'] = {
            'category': best_case['category'],
            'status': best_case['status'],
            'similarity': f"{cbr_res['similarity']:.2%}",
            'similarity_raw': round(cbr_res['similarity'], 4),
            'sentiment': cbr_res['sentiment'],
            'matched_case_id': best_case.get('id', 'CAT_GENERAL'),
            'recommendation': best_case.get('rekomendasi', '')
        }

        # Perbarui prioritas workflow jika sebelumnya masih default 'baru' & 'normal'
        wf = record.setdefault('workflow', {})
        if wf.get('status') == 'baru' and wf.get('priority') in {'normal', None}:
            wf['priority'] = cbr_res['priority']

        count += 1

    file_path = get_feedback_file_path()
    with open(file_path, 'w', encoding='utf-8') as out:
        json.dump(records, out, indent=4)

    return count

# ==============================================================================
# 6. ENHANCED ANALYTICS & INSIGHT AGGREGATOR
# ==============================================================================
def get_feedback_analytics(records: list) -> dict:
    """Ringkasan statistik agregat mendalam untuk dashboard operasional admin."""
    total = len(records)
    if total == 0:
        return {
            'total': 0, 'open_count': 0, 'critical_count': 0, 'completion_rate': 0,
            'categories': {}, 'workflow_statuses': {}, 'priorities': {},
            'sentiments': {}, 'top_features': [], 'average_similarity': '0.00%',
            'response_rate': '0%'
        }

    categories = Counter(item.get('analysis', {}).get('category', 'General') for item in records)
    statuses = Counter(item.get('workflow', {}).get('status', 'baru') for item in records)
    priorities = Counter(item.get('workflow', {}).get('priority', 'normal') for item in records)
    sentiments = Counter(item.get('analysis', {}).get('sentiment', 'Netral') for item in records)

    features_counter = Counter()
    total_sim = 0.0
    answered_count = 0

    for item in records:
        for f in item.get('features', []):
            features_counter[f] += 1
        
        sim_val = item.get('analysis', {}).get('similarity', '0%')
        try:
            val = float(str(sim_val).replace('%', ''))
            total_sim += val
        except ValueError:
            pass

        if item.get('workflow', {}).get('admin_response', '').strip():
            answered_count += 1

    open_count = sum(count for state, count in statuses.items() if state not in {'selesai', 'ditutup'})
    critical_count = priorities.get('kritis', 0) + priorities.get('tinggi', 0)
    done_count = statuses.get('selesai', 0) + statuses.get('ditutup', 0)
    completion_rate = round((done_count / total) * 100) if total else 0
    response_rate = round((answered_count / total) * 100) if total else 0
    avg_similarity = round(total_sim / total, 1) if total else 0.0

    # Top features diperkaya dengan nama dan icon
    top_features_list = []
    for f_code, count in features_counter.most_common(6):
        meta = FEATURE_DEFINITIONS.get(f_code, {})
        top_features_list.append({
            'code': f_code,
            'name': meta.get('name', f_code),
            'category': meta.get('category', 'Lainnya'),
            'icon': meta.get('icon', 'bi-tag'),
            'badge_class': meta.get('badge_class', 'badge-secondary'),
            'count': count
        })

    return {
        'total': total,
        'open_count': open_count,
        'critical_count': critical_count,
        'completion_rate': completion_rate,
        'response_rate': f"{response_rate}%",
        'average_similarity': f"{avg_similarity}%",
        'categories': dict(categories),
        'workflow_statuses': dict(statuses),
        'priorities': dict(priorities),
        'sentiments': dict(sentiments),
        'top_features': top_features_list
    }

# ==============================================================================
# 7. AI ASSISTANCE (SMART REPLY & EXECUTIVE SUMMARY)
# ==============================================================================
def generate_ai_smart_reply(feedback_item: dict) -> str:
    """
    Membuat draf balasan profesional dari admin untuk pengguna menggunakan
    LLMClient (Gemini), dengan fallback deterministik yang ramah dan solutif.
    """
    user_name = feedback_item.get('user', 'Siswa MathThon')
    comment = feedback_item.get('comment', '')
    features = [FEATURE_DEFINITIONS.get(f, {}).get('name', f) for f in feedback_item.get('features', [])]
    analysis = feedback_item.get('analysis', {})
    category = analysis.get('category', 'Layanan')
    recom = analysis.get('recommendation', '')

    prompt = f"""Kamu adalah asisten admin untuk platform edukasi matematika 'MathThon'.
Tugasmu adalah menulis draf balasan yang sopan, solutif, empatik, dan profesional kepada pengguna/siswa yang memberikan feedback.

Data Feedback:
- Nama Pengguna: {user_name}
- Kategori Feedback: {category}
- Masukan Pengguna: "{comment if comment else '(Tidak ada komentar spesifik)'}"
- Pilihan Kendala/Fitur: {', '.join(features) if features else 'Tidak ada'}
- Rekomendasi Solusi Sistem (CBR): {recom}

Aturan Penulisan:
1. Sapa nama pengguna dengan ramah.
2. Apresiasi masukannya untuk peningkatan kualitas MathThon.
3. Jelaskan langkah konkret yang sedang/akan dilakukan tim admin sesuai rekomendasi CBR.
4. Gunakan bahasa Indonesia yang baik, bersahabat untuk pelajar (1-2 paragraf singkat, jangan bertele-tele).
5. Jangan gunakan format markdown judul (#), cukup teks paragraf biasa."""

    try:
        from Back_End.ai.llm_client import LLMClient
        client = LLMClient(provider="gemini")
        reply = client.generate(prompt=prompt, temperature=0.5, max_output_tokens=350)
        if reply and len(reply.strip()) > 30:
            return reply.strip()
    except Exception:
        pass

    # Fallback ramah jika API Gemini sedang tidak tersedia / kuota limit
    if 'bug' in comment.lower() or 'error' in comment.lower() or category == 'Teknis & Bug':
        return (
            f"Halo {user_name}, terima kasih banyak atas laporannya. "
            f"Tim pengembang MathThon sedang meninjau kendala teknis yang Anda alami. "
            f"Kami segera melakukan perbaikan agar pembelajaran Anda kembali nyaman dan lancar."
        )
    elif category == 'Konten Materi':
        return (
            f"Halo {user_name}, terima kasih atas masukannya mengenai materi matematika kami. "
            f"Saran Anda sangat berharga bagi kami untuk menyederhanakan penjelasan teori dan memperkaya contoh latihan soal nyata."
        )
    else:
        return (
            f"Halo {user_name}, terima kasih telah meluangkan waktu memberikan masukan untuk MathThon. "
            f"Saran Anda telah kami catat dalam rencana peningkatan sistem agar pengalaman belajar menjadi semakin optimal."
        )

def generate_ai_executive_summary(records: list) -> str:
    """
    Menyusun ringkasan eksekutif tingkat tinggi dari seluruh feedback terkumpul
    untuk membantu admin mengambil keputusan strategis platform.
    """
    analytics = get_feedback_analytics(records)
    total = analytics['total']
    if total == 0:
        return "Belum ada feedback yang dapat dianalisis."

    sample_comments = [
        f"- {r.get('user', 'Anon')}: \"{r.get('comment')}\" (Kategori: {r.get('analysis', {}).get('category')})"
        for r in records[:10] if r.get('comment')
    ]

    prompt = f"""Kamu adalah AI Strategy Consultant untuk platform 'MathThon'.
Analisis data statistik dan sampel feedback berikut, lalu buatkan ringkasan eksekutif komprehensif dalam bahasa Indonesia:

Statistik:
- Total Masukan: {total}
- Perlu Tindak Lanjut: {analytics['open_count']}
- Kritis / Mendesak: {analytics['critical_count']}
- Kategori Terbesar: {json.dumps(analytics['categories'], ensure_ascii=False)}
- Sentimen Pengguna: {json.dumps(analytics['sentiments'], ensure_ascii=False)}
- Fitur Paling Banyak Disorot: {', '.join([f['name'] + f" ({f['count']}x)" for f in analytics['top_features']])}

Sampel Masukan Pengguna:
{chr(10).join(sample_comments)}

Format Output (Gunakan bullet points rapi):
1. **Ringkasan Sentimen & Kepuasan Pengguna**
2. **Top Pain Points / Masalah Kritis yang Perlu Segera Ditangani**
3. **Rekomendasi Tindakan Strategis untuk Tim Pengembang & Tim Kurikulum**"""

    try:
        from Back_End.ai.llm_client import LLMClient
        client = LLMClient(provider="gemini")
        summary = client.generate(prompt=prompt, temperature=0.4, max_output_tokens=600)
        if summary and len(summary.strip()) > 50:
            return summary.strip()
    except Exception:
        pass

    # Fallback ringkasan analitik
    return (
        f"**Ringkasan Analitik MathThon**\n\n"
        f"• **Volume Masukan**: Terkumpul {total} feedback, dengan {analytics['open_count']} tiket membutuhkan tindak lanjut aktif.\n"
        f"• **Isu Kritis**: Terdeteksi {analytics['critical_count']} tiket prioritas tinggi/kritis, terutama pada kategori {list(analytics['categories'].keys())[0] if analytics['categories'] else '-'}.\n"
        f"• **Tindakan yang Disarankan**: Prioritaskan debugging bug interaksi dan perbaikan kalkulator matematika, disusul optimasi visualisasi grafik dan penambahan contoh soal kontekstual."
    )
