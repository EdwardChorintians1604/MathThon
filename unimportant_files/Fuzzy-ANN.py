import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# === INPUT VARIABLES ===
# Kualitas Layanan: 0–10
layanan = ctrl.Antecedent(np.arange(0, 11, 1), 'layanan')
# Harga: 0–10
harga = ctrl.Antecedent(np.arange(0, 11, 1), 'harga')
# OUTPUT VARIABLE: Kepuasan (0–10)
kepuasan = ctrl.Consequent(np.arange(0, 11, 1), 'kepuasan')

# === FUZZY SETS (Membership Functions) ===
layanan['buruk'] = fuzz.trimf(layanan.universe, [0, 0, 5])
layanan['sedang'] = fuzz.trimf(layanan.universe, [0, 5, 10])
layanan['baik'] = fuzz.trimf(layanan.universe, [5, 10, 10])

harga['murah'] = fuzz.trimf(harga.universe, [0, 0, 5])
harga['sedang'] = fuzz.trimf(harga.universe, [0, 5, 10])
harga['mahal'] = fuzz.trimf(harga.universe, [5, 10, 10])

# Untuk Mamdani & Tsukamoto → output fuzzy
kepuasan['rendah'] = fuzz.trimf(kepuasan.universe, [0, 0, 5])
kepuasan['sedang'] = fuzz.trimf(kepuasan.universe, [0, 5, 10])
kepuasan['tinggi'] = fuzz.trimf(kepuasan.universe, [5, 10, 10])

# === RULES untuk semua metode ===
rule1 = ctrl.Rule(layanan['buruk'] | harga['mahal'], kepuasan['rendah'])
rule2 = ctrl.Rule(layanan['sedang'] & harga['sedang'], kepuasan['sedang'])
rule3 = ctrl.Rule(layanan['baik'] & harga['murah'], kepuasan['tinggi'])

# === MAMDANI ===
mamdani_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
mamdani_sim = ctrl.ControlSystemSimulation(mamdani_ctrl)

mamdani_sim.input['layanan'] = 7
mamdani_sim.input['harga'] = 3
mamdani_sim.compute()

print("=== HASIL METODE MAMDANI ===")
print(f"Kepuasan (Mamdani): {mamdani_sim.output['kepuasan']:.2f}")

# === SUGENO (output berupa konstanta/linear function) ===
# Di Sugeno, output tidak fuzzy, tapi berupa fungsi atau nilai konstan

# Fungsi keluaran (konstan)
def sugeno_output(layanan_val, harga_val):
    # rule1: buruk/mahal → kepuasan rendah (nilai 3)
    # rule2: sedang/sedang → kepuasan sedang (nilai 6)
    # rule3: baik/murah → kepuasan tinggi (nilai 9)
    μ1 = max(fuzz.interp_membership(layanan.universe, layanan['buruk'].mf, layanan_val),
             fuzz.interp_membership(harga.universe, harga['mahal'].mf, harga_val))
    μ2 = min(fuzz.interp_membership(layanan.universe, layanan['sedang'].mf, layanan_val),
             fuzz.interp_membership(harga.universe, harga['sedang'].mf, harga_val))
    μ3 = min(fuzz.interp_membership(layanan.universe, layanan['baik'].mf, layanan_val),
             fuzz.interp_membership(harga.universe, harga['murah'].mf, harga_val))

    # Defuzzifikasi (Weighted Average)
    z = (μ1*3 + μ2*6 + μ3*9) / (μ1 + μ2 + μ3)
    return z

sugeno_val = sugeno_output(7, 3)
print("\n=== HASIL METODE SUGENO ===")
print(f"Kepuasan (Sugeno): {sugeno_val:.2f}")

# === TSUKAMOTO ===
# Tiap aturan menghasilkan crisp (karena output monoton)

def tsukamoto_output(layanan_val, harga_val):
    def z_low(α): return 5 - α*5  # rendah
    def z_med(α): return 5*α + 2  # sedang
    def z_high(α): return 5 + α*5  # tinggi 

    μ1 = max(fuzz.interp_membership(layanan.universe, layanan['buruk'].mf, layanan_val),
             fuzz.interp_membership(harga.universe, harga['mahal'].mf, harga_val))
    μ2 = min(fuzz.interp_membership(layanan.universe, layanan['sedang'].mf, layanan_val),
             fuzz.interp_membership(harga.universe, harga['sedang'].mf, harga_val))
    μ3 = min(fuzz.interp_membership(layanan.universe, layanan['baik'].mf, layanan_val),
             fuzz.interp_membership(harga.universe, harga['murah'].mf, harga_val))

    z1 = z_low(μ1)
    z2 = z_med(μ2)
    z3 = z_high(μ3)

    # Defuzzifikasi rata-rata berbobot
    z_final = (μ1*z1 + μ2*z2 + μ3*z3) / (μ1 + μ2 + μ3)
    return z_final

tsukamoto_val = tsukamoto_output(7, 3)
print("\n=== HASIL METODE TSUKAMOTO ===")
print(f"Kepuasan (Tsukamoto): {tsukamoto_val:.2f}")
