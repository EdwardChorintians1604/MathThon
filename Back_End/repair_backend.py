import os
import re
import logging

# Gunakan path yang benar (e:\MathThon)
file_path = os.path.join(os.path.dirname(__file__), "Back_End", "__init__.py")
if not os.path.exists(file_path):
    # Fallback jika dijalankan dari tempat lain
    file_path = r"e:\MathThon\Back_End\__init__.py"

if not os.path.exists(file_path):
    print(f"Error: File tidak ditemukan di {file_path}")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Marker yang benar-benar ada di __init__.py Anda saat ini
marker = '@app.route("/user/google_login", methods=["POST"])'

# Konten yang akan dimasukkan
insert_content = r'''
    # ==========================================
    # ROUTE: USER LOGOUT AND SETTINGS
    # ==========================================

    # IMPORTS for injected routes. These are necessary to prevent NameError.
    import math
    import uuid
    import re
    from datetime import datetime, timedelta
    from werkzeug.security import generate_password_hash

    # ==========================================

    @app.route("/user/settings_user")
    @user_required  # Pastikan pengguna sudah login
    def settings_user():
        """Tampilkan halaman pengaturan pengguna."""
        user_data = get_user_data_for_template(app)
        return render_template("user/pengaturan.html", **user_data)
    
    @app.route("/user/calculator_user", methods=["GET"])
    @user_required
    def calculator_user():
        """Tampilkan halaman kalkulator."""
        user_data = get_user_data_for_template(app) 
        return render_template("user/calculator.html", **user_data)

    @app.route("/user/calculator_user", methods=["POST"])
    @user_required
    def submit_calculator_user():
        """Proses permintaan kalkulator dari pengguna."""
        user_data = get_user_data_for_template(app) 
        problem = request.form.get("problem", "").strip()

        if not problem:
            flash("Masukkan soal matematika untuk diselesaikan.", "danger")
            return render_template("user/calculator.html", **user_data)

        try:
            solution_steps = solve_word_problem_logic(app, problem)
            return render_template("user/calculator.html", solution=solution_steps, problem=problem, **user_data)
        except Exception as e:
            logging.error(f"Error solving problem '{problem}': {e}")
            flash("Terjadi kesalahan saat menyelesaikan soal. Coba lagi nanti.", "danger")
            return render_template("user/calculator.html", **user_data)

    # ==========================================
    # ROUTE: API CALCULATOR (PYTHON BACKEND)
    # ==========================================
    def safe_calculate(expression):
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
        expr = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expr)
        
        # Handle Akar (akar 9 -> sqrt(9))
        expr = re.sub(r'akar\s+(\d+(\.\d+)?)', r'sqrt(\1)', expr, flags=re.IGNORECASE)
        
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

    @app.route('/api/calculate', methods=['POST'])
    def calculate_api():
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Handle Ans
        if 'Ans' in expression:
            last_result = session.get('last_result', 0)
            expression = expression.replace('Ans', str(last_result))

        result = safe_calculate(expression)
        
        if result == "Error":
            return jsonify({'status': 'error', 'result': 'Error Syntax'})
        
        # Store result for Ans
        session['last_result'] = result
        
        return jsonify({'status': 'success', 'result': str(result)})

    @app.route("/user/logout_user")
    @user_required
    def logout_user():
        """Membersihkan sesi pengguna dan mengarahkan ke halaman login."""  
        # Hapus semua data dari sesi untuk logout
        session.clear()
        # Memberikan pesan konfirmasi kepada pengguna
        flash("Anda telah berhasil logout.", "success")
        return redirect(url_for("login_user"))

    @app.route("/user/forget_password_user", methods=["GET", "POST"])
    def forget_password_user():
        if request.method == "POST":
            # Blok ini untuk menangani request POST (saat form disubmit)
            # Semua alur di dalam blok ini sudah memiliki `return`.
            # (Logika POST Anda yang sudah ada diletakkan di sini)
            pass  # Placeholder, karena logika POST Anda sudah benar.

        # Baris ini untuk menangani request GET (saat halaman diakses pertama kali).
        # Error `TypeError` yang Anda alami biasanya terjadi jika baris ini
        # tidak sengaja masuk ke dalam blok `if` di atas (salah indentasi).
        # Pastikan baris ini berada di level indentasi dasar fungsi.
        return render_template("user/forget_password_user.html")
        
    @app.route("/user/reset_password_user/<token>", methods=["GET", "POST"])
    def reset_password_user(token):
        if request.method == "POST":
            new_password = request.form.get("new_password")
            if not new_password:
                flash("Password baru wajib diisi.", "danger")
                return redirect(url_for('reset_password_user', token=token))

            conn = None
            try:
                conn = get_db_connection(app)
                cursor = conn.cursor(dictionary=True)

                cursor.execute("SELECT user_id FROM password_reset_tokens WHERE token = %s AND expires_at > NOW()", (token,))
                reset_token_data = cursor.fetchone()

                if not reset_token_data:
                    flash("Token tidak valid atau kadaluarsa.", "danger")
                    return redirect(url_for('login_user'))
                
                user_id = reset_token_data['user_id']
                hashed_password = generate_password_hash(new_password)

                cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))
                cursor.execute("DELETE FROM password_reset_tokens WHERE token = %s", (token,))
                conn.commit()

                flash("Password Anda telah berhasil diperbarui!", "success")
                return redirect(url_for('login_user'))
            except Exception as e:
                logging.error(f"Kesalahan saat mereset password: {e}")
                flash("Terjadi kesalahan. Mohon coba lagi nanti.", "danger")
                return redirect(url_for('reset_password_user', token=token))
            finally:
                if conn:
                    conn.close()
        
        return render_template("user/reset_password_user.html", token=token)
'''

if marker in content:
    # Hindari duplikasi jika script dijalankan berkali-kali
    if "logout_user" in content:
        print("Konten sepertinya sudah ada atau sudah diperbaiki.")
    else:
        new_content = content.replace(marker, insert_content + "\n" + marker)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully inserted content.")
else:
    print(f"Marker '{marker}' not found in {file_path}!")
