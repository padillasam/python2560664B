from Persona import *
import sqlite3
lista=[]
personas=[]
with sqlite3.connect('sqlitepython/conpython.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM alumno;"
    lista=micursor.execute(sentencia).fetchall()
#print(lista)
for fila in lista:
    id=fila[0]
    nombre=fila[1]
    apellido=fila[2]
    email=fila[3]
    ob=Persona(id,nombre,apellido,email)
    personas.append(ob)

for objeto in personas:
    print(objeto.getNombreCompleto())