from typing import Optiona1
from fastapi  import  FasAPI
from fastapi.responses import HTMLResponse

app = fastAPI

lista_integrantes = [{'item_id': 1, 'matricula': 091810, 'nombre': 'Cynthia', 'Apaterno':'Hernandez', 'AMaterno':'Morales', 'edad': 21},
                     {'item_id': 2, 'matricula': 091810, 'nombre': 'Diana','Apaterno':'Rodriguez', 'AMaterno':'Aguilar','edad': 21},
                     {'item_id': 3, 'matricula': 091810, 'nombre': 'Gerardo', 'Apaterno':'Perez', 'AMaterno':'Perez','edad': 21},
                     {'item_id': 4, 'matricula': 091810245, 'nombre': 'Luis', 'Apaterno':'Perez', 'AMaterno':'Morales','edad': 21},
                     {'item_id': 5, 'matricula': 091810, 'nombre': 'Carlos', 'Apaterno':'Cinto', 'AMaterno':'Ortiz','edad': 21},
                     {'item_id': 6, 'matricula': 091810, 'nombre': 'Juan', 'Apaterno':'Dominguez', 'AMaterno':'Herrera', 'edad': 21},
                     {'item_id': 7, 'matricula': 091810, 'nombre': 'Azucena','Apaterno':'Gonzalez', 'AMaterno':'Sanchez', 'edad': 21},
                     {'item_id': 8, 'matricula': 091810, 'nombre': 'Maria','Apaterno':'Santizo', 'AMaterno':'Estrada', 'edad': 21},
                     {'item_id': 9, 'matricula': 091810, 'nombre': 'Pedro', 'Apaterno':'Arrecho', 'AMaterno':'Escalante', 'edad': 21},
                     {'item_id': 10, 'matricula': 091810, 'nombre': 'Ursula','Apaterno':'Lopez', 'AMaterno':'Lopez', 'edad': 21}]

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
