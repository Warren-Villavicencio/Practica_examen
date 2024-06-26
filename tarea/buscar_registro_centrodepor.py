# Importamos la clase sessionmaker de sqlalchemy.orm que nos permitirá crear una sesión de base de datos.
from sqlalchemy.orm import sessionmaker

# Importamos la clase centrodeportivo de nuestro módulo tablas. Esta clase representa la tabla centrodeportivo en nuestra base de datos.
from tablas import centrodeportivo

# Importamos el objeto engine de nuestro módulo base_datos. Este objeto representa la conexión a nuestra base de datos.
from base_datos import engine

# Creamos una clase Session utilizando el método sessionmaker y pasándole nuestro objeto engine. Esta clase Session nos permitirá crear instancias de sesión para interactuar con la base de datos.
Session = sessionmaker(bind=engine) 

# Creamos una instancia de Session. Esta instancia representa una "conversación" con nuestra base de datos y nos permitirá ejecutar consultas.
session = Session()

# Solicitamos al usuario que ingrese el nombre del centro deportivo que desea buscar.
nombre_local = input("Ingresar el nombre del Centro deportivo que desea buscar: ")

# Realizamos una consulta a la base de datos para encontrar todos los centros deportivos que tengan el nombre ingresado por el usuario.
lista_centrodeportivo = session.query(centrodeportivo).filter(centrodeportivo.nombre == nombre_local).all()

# Verificamos si encontramos algún centro deportivo con el nombre ingresado por el usuario.
if not lista_centrodeportivo:
    # Si no encontramos ningún centro deportivo, informamos al usuario que el centro deportivo no se encuentra en la base de datos.
    print("El Centro deportivo con el nombre '{}' no se encuentra en la base de datos.".format(nombre_local))
else:
    # Si encontramos uno o más centros deportivos, los imprimimos uno por uno.
    for l in lista_centrodeportivo:
        print(l)
