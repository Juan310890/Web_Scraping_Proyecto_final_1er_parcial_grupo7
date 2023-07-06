import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
# obtengo la pagina a analizar
html_doc = requests.get(url)
# print(html_doc.text)
# parsear la pagina wb
soup = BeautifulSoup(html_doc.text, 'html.parser')

# print(soup.prettify())

titulo_datos = soup.h1.string
print(titulo_datos)

tabla = soup.find('table')

# Obtener las filas de la tabla
filas = tabla.find_all('tr')

Nombre = []
Apellido = []
Cedula = []
Sexo = []
Edad = []
Disciplina = []
Ciudad = []
Sede = []
Competencia = []

# Iterar sobre las filas e imprimir los datos
for fila in filas:
    # Obtener las celdas de la fila
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        Nombre.append(celdas[1].string)
        Apellido.append(celdas[2].string)
        Cedula.append(celdas[3].string)
        Sexo.append(celdas[4].string)
        Edad.append(celdas[5].string)
        Disciplina.append(celdas[6].string)
        Ciudad.append(celdas[7].string)
        Sede.append(celdas[8].string)
        Competencia.append(celdas[9].string)
    print(Nombre)
    print(Apellido)
    print(Cedula)
    print(Sexo)
    print(Edad)
    print(Disciplina)
    print(Ciudad)
    print(Sede)
    print(Competencia)

    df = pd.DataFrame(
        {'Nombre': Nombre, 'Apellido': Apellido, 'Cedula': Cedula, 'Sexo': Sexo, 'Edad': Edad, 'Disciplina': Disciplina,
         'Ciudad': Ciudad, 'Sede': Sede, 'Competencia': Competencia})
    df.to_csv('deportistas.csv', index=False, encoding='utf-8')
