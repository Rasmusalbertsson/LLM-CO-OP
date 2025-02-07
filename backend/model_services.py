# backend/services/model_service.py
import subprocess

def call_deepseek(prompt: str) -> str:
    # Exempel på hur du kan anropa modellen via kommandorad (om Ollama erbjuder detta)
    # Modifiera efter behov om du har ett Python-SDK.
    command = f"ollama run deepseek --prompt \"{prompt}\""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Fel vid modellanrop: {e}"
