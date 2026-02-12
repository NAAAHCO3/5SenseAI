from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="5SensAI - API Demo")

class AuditoriaInput(BaseModel):
    texto: str
    setor: str

@app.post("/predict")
async def predict_demo(data: AuditoriaInput):
    """
    Demonstração da interface de predição.
    No SaaS real, este endpoint utiliza um modelo TF-IDF + LogReg 
    treinado em +10k registros para classificar o Senso 5S.
    """
    return {
        "status": "Processado (Modo Demo)",
        "texto": data.texto,
        "classificacao": "Conforme",
        "senso_identificado": "Seiso (Limpeza)",
        "probabilidade": 0.98
    }

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API 5SensAI. Entre em contato para acesso completo."}