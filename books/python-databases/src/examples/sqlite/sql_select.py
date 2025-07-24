import sqlite3

conn = sqlite3.connect("companies.db")
crs = conn.cursor()

employees = 3

sql = 'SELECT * FROM companies WHERE employees >= ?'
for company in crs.execute(sql, (employees,)):
    print(company)

print('-----------')

year = 2000
sql = 'SELECT id, name FROM companies WHERE employees >= ? AND established < ?'
for id, name in crs.execute(sql, (employees, year)):
    print(f"{id} - {name}")

conn.close()
