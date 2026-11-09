from fastapi import FastAPI
from pydantic import BaseModel
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL_NAME = "mistral"

app = FastAPI(
    title="ML III - LLM Local API",
    description="API didática que conecta uma aplicação FastAPI a um modelo Mistral rodando localmente via Ollama.",
    version="1.0",
)

class ChatRequest(BaseModel):
    messages: list[dict]
    temperature: float = 0.7

@app.get("/")
def root():
    return {
        "mensagem": "API funcionando!",
        "modelo": MODEL_NAME,
        "backend_llm": "Ollama local",
        "endpoint_principal": "/chat",
        "documentacao": "/docs",
    }

@app.get("/status")
def status():
    try:
        response = requests.get("http://127.0.0.1:11434/api/tags", timeout=5)
        response.raise_for_status()
        return {
            "api": "online",
            "ollama": "online",
            "modelo": MODEL_NAME,
        }
    except Exception:
        return {
            "api": "online",
            "ollama": "offline",
            "modelo": MODEL_NAME,
        }

@app.post("/chat")
def chat(request: ChatRequest):
    payload = {
        "model": MODEL_NAME,
        "messages": request.messages,
        "stream": False,
        "options": {
            "temperature": request.temperature
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        result = response.json()

        return {
            "resposta": result["message"]["content"],
            "modelo": MODEL_NAME,
        }

    except requests.exceptions.ConnectionError:
        return {
            "erro": "Não foi possível conectar ao Ollama. Verifique se ele está instalado e em execução."
        }

    except Exception as e:
        return {
            "erro": f"Erro inesperado: {e}"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
