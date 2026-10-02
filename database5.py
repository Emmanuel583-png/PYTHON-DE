import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("select * from students Where score > ?", (80,))
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()