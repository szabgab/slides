import sqlite3

conn = sqlite3.connect("companies.db")
conn.row_factory = sqlite3.Row

crs = conn.cursor()

employees = 0
year = 2000

sql = 'SELECT * FROM companies WHERE employees >= ? AND established < ?'
for company in crs.execute(sql, (employees, year)):
    # returns sqlite3.Row objects, but they can also act as dictionaries
    print(f"{company['id']} - {company['name']} - {company['employees']} - {company['established']}")

conn.close()
