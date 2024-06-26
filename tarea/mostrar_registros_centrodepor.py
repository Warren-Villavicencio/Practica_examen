# Importamos la clase sessionmaker de sqlalchemy.orm que nos permitirá crear una sesión de base de datos.
from sqlalchemy.orm import sessionmaker

# Importamos la clase centrodeportivo de nuestro módulo tablas. Esta clase representa la tabla centrodeportivo en nuestra base de datos.
from tablas import centrodeportivo

# Importamos el objeto engine de nuestro módulo base_datos. Este objeto representa la conexión a nuestra base de datos.
from base_datos import engine

# Imprimimos un mensaje para indicar que vamos a mostrar todos los centros deportivos que se han ingresado.
print ("                                                                             ")
print ("***MOSTRANDO TODOS LOS CENTROS DEPORTIVOS QUE ACTUALMENTE SE HAN INGRESADO***")
print ("                                                                             ")

# Creamos una clase Session utilizando el método sessionmaker y pasándole nuestro objeto engine. Esta clase Session nos permitirá crear instancias de sesión para interactuar con la base de datos.
Session = sessionmaker(bind=engine) 

# Creamos una instancia de Session. Esta instancia representa una "conversación" con nuestra base de datos y nos permitirá ejecutar consultas.
session = Session()

# Realizamos una consulta a la base de datos para obtener todos los centros deportivos.
lista_centrodeportivo = session.query(centrodeportivo).all()

# Iteramos sobre la lista de centros deportivos e imprimimos cada uno.
for l in lista_centrodeportivo:
    print(l)
