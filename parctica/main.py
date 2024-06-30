# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "data.db"
conn = sqlite3.connect('data.db')

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Definimos la consulta SQL para crear la tabla "Autor"
# La tabla tiene los campos "nombre", "apellido", "cedula" y "edad"
cadena_sql = 'CREATE TABLE Autor (nombre TEXT, apellido TEXT, cedula TEXT, edad INTEGER)'

# Ejecutamos la consulta SQL
cursor.execute(cadena_sql)

# Cerramos el cursor
cursor.close()
