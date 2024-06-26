from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine
Base = declarative_base()

class Empresa(Base):
  __tablename__ = 'empresa' 
  id = Column(Integer, primary_key=True) 
  nombre_empresa = Column(String) 
  siglas = Column(String)
  direccion = Column(String)  
  
  def __str__(self):
   return "%s %s %s" % (self.nombre_empresa, self.siglas, self.direccion)

Base.metadata.create_all(engine)

