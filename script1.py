import sqlite3
#create connection object
conn = sqlite3.connect("lite.db")
#create a cursor object
cur = conn.cursor()
#sql code
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
conn.commit()
conn.close()
