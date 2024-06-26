from sqlalchemy.orm import sessionmaker
from tablas import centrodeportivo
from base_datos import engine

#Permite ingresar por teclado registros a la tabla Centro deportivo.
Session = sessionmaker(bind=engine)
session = Session()


def ingresar_centro_deportivo():
    
    nombre = input("Ingrese el nombre del centro deportivo: ")
    direccion = input("Ingrese la dirección del centro deportivo: ")
    horario = input("Ingrese el horario del centro deportivo: ")
    telefono = input("Ingrese el teléfono del centro deportivo: ")

    
    nuevo_centro = centrodeportivo(nombre=nombre, direccion=direccion, horario=horario, telefono=telefono)

    
    session.add(nuevo_centro)
    session.commit()
    print("Centro deportivo ingresado con éxito.")


ingresar_centro_deportivo()


session.close()
