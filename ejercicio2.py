from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def mostrar_inicio():

    @app.get("/integrantes/{item_id}")
    async def leer_integrante(item_id: int, matricula: int, nombre: str, edad: Optional[int] = None):
        respuesta = f"""
        <html>
        <head>
            <title>{nombre}</title>
        </head>
        <body>
            <h3>Sitio Personal</h3>
            <ul>
                <li>Matricula: {matricula}</li>
                <li>Nombre: {nombre}</li>
                <li>Edad: {edad}</li>
            </>
        </body>
        </html>
        """
        return HTMLResponse(content=respuesta, status_code=200)
