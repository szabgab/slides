# SQLite
{id: sqlite}


## About SQLite
{id: about-sqlite}

* [SQLite](https://sqlite.org/) the most popular embedded relational database.
* No need for exteranl server process. The client directly accesses the file containing the data.
* It has an in-memory version.

* Command-line tool is called `sqlite3`


## Using SQLite in programming languages
{id: using-sqlite-in-programming-languages}

* [Rust](https://rust.code-maven.com/slides/rust/sqlite)
* [Python](https://slides.code-maven.com/python/sqlite)
* [Perl](https://slides.code-maven.com/perl/perl-dbi)
* ...

## CREATE INSERT SELECT
{id: create-insert-select}
{i: CREATE}
{i: INSERT}
{i: SELECT}

![](examples/create-insert-select.sql)

```
$ sqlite3 demo.db < create-insert-select.sql
Foo|foo@example.com
Bar|bar@example.com

$ rm -f demo.db
```

## AUTOINCREMENT
{id: atoincrement}

![](examples/autoincrement.sql)

```
$ sqlite3 demo.db < autoincrement.sql
1|foo
2|bar

$ rm -f demo.db
```

## Field with DEFAULT value
{id: field-with-default-value}


```
$ sqlite3 demo.db < default-value.sql ; rm -f demo.db
Language?|SQL
Database?|SQLite
Meaning of life?|42
```
