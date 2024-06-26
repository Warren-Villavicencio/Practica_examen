import sqlite3

cursor = sqlite3.connect('ejemplo.db')

cursor.execute("delete from productos where id=4")

cursor.commit()

cursor.close()
