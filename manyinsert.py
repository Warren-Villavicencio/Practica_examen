import sqlite3

conectar = sqlite3.connect('ejemplo.db')

cursor = conectar.cursor()

productos = [
    (6, 'Protoboard', 50),
    (7, 'Board', 80)
]
cursor.executemany("INSERT INTO productos (id, nombre, precio) VALUES (?, ?, ?)", productos)

conectar.commit()
conectar.close()

