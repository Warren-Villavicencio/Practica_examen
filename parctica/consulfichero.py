import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursito = conexion.cursor()
cursito.execute('select * from productos')
campos = cursito.description

for fila in cursito:
    print(fila)
conexion.commit()    
conexion.close()    
    

