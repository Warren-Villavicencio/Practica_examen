import sqlite3

conn = sqlite3.connect('ejemplo.db')

cursor = conn.cursor()


cursor.execute("SELECT * FROM productos where id=3 ")

conn.commit()

print(cursor.fetchone())

conn.close()

