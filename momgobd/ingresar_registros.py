from base_conexion import client


db = client.Mibase

# Aquí se permite Ingresar registros pro teclado a las  tablas "centrodeportivo"y "localcomida".

def ingresar_centro_deportivo():
    coleccion = db.centrodeportivo
    nombre = input("Ingrese el nombre del centro deportivo: ")
    direccion = input("Ingrese la dirección del centro deportivo: ")
    telefono = input("Ingrese el teléfono del centro deportivo: ")

    
    documento = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": int(telefono)  
    }

    
    coleccion.insert_one(documento)
    print("Centro deportivo ingresado con éxito.")


def ingresar_local_comida():
    coleccion = db.localcomida
    nombre = input("Ingrese el nombre del local de comida: ")
    direccion = input("Ingrese la dirección del local de comida: ")
    telefono = input("Ingrese el teléfono del local de comida: ")

    
    documento = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": int(telefono)  
    }

   
    coleccion.insert_one(documento)
    print("Local de comida ingresado con éxito.")


ingresar_centro_deportivo()
ingresar_local_comida()
