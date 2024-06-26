from sqlalchemy.orm import sessionmaker
from tablas import centrodeportivo
from tablas import localcomida
from base_datos import engine

#Agrega a las tablas local de comida y centro deportivo registros previamente ingresados.
Session = sessionmaker(bind=engine) 
session = Session()


centrodeportivo1 = centrodeportivo(nombre= "Gympower", direccion= "Avenida León févres cordero", horario="9:00 AM - 20:00 PM",
        telefono=59380555555)
centrodeportivo2 = centrodeportivo(nombre="Carlos & Misha Gym", direccion="Eleodoro Aviles Minuche", horario="9:00 AM - 20:00 PM",
        telefono=59342234489)
centrodeportivo3 = centrodeportivo(nombre= "Iron Gym", direccion="Av. Francisco de Orellana", horario="9:00 AM - 20:00 PM",
        telefono=59345113796)
centrodeportivo4 = centrodeportivo(nombre= "Miriam's Gym", direccion= "Av. del Rotarismo", horario="9:00 AM - 20:00 PM",
        telefono= 59342887675)

session.add(centrodeportivo1)
session.add(centrodeportivo2)
session.add(centrodeportivo3)
session.add(centrodeportivo4)


localcomida1 = localcomida(nombre= "Pepe Crabs Seafood Restaurant (Los cangrejos de Pepe Loza)", direccion="Alborada 13 ava Mz 25 V 16 Frente Supercines Rio Norte entrando por, veterinaria Pets", horario="9:00 AM - 20:00 PM",
        telefono=59342175158)
localcomida2 = localcomida(nombre= "El Buen Asado", direccion="Sauces 8 Mz.454.f13.v9, Av. Rodolfo Baquerizo Nazur", horario="9:00 AM - 20:00 PM",
        telefono=5937885585)
localcomida3 = localcomida(nombre="Mercado del Río", direccion= " Avenida Malecón y Calle Colón MALECON 2000", horario="9:00 AM - 20:00 PM",
        telefono=5937589588)
localcomida4 = localcomida(nombre= "El Marino Restaurante: Carnes a la Parrilla y Comida Tradicional en Guayaquil", direccion="Dr. Francisco Rizzo V 5", horario="9:00 AM - 20:00 PM",
        telefono=593989137647)

session.add(localcomida1)
session.add(localcomida2)
session.add(localcomida3)
session.add(localcomida4)


session.commit()
