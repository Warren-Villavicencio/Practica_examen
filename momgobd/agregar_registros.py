
from base_conexion import client

# Aquí se permite agregar registros previamente ingresados a las tablas "centrodeportivo"y "localcomida".

db = client.Mibase
coleccion = db.centrodeportivo

lista = [
{"nombre": "Gympower", "direccion": "Avenida León févres cordero", "telefono": 59380555555},
{"nombre": "Carlos & Misha Gym", "direccion": "Eleodoro Aviles Minuche", "telefono": 59342234489},
{"nombre": "Iron Gym", "direccion": "Av. Francisco de Orellana", "telefono": 59345113796},
{"nombre": "Miriam's Gym", "direccion": "Av. del Rotarismo", "telefono": 59342887675}
]

coleccion.insert_many(lista)

db = client.Mibase
coleccion = db.localcomida

lista = [
{"nombre": "Pepe Crabs Seafood Restaurant (Los cangrejos de Pepe Loza)", "direccion": "Alborada 13 ava Mz 25 V 16 Frente Supercines Rio Norte entrando por, veterinaria Pets", "telefono": 59342175158},
{"nombre": "El Buen Asado", "direccion": "Sauces 8 Mz.454.f13.v9, Av. Rodolfo Baquerizo Nazur", "telefono": 5937885585},
{"nombre": "Mercado del Río", "direccion": " Avenida Malecón y Calle Colón MALECON 2000", "telefono": 5937589588},
{"nombre": "El Marino Restaurante: Carnes a la Parrilla y Comida Tradicional en Guayaquil", "direccion": "Dr. Francisco Rizzo V 5", "telefono": 593989137647}
]

coleccion.insert_many(lista)

