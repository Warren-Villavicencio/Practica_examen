from sqlalchemy.orm import sessionmaker
from tablas import localcomida
from base_datos import engine

# Permite borrar un registro especifico de la tabla local de comida

Session = sessionmaker(bind=engine)
session = Session()


nombre_local = input("Ingresar el nombre del local de comida que desea borrar: ")

local_a_borrar = session.query(localcomida).filter(localcomida.nombre == nombre_local).first()


if local_a_borrar is not None:
    session.delete(local_a_borrar)
    session.commit()
    print(f"El local de comida con el nombre '{nombre_local}' ha sido borrado exitosamente.")
else:
    print(f"No es posible borrar el registro porque el local de comida con el nombre '{nombre_local}' no existe.")


session.close()
