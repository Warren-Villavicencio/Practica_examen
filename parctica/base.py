# Importamos el módulo sqlite3
import sqlite3

# Importamos la conexión a la base de datos desde el módulo main
from main import conn

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Definimos la consulta SQL para insertar un autor en la tabla "Autor"
# Los valores se insertan en los campos "nombre", "apellido", "cedula" y "edad"
# Los valores se formatean en la cadena SQL usando el operador de formato %
cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# Ejecutamos la consulta SQL
cursor.execute(cadena_sql)

# Hacemos commit para guardar los cambios en la base de datos
conn.commit()
