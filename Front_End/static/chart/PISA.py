import os
import pandas as pd
import matplotlib.pyplot as plt

# Tentukan path absolut ke file CSV
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "api", "education_data", "PISA.csv")

# Cek apakah file ada
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File tidak ditemukan di: {file_path}")

# Membaca data CSV
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig')
except Exception as e:
    raise Exception(f"Gagal membaca CSV: {e}")

# Menampilkan 5 data teratas
print("Data sample:")
print(df.head(), "\n")

# Cek kolom yang tersedia
print("Kolom yang ditemukan dalam dataset:")
print(df.columns.tolist(), "\n")

# Contoh: asumsi kolom berisi ['Negara', 'Membaca', 'Matematika', 'Sains']
# Sesuaikan dengan nama kolom di file Anda
required_columns = ['Category','x_maths', 'x_reading', 'x_scie']

for col in required_columns:
    if col not in df.columns:
        print(f"⚠ Kolom '{col}' tidak ditemukan di CSV. Harap sesuaikan nama kolom!")
        exit()

# Visualisasi skor PISA (batang)
plt.figure(figsize=(12, 6))
df_sorted = df.sort_values(by='x_maths', ascending=False) # Menggunakan 'x_maths' untuk sorting

# Pastikan kolom 'Category' digunakan sebagai label sumbu x
plt.bar(df_sorted['Category'], df_sorted['x_maths'], color='skyblue', label='Matematika')
plt.bar(df_sorted['Category'], df_sorted['x_reading'], alpha=0.7, color='orange', label='Membaca')
plt.bar(df_sorted['Category'], df_sorted['x_scie'], alpha=0.6, color='green', label='Sains')

plt.title("Skor PISA per Negara")
plt.xlabel("Negara")
plt.ylabel("Skor")
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)

# Simpan grafik ke file
output_path = os.path.join(base_dir, "PISA_Score_Chart.png")
plt.savefig(output_path)
plt.show()

print(f"✅ Grafik berhasil disimpan di: {output_path}")
