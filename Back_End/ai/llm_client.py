import os
import time
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    genai = None
    GEMINI_AVAILABLE = False

class LLMClient:
    def __init__(self, provider: str = "ollama", api_url: str | None = None, api_key: str | None = None, model: str | None = None, max_retries: int = 2):
        self.provider = provider.lower()
        self.max_retries = max_retries

        if self.provider == "ollama":
            self.api_url = api_url or os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
            self.model = model or os.getenv("MODEL_NAME", "qwen2.5-coder:7b")
            if not self.api_url:
                raise RuntimeError("OLLAMA_API_URL tidak ditemukan. Tambahkan ke .env atau ke app.config.")
        elif self.provider == "gemini":
            if not GEMINI_AVAILABLE:
                raise RuntimeError("google-generativeai tidak terinstall. Install dengan: pip install google-generativeai")
            self.api_key = api_key or os.getenv("GEMINI_API_KEY")
            raw_model = model or os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
            if raw_model in ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.5-flash", "gemini-1.0-pro"]:
                raw_model = "gemini-3.6-flash"
            self.model = raw_model
            if not self.api_key:
                raise RuntimeError("GEMINI_API_KEY tidak ditemukan. Tambahkan ke .env atau ke app.config.")
            genai.configure(api_key=self.api_key)
        else:
            raise ValueError("Provider harus 'ollama' atau 'gemini'")
    def _extract_text(self, resp) -> str:
        try:
            if resp is None:
                return ""
            if isinstance(resp, str):
                return resp
            if hasattr(resp, "text"):
                return resp.text
            if hasattr(resp, "content"):
                return resp.content
            if isinstance(resp, dict):
                if "candidates" in resp and resp["candidates"]:
                    c = resp["candidates"][0]
                    return c.get("content") or c.get("text") or str(c)
                if "outputs" in resp and resp["outputs"]:
                    o = resp["outputs"][0]
                    if isinstance(o, dict):
                        return o.get("content") or o.get("text") or str(o)
                if "output" in resp:
                    return str(resp["output"])
            return str(resp)
        except Exception:
            return str(resp)

    def generate(self, prompt: str | None = None, messages: list | None = None, temperature: float = 0.3, top_p: float = 0.85, max_output_tokens: int = 2048, stop_sequences: list | None = None) -> str:
        last_exc = None
        for attempt in range(1, self.max_retries + 2):
            try:
                if self.provider == "ollama":
                    # Convert messages to prompt if provided
                    full_prompt = prompt
                    if messages:
                        # Combine system and user messages
                        system_msg = ""
                        user_msgs = []
                        for msg in messages:
                            if msg.get("role") == "system":
                                system_msg = msg.get("content", "")
                            elif msg.get("role") == "user":
                                user_msgs.append(msg.get("content", ""))
                        
                        # For Ollama, we often use a specific template, but a simple concat is common for base prompts
                        full_prompt = f"System: {system_msg}\n\nUser: " + "\n".join(user_msgs) if system_msg else "\n".join(user_msgs)

                    if not full_prompt:
                        raise ValueError("Either prompt or messages must be provided")

                    # Ollama API payload
                    payload = {
                        "model": self.model,
                        "prompt": full_prompt,
                        "stream": False,
                        "options": {
                            "temperature": temperature,
                            "top_p": top_p,
                            "num_predict": max_output_tokens,
                        }
                    }
                    # Tambahkan stop sequences jika disediakan
                    if stop_sequences:
                        payload["options"]["stop"] = stop_sequences

                    response = requests.post(self.api_url, json=payload, timeout=120)

                    # Logging tambahan agar mudah diagnosa endpoint yang salah
                    if not response.ok:
                        logging.warning(
                            "Ollama response not ok: status=%s body=%s",
                            response.status_code,
                            response.text[:500],
                        )
                        raise RuntimeError(f"Ollama API Error ({response.status_code}): {response.text}")
                    result = response.json()
                    return result.get("response", "")

                elif self.provider == "gemini":
                    # Use Google Gemini API
                    if not messages:
                        # Convert prompt to messages format
                        messages = [{"role": "user", "content": prompt or ""}]

                    system_instruction = None
                    gemini_messages = []

                    # Separate system instruction from chat history
                    for msg in messages:
                        role = msg.get("role")
                        content = msg.get("content", "").strip()

                        if not content:
                            continue

                        if role == "system":
                            system_instruction = content
                        elif role in ["user", "model", "assistant"]:
                            # Map 'assistant' role to 'model' for Gemini API
                            gemini_role = "model" if role in ["model", "assistant"] else "user"
                            gemini_messages.append({"role": gemini_role, "parts": [{"text": content}]})

                    candidate_models = [self.model]
                    for fallback_m in ["gemini-3.6-flash", "gemini-flash-latest", "gemini-pro-latest"]:
                        if fallback_m not in candidate_models:
                            candidate_models.append(fallback_m)

                    last_model_error = None
                    for mod_name in candidate_models:
                        try:
                            try:
                                if system_instruction:
                                    model = genai.GenerativeModel(mod_name, system_instruction=system_instruction)
                                else:
                                    model = genai.GenerativeModel(mod_name)
                            except TypeError:
                                # Fallback jika versi google-generativeai < 0.5.0
                                model = genai.GenerativeModel(mod_name)
                                if system_instruction:
                                    if gemini_messages and gemini_messages[0].get("role") == "user":
                                        gemini_messages[0]["parts"][0]["text"] = f"[Instruksi Sistem:\n{system_instruction}]\n\n" + gemini_messages[0]["parts"][0]["text"]
                                    else:
                                        gemini_messages.insert(0, {"role": "user", "parts": [{"text": f"[Instruksi Sistem:\n{system_instruction}]"}]})
                                        gemini_messages.insert(1, {"role": "model", "parts": [{"text": "Baik, saya mengerti."}]})

                            gemini_stop_sequences = stop_sequences[:5] if stop_sequences else None

                            response = model.generate_content(
                                gemini_messages,
                                generation_config=genai.types.GenerationConfig(
                                    temperature=temperature,
                                    max_output_tokens=max_output_tokens,
                                    top_p=top_p,
                                    stop_sequences=gemini_stop_sequences
                                )
                            )
                            return self._extract_text(response)
                        except Exception as m_err:
                            last_model_error = m_err
                            err_str = str(m_err).lower()
                            if "404" in err_str or "not found" in err_str:
                                logging.warning("Model %s 404 not found, mencoba fallback model berikutnya...", mod_name)
                                continue
                            raise m_err

                    if last_model_error:
                        raise last_model_error

            except Exception as e:
                last_exc = e
                logging.warning("LLM generate attempt %d failed: %s", attempt, e)
                time.sleep(0.6 * attempt)
                continue

        # Fallback darurat ke Ollama lokal jika Gemini bermasalah
        if self.provider == "gemini":
            try:
                logging.info("Gemini gagal setelah retry, mencoba fallback ke Ollama lokal...")
                ollama_client = LLMClient(provider="ollama")
                return ollama_client.generate(prompt=prompt, messages=messages, temperature=temperature, top_p=top_p, max_output_tokens=max_output_tokens)
            except Exception as ollama_err:
                logging.warning("Fallback ke Ollama juga gagal: %s", ollama_err)

        raise RuntimeError(f"LLM request failed after retries: {last_exc}")
