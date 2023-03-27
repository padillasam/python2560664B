import sqlite3
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
con=sqlite3.connect('sqlitepython/conpython.db')
print(type(con))
micursor=con.cursor()
print(type(micursor))
sentencia="SELECT * from alumno;"
micursor.execute(sentencia)
for fila in micursor.fetchall():
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('-'*50)