import matplotlib.pyplot as plt
import pandas as pd
import os

# Penyesuaian: script berada di chart/ dalam static/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File CSV pasti ada di static/chart/api/education_data/kelayakan-pendidikan-indonesia.csv
# Nama file harus dipastikan tepat (strip, bukan underscore dan ejaan benar)
csv_path = os.path.join(BASE_DIR, "api", "education_data", "kelayakan-pendidikan-indonesia.csv")
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"File tidak ditemukan: {csv_path}")

print("Membaca data dari:", csv_path)

# Otomatis cek delimiter (untuk robust meski contoh hanya ',')
with open(csv_path, encoding='utf-8-sig') as f:
    firstline = f.readline()
    delimiter = ',' if firstline.count(',') > firstline.count(';') else ';'

df = pd.read_csv(csv_path, delimiter=delimiter, encoding='utf-8-sig')

print("Kolom yang tersedia:", df.columns.tolist())
print(df.head(3))

# Penyesuaian: kelayakan-pendidikan-indonesia.csv kolom-kolomnya berbeda.
# Kolom penting: 'Provinsi', 'Siswa', 'Putus Sekolah', 'Mengulang', 'Ruang kelas(ba…)'
# Ambil info provinsi dan beberapa indikator utama

prov_col = [col for col in df.columns if 'prov' in col.lower() or 'provinsi' in col.lower()]
provinsi_col = prov_col[0] if prov_col else df.columns[0]

indikator_dict = {
    'Siswa': [col for col in df.columns if 'siswa' in col.lower()],
    'Putus Sekolah': [col for col in df.columns if 'putus' in col.lower()],
    'Mengulang': [col for col in df.columns if 'mengulang' in col.lower()],
    'Ruang Kelas (Baik)': [col for col in df.columns if 'ruang kelas' in col.lower() and 'baik' in col.lower()]
}

# Pilih hanya yang ditemukan
indikator_dict = {k: v[0] for k, v in indikator_dict.items() if v}

if not indikator_dict:
    raise ValueError("Tidak menemukan indikator utama dalam kolom CSV.")

provinsi = df[provinsi_col]
n_indikator = len(indikator_dict)

plt.figure(figsize=(max(10, len(provinsi) * 0.6), 6))

bar_width = 0.18
bar_pos = range(len(provinsi))

# Plot beberapa indikator
for idx, (label, col) in enumerate(indikator_dict.items()):
    # Untuk offset agar bar tidak saling menimpa
    posisi = [i + (idx - n_indikator/2)*bar_width + bar_width/2 for i in bar_pos]
    y = pd.to_numeric(df[col], errors='coerce')
    plt.bar(posisi, y, width=bar_width, label=label)

plt.xticks(bar_pos, provinsi, rotation=70, ha='right', fontsize=9)
plt.xlabel('Provinsi')
plt.ylabel('Jumlah / Angka')
plt.title('Indikator Pendidikan per Provinsi (sumber Kemendikbud)')
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.3)

OUTPUT_PNG_PATH = os.path.join(BASE_DIR, "education.png")
plt.savefig(OUTPUT_PNG_PATH, dpi=150)
plt.close()
print("Grafik berhasil disimpan di:", OUTPUT_PNG_PATH)
