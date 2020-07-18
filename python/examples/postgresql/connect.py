import psycopg2

try:
    conn = psycopg2.connect("postgresql:///testdb")
    #conn = psycopg2.connect("dbname='testdb' user='ubuntu' host='localhost' password='secret'")
except Exception as e:
    print("I am unable to connect to the database: ", e)
