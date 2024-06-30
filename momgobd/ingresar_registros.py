# Importamos el cliente de la base de datos desde el módulo base_conexion
from base_conexion import client

# Nos conectamos a la base de datos llamada "Mibase"
db = client.Mibase

# Definimos una función para ingresar un registro en la colección "centrodeportivo"
def ingresar_centro_deportivo():
    # Nos conectamos a la colección "centrodeportivo"
    coleccion = db.centrodeportivo

    # Solicitamos al usuario que ingrese los datos del centro deportivo
    nombre = input("Ingrese el nombre del centro deportivo: ")
    direccion = input("Ingrese la dirección del centro deportivo: ")
    telefono = input("Ingrese el teléfono del centro deportivo: ")

    # Creamos un documento con los datos ingresados por el usuario
    documento = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": int(telefono)  
    }

    # Insertamos el documento en la colección "centrodeportivo"
    coleccion.insert_one(documento)

    # Informamos al usuario que el centro deportivo fue ingresado con éxito
    print("Centro deportivo ingresado con éxito.")

# Definimos una función para ingresar un registro en la colección "localcomida"
def ingresar_local_comida():
    # Nos conectamos a la colección "localcomida"
    coleccion = db.localcomida

    # Solicitamos al usuario que ingrese los datos del local de comida
    nombre = input("Ingrese el nombre del local de comida: ")
    direccion = input("Ingrese la dirección del local de comida: ")
    telefono = input("Ingrese el teléfono del local de comida: ")

    # Creamos un documento con los datos ingresados por el usuario
    documento = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": int(telefono)  
    }

    # Insertamos el documento en la colección "localcomida"
    coleccion.insert_one(documento)

    # Informamos al usuario que el local de comida fue ingresado con éxito
    print("Local de comida ingresado con éxito.")

# Llamamos a las funciones para ingresar los registros
ingresar_centro_deportivo()
ingresar_local_comida()
