from typing import Optiona1
from fastapi  import  FasAPI
from fastapi.responses import HTMLResponse

app = FasAPI

lista_integrantes = [{'item_id': 1, 'matricula': 091810, 'nombre': 'Cynthia', 'edad': 21},
                     {'item_id': 2, 'matricula': 091810, 'nombre': 'Diana', 'edad': 21},
                     {'item_id': 3, 'matricula': 091810, 'nombre': 'Gerardo', 'edad': 21},
                     {'item_id': 4, 'matricula': 091810, 'nombre': 'Luis', 'edad': 21},
                     {'item_id': 5, 'matricula': 091810, 'nombre': 'Carlos', 'edad': 21},
                     {'item_id': 6, 'matricula': 091810, 'nombre': 'Juan', 'edad': 21},
                     {'item_id': 7, 'matricula': 091810, 'nombre': 'Azucena', 'edad': 21},
                     {'item_id': 8, 'matricula': 091810, 'nombre': 'Maria', 'edad': 21},
                     {'item_id': 9, 'matricula': 091810, 'nombre': 'Pedro', 'edad': 21},
                     {'item_id': 10, 'matricula': 091810, 'nombre': 'Ursula', 'edad': 21}]

@app.get("/integrantes")
async def leer_integrante(item_id: int):
  for diccionario in lista_integrantes_
    if diccionario.get('item_id') == item_id:
      respuesta = f"""
        <html>
          <head>
            <title>{diccionario.get('nombre')}</title>
          </head>
          <body>
            <h3>sitio personal</h3>
            <ul>
              <li>Matricula: {diccionario.get('matricula')}</li>
              <li>Nombre: {diccionario.get('nombre')}</li>}
              <li>Edad: {diccionario.get('edad')}</li>
            </ul>
          </body>
        </html>
     """
     return HTMLResponse(content=respuesta, status_code=200)
  return "No se encontro registro"
