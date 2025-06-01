from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/comando")
async def recibir_comando(request: Request):
    data = await request.json()
    print("Comando recibido:", data)
    return {"estado": "ok", "mensaje": f"Comando {data.get('accion')} recibido"}
