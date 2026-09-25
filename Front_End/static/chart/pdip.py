import pandas as pd
import matplotlib.pyplot as plt
import os

# Tentukan path absolut ke file Excel
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "api", "education_data", "perbandingan-skor-pisa-indonesia-dari-tahun-ke-tahun-alami-penurunan-pada-2022.xlsx")

# Cek apakah file ada
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File tidak ditemukan di: {file_path}")

df = pd.read_excel(file_path)

output_path = os.path.join(base_dir, "PISA_Score_Chart_From_Excel.csv")
df.to_csv(output_path, index=False)
print(f"✅ File CSV berhasil disimpan di: {output_path}")

print(df)
