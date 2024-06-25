import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursito = conexion.cursor()
cursito.execute('insert into productos (nombre, precio) values(?, ?)', ('Teclado', 50))
                
conexion.commit()
conexion.close()


