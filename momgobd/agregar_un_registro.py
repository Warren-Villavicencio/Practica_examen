# Importamos el cliente de la base de datos desde el módulo base_conexion
from base_conexion import client

# Aquí se permite agregar solo un registro previamente ingresado a las tablas "centrodeportivo" y "localcomida".

# Nos conectamos a la base de datos llamada "Mibase"
db = client.Mibase

# Nos conectamos a la colección (tabla) "centrodeportivo" dentro de "Mibase"
coleccion = db.centrodeportivo

# Creamos un diccionario que representa un registro que queremos insertar en la colección "centrodeportivo"
data_01 = {"nombre": "Miriam's Gym", "direccion": "Av. del Rotarismo", "telefono": 59342887675}

# Insertamos el registro en la colección "centrodeportivo"
coleccion.insert_one(data_01)

# Nos conectamos a la colección (tabla) "localcomida" dentro de "Mibase"
coleccion = db.localcomida

# Creamos un diccionario que representa un registro que queremos insertar en la colección "localcomida"
data_01 = {"nombre": "Mercado del Río", "direccion": " Avenida Malecón y Calle Colón MALECON 2000", "telefono": 5937589588}

# Insertamos el registro en la colección "localcomida"
coleccion.insert_one(data_01)
