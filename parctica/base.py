import sqlite3
from main import conn

cursor = conn.cursor()


cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \

VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

cursor.execute(cadena_sql)
conn.commit()
