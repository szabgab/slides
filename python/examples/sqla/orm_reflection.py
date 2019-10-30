from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.prepare(engine, reflect=True)
Genre = Base.classes.genre

print(Genre.metadata.sorted_tables)

for c in Base.classes:
     print(c)

#session = Session(engine)
#session.add(Address(email_address="foo@bar.com", user=User(name="foo")))
#session.commit()