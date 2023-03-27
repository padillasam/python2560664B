import sqlite3

with sqlite3.connect('sqlitepython/conpython.db')as con:
    micursor=con.cursor()
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"
    #print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())

miselect(con,'alumno','email','=','dbrabon2@irs.gov')
