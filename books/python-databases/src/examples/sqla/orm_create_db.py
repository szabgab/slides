import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id   = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False, unique=True)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)

class Cast(Base):
    __tablename__ = 'cast'
    id = Column(Integer, primary_key=True)
    character = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    movie_id = Column(Integer, ForeignKey('movie.id'))



if __name__ == '__main__':
    dbname = 'imdb.db'
    if os.path.exists(dbname):
        os.unlink(dbname)
    engine = create_engine('sqlite:///' + dbname)
    Base.metadata.create_all(engine)

