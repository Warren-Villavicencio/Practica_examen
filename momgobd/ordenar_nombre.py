import pymongo
from base_conexion import client

# permite ordenar las tablas "centrodeportivo"y "localcomida" de manera acendente 
# por el campo "nombre"

db = client.Mibase
coleccion = db.localcomida
print("                                                              ")
print("***|Registros ordenados por nombre de la tabla localcomida|***")
print("                                                              ")
data = coleccion.find()

data_02 = data.sort([("nombre", pymongo.ASCENDING)])

for registro in data_02:
    print(registro)
    
       

coleccion = db.centrodeportivo
print("                                                                  ")
print("***|Registros ordenados por nombre de la tabla centrodeportivo|***")
print("                                                                  ")
data = coleccion.find()

data_02 = data.sort([("nombre", pymongo.ASCENDING)])

for registro in data_02:
    print(registro)   