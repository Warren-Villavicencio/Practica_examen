# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conexion = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutamos una consulta SQL para seleccionar todos los campos de la tabla "productos"
cursor.execute("SELECT * FROM productos ")

# Obtenemos el primer registro del resultado de la consulta SQL
productos = cursor.fetchone()

# Iteramos sobre cada campo del registro y lo imprimimos
for producto in productos:
    print(producto)

# Hacemos commit para guardar los cambios en la base de datos
conexion.commit()

# Cerramos la conexión a la base de datos
conexion.close()
