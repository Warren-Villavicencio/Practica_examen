# Importamos la conexión a la base de datos desde el módulo base_datos
from base_datos import conn

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Definimos los datos de la empresa que queremos insertar
nombre_empresa = "La Gran Venta de Telas"
siglas = "LVT"
direccion = "Av Principal y Gran Colombia"

# Creamos la consulta SQL para insertar la empresa en la tabla "Empresa"
cadena_sql = "INSERT INTO Empresa (nombre_empresa, siglas, direccion) VALUES (?, ?, ?)"

# Ejecutamos la consulta SQL con los datos de la empresa
cursor.execute(cadena_sql, (nombre_empresa, siglas, direccion))

# Hacemos commit para guardar los cambios en la base de datos
conn.commit()

# Creamos la consulta SQL para actualizar la dirección de la empresa en la tabla "Empresa"
cadena = "UPDATE Empresa SET direccion=? WHERE siglas=?"

# Ejecutamos la consulta SQL con la nueva dirección y las siglas de la empresa
cursor.execute(cadena, (direccion_nueva, siglas))

# Hacemos commit para guardar los cambios en la base de datos
conn.commit()
