from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)

conn = engine.connect()
results = conn.execute('SELECT balance, name FROM person WHERE id < :id', id = 3)
print(results.fetchall())   # [(100, 'Joe'), (100, 'Jane')]
conn.close()
