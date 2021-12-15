import sqlite3

conn = sqlite3.connect("companies.db")
crs = conn.cursor()

sql = '''
    CREATE TABLE companies (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    name        VARCRCHAR(100) UNIQUE NOT NULL,
                    established INTEGER NOT NULL,
                    employees   INTEGER DEFAULT 0
)
'''

try:
    crs.execute(sql)
except sqlite3.OperationalError as err:
    print(f'sqlite error: {err.args[0]}')  # table companies already exists
    print(f'remove companies.db to show how it works')

conn.commit()

conn.close()

print('done')
