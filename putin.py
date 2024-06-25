import sqlite3


conectar = sqlite3.connect('ejemplo.db')
cursor = conectar.cursor()
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)
conectar.commit()
conectar.close()    