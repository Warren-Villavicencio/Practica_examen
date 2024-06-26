
from base_conexion import client

# Aquí se permite agregar solo un registro previamente ingresado a las tablas "centrodeportivo"y "localcomida".


db = client.Mibase
coleccion = db.centrodeportivo


data_01 = {"nombre": "Miriam's Gym", "direccion": "Av. del Rotarismo", "telefono": 59342887675}

coleccion.insert_one(data_01)

db = client.Mibase
coleccion = db.localcomida


data_01 = {"nombre": "Mercado del Río", "direccion": " Avenida Malecón y Calle Colón MALECON 2000", "telefono": 5937589588}

coleccion.insert_one(data_01)


