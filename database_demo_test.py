import sqlite3

raw_book_sales = [
    {"book_title": "Python Basics", "category": "tech", "price": "$15.00", "qty": "3"},
    {"book_title": "Database Design", "category": "tech", "price": "$25.50", "qty": "2"},
    {"book_title": "Atomic Habits", "category": "self_help", "price": "$12.00", "qty": "5"},
    {"book_title": "Clean Code", "category": "tech", "price": "$30.00", "qty": "1"}
]

conn = sqlite3.connect("local_bookshop.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS initial_sales(
               book_title TEXT,
               category TEXT,
               price TEXT,
               qty TEXT
               )""")

#inserting the material in appropriate columns
for data in raw_book_sales:
    cursor.execute("INSERT OR IGNORE INTO initial_sales VALUES(?,?,?,?)",
                   (data["book_title"], data["category"], data["price"], data["qty"]))
    
conn.commit()

import pandas as pd

df = pd.read_sql_query("select * from initial_sales", conn)

#turning df["qty"] to interger state for future calculation
df["cleaned_qty"] = df["qty"].astype(int)

#turning df["price"] to float by removing the str for future calculation
df["cleaned_price"] = df["price"].str.replace("$", "").astype(float)

df["ttl_rev_gen"] = df["cleaned_price"] * df["cleaned_qty"]

#dropping unuseful columns for a clean out look
df = df.drop(columns= ["price","qty"])

df.to_sql("new_table", conn, index=False, if_exists="replace")

query = """
            SELECT category, SUM(ttl_rev_gen) as total_revenue
            FROM new_table
            GROUP BY category
"""

result = pd.read_sql_query(query, conn)
print(result)

conn.close()