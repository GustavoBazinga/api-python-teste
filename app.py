from pydantic import BaseModel
from typing import List, Dict
from fastapi import FastAPI
from fastapi import APIRouter, HTTPException










MENSAGEM_HOME: str    ="Bem-vindo à API de Recomendação de Produtos"


# Criando o App
app = FastAPI()

# Iniciando o servidor

@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}


