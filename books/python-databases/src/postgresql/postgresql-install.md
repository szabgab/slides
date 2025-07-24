# PostgreSQL install

```
$ sudo aptitude install postgresql

$ sudo -i -u postgres
$ createuser --interactive
  Add "ubuntu" as superuser   (we need a username that matches our Linux username)
$ createdb testdb

$ psql
$ sudo -u postgres psql

$ psql testdb
testdb=# CREATE TABLE people (id INTEGER PRIMARY KEY, name VARCHAR(100));
```


