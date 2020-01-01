import os
from sqlalchemy import create_engine

dbname = 'test.db'

engine = create_engine('sqlite:///' + dbname)

engine.execute('INSERT INTO person (name, balance) VALUES (:name, :balance)', name = 'Joe', balance = 100)
engine.execute('INSERT INTO person (name, balance) VALUES (:name, :balance)', name = 'Jane', balance = 100)
engine.execute('INSERT INTO person (name, balance) VALUES (:name, :balance)', name = 'Melinda', balance = 100)
engine.execute('INSERT INTO person (name, balance) VALUES (:name, :balance)', name = 'George', balance = 100)


