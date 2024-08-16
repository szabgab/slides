# SQLite
{id: sqlite}

## About SQLite
{id: about-sqlite}

* [SQLite](https://sqlite.org/) the most popular embedded relational database.
* No need for external server process. The client directly accesses the file containing the data.
* It has an in-memory version.

* Command-line tool is called `sqlite3`


## Using SQLite in programming languages
{id: using-sqlite-in-programming-languages}

* [Rust](https://rust.code-maven.com/slides/rust/sqlite)
* [Python](https://slides.code-maven.com/python/sqlite)
* [Perl](https://slides.code-maven.com/perl/perl-dbi)
* ...


## Install SQLite command-line tool
{id: install-sqlite-command-line-tool}

* [Download page](https://www.sqlite.org/download.html)

Debian/Ubuntu Linux:

```
$ sudo apt install sqlite3
```

## Version of SQLite
{id: version-of-sqlite}

```
$ echo .version | sqlite3
SQLite 3.45.1 2024-01-30 16:01:20 e876e51a0ed5c5b3126f52e532044363a014bc594cfefa87ffb5b82257ccalt1
zlib version 1.3
gcc-13.2.0 (64-bit)
```

## Help with SQLite
{id: help-with-sqlite}

```
echo .help | sqlite3
```

## SQLite interactive shell
{id: sqlite-interactive-shell}

```
$ sqlite3
SQLite version 3.45.1 2024-01-30 16:01:20
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.

sqlite> .version
SQLite 3.45.1 2024-01-30 16:01:20 e876e51a0ed5c5b3126f52e532044363a014bc594cfefa87ffb5b82257ccalt1
zlib version 1.3
gcc-13.2.0 (64-bit)

sqlite> .help
...

sqlite> .quit
```

## SQLite interactive shell - CREATE-INSERT-SELECT manually
{id: sqlite-interactive-shell-manually}

* Using in-memory database

```
sqlite3
```

* Using a database file

```
sqlite3 my.db
```


## CREATE INSERT SELECT
{id: create-insert-select}
{i: CREATE}
{i: INSERT}
{i: SELECT}

![](examples/create-insert-select.sql)

* In memory:

```
$ sqlite3 < create-insert-select.sql
Foo|foo@example.com
Bar|bar@example.com
```

* In file:

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

## Missing value
{id: missing-value}

![](examples/missing-text-value.sql)

```
$ sqlite3 demo.db < missing-text-value.sql ; rm -f demo.db
Language?|SQL
Database?|SQLite
Meaning of life?|
```

![](examples/missing-integer-value.sql)

```
$ sqlite3 demo.db < missing-integer-value.sql ; rm -f demo.db
2+2|4
2-2|0
Meaning of life?|
```

## Field with DEFAULT value
{id: field-with-default-value}

![](examples/default-value.sql)

```
$ sqlite3 demo.db < default-value.sql ; rm -f demo.db
Language?|SQL
Database?|SQLite
Meaning of life?|42
```

## FOREIGN KEY
{id: foreign-key}

* [SQLite Foreign key](https://sqlite.org/foreignkeys.html)

![](examples/foreign-key.sql)


## PRAGMA
{id: pragma}

[PRAGMA](https://sqlite.org/pragma.html)

## UPDATE
{id: update}

![](examples/update.sql)


## SQLite Transaction - in a bank
{id: sqlite-transactions-in-a-bank}

* Setup Bank accounts with some initial money.
* Move some money from one account to another - two separate steps. Worked.
* Move some money from one account to another - two separate steps - stop in the middle. Failed.
* Move some money from one account to another - Transaction - stop in the middle. Worked. (money stayed where it was)
* Remove bank

![](examples/bank/setup_bank.sql)
![](examples/bank/show.sql)
![](examples/bank/transfer.sql)
![](examples/bank/without_transaction.sql)
![](examples/bank/with_transaction.sql)

![](examples/bank/steps.sh)

![](examples/bank/out.out)



* TODO: loading a large CSV file into the database and running queries.
* TODO: creating a multi-tabe database, dumping it and then loading it and running queries against it.
* TODO: FOREIGN KEY - cascading deletition?


