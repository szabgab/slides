import psycopg2

try:
    #conn = psycopg2.connect("postgresql:///testdb")
    conn = psycopg2.connect("dbname='default_database' user='username' host='pgdatabase' password='password'")
except Exception as err:
    print(f"I am unable to connect to the database: {err}")

cur = conn.cursor()

try:
    cur.execute("SELECT * from people")
    for row in cur.fetchall():
        print(row)
except Exception as err:
    print(err)

