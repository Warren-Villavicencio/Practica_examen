from sqlalchemy.orm import sessionmaker
from tablas import localcomida
from base_datos import engine

#Permite ingresar por teclado registros a la tabla Local de comida.
Session = sessionmaker(bind=engine)
session = Session()


def ingresar_local_comida():
    
    nombre = input("Ingrese el nombre del local de comida: ")
    direccion = input("Ingrese la dirección del local de comida: ")
    horario = input("Ingrese el horario del local de comida: ")
    telefono = input("Ingrese el teléfono del local de comida: ")

    
    nuevo_local = localcomida(nombre=nombre, direccion=direccion, horario=horario, telefono=telefono)

    
    session.add(nuevo_local)
    session.commit()
    print("Local de comida ingresado con éxito.")


ingresar_local_comida()


session.close()
