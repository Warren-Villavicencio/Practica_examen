
import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursito = conexion.cursor()

cursito.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')

conexion.close
