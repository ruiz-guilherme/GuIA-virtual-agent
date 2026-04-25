import requests
from app.config import OLLAMA_URL, MODELO

def perguntar_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODELO, "prompt": prompt, "stream": False}
    )
    return response.json()['response']