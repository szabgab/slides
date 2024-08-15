import sqlite3

conn = sqlite3.connect(":memory:")
crs = conn.cursor()

# use the database here

conn.close()
