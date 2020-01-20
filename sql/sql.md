# SQL
{id: sql}

## RDBMS - Relational Databases
{id: sql-rdbms}
{i: RDBMS}

* [RDBMS - Relational database management system](https://en.wikipedia.org/wiki/Relational_database_management_system)
* [SQL - Structured Query Language](https://en.wikipedia.org/wiki/SQL)
* [DDL - Data definition language](https://en.wikipedia.org/wiki/Data_definition_language)
* [DML - Data Manipulation Language](https://en.wikipedia.org/wiki/Data_manipulation_language)
* [Database schema](https://en.wikipedia.org/wiki/Database_schema)
* [ACID - Atomicity, Consistency, Isolation, Durability](https://en.wikipedia.org/wiki/ACID)
* [CRUD - Create, read, update and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
* [Candidate key](http://en.wikipedia.org/wiki/Candidate_key)
* [Cartesian product](http://en.wikipedia.org/wiki/Cartesian_product)
* [Database normalization](https://en.wikipedia.org/wiki/Database_normalization)



## Popular Relational Databases
{id: sql-popular-rdbms}

* [Oracle](https://en.wikipedia.org/wiki/Oracle_Database)
* [MySQL](https://en.wikipedia.org/wiki/MySQL) (open source)
* [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
* [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) (open source)
* [IBM DB2](https://en.wikipedia.org/wiki/IBM_DB2)
* [IBM Informix](https://en.wikipedia.org/wiki/IBM_Informix)
* [SAP Sybase](https://en.wikipedia.org/wiki/Adaptive_Server_Enterprise)
* [Teradata](https://en.wikipedia.org/wiki/Teradata)
* [SQLite](https://en.wikipedia.org/wiki/SQLite) (open source)
* [Microsoft Access](https://en.wikipedia.org/wiki/Microsoft_Access)



## NoSQL
{id: sql-nosql}
{i: NoSQL}

* [NoSQL](https://en.wikipedia.org/wiki/NoSQL)
* [MongoDB](https://www.mongodb.com/)
* [Redis](https://redis.io/)
* [Apache Cassandra](http://cassandra.apache.org/)



## SQL Standards
{id: sql-standards}

* 1986
* ...
* 1999
* ...
* 2011



## Description
{id: sql-description}


An RDBMS holds data in tables. The columns of each table has names describing the value they hold.
Each row in this dable contains the data.




## Schemas
{id: sql-schemas}


Each databse usually can hold several schemas. Each schema is a set of tables and other database elements.
Usually each project has its own schema and usually there is no relation between data information
in one schema and another schema.




## CREATE TABLE
{id: sql-create-table}
{i: CREATE}
{i: ENUM}
{i: VARCHAR}
{i: FLOAT}
{i: INTEGER}
{i: DATE}
{i: ENUM}
{i: DDL}

* [DDL - Data definition language](https://en.wikipedia.org/wiki/Data_definition_language) (part of SQL)
* Column types
* Comments

![](examples/create_person.sql)


## DML - Data Manipulation Language
{id: sql-dml}
{i: DML}

* [DML](https://en.wikipedia.org/wiki/Data_manipulation_language)
* INSERT
* UPDATE
* DELETE
* SELECT



## INSERT
{id: sql-insert}
{i: INSERT}
![](examples/insert_people.sql)


## SELECT
{id: sql-select}
{i: SELECT}
{i: FROM}
![](examples/select_all.sql)

```
select * from person;
+----------------------+--------+--------+------------+---------------+--------+
| name                 | height | weight | birthday   | occupation    | gender |
+----------------------+--------+--------+------------+---------------+--------+
| Musashimaru Koyo     |   1.92 |    235 | 1971-05-02 | sumo wrestler | male   |
| Tara Nott Cunningham |   1.54 |     48 | 1972-05-10 | weight lifter | female |
| Elisa Di Francisca   |   1.77 |     65 | 1982-12-13 | foil fencer   | female |
| Alfrd Hajos          |   NULL |   NULL | 1878-02-01 | swimmer       | male   |
| Krisztina Egerszegi  |   1.74 |     57 | 1974-08-16 | swimmer       | female |
| Sharran Alexander    |   1.82 |    203 | NULL       | sumo wrestler | female |
+----------------------+--------+--------+------------+---------------+--------+
6 rows in set (0.00 sec)
```



## NULL
{id: sql-null}
{i: NULL}

If a field does not have a value, it has a <b>NULL</b> value in it. It is not the empty string. Not the number 0. It is <b>NULL</b>




## Reject INSERT
{id: sql-reject-insert}
![](examples/insert_people_bad.sql)

```
ERROR 1265 (01000): Data truncated for column 'height' at row 1
```


## SELECT WHERE
{id: sql-select-where}
{i: WHERE}
![](examples/select_sumo.sql)

```
+-------------------+--------+--------+------------+---------------+--------+
| name              | height | weight | birthday   | occupation    | gender |
+-------------------+--------+--------+------------+---------------+--------+
| Musashimaru Koyo  |   1.92 |    235 | 1971-05-02 | sumo wrestler | male   |
| Sharran Alexander |   1.82 |    203 | NULL       | sumo wrestler | female |
+-------------------+--------+--------+------------+---------------+--------+
2 rows in set (0.00 sec)
```


## WHERE not
{id: sql-where-not}

```
SELECT * FROM person WHERE occupation != "sumo wrestler";

+----------------------+--------+--------+------------+---------------+--------+
| name                 | height | weight | birthday   | occupation    | gender |
+----------------------+--------+--------+------------+---------------+--------+
| Tara Nott Cunningham |   1.54 |     48 | 1972-05-10 | weight lifter | female |
| Elisa Di Francisca   |   1.77 |     65 | 1982-12-13 | foil fencer   | female |
| Alfrd Hajos          |   NULL |   NULL | 1878-02-01 | swimmer       | male   |
| Krisztina Egerszegi  |   1.74 |     57 | 1974-08-16 | swimmer       | female |
+----------------------+--------+--------+------------+---------------+--------+
4 rows in set (0.00 sec)
```



## SELECT WHERE
{id: sql-select-partial-results}
![](examples/select_sumo_partial.sql)


## Aggregates
{id: sql-aggregates}
{i: COUNT}
![](examples/count_people.sql)


## constraints
{id: sql-constraints}
{i: NOT NULL}
{i: UNIQUE}
{i: PRIMARY KEY}
![](examples/cars.sql)
![](examples/insert_car.sql)
![](examples/insert_unsold_car.sql)
![](examples/insert_another_unsold_car.sql)


## PRIMARY KEY
{id: sql-primary-key}

* [natural primary key](https://en.wikipedia.org/wiki/Natural_key)
* [surrogate primary key](https://en.wikipedia.org/wiki/Surrogate_key)



## ACID
{id: sql-acid}
{i: ACID}

* [ACID](https://en.wikipedia.org/wiki/ACID)
* [Atomicity](https://en.wikipedia.org/wiki/Atomicity_(database_systems))
* [Consistency](https://en.wikipedia.org/wiki/Consistency_(database_systems))
* [Isolation](https://en.wikipedia.org/wiki/Isolation_(database_systems))
* [Durability](https://en.wikipedia.org/wiki/Durability_(database_systems))




