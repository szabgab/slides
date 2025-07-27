from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from orm_create_db import Base, Genre, Movie, Person, Cast

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.metadata.bind = engine

session = Session(engine)
genre = {}
for name in ('Action', 'Animation', 'Comedy', 'Documentary', 'Family', 'Horror'):
    genre[name] = Genre(name = name)
    session.add(genre[name])

print(genre['Animation'].name) # Animation
print(genre['Animation'].id)   # None
session.commit()

print(genre['Animation'].name) # Animation
print(genre['Animation'].id)   # 2
session.add(Movie(title = "Sing", genre = genre['Animation']))
session.commit()


