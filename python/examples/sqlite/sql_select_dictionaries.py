import sqlite3

conn = sqlite3.connect("sample.db")
conn.row_factory = sqlite3.Row

c = conn.cursor()

minimum = 0

sql = '''SELECT * FROM companies WHERE employees >= ?'''
for company in c.execute(sql, (minimum,)):
    # returns sqlite3.Row objects, but they can also act as dictionaries
    print(f"{company['id']} - {company['name']} - {company['employees']}")

conn.close()
