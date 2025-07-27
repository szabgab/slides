from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)
result = engine.execute('SELECT COUNT(*) FROM person')

r = result.fetchone()[0]
print(r)

result.close()