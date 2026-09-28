import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

for m_name in ["gemini-3.8-flash", "gemini-flash-latest", "gemini-3.5-flash", "gemini-pro-latest"]:
    try:
        model = genai.GenerativeModel(m_name)
        res = model.generate_content("Berapakah turunan dari f(x) = sin(x)*cos(x)? Jawab singkat.")
        print(f"SUCCESS with {m_name}:")
        print(res.text.strip())
        print("-" * 40)
    except Exception as e:
        print(f"FAILED with {m_name}: {e}")
