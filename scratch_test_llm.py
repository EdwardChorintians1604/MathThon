import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("=== ENVIRONMENT CHECK ===")
print("GEMINI_API_KEY exists:", bool(os.getenv("GEMINI_API_KEY")))
if os.getenv("GEMINI_API_KEY"):
    key = os.getenv("GEMINI_API_KEY")
    print("GEMINI_API_KEY preview:", key[:6] + "..." + key[-4:])
print("GEMINI_MODEL:", os.getenv("GEMINI_MODEL"))
print("MODEL_NAME:", os.getenv("MODEL_NAME"))
print("OLLAMA_API_URL:", os.getenv("OLLAMA_API_URL"))

print("\n=== TESTING LLM CLIENT ===")
try:
    from Back_End.ai.llm_client import LLMClient
    client = LLMClient(provider="gemini")
    print("LLMClient initialized with provider='gemini', model=", client.model)
    res = client.generate(prompt="Hitung turunan pertama dari f(x) = 3x^2 + 5x - 7")
    print("\n--- RESPONSE FROM GEMINI ---")
    print(res[:500] if res else "(Empty response)")
except Exception as e:
    print("Error calling Gemini:", type(e), e)

print("\n=== TESTING OLLAMA CLIENT ===")
try:
    ollama_client = LLMClient(provider="ollama")
    print("OLLAMA model:", ollama_client.model)
    print("OLLAMA url:", ollama_client.api_url)
    res_ol = ollama_client.generate(prompt="Hitung 2+2")
    print("Ollama response:", res_ol[:200])
except Exception as e:
    print("Error calling Ollama:", type(e), e)
