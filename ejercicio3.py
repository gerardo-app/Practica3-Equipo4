from typing import Optional
from fastapi import  FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_integrantes = [{'item_id': 1, 'matricula': 918102, 'nombre': 'Cynthia', 'Apaterno':'Hernandez', 'AMaterno':'Morales', 'edad': 21, 'Correo':'cynthia@gmail.com', 'Telefono': 9190000754, 'Carrera': 'IRIyC'},
                     {'item_id': 2, 'matricula': 918102, 'nombre': 'Diana','Apaterno':'Rodriguez', 'AMaterno':'Aguilar','edad': 21, 'Correo':'diana@gmail.com', 'Telefono': 9191547863, 'Carrera': 'IRIyC'},
                     {'item_id': 3, 'matricula': 918102, 'nombre': 'Gerardo', 'Apaterno':'Perez', 'AMaterno':'Perez','edad': 21, 'Correo':'gerardo@gmail.com', 'Telefono': 9617897704, 'Carrera': 'IRIyC'},
                     {'item_id': 4, 'matricula': 91810245, 'nombre': 'Luis', 'Apaterno':'Perez', 'AMaterno':'Morales','edad': 21, 'Correo':'luis@gmail.com', 'Telefono': 9621501328, 'Carrera': 'IRIyC'},
                     {'item_id': 5, 'matricula': 918102, 'nombre': 'Carlos', 'Apaterno':'Cinto', 'AMaterno':'Ortiz','edad': 21, 'Correo':'carlos@gmail.com', 'Telefono': 9617527681, 'Carrera': 'IRIyC'},
                     {'item_id': 6, 'matricula': 918102, 'nombre': 'Juan', 'Apaterno':'Dominguez', 'AMaterno':'Herrera', 'edad': 21, 'Correo':'juan@gmail.com', 'Telefono': 9190448573, 'Carrera': 'Ing. Civil'},
                     {'item_id': 7, 'matricula': 918102, 'nombre': 'Azucena','Apaterno':'Gonzalez', 'AMaterno':'Sanchez', 'edad': 21, 'Correo':'azucena@gmail.com', 'Telefono': 9618975326, 'Carrera': 'Contabilidad'},
                     {'item_id': 8, 'matricula': 918102, 'nombre': 'Maria','Apaterno':'Santizo', 'AMaterno':'Estrada', 'edad': 21, 'Correo':'maria@gmail.com', 'Telefono': 9196405124, 'Carrera': 'Turismo'},
                     {'item_id': 9, 'matricula': 918102, 'nombre': 'Pedro', 'Apaterno':'Arrecho', 'AMaterno':'Escalante', 'edad': 21, 'Correo':'pedro@gmail.com', 'Telefono': 9195721687, 'Carrera': 'IRIyC'},
                     {'item_id': 10, 'matricula': 918102, 'nombre': 'Ursula','Apaterno':'Lopez', 'AMaterno':'Lopez', 'edad': 21, 'Correo':'ursula@gmail.com', 'Telefono': 9627951031, 'Carrera': 'Gastronomia'}]

@app.get("/integrantes")
async def leer_integrante(item_id : int):
  for diccionario in lista_integrantes:
      if diccionario.get('item_id') == item_id:
          respuesta = f"""
            <html>
            <head>
                <tit++le>{diccionario.get('nombre')}</title>
            </head>
            <body>
                <h3>sitio personal</h3>
                <ul>
                    <li>Matricula: {diccionario.get('matricula')}</li>
                    <li>Nombre: {diccionario.get('nombre')}</li>
                    <li>Apaterno: {diccionario.get('Apaterno')}</li>
                    <li>AMaterno: {diccionario.get('AMaterno')}</li>
                    <li>Edad: {diccionario.get('edad')}</li>
                    <li>Correo: {diccionario.get('correo')}</li>
                    <li>Telefono: {diccionario.get('Telefono')}</li>
                    <li>Carrera: {diccionario.get('Carrera')}</li>
                </ul>
            </body>
            </html>
          """
          return HTMLResponse(content=respuesta, status_code=200)
  return "No se encontro registro"
