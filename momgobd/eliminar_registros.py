
from base_conexion import client


# Aqui se permite eliminar el total de los registros 
# tanto de la tabla localcomida como la tabla centrodeportivo.

db = client.Mibase


db.drop_collection("localcomida")
db.drop_collection("centrodeportivo")
