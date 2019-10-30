import os
from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)
result = engine.execute('SELECT * FROM person')

for row in result:
    print(row)

result.close()

# (1, 'Joe', 100)
# (2, 'Jane', 100)
# (3, 'Melinda', 100)
# (4, 'George', 100)
