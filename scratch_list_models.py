import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("Key:", api_key[:6] + "..." + api_key[-4:] if api_key else "None")

genai.configure(api_key=api_key)
try:
    print("Listing available models for this key:")
    found = False
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(f"- {m.name} ({m.display_name})")
            found = True
    if not found:
        print("No models found with generateContent!")
except Exception as e:
    print("Error listing models:", type(e), e)
