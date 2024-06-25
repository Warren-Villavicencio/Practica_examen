import sqlite3

cursor = sqlite3.connect('ejemplo.db')

cursor.execute("update productos set precio=800 where id=4")

cursor.commit()

cursor.close()
