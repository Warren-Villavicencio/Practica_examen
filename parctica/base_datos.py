# Importamos el módulo sqlite3
import sqlite3

# Nos conectamos a la base de datos SQLite llamada "base_ejemplo.db"
# La función connect() establece una conexión a la base de datos.
# Si la base de datos especificada no existe, SQLite la creará.
conn = sqlite3.connect('base_ejemplo.db')
