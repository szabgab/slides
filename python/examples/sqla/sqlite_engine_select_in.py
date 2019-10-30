from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)

results = engine.execute("SELECT * FROM person WHERE name IN ('Joe', 'Jane')")
print(results.fetchall()) # [(2, 'Jane', 100), (1, 'Joe', 100)]

# engine.execute("SELECT * FROM person WHERE name IN (:a0, :a1)", a0 = 'Joe', a1 = 'Jane')
