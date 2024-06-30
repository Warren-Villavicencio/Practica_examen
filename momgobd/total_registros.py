# Importamos el cliente de la base de datos desde el módulo base_conexion
from base_conexion import client

# Nos conectamos a la base de datos llamada "Mibase"
db = client.Mibase

# Nos conectamos a la colección (tabla) "localcomida" dentro de "Mibase"
coleccion = db.localcomida

# Imprimimos un encabezado para los registros de la tabla "localcomida"
print("***|Total de registros de la tabla localcomida|***")

# Obtenemos todos los documentos (registros) de la colección "localcomida"
data_02 = coleccion.find()

# Imprimimos cada registro
for registro in data_02:
    print(registro)

# Nos conectamos a la colección (tabla) "centrodeportivo" dentro de "Mibase"
coleccion = db.centrodeportivo

# Imprimimos un encabezado para los registros de la tabla "centrodeportivo"
print("***|Total de registros de la tabla centrodeportivo|***")

# Obtenemos todos los documentos (registros) de la colección "centrodeportivo"
data_02 = coleccion.find()

# Imprimimos cada registro
for registro in data_02:
    print(registro)
