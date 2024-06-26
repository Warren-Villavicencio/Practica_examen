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

# Solicitamos al usuario que ingrese el nombre del centro deportivo que desea borrar.
nombre_centrodeportivo = input("Ingresar el nombre del Centro deportivo que desea borrar: ")

# Realizamos una consulta a la base de datos para encontrar el primer centro deportivo que tenga el nombre ingresado por el usuario.
centrodeportivo_a_borrar = session.query(centrodeportivo).filter(centrodeportivo.nombre == nombre_centrodeportivo).first()

# Verificamos si encontramos un centro deportivo con el nombre ingresado por el usuario.
if centrodeportivo_a_borrar is not None:
    # Si encontramos un centro deportivo, lo borramos de la base de datos y confirmamos los cambios con un commit.
    session.delete(centrodeportivo_a_borrar)
    session.commit()
    # Informamos al usuario que el centro deportivo ha sido borrado exitosamente.
    print(f"El local de comida con el nombre '{nombre_centrodeportivo}' ha sido borrado exitosamente.")
else:
    # Si no encontramos un centro deportivo, informamos al usuario que no es posible borrar el registro porque el centro deportivo no existe.
    print(f"No es posible borrar el registro porque el Centro deportivo con el nombre '{nombre_centrodeportivo}' no existe.")

# Cerramos la sesión.
session.close()

