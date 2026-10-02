import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute ("""
create table if not exists students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                department text,
                level integer,
                score integer
                )
""")

conn.commit()
conn.close()
print("table created")

