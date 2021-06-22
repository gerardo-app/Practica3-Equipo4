from fastapi import FastAPI
from fastapi import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def mostrar_inicio():
    contenido_html = """
    <html>
    <head>
        <title>Equipo4</title>
    </head>
    <body>
        <h3>Bienvenidos</h3>
        <p>Este sitio pertenece al Equipo 4 y mostrará los datos de los integrantes</p>
        <a href="gerardo.html">Gerardo</a>
    </body>
    </html>
    """
    return HTMLResponse (content=contenido_html, status_code=200)
