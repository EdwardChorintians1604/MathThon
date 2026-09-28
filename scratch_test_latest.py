import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("Testing gemini-flash-latest...", flush=True)
try:
    m = genai.GenerativeModel("gemini-flash-latest")
    r = m.generate_content("Hitung 2+3*4. Jawab singkat.")
    print("Result gemini-flash-latest:", r.text.strip(), flush=True)
except Exception as e:
    print("Error:", e, flush=True)

print("Testing gemini-pro-latest...", flush=True)
try:
    m = genai.GenerativeModel("gemini-pro-latest")
    r = m.generate_content("Hitung 2+3*4. Jawab singkat.")
    print("Result gemini-pro-latest:", r.text.strip(), flush=True)
except Exception as e:
    print("Error:", e, flush=True)
