import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

for m_name in ["gemini-2.5-flash", "gemini-flash-latest", "gemini-2.5-flash-lite", "gemini-2.5-pro"]:
    try:
        model = genai.GenerativeModel(m_name)
        res = model.generate_content("Hitung 15 * 14 dan jelaskan.")
        print(f"SUCCESS with {m_name}:")
        print(res.text[:200])
        print("-" * 40)
        break
    except Exception as e:
        print(f"FAILED with {m_name}: {e}")
