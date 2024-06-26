
from base_conexion import client

# Cuenta el total de registros por cada tabla
db = client.Mibase

coleccion_comida = db.localcomida
numero_registros_comida = coleccion_comida.count_documents({})
print(f"Colección: localcomida - Registros: {numero_registros_comida}")

coleccion_deportes = db.centrodeportivo
numero_registros_deportes = coleccion_deportes.count_documents({})
print(f"Colección: centrodeportivo - Registros: {numero_registros_deportes}")
