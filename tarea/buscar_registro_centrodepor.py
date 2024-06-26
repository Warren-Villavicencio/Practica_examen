from sqlalchemy.orm import sessionmaker
from tablas import centrodeportivo
from base_datos import engine


Session = sessionmaker(bind=engine)
session = Session()


nombre_local = input("Ingresar el nombre del Centro deportivo que desea buscar: ")


lista_centrodeportivo = session.query(Centrodeportivo).filter(centrodeportivo.nombre == nombre_local).all()


if not lista_centrodeportivo:
    print("El Centro deportivo con el nombre '{}' no se encuentra en la base de datos.".format(nombre_local))
else:
   
    for l in lista_centrodeportivo:
        print(l)
