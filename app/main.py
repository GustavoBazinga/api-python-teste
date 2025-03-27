from typing import Dict
from fastapi import FastAPI
from app.routers import produtos, usuarios


MENSAGEM_HOME: str = "Hello Wordl"


# Criando o App
app = FastAPI()

app.include_router(produtos.router)
app.include_router(usuarios.router)

# Iniciando o servidor


@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}
