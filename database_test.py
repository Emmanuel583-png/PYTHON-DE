import sqlite3
import pandas as pd


conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists students(
               name TEXT,
               department TEXT,
               level INTEGER,
               score INTEGER
               )
""")
conn.commit()

students = [
    ("Emmanuel", "Physics", 300, 85),
    ("Tolu", "Chemistry", 200, 42),
    ("Amara", "Physics", 100, 91),
    ("Blessing", "Chemistry", 400, 36),
    ("Kemi", "Physics", 300, 78),
]

cursor.executemany("""
INSERT INTO students (name, department, level, score)
VALUES(?,?,?,?)
""", students)
conn.commit()

df = pd.read_sql_query("select * from students where score > 50", conn)
print(df)

conn.close()