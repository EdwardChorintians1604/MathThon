import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ===========================
# KONFIGURASI FILE & DIREKTORI
# ===========================
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "api", "education_data", "PISA_Score_Chart_From_Excel.csv")

# Pastikan file CSV ada
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File tidak ditemukan di: {file_path}")

# ===========================
# MEMBACA DATA CSV
# ===========================
df = pd.read_csv(file_path, encoding='utf-8-sig')
print("Kolom yang tersedia:", df.columns.tolist())
print("\nData sample:\n", df.head())

# ===========================
# CEK & SESUAIKAN NAMA KOLOM
# ===========================
# Pastikan kolom berikut ada dalam file CSV
required_cols = ['Matematika', 'Membaca', 'Sains']
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"⚠ Kolom '{col}' tidak ditemukan di CSV. Harap sesuaikan nama kolom!")

# ===========================
# HITUNG RATA-RATA SETIAP KATEGORI
# ===========================
avg_math = df['Matematika'].mean()
avg_read = df['Membaca'].mean()
avg_sci = df['Sains'].mean()

# Buat data untuk diagram batang
subjects = ['Matematika', 'Membaca', 'Sains']
averages = [avg_math, avg_read, avg_sci]
colors = ['#2E86AB', '#A23B72', '#F18F01']

# ===========================
# MEMBUAT DIAGRAM BATANG
# ===========================
plt.figure(figsize=(10, 6))
bars = plt.bar(subjects, averages, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)

# Tambahkan nilai di atas setiap batang
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 5,
             f'{height:.1f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Konfigurasi grafik
plt.title('Rata-rata Skor PISA Indonesia per Bidang (2006-2022)\nData berdasarkan OECD', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Bidang Studi', fontsize=12, fontweight='bold')
plt.ylabel('Rata-rata Skor', fontsize=12, fontweight='bold')
plt.ylim(0, max(averages) + 50)  # Beri sedikit ruang di atas batang tertinggi

# Grid untuk memudahkan pembacaan
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Rotasi label jika diperlukan
plt.xticks(rotation=0)

plt.tight_layout()

# ===========================
# SIMPAN GAMBAR
# ===========================
output_path = os.path.join(base_dir, "api", "education_data", "PISA_Score_BarChart.png")
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.show()

# ===========================
# CETAK KESIMPULAN
# ===========================
print("\n📊 HASIL ANALISIS DIAGRAM BATANG PISA:")
print("=" * 50)
print(f"📐 Matematika : {avg_math:.2f}")
print(f"📖 Membaca    : {avg_read:.2f}")
print(f"🔬 Sains      : {avg_sci:.2f}")
print("=" * 50)

max_value = max(averages)
min_value = min(averages)
max_subject = subjects[averages.index(max_value)]
min_subject = subjects[averages.index(min_value)]

print(f"🏆 Bidang dengan skor TERTINGGI: {max_subject} ({max_value:.2f})")
print(f"📉 Bidang dengan skor TERENDAH : {min_subject} ({min_value:.2f})")
print(f"📈 Selisih tertinggi-terendah : {max_value - min_value:.2f} poin")

print(f"\n✅ Diagram batang berhasil disimpan di: {output_path}")