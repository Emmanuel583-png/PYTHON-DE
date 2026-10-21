import sqlite3

conn = sqlite3.connect("logistics.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists shipment(
               shipment_id TEXT,
               destination TEXT,
               weight INTEGER
               )
""")

conn.commit()


batch_data = [
    ("shp-001", "Abuja", 120), 
    ("shp-002", "Lagos", 300),
    ("shp-003", "delta-state", 400)
]

cursor.executemany("insert into shipment VALUES(?,?,?)", batch_data)

conn.commit()