from sqlalchemy import create_engine

# se genera en enlace al gestor de base de

# datos para el ejemplo se usa la base de datos

# sqlite
engine = create_engine('sqlite:///ejemplo001.db')

# se crea la clase llamada Base que permite definir las clases bajo las

# características de SQLAlchemy

Base = declarative_base()


# Se crea la una entidad llamada Autor, que hereda

# de Base

class Autor(Base):

 __tablename__ = 'autor' # El nombre de la entidad en sqlite

# Se definen los atributos

id = Column(Integer, primary_key=True) # este atributo es entero y

# se lo considera como llave

# primaria

nombre = Column(String) # atributo de tipo String

apellido = Column(String)

nacionalidad = Column(String)

edad = Column(Integer)

# Sentencia que permite crear o migrar las clases en Python al

# gestor de base de datos, expresado en el engine.

Base.metadata.create_all(engine)