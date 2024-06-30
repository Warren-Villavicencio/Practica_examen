# Importamos el cliente de la base de datos desde el módulo base_conexion
from base_conexion import client

# Nos conectamos a la base de datos llamada "Mibase"
db = client.Mibase

# Nos conectamos a la colección (tabla) "localcomida" dentro de "Mibase"
coleccion_comida = db.localcomida

# Contamos el número de documentos (registros) en la colección "localcomida"
numero_registros_comida = coleccion_comida.count_documents({})

# Imprimimos el número de registros en la colección "localcomida"
print(f"Colección: localcomida - Registros: {numero_registros_comida}")

# Nos conectamos a la colección (tabla) "centrodeportivo" dentro de "Mibase"
coleccion_deportes = db.centrodeportivo

# Contamos el número de documentos (registros) en la colección "centrodeportivo"
numero_registros_deportes = coleccion_deportes.count_documents({})

# Imprimimos el número de registros en la colección "centrodeportivo"
print(f"Colección: centrodeportivo - Registros: {numero_registros_deportes}")
