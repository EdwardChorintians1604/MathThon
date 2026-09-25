import os
from Back_End.__init__ import create_app
from pyngrok import ngrok

if __name__ == "__main__":
    app = create_app()
    
    # Konfigurasi dari environment variable
    flask_env = os.getenv('FLASK_ENV', 'development')
    port = int(os.getenv('PORT', 5000))
    debug_mode = flask_env == 'development'
    
    if flask_env == 'development':
        try:
            from pyngrok import ngrok, conf
            # Set path ke ngrok sistem untuk menghindari WinError 193 (corrupted internal binary)
            system_ngrok = r"C:\Users\acer\AppData\Local\Microsoft\WindowsApps\ngrok.exe"
            if os.path.exists(system_ngrok):
                conf.get_default().ngrok_path = system_ngrok
            
            # BAGIAN 1: Membersihkan tunnel lama
            for tunnel in ngrok.get_tunnels():
                ngrok.disconnect(tunnel.public_url)
                print(f" * Memutuskan tunnel ngrok yang ada: {tunnel.public_url}")

            # BAGIAN 2: Membuat tunnel baru (setelah bersih-bersih)
            public_url = ngrok.connect(port)
            print(f" * Terhubung dengan ngrok. URL Publik: {public_url}")
        except ImportError:
            print(" * pyngrok tidak terinstal. Menjalankan tanpa ngrok.")
        except Exception as e:
            print(f" * Gagal menjalankan ngrok: {e}")

    try:
        # Host 0.0.0.0 diperlukan untuk hosting publik/container
        app.run(debug=debug_mode, use_reloader=False, host='0.0.0.0', port=port)
    finally:
        if flask_env == 'development':
            try:
                from pyngrok import ngrok
                ngrok.kill()
            except:
                pass
