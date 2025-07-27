from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from orm_create_db import Base, Genre, Movie, Person, Cast

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.metadata.bind = engine

session = Session(engine)

movies = session.query(Movie).all()
for m in movies:
    print(m.title, "-", m.genre.name)
