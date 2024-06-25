from base_datos import conn
cursor = conn.cursor()
nombre_empresa = "La Gran Venta de Telas"
siglas = "LVT"
direccion = "Av Principal y Gran Colombia"
cadena_sql = "INSERT INTO Empresa (nombre_empresa, siglas, direccion) VALUES (?, ?, ?)"
cursor.execute(cadena_sql, (nombre_empresa, siglas, direccion))
conn.commit()


cadena = "UPDATE Empresa SET direccion=? WHERE siglas=?"
cursor.execute(cadena, (direccion_nueva, siglas))
conn.commit()

