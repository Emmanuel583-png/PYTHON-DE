import sqlite3

conn = sqlite3.connect("logistics.db")
cursor = conn.cursor()

#fetching all matching rows 
cursor.execute("select * from shipment WHERE weight > 150 ")

rows = cursor.fetchall()

for row in rows:
    print(f"this is {row[0]} and {row[1]} is {row[2]}")

conn.close()