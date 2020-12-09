from fastapi import FastAPI, HTTPException
import db

app = FastAPI()


@app.get("/contactos/resumen/")
async def obtener_lista_contactos():
    return db.obtener_lista_contactos()


@app.post("/ordenes/crear/")
async def crear_contacto(contacto: db.Contacto):
    operacion_exitosa = db.crear_contacto(contacto)
    if operacion_exitosa:
        return {"mensaje": "contacto creado correctamente"}
    else:
        raise HTTPException(
            status_code=400, detail="Contacto no pudo ser creado: ya existía un contacto con ")
