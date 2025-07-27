# SQLAlchemy engine

* create_engine

```
engine = create_engine('sqlite:///test.db')               # relative path
engine = create_engine('sqlite:////full/path/to/test.db') # full path
engine = create_engine('sqlite://')                       # in memory database
```


**PostgreSQL**


```
engine = create_engine('postgresql://user:password@hostname/dbname')
engine = create_engine('postgresql+psycopg2://user:password@hostname/dbname')
```


**MySQL**


```
engine = create_engine("mysql://user:password@hostname/dbname", encoding='latin1') # defaults to utf-8
```


