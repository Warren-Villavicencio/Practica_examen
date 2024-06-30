# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
# La función connect() devuelve un objeto que representa la conexión a la base de datos
cursor = sqlite3.connect('ejemplo.db')

# Ejecutamos una consulta SQL para eliminar el producto con id 4 de la tabla "productos"
cursor.execute("delete from productos where id=4")

# Hacemos commit para guardar los cambios en la base de datos
cursor.commit()

# Cerramos la conexión a la base de datos
cursor.close()
