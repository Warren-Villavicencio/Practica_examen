from sqlalchemy.orm import sessionmaker
from tablas import centrodeportivo
from base_datos import engine

# Permite borrar un registro especifico de la tabla Centro deportivo

Session = sessionmaker(bind=engine)
session = Session()


nombre_centrodeportivo = input("Ingresar el nombre del Centro deportivo que desea borrar: ")

centrodeportivo_a_borrar = session.query(centrodeportivo).filter(centrodeportivo.nombre == nombre_centrodeportivo).first()


if centrodeportivo_a_borrar is not None:
    session.delete(centrodeportivo_a_borrar)
    session.commit()
    print(f"El local de comida con el nombre '{nombre_centrodeportivo}' ha sido borrado exitosamente.")
else:
    print(f"No es posible borrar el registro porque el Centro deportivo con el nombre '{nombre_centrodeportivo}' no existe.")


session.close()
