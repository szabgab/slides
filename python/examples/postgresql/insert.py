import psycopg2

try:
    conn = psycopg2.connect("postgresql:///testdb")
except Exception as e:
    print("I am unable to connect to the database: ", e)

cur = conn.cursor()

uid = 1
name = 'Foo'

try:
    cur.execute("INSERT INTO people (id, name) VALUES (%s, %s)", (uid, name))
    conn.commit()
except Exception as e:
    print(e)

