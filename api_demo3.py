import requests #for apis
import sqlite3 #for database work and sql
import pandas as pd

request = requests.get("https://jsonplaceholder.typicode.com/users")
users = request.json()

conn = sqlite3.connect("work_on_api")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               id INTEGER,
               name TEXT,
               email TEXT)
""")

for use in users:
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?,?,?)",
                   (use['id'], use['name'], use['email']))
    
conn.commit()

df = pd.read_sql_query("select * from users", conn)

conn.close()
print(f"success")

