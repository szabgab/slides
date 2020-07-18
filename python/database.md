# SQLite Database Access
{id: database}

## SQLite
{id: sqlite}
{i: sqlite}

* [sqlite3](http://docs.python.org/library/sqlite3.html)



## Connecting to SQLite database
{id: sqlite-connect}
{i: connect|sqlite}
{i: cursor|sqlite}
![](examples/database/sql_connect.py)


## Create TABLE in SQLite
{id: sqlite-create}
{i: CREATE|sqlite}
{i: execute|sqlite}
{i: commit|sqlite}

execute and commit

![](examples/database/sql_create.py)


## INSERT data into SQLite database
{id: sqlite-insert}
{i: INSERT|sqlite}
{i: UPDATE|sqlite}
{i: ?|sqlite}

Use placeholders (?) supply the data in tuples.

![](examples/database/sql_insert.py)

UPDATE works quite similar, but it might have a WHERE clause.



## SELECT data from SQLite database
{id: sqlite-select}
{i: SELECT|sqlite}
{i: fetchone|sqlite}
![](examples/database/sql_select.py)

Use the result as an iterator, or call the fetchone method. If the result set might be empty,
then the fetchone might return None. Check for it!




## A counter
{id: sqlite-counter}
![](examples/database/counter.py)




