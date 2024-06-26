# Importamos la clase sessionmaker de sqlalchemy.orm que nos permitirá crear una sesión de base de datos.
from sqlalchemy.orm import sessionmaker

# Importamos la clase localcomida de nuestro módulo tablas. Esta clase representa la tabla localcomida en nuestra base de datos.
from tablas import localcomida

# Importamos el objeto engine de nuestro módulo base_datos. Este objeto representa la conexión a nuestra base de datos.
from base_datos import engine

# Creamos una clase Session utilizando el método sessionmaker y pasándole nuestro objeto engine. Esta clase Session nos permitirá crear instancias de sesión para interactuar con la base de datos.
Session = sessionmaker(bind=engine) 

# Creamos una instancia de Session. Esta instancia representa una "conversación" con nuestra base de datos y nos permitirá ejecutar consultas.
session = Session()

# Solicitamos al usuario que ingrese el nombre del local de comida que desea borrar.
nombre_local = input("Ingresar el nombre del local de comida que desea borrar: ")

# Realizamos una consulta a la base de datos para encontrar el primer local de comida que tenga el nombre ingresado por el usuario.
local_a_borrar = session.query(localcomida).filter(localcomida.nombre == nombre_local).first()

# Verificamos si encontramos un local de comida con el nombre ingresado por el usuario.
if local_a_borrar is not None:
    # Si encontramos un local de comida, lo borramos de la base de datos y confirmamos los cambios con un commit.
    session.delete(local_a_borrar)
    session.commit()
    # Informamos al usuario que el local de comida ha sido borrado exitosamente.
    print(f"El local de comida con el nombre '{nombre_local}' ha sido borrado exitosamente.")
else:
    # Si no encontramos un local de comida, informamos al usuario que no es posible borrar el registro porque el local de comida no existe.
    print(f"No es posible borrar el registro porque el local de comida con el nombre '{nombre_local}' no existe.")

# Cerramos la sesión.
session.close()
