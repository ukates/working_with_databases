import psycopg2

def create_table():
    #create connection object
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    #create a cursor object
    cur = conn.cursor()
    #sql code
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
update(20, 8, "Orange")
#update(11, 6, "Water Glass")
#print(view())
