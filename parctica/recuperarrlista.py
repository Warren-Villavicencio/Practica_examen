# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conectar = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursor = conectar.cursor()

# Ejecutamos una consulta SQL para seleccionar todos los campos de la tabla "productos"
cursor.execute("SELECT * FROM productos")

# Obtenemos todos los registros del resultado de la consulta SQL
tecnologias = cursor.fetchall()

# Iteramos sobre cada registro y lo imprimimos
for producto in tecnologias:
    print(producto)

# Hacemos commit para guardar los cambios en la base de datos
conectar.commit()

# Cerramos la conexión a la base de datos
conectar.close()
