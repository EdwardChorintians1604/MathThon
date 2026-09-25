from Back_End.__init__ import create_app
import os
from dotenv import load_dotenv

load_dotenv()

def debug_routes():
    app = create_app()
    print("Registered Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint} -> {rule.rule}")

if __name__ == "__main__":
    debug_routes()
