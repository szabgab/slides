import psycopg2

try:
    #conn = psycopg2.connect("postgresql:///testdb")
    conn = psycopg2.connect("dbname='default_database' user='username' host='pgdatabase' password='password'")
except Exception as err:
    print(f"I am unable to connect to the database: {err}")
