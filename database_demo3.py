import pandas as pd
import sqlite3

conn = sqlite3.connect("logistics.db")

df = pd.read_sql_query("select * from shipment WHERE weight >160", conn) #printing without looping 
print(f"data type of df: {type(df)}")
print(df)
