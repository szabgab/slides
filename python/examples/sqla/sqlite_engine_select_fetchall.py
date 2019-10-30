from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)
result = engine.execute('SELECT * FROM person WHERE id >= :id', id=3)

rows = result.fetchall()
print(rows)        # [(3, 'Melinda', 100), (4, 'George', 100)]

result.close()
