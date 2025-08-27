from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# carregar modelo
modelo = joblib.load('modelo.joblib')

app = FastAPI()

class Entrada(BaseModel):
    texto: str

@app.post("/prever")
def prever(dados: Entrada):
    pred = modelo.predict([dados.texto])
    return {"texto": dados.texto, "sentimento": "positivo" if pred == 1 else "negativo"}
