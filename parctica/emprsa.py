from base_datos import conn

cursor = conn.cursor()

cadena_sql = 'CREATE TABLE Empresa (nombre_empresa TEXT, siglas TEXT, direccion TEXT, \
 edad INTEGER)'
 
cursor.execute(cadena_sql)

cursor.close()


