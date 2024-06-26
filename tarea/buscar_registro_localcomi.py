from sqlalchemy.orm import sessionmaker
from tablas import localcomida
from base_datos import engine


Session = sessionmaker(bind=engine)
session = Session()


nombre_local = input("Ingresar el nombre del local de comida que desea buscar: ")


lista_localcomida = session.query(localcomida).filter(localcomida.nombre == nombre_local).all()


if not lista_localcomida:
    print("El local de comida con el nombre '{}' no se encuentra en la base de datos.".format(nombre_local))
else:
    
    for l in lista_localcomida:
        print(l)
