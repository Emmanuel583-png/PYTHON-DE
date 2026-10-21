#this vsc sheet is for learning how to carry unclean data and cleaning it to its useful state
import sqlite3

# Raw incoming data from a remote sensor
raw_sensor_batch = [
    {"sensor_id": "SEN-101", "reading": "25.5C", "status": "active"},
    {"sensor_id": "SEN-102", "reading": "30.0C", "status": "warning"},
    {"sensor_id": "SEN-101", "reading": "26.2C", "status": "active"}
]

conn = sqlite3.connect("factory_pipeline.db")

cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS raw_sensors(
        sensor_id TEXT,
        reading TEXT,
        status TEXT)
"""
)

for item in raw_sensor_batch:
    cursor.execute("insert into raw_sensors VALUES(?,?,?)",
                   (item["sensor_id"], item["reading"], item["status"]) )

conn.commit()

#pulling and transforming with pandas
import pandas as pd

df = pd.read_sql_query("select * from raw_sensors", conn)
print(df)

#replacing the character or letter c and dropping the column
df["temp_in_C"] = df["reading"].str.replace("C", "").astype(float)

df = df.drop(columns= ["reading"])

df.to_sql("clean_sensors", conn, if_exists="replace", index=False)
conn.close()

