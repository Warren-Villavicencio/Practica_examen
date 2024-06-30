# Importamos la conexión a la base de datos desde el módulo base_datos
from base_datos import conn

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Definimos la consulta SQL para crear la tabla "Empresa"
# La tabla tiene los campos "nombre_empresa", "siglas", "direccion" y "edad"
cadena_sql = 'CREATE TABLE Empresa (nombre_empresa TEXT, siglas TEXT, direccion TEXT, \
 edad INTEGER)'

# Ejecutamos la consulta SQL
cursor.execute(cadena_sql)

# Cerramos el cursor
cursor.close()
