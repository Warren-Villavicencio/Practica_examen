# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
# La función connect() devuelve un objeto que representa la conexión a la base de datos
cursor = sqlite3.connect('ejemplo.db')

# Ejecutamos una consulta SQL para actualizar el precio del producto con id 4 en la tabla "productos"
# El nuevo precio es 800
cursor.execute("update productos set precio=800 where id=4")

# Hacemos commit para guardar los cambios en la base de datos
cursor.commit()

# Cerramos la conexión a la base de datos
cursor.close()
