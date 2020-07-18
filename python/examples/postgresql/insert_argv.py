import psycopg2
import sys

if len(sys.argv) != 3:
    exit("Usage: {} ID NAME".format(sys.argv[0]))

uid, name = sys.argv[1:]


try:
    conn = psycopg2.connect("postgresql:///testdb")
except Exception as e:
    print("I am unable to connect to the database: ", e)

cur = conn.cursor()

try:
    cur.execute("INSERT INTO people (id, name) VALUES (%s, %s)", (uid, name))
    conn.commit()
except Exception as e:
    print(e)


