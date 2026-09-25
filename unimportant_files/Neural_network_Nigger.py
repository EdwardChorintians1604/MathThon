"""
=============================================================
  ANN dengan Delta Rule - Prediksi Pilihan Makanan Pelanggan
=============================================================
Studi kasus: Memprediksi apakah suatu makanan SERING dipilih
pelanggan berdasarkan fitur: harga_murah, porsi_besar, populer_media_sosial
=============================================================
"""

import numpy as np

# ------------------------------------------------------------------
# 1. DATA TRAINING
# ------------------------------------------------------------------
# Fitur: [harga_murah, porsi_besar, populer_di_medsos]
# Label: 1 = sering dipilih, 0 = jarang dipilih

nama_makanan = [
    "Nasi Goreng Spesial",
    "Sate Ayam",
    "Mie Ayam Bakso",
    "Gado-Gado",
    "Ayam Bakar",
    "Pecel Lele",
    "Soto Betawi",
    "Ketoprak",
    "Nasi Padang",
    "Bakso Malang",
]

# [harga_murah, porsi_besar, populer_medsos]
X = np.array([
    [1, 1, 1],   # Nasi Goreng Spesial
    [0, 0, 1],   # Sate Ayam
    [1, 1, 0],   # Mie Ayam Bakso
    [1, 0, 0],   # Gado-Gado
    [0, 1, 1],   # Ayam Bakar
    [1, 1, 0],   # Pecel Lele
    [0, 1, 1],   # Soto Betawi
    [1, 0, 0],   # Ketoprak
    [0, 1, 1],   # Nasi Padang
    [1, 1, 1],   # Bakso Malang
])

# Target: sering dipilih (1) atau tidak (0)
y = np.array([1, 0, 1, 0, 1, 1, 1, 0, 1, 1])

# ------------------------------------------------------------------
# 2. INISIALISASI PARAMETER
# ------------------------------------------------------------------
np.random.seed(0)
n_fitur   = X.shape[1]
w         = np.random.randn(n_fitur) * 0.1  # bobot awal kecil
b         = 0.0                              # bias awal
lr        = 0.1                             # learning rate
epochs    = 200

# ------------------------------------------------------------------
# 3. FUNGSI BANTU
# ------------------------------------------------------------------
def aktivasi(net):
    """Fungsi aktivasi threshold (step function)."""
    return 1 if net >= 0.5 else 0

def hitung_akurasi(X, y, w, b):
    benar = 0
    for i in range(len(X)):
        out   = np.dot(X[i], w) + b
        pred  = aktivasi(out)
        if pred == y[i]:
            benar += 1
    return benar / len(X) * 100

# ------------------------------------------------------------------
# 4. TRAINING DELTA RULE
# ------------------------------------------------------------------
print("=" * 55)
print("  ANN Delta Rule - Prediksi Pilihan Makanan Pelanggan")
print("=" * 55)
print(f"\nParameter Training:")
print(f"  - Learning Rate : {lr}")
print(f"  - Epochs        : {epochs}")
print(f"  - Jumlah Fitur  : {n_fitur} (harga_murah, porsi_besar, medsos)")
print(f"  - Data Training : {len(X)} menu makanan\n")

history_mse = []

for epoch in range(epochs):
    total_error = 0

    for i in range(len(X)):
        # ---- Forward Pass ----
        net    = np.dot(X[i], w) + b   # net input
        output = net                    # output linear (sebelum threshold)

        # ---- Hitung Error ----
        error  = y[i] - output
        total_error += error ** 2

        # ---- Update Bobot (Delta Rule) ----
        # Δw = η × error × x
        w += lr * error * X[i]
        b += lr * error

    mse = total_error / len(X)
    history_mse.append(mse)

    if (epoch + 1) % 40 == 0:
        akurasi = hitung_akurasi(X, y, w, b)
        print(f"  Epoch {epoch+1:>3} | MSE: {mse:.4f} | Akurasi: {akurasi:.1f}%")

# ------------------------------------------------------------------
# 5. HASIL PREDIKSI
# ------------------------------------------------------------------
print("\n" + "=" * 55)
print("  HASIL PREDIKSI")
print("=" * 55)
print(f"  {'Nama Makanan':<25} {'Target':^8} {'Prediksi':^10} {'Status':^8}")
print("  " + "-" * 53)

benar = 0
for i in range(len(X)):
    net   = np.dot(X[i], w) + b
    pred  = aktivasi(net)
    label_target = "Sering" if y[i] == 1 else "Jarang"
    label_pred   = "Sering" if pred == 1  else "Jarang"
    status       = "✓" if pred == y[i] else "✗"
    if pred == y[i]:
        benar += 1
    print(f"  {nama_makanan[i]:<25} {label_target:^8} {label_pred:^10} {status:^8}")

akurasi_akhir = benar / len(X) * 100
print("  " + "-" * 53)
print(f"\n  Akurasi Akhir : {benar}/{len(X)} = {akurasi_akhir:.1f}%")

# ------------------------------------------------------------------
# 6. BOBOT AKHIR
# ------------------------------------------------------------------
print("\n" + "=" * 55)
print("  BOBOT AKHIR JARINGAN")
print("=" * 55)
fitur_nama = ["Harga Murah", "Porsi Besar", "Populer Medsos"]
for i, nama in enumerate(fitur_nama):
    print(f"  w_{nama:<18}: {w[i]:+.4f}")
print(f"  {'Bias':<20}: {b:+.4f}")

# ------------------------------------------------------------------
# 7. PREDIKSI DATA BARU
# ------------------------------------------------------------------
print("\n" + "=" * 55)
print("  PREDIKSI MENU BARU")
print("=" * 55)
menu_baru = np.array([
    [1, 1, 1],   # murah + besar + viral
    [0, 0, 0],   # mahal + kecil + tidak viral
    [1, 0, 1],   # murah + kecil + viral
])
nama_baru = ["Nasi Uduk Komplit (murah+besar+viral)",
             "Steak Wagyu (mahal+kecil+biasa)",
             "Es Kopi Kekinian (murah+viral)"]

for i, menu in enumerate(menu_baru):
    net  = np.dot(menu, w) + b
    pred = aktivasi(net)
    hasil = "SERING Dipilih ✓" if pred == 1 else "JARANG Dipilih ✗"
    print(f"  {nama_baru[i]}")
    print(f"    → Prediksi: {hasil}\n")

print("=" * 55)
print("  Selesai! Model berhasil dilatih dengan Delta Rule.")
print("=" * 55)