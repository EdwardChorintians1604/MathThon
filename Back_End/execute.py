from Back_End.__init__ import create_app

execute = create_app()

# ===========================================
# MAIN PROGRAM
# ===========================================
if __name__ == "__main__":
    execute.run(debug=True)
