import sqlite3

conectar = sqlite3.connect('ejemplo.db')

cursor = conectar.cursor()
cursor.execute("SELECT * FROM productos")
tecnologias = cursor.fetchall()
for producto in tecnologias:
    print(producto)
    
conectar.commit()
conectar.close()


