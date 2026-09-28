import os
import sys
from dotenv import load_dotenv

load_dotenv()

from Back_End.ai.llm_client import LLMClient

print("--- 1. Testing Gemini Client with updated configuration ---")
client = LLMClient(provider="gemini")
print(f"Gemini client initialized with model: {client.model}")
prompt = "Selesaikan persamaan kuadrat x^2 - 5x + 6 = 0. Tuliskan langkahnya secara singkat dan hasil akhirnya."
res = client.generate(prompt=prompt)
print("\nResponse from Gemini:")
print(res[:600])

print("\n--- 2. Testing Ollama Fallback Model Configuration ---")
ollama_client = LLMClient(provider="ollama")
print(f"Ollama client model: {ollama_client.model}")
