
# Importamos la función create_engine del módulo sqlalchemy. Esta función nos permitirá crear un objeto de motor que establece una conexión con nuestra base de datos.
from sqlalchemy import create_engine

# Creamos un objeto de motor llamado 'engine' utilizando la función create_engine. Le pasamos una cadena de conexión que especifica el tipo de base de datos y el nombre de la base de datos.
# En este caso, estamos utilizando SQLite como nuestro sistema de gestión de bases de datos, y el nombre de nuestra base de datos es 'Mibase.db'.
# La cadena 'sqlite:///' indica que queremos usar SQLite y que nuestra base de datos se encuentra en el mismo directorio que nuestro script de Python.
engine = create_engine('sqlite:///Mibase.db')
