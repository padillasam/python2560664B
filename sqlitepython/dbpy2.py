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

#miselect(con,'alumno','email','=','dbrabon2@irs.gov')
#miselect(con,'alumno','id','<=',5)

def modificar(conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación exitosa !!!!')

#modificar(con,'alumno','nombre','Vegeta',1)
#DELETE FROM table_name WHERE condition;
def eliminar(conexion,tabla,campo,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación exitosa !!!!')

eliminar(con,'alumno','id',3)