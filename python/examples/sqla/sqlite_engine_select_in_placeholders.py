from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)


names = ['Joe', 'Jane']
placeholders = []
data = {}
for i in range(len(names)):
    placeholders.append(':a' + str(i))
    data['a' + str(i)] = names[i]

# print(placeholders)  # [':a0', ':a1']
# print(data)          # {'a0': 'Joe', 'a1': 'Jane'}

sql = "SELECT * FROM person WHERE name IN ({})".format(', '.join(placeholders))
# print(sql)  #  SELECT * FROM person WHERE name IN (:a0, :a1)

#results = engine.execute(sql, a0 = 'Jane', a1 = 'Joe')
results = engine.execute(sql, **data)
print(results.fetchall()) # [(2, 'Jane', 100), (1, 'Joe', 100)]
