
from base_conexion import client

# Con esta consulta se permite obtener la cantidad total de los registros 
# tanto de la tabla "centrodeportivo"y "localcomida".

db = client.Mibase
coleccion = db.localcomida

print("                                                  ")
print("***|Total de registros de la tabla localcomida|***")
print("                                                  ")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)
    
    
coleccion = db.centrodeportivo   

print("                                                      ")
print("***|Total de registros de la tabla centrodeportivo|***")
print("                                                      ")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)
 
