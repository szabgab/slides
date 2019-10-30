from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

dbname = 'imdb.db'
engine = create_engine('sqlite:///' + dbname)

Base.prepare(engine, reflect=True)
Genre  = Base.classes.genre
Movie  = Base.classes.movie
Person = Base.classes.person
Cast   = Base.classes.cast



session = Session(engine)
for name in ('Action', 'Animation', 'Comedy', 'Documentary', 'Family', 'Horror'):
    session.add(Genre(name = name))

session.add(Movie(title = "Sing", genre_id=2))
session.add(Movie(title = "Moana", genre_id=2))
session.add(Movie(title = "Trolls", genre_id=2))
session.add(Movie(title = "Power Rangers", genre_id=1))

session.commit()




