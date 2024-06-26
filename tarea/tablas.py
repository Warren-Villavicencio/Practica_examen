from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

from base_datos import engine


Base = declarative_base()

class centrodeportivo(Base):
    __tablename__ = 'centrodeportivo' 
    id = Column(Integer, primary_key=True) 
    nombre = Column(String) 
    direccion = Column(String)
    horario = Column(String)
    telefono = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.direccion, self.horario,
        self.telefono)


class localcomida(Base):
    __tablename__ = 'localcomida' 
    id = Column(Integer, primary_key=True) 
    nombre = Column(String) 
    direccion = Column(String)
    horario = Column(String)
    telefono = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.direccion, self.horario,
        self.telefono)


Base.metadata.create_all(engine)
