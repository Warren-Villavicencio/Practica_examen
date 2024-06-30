# Importamos el cliente de la base de datos desde el módulo base_conexion
from base_conexion import client

# Nos conectamos a la base de datos llamada "Mibase"
db = client.Mibase

# Eliminamos la colección (tabla) "localcomida" de la base de datos "Mibase"
db.drop_collection("localcomida")

# Eliminamos la colección (tabla) "centrodeportivo" de la base de datos "Mibase"
db.drop_collection("centrodeportivo")
