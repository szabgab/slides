import os
from sqlalchemy import create_engine

dbname = 'test.db'
if os.path.exists(dbname):
    os.unlink(dbname)

engine = create_engine('sqlite:///' + dbname)  # Engine

engine.execute('''
    CREATE TABLE person (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) UNIQUE,
        balance INTEGER NOT NULL
    );
''')


