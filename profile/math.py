from flask import Flask, render_template, request, jsonify, session
import math
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# --- Wrapper Trigonometric untuk Degree Support ---
def sin_deg(x): return math.sin(math.radians(x))
def cos_deg(x): return math.cos(math.radians(x))
def tan_deg(x): return math.tan(math.radians(x))

# --- Logika Pemrosesan Bahasa & Matematika ---
def safe_calculate(expression):
    # Ambil last_answer dari session (aman untuk multi-user)
    last_answer = session.get('last_answer', 0)

    # 1. Normalisasi Input
    expr = expression.replace(',', '.')  # Koma jadi titik

    # 2. Natural Language Processing (Regex)
    # Ubah kata-kata menjadi operator Python
    expr = re.sub(r'\s+tambah\s+', ' + ', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\s+kurang\s+', ' - ', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\s+kali\s+', ' * ', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\s+bagi\s+', ' / ', expr, flags=re.IGNORECASE)

    # Handle Ans (last answer) - ganti sebelum proses lain
    expr = re.sub(r'\bAns\b', str(last_answer), expr, flags=re.IGNORECASE)

    # Handle Modulo keyword "mod" -> %  (harus SEBELUM handler persen)
    expr = re.sub(r'\s+mod\s+', ' % ', expr, flags=re.IGNORECASE)

    # Handle Persen: hanya ubah ke /100 jika TIDAK digunakan sebagai modulo
    # Contoh: "50 %" -> "(50/100)", tapi "10 % 3" sudah ditangani sebagai modulo di atas
    expr = re.sub(r'(\d+(\.\d+)?)\s*%(?!\s*[\d(])', r'(\1/100)', expr)

    # Handle Akar (akar 9 -> sqrt(9))
    expr = re.sub(r'akar\s*(\d+(\.\d+)?)', r'sqrt(\1)', expr, flags=re.IGNORECASE)

    # Handle Kombinasi dan Permutasi dengan notasi (n,k) atau keyword
    expr = re.sub(r'(kombinasi|nCr)\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)', r'comb(\2, \3)', expr, flags=re.IGNORECASE)
    expr = re.sub(r'(permutasi|nPr)\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)', r'perm(\2, \3)', expr, flags=re.IGNORECASE)

    # Handle Kombinasi dan Permutasi tanpa kurung (10 Kombinasi 2 -> comb(10, 2))
    expr = re.sub(r'(\d+)\s+(kombinasi|nCr)\s+(\d+)', r'comb(\1, \3)', expr, flags=re.IGNORECASE)
    expr = re.sub(r'(\d+)\s+(permutasi|nPr)\s+(\d+)', r'perm(\1, \3)', expr, flags=re.IGNORECASE)

    # Handle Logaritma
    expr = re.sub(r'\bln\s*\(', 'log(', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\blog10\s*\(', 'log10(', expr, flags=re.IGNORECASE)
    expr = re.sub(r'log\s+basis\s+(\d+(\.\d+)?)\s+dari\s+(\d+(\.\d+)?)', r'log(\3, \1)', expr, flags=re.IGNORECASE)
    expr = re.sub(r'(?<![a-zA-Z0-9_])log\s+(\d+(\.\d+)?)', r'log(\1)', expr, flags=re.IGNORECASE)

    # Handle Faktorial (5! -> factorial(5))
    expr = re.sub(r'(\d+)!', r'factorial(\1)', expr)

    # Handle Pangkat (^ -> **)
    expr = expr.replace('^', '**')

    # 3. Definisikan Fungsi/Konstanta yang aman untuk digunakan
    allowed_names = {
        "sin": sin_deg,         # Trigonometri dalam DERAJAT
        "cos": cos_deg,
        "tan": tan_deg,
        "log": math.log,        # Natural log (ln) — default 1 arg = ln
        "log10": math.log10,    # log basis 10
        "sqrt": math.sqrt,
        "exp": math.exp,        # e^x
        "abs": abs,             # Nilai absolut
        "pi": math.pi,
        "e": math.e,
        "comb": math.comb,
        "perm": math.perm,
        "factorial": math.factorial,
        "radians": math.radians,
        "degrees": math.degrees,
        "pow": pow,
    }

    try:
        # 4. Evaluasi dalam lingkup terbatas (whitelist)
        code = compile(expr, "<string>", "eval")
        result = eval(code, {"__builtins__": {}}, allowed_names)

        # Simpan last answer ke session
        if isinstance(result, (int, float)):
            session['last_answer'] = result

        # Format hasil: hilangkan desimal jika bulat (10.0 -> 10)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return round(result, 10)  # Batasi presisi desimal

    except Exception as e:
        return "Error"

# --- Routes ---

@app.route('/')
def calculator_user():
    return render_template('user/calculator.html')

@app.route('/api/calculate', methods=['POST'])
def calculate_api():
    data = request.get_json()
    expression = data.get('expression', '')
    
    result = safe_calculate(expression)
    
    if result == "Error":
        return jsonify({'status': 'error', 'result': 'Error Syntax'})
    
    return jsonify({'status': 'success', 'result': str(result)})

if __name__ == '__main__':
    app.run(debug=True)