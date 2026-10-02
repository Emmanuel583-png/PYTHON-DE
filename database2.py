import sqlite3 

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO students (name, department, level, score)
VALUES(?,?,?,?)
""", ("Emmanuel", "physics", 300, 85))

conn.commit()
conn.close()
print("its has been recorded!!")