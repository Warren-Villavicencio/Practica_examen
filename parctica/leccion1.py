# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conexion = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursito = conexion.cursor()

# Ejecutamos una consulta SQL para crear la tabla "productos"
# La tabla tiene los campos "id", "nombre" y "precio"
# El campo "id" es la clave primaria y se autoincrementa
# Los campos "nombre" y "precio" no pueden ser NULL
cursito.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')

# Cerramos la conexión a la base de datos
conexion.close()
