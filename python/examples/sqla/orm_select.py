from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from orm_create_db import Base, Genre, Movie, Person, Cast

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.metadata.bind = engine

session = Session(engine)

for g in session.query(Genre).all():
    print(g.name, g.id)

print("---")
animation = session.query(Genre).filter(Genre.name == 'Animation').one()
print(animation.name, animation.id)
