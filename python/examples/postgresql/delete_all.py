import psycopg2

try:
    conn = psycopg2.connect("postgresql:///testdb")
except Exception as e:
    print("I am unable to connect to the database: ", e)

cur = conn.cursor()

try:
    cur.execute("DELETE FROM people")
    conn.commit()
except Exception as e:
    print(e)

try:
    cur.execute("SELECT * from people")
    for r in cur.fetchall():
        print(r)
except Exception as e:
    print(e)




