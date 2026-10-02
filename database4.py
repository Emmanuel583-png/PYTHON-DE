#using select function for fetching data 

import sqlite3
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("select * from students")
rows = cursor.fetchall()

for row in rows:
    print(f"{row[1]} scored {row[4]}")
    
conn.commit()
conn.close()