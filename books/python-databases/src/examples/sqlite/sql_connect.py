import sqlite3

conn = sqlite3.connect("companies.db")
crs = conn.cursor()

# use the database here

conn.close()
