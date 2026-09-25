from Back_End.__init__ import create_app

if __name__ == "__main__":
    app = create_app()
    print(" * Starting Flask server without ngrok for debugging...")
    app.run(debug=True, use_reloader=True, port=5000)
