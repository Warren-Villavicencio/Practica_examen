import sqlite3

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()
cursor.execute("SELECT * FROM productos ")
productos = cursor.fetchone()

for producto in productos:
    print(producto) 
conexion.commit()    
conexion.close()

