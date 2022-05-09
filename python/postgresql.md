# PostgreSQL
{id: postgresql}

## PostgreSQL install
{id: postgresql-install}

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

## PostgreSQL with Docker compose
{id: postgresql-with-docker-compose}

![](examples/postgresql/Dockerfile)

![](examples/postgresql/docker-compose.yml)

```
docker-compose up
```

```
docker exec -it postgresql_app_1 bash
```


## Python and Postgresql
{id: postgresql-python}

```
$ sudo aptitude install python3-postgresql
$ sudo aptitude install python3-psycopg2
```


## PostgreSQL connect
{id: postgresql-connect}

![](examples/postgresql/connect.py)

## PostgreSQL create table
{id: postgresql-create-table}

![](examples/postgresql/create_table.py)



## INSERT
{id: postgresql-insert}

![](examples/postgresql/insert.py)

```
duplicate key value violates unique constraint "people_pkey"
DETAIL:  Key (id)=(1) already exists.
```

## INSERT (from command line)
{id: postgresql-insert-argv}

![](examples/postgresql/insert_argv.py)


## SELECT
{id: postgresql-select}

![](examples/postgresql/select_all.py)


## DELETE
{id: postgresql-delete}

![](examples/postgresql/delete_all.py)




