# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "ejemplo.db"
conexion = sqlite3.connect('ejemplo.db')

# Creamos un cursor para ejecutar consultas SQL
cursito = conexion.cursor()

# Ejecutamos una consulta SQL para insertar un producto en la tabla "productos"
# El producto tiene el nombre "Teclado" y el precio 50
cursito.execute('insert into productos (nombre, precio) values(?, ?)', ('Teclado', 50))

# Hacemos commit para guardar los cambios en la base de datos
conexion.commit()

# Cerramos la conexión a la base de datos
conexion.close()
