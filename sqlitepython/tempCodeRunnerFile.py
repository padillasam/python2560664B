import sqlite3
con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
print(type(con))
micursor=con.cursor()
print(type(micursor))