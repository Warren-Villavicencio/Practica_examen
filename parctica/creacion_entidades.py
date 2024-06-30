# Importamos la conexión a la base de datos desde el módulo base_datos
from base_datos import conn

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Definimos la consulta SQL para crear la tabla "Autor"
# La tabla tiene los campos "nombre", "apellido", "cedula" y "edad"
cadena_sql = 'CREATE TABLE Autor (nombre TEXT, apellido TEXT, cedula TEXT, \
 edad INTEGER)'

# Ejecutamos la consulta SQL
cursor.execute(cadena_sql)

# Cerramos el cursor
cursor.close()
