# SQLite Database Access
{id: sqlite}

## SQLite
{id: sqlite3}
{i: sqlite}

* [sqlite3](http://docs.python.org/library/sqlite3.html)


## Connecting to SQLite database
{id: sqlite-connect}
{i: connect|sqlite}
{i: cursor|sqlite}

![](examples/sqlite/sql_connect.py)


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
{i: :memory:}

![](examples/sqlite/sql_autoincrement.py)

