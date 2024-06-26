from sqlalchemy.orm import sessionmaker

from tablas import centrodeportivo

from base_datos import engine
print ("                                                                             ")
print ("***MOSTRANDO TODOS LOS CENTROS DEPORTIVOS QUE ACTUALMENTE SE HAN INGRESADO***")
print ("                                                                             ")

Session = sessionmaker(bind=engine) 
session = Session()

lista_centrodeportivo = session.query(centrodeportivo).all()

for l in lista_centrodeportivo:
    print(l)
