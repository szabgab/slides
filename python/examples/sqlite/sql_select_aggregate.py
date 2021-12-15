import sqlite3

conn = sqlite3.connect("companies.db")
crs = conn.cursor()

employees = 3
year = 2000

sql = 'SELECT COUNT(id) FROM companies WHERE employees >= ? AND established < ?'
crs.execute(sql, (employees, year))
row = crs.fetchone()
print(row)
print(row[0])

name = '%o%'
sql = 'SELECT SUM(employees) FROM companies WHERE name LIKE ? AND established < ?'
crs.execute(sql, (name, year))
row = crs.fetchone()
print(row)
print(row[0])


conn.close()
