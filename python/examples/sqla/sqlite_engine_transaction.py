from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)

conn = engine.connect()

trans = conn.begin()

src = 'Joe'
dst = 'Jane'
payment = 3

results = conn.execute("SELECT balance, name FROM person WHERE name = :name", name = src)
src_balance = results.fetchone()[0]
results.fetchall()
print(src_balance)


results = conn.execute("SELECT balance, name FROM person WHERE name = :name", name = dst)
dst_balance = results.fetchone()[0]
results.fetchall()
print(dst_balance)

conn.execute('UPDATE person SET balance = :balance WHERE name=:name', balance = src_balance - payment, name = src)
conn.execute('UPDATE person SET balance = :balance WHERE name=:name', balance = dst_balance + payment, name = dst)

trans.commit()

# trans.rollback()

conn.close()

results = engine.execute("SELECT * FROM person")
print(results.fetchall())
