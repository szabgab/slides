import psycopg2

try:
    #conn = psycopg2.connect("postgresql:///testdb")
    conn = psycopg2.connect("dbname='default_database' user='username' host='pgdatabase' password='password'")
except Exception as err:
    print(f"I am unable to connect to the database: {err}")

cur = conn.cursor()

try:
    cur.execute("CREATE TABLE people (id INTEGER PRIMARY KEY, name VARCHAR(100))")
    conn.commit()
except Exception as err:
    print(err)

