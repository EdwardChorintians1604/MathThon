import os

file_path = r"f:\MathThon\Back_End\__init__.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = 'def safe_calculate(expression):'
end_marker = "@app.route('/api/calculate', methods=['POST'])"

# Find start
start_idx = content.find(start_marker)
# Find end (after start)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Construct the new content
    new_safe_calculate = '''def safe_calculate(expression):
        # 1. Normalisasi Input
        expr = expression.replace(',', '.')  # Koma jadi titik
        
        # 2. Natural Language Processing (Regex)
        expr = re.sub(r'\s+tambah\s+', '+', expr, flags=re.IGNORECASE)
        expr = re.sub(r'\s+kurang\s+', '-', expr, flags=re.IGNORECASE)
        expr = re.sub(r'\s*(kali|x)\s*', '*', expr, flags=re.IGNORECASE)
        expr = re.sub(r'\s*(bagi|:)\s*', '/', expr, flags=re.IGNORECASE)
        
        # Handle Modulo (mod -> %)
        expr = re.sub(r'\s+mod\s+', '%', expr, flags=re.IGNORECASE)

        # Handle Persen (50% -> 0.5)
        expr = re.sub(r'(\d+(\.\d+)?)%', r'(\\1/100)', expr)
        
        # Handle Akar (akar 9 -> sqrt(9))
        expr = re.sub(r'akar\s+(\d+(\.\d+)?)', r'sqrt(\\1)', expr, flags=re.IGNORECASE)
        
        # 3. Whitelist Fungsi Matematika
        allowed_names = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log, # ln
            "log10": math.log10,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            "exp": math.exp,
            "pow": pow,
            "factorial": math.factorial,
            "radians": math.radians,
            "degrees": math.degrees,
            "abs": abs,
            "round": round
        }

        try:
            # 4. Evaluasi string menjadi kode
            code = compile(expr, "<string>", "eval")
            result = eval(code, {"__builtins__": {}}, allowed_names)
            
            # Format hasil
            if isinstance(result, float) and result.is_integer():
                return int(result)
            if isinstance(result, float):
                return round(result, 10)
            return result
            
        except Exception as e:
            return "Error"

    '''
    
    # Replace
    new_content = content[:start_idx] + new_safe_calculate + content[end_idx:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced safe_calculate.")
else:
    print("Markers not found!")
