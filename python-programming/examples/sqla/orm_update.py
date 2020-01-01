from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from orm_create_db import Base, Genre, Movie, Person, Cast

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.metadata.bind = engine

session = Session(engine)

movie = session.query(Movie).filter(Movie.title == 'Gostbuster').one()
print(movie.title)
movie.title = 'Ghostbusters'
session.commit()

print(movie.title)

