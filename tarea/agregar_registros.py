# Importamos la clase sessionmaker de sqlalchemy.orm que nos permitirá crear una sesión de base de datos.
from sqlalchemy.orm import sessionmaker

# Importamos las clases centrodeportivo y localcomida de nuestro módulo tablas. Estas clases representan las tablas en nuestra base de datos.
from tablas import centrodeportivo
from tablas import localcomida

# Importamos el objeto engine de nuestro módulo base_datos. Este objeto representa la conexión a nuestra base de datos.
from base_datos import engine

# Creamos una clase Session utilizando el método sessionmaker y pasándole nuestro objeto engine. Esta clase Session nos permitirá crear instancias de sesión para interactuar con la base de datos.
Session = sessionmaker(bind=engine) 

# Creamos una instancia de Session. Esta instancia representa una "conversación" con nuestra base de datos y nos permitirá ejecutar consultas.
session = Session()

# Creamos varias instancias de la clase centrodeportivo. Cada instancia representa un registro en la tabla centrodeportivo de nuestra base de datos.
centrodeportivo1 = centrodeportivo(nombre= "Gympower", direccion= "Avenida León févres cordero", horario="9:00 AM - 20:00 PM", telefono=59380555555)
centrodeportivo2 = centrodeportivo(nombre="Carlos & Misha Gym", direccion="Eleodoro Aviles Minuche", horario="9:00 AM - 20:00 PM", telefono=59342234489)
centrodeportivo3 = centrodeportivo(nombre= "Iron Gym", direccion="Av. Francisco de Orellana", horario="9:00 AM - 20:00 PM", telefono=59345113796)
centrodeportivo4 = centrodeportivo(nombre= "Miriam's Gym", direccion= "Av. del Rotarismo", horario="9:00 AM - 20:00 PM", telefono= 59342887675)

# Agregamos las instancias de centrodeportivo a nuestra sesión. Esto no ejecuta ninguna consulta en la base de datos todavía, simplemente marca estas instancias para ser incluidas cuando se realice un commit.
session.add(centrodeportivo1)
session.add(centrodeportivo2)
session.add(centrodeportivo3)
session.add(centrodeportivo4)

# Hacemos lo mismo para la tabla localcomida.
localcomida1 = localcomida(nombre= "Pepe Crabs Seafood Restaurant (Los cangrejos de Pepe Loza)", direccion="Alborada 13 ava Mz 25 V 16 Frente Supercines Rio Norte entrando por, veterinaria Pets", horario="9:00 AM - 20:00 PM", telefono=59342175158)
localcomida2 = localcomida(nombre= "El Buen Asado", direccion="Sauces 8 Mz.454.f13.v9, Av. Rodolfo Baquerizo Nazur", horario="9:00 AM - 20:00 PM", telefono=5937885585)
localcomida3 = localcomida(nombre="Mercado del Río", direccion= " Avenida Malecón y Calle Colón MALECON 2000", horario="9:00 AM - 20:00 PM", telefono=5937589588)
localcomida4 = localcomida(nombre= "El Marino Restaurante: Carnes a la Parrilla y Comida Tradicional en Guayaquil", direccion="Dr. Francisco Rizzo V 5", horario="9:00 AM - 20:00 PM", telefono=593989137647)

session.add(localcomida1)
session.add(localcomida2)
session.add(localcomida3)
session.add(localcomida4)

# Finalmente, llamamos al método commit de nuestra sesión. Esto ejecuta todas las consultas acumuladas en la sesión (en este caso, las consultas INSERT para nuestras instancias de centrodeportivo y localcomida) y luego cierra la sesión.
session.commit()

