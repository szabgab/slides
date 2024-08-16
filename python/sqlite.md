# SQLite Database Access
{id: sqlite}

## SQLite
{id: sqlite3}
{i: sqlite}

* [SQLite](https://sqlite.org/) the most popular embedded relational database.
* [sqlite3](http://docs.python.org/library/sqlite3.html) - Python library to use SQLite.


## Connecting to SQLite database
{id: sqlite-connect}
{i: connect|sqlite}
{i: cursor|sqlite}

This connects to the database in the given file. If the file does not exist yet this will create the file and prepare it to hold
an SQLite database. No tables are created at this point and no data is inserted.

![](examples/sqlite/sql_connect.py)

## Connecting to in-memory SQLite database
{id: sqlite-in-memory-connect}

We can also create in-memory database.

This is not persistent, but it can be useful to load some data into memory and then do fast SQL queries on
that database.

![](examples/sqlite/in_memory.py)


## Create TABLE in SQLite
{id: sqlite-create}
{i: CREATE|sqlite}
{i: execute|sqlite}
{i: commit|sqlite}

execute and commit

![](examples/sqlite/sql_create.py)

## INSERT data into SQLite database
{id: sqlite-insert}
{i: INSERT|sqlite}
{i: ?|sqlite}

![](examples/sqlite/sql_insert.py)

* Use placeholders (?) supply the data in tuples and to avoid [Bobby tables](https://bobby-tables.com/)

## SELECT data from SQLite database
{id: sqlite-select}
{i: SELECT|sqlite}

![](examples/sqlite/sql_select.py)

* Use the result as an iterator.


## SELECT aggregate data from SQLite database
{id: sqlite-select-aggregate}
{i: SELECT|sqlite}
{i: COUNT|sqlite}
{i: SUM|sqlite}
{i: fetchone|sqlite}

![](examples/sqlite/sql_select_aggregate.py)

{aside}
If expecting only one row, call the fetchone method.
If the result set might be empty, then the fetchone might return None. Check for it!
{/aside}


## SELECT data from SQLite database into dictionaries
{id: sqlite-select-dictionary}

![](examples/sqlite/sql_select_dictionaries.py)

## UPDATE data in SQLite database
{id: sqlite-update}
{i: UPDATE|sqlite}

* UPDATE works quite similar, but it might have a WHERE clause.

![](examples/sqlite/sql_update.py)

## A counter
{id: sqlite-counter}

![](examples/sqlite/counter.py)

## SQLite in-memory AUTOINCREMENT
{id: sqlite-in-memory-autoincrement}
{i: AUTOINCREMENT}
{i: memory}

![](examples/sqlite/sql_autoincrement.py)

## SQLite in-memory field with DEFAULT value
{id: sqlite-in-memory-field-with-default-value}
{i: DEFAULT}
{i: memory}

![](examples/sqlite/sql_defaults.py)

## SQLite transactions
{id: sqlite-transactions}
{i: TBD}

This example is supposed to show the importance of transactions, but so far I failed to replicate the problem as we have in
[this example](https://slides.code-maven.com/sqlite/sqlite-transactions-in-a-bank)

![](examples/sqlite/in_memory_bank.py)

