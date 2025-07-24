import psycopg2
import sys

if len(sys.argv) != 3:
    exit("Usage: {} ID NAME".format(sys.argv[0]))

uid, name = sys.argv[1:]


try:
    #conn = psycopg2.connect("postgresql:///testdb")
    conn = psycopg2.connect("dbname='default_database' user='username' host='pgdatabase' password='password'")
except Exception as err:
    print(f"I am unable to connect to the database: {err}")

cur = conn.cursor()

try:
    cur.execute("INSERT INTO people (id, name) VALUES (%s, %s)", (uid, name))
    conn.commit()
except Exception as err:
    print(err)


