# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conn = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejecutamos una consulta SQL para seleccionar todos los campos del producto con id 3 en la tabla "productos"
cursor.execute("SELECT * FROM productos where id=3 ")

# Hacemos commit para guardar los cambios en la base de datos
conn.commit()

# Obtenemos el primer registro del resultado de la consulta SQL y lo imprimimos
print(cursor.fetchone())

# Cerramos la conexión a la base de datos
conn.close()
