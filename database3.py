import sqlite3

students = [
    ("Kayode", "Geophysics", "400", "200"),
    ("Tochukwu", "physics", "200", "4"),
    ("Apokalito", "maths", "300", "69"),
    ("Wealth", "Medicine", "600", "200"),

]

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.executemany("""
INSERT INTO students (name, department, level, score)
VALUES(?,?,?,?)
""", students)

conn.commit()
conn.close()
print("lets gooo")