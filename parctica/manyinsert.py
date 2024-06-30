# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conectar = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursor = conectar.cursor()

# Definimos una lista de productos que queremos insertar en la tabla "productos"
# Cada producto es una tupla que contiene el id, el nombre y el precio del producto
productos = [
    (6, 'Protoboard', 50),
    (7, 'Board', 80)
]

# Ejecutamos una consulta SQL para insertar los productos en la tabla "productos"
# La función executemany() permite ejecutar la misma consulta SQL varias veces con diferentes valores
cursor.executemany("INSERT INTO productos (id, nombre, precio) VALUES (?, ?, ?)", productos)

# Hacemos commit para guardar los cambios en la base de datos
conectar.commit()

# Cerramos la conexión a la base de datos
conectar.close()
