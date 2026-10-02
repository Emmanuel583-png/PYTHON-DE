import sqlite3
import pandas as pd

conn = sqlite3.connect("university.db")

df = pd.read_sql_query("select * from students where score > 50 ", conn)
print(df)

conn.close()