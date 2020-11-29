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

## SELECT data from SQLite database
{id: sqlite-select}
{i: SELECT|sqlite}
{i: fetchone|sqlite}

![](examples/sqlite/sql_select.py)

Use the result as an iterator, or call the fetchone method. If the result set might be empty,
then the fetchone might return None. Check for it!

## SELECT data from SQLite database into dictionaries
{id: sqlite-select-dictionary}

![](examples/sqlite/sql_select_dictionaries.py)


## INSERT data into SQLite database
{id: sqlite-insert}
{i: INSERT|sqlite}
{i: UPDATE|sqlite}
{i: ?|sqlite}

Use placeholders (?) supply the data in tuples.

![](examples/sqlite/sql_insert.py)

UPDATE works quite similar, but it might have a WHERE clause.






## A counter
{id: sqlite-counter}

![](examples/sqlite/counter.py)


