import sqlite3

conn = sqlite3.connect("sample.db")
c = conn.cursor()

try:
    c.execute('''CREATE TABLE companies (
        id PRIMARY KEY,
        name VARCRCHAR(100) UNIQUE NOT NULL,
        employees INTEGER DEFAULT 0)''')
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])  # table companies already exists

conn.commit()

conn.close()

print('done')
