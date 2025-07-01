import sqlite3

conn = sqlite3.connect("companies.db")
crs = conn.cursor()

name = 'Hostlocal'

sql = 'SELECT employees FROM companies WHERE name = ?'
crs.execute(sql, (name,))
row = crs.fetchone()
employees = row[0]


sql = 'UPDATE companies SET employees=? WHERE name = ?'
crs.execute(sql, (employees+1, name))
conn.commit()

print('-----------')

sql = 'SELECT name, employees FROM companies'
for name, employees in crs.execute(sql):
    print(f"{name} - {employees}")


conn.close()

