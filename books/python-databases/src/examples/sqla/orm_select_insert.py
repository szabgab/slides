from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from orm_create_db import Base, Genre, Movie, Person, Cast

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.metadata.bind = engine

session = Session(engine)

animation = session.query(Genre).filter(Genre.name == 'Animation').one()
session.add(Movie(title = "Moana", genre = animation))
session.add(Movie(title = "Trolls", genre = animation))

action = session.query(Genre).filter(Genre.name == 'Action').one()
session.add(Movie(title = "Power Rangers", genre = action))

comedy = session.query(Genre).filter(Genre.name == 'Comedy').one()
session.add(Movie(title = "Gostbuster", genre = comedy))


session.commit()
