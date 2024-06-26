from sqlalchemy.orm import sessionmaker

from tablas import localcomida

from base_datos import engine
print ("                                                                            ")
print ("***MOSTRANDO TODOS LOS LOCALES DE COMIDA QUE ACTUALMENTE SE HAN INGRESADO***")
print ("                                                                            ")

Session = sessionmaker(bind=engine) 
session = Session()

lista_localcomida = session.query(localcomida).all()

for l in lista_localcomida:
    print(l)
