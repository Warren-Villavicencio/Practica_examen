# Importamos el módulo pymongo y el cliente de la base de datos desde el módulo base_conexion
import pymongo
from base_conexion import client

# Nos conectamos a la base de datos llamada "Mibase"
db = client.Mibase

# Nos conectamos a la colección (tabla) "localcomida" dentro de "Mibase"
coleccion = db.localcomida

# Imprimimos un encabezado para los registros de la tabla "localcomida"
print("***|Registros ordenados por nombre de la tabla localcomida|***")

# Obtenemos todos los documentos (registros) de la colección "localcomida"
data = coleccion.find()

# Ordenamos los documentos por el campo "nombre" en orden ascendente
data_02 = data.sort([("nombre", pymongo.ASCENDING)])

# Imprimimos cada registro
for registro in data_02:
    print(registro)

# Nos conectamos a la colección (tabla) "centrodeportivo" dentro de "Mibase"
coleccion = db.centrodeportivo

# Imprimimos un encabezado para los registros de la tabla "centrodeportivo"
print("***|Registros ordenados por nombre de la tabla centrodeportivo|***")

# Obtenemos todos los documentos (registros) de la colección "centrodeportivo"
data = coleccion.find()

# Ordenamos los documentos por el campo "nombre" en orden ascendente
data_02 = data.sort([("nombre", pymongo.ASCENDING)])

# Imprimimos cada registro
for registro in data_02:
    print(registro)
