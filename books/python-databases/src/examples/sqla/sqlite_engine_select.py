from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)
result = engine.execute('SELECT * FROM person WHERE id=:id', id=3)

print(result)            # <sqlalchemy.engine.result.ResultProxy object at 0x1013c9da0>

row = result.fetchone()
print(row)               # (3, 'Melinda', 100)  - Its a tuple
print(row['name'])       # Melinda              - And a dictionary
print(row.name)          # Melinda   - and object with methods for the columns

for k in row.keys():     # keys also works on it
    print(k)             # id, name, balance

result.close()