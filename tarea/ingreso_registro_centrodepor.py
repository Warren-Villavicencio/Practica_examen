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

# Definimos una función llamada ingresar_centro_deportivo. Esta función solicitará al usuario que ingrese los detalles de un centro deportivo y luego agregará ese centro deportivo a la base de datos.
def ingresar_centro_deportivo():
    
    # Solicitamos al usuario que ingrese los detalles del centro deportivo.
    nombre = input("Ingrese el nombre del centro deportivo: ")
    direccion = input("Ingrese la dirección del centro deportivo: ")
    horario = input("Ingrese el horario del centro deportivo: ")
    telefono = input("Ingrese el teléfono del centro deportivo: ")

    # Creamos una nueva instancia de la clase centrodeportivo con los detalles ingresados por el usuario.
    nuevo_centro = centrodeportivo(nombre=nombre, direccion=direccion, horario=horario, telefono=telefono)

    # Agregamos la nueva instancia de centrodeportivo a nuestra sesión. Esto no ejecuta ninguna consulta en la base de datos todavía, simplemente marca esta instancia para ser incluida cuando se realice un commit.
    session.add(nuevo_centro)
    
    # Llamamos al método commit de nuestra sesión. Esto ejecuta todas las consultas acumuladas en la sesión (en este caso, la consulta INSERT para nuestra nueva instancia de centrodeportivo) y luego cierra la sesión.
    session.commit()
    
    # Informamos al usuario que el centro deportivo ha sido ingresado con éxito.
    print("Centro deportivo ingresado con éxito.")

# Llamamos a la función ingresar_centro_deportivo para ejecutarla.
ingresar_centro_deportivo()

# Cerramos la sesión.
session.close()
