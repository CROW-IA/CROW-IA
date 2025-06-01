from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡CROW IA funcionando correctamente!"}


=======
    return {"mensaje": "¡CROW IA funcionando correctamente!"}
>>>>>>> ea147cf (Fix: configuración para Render y ruta raíz activa)
