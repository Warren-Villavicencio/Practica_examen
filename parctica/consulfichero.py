# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conexion = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursito = conexion.cursor()

# Ejecutamos una consulta SQL para seleccionar todos los campos de la tabla "productos"
cursito.execute('select * from productos')

# Obtenemos la descripción de los campos de la tabla "productos"
campos = cursito.description

# Iteramos sobre cada fila del resultado de la consulta SQL y la imprimimos
for fila in cursito:
    print(fila)

# Hacemos commit para guardar los cambios en la base de datos
conexion.commit()

# Cerramos la conexión a la base de datos
conexion.close()
