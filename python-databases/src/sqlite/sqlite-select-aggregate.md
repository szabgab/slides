# SELECT aggregate data from SQLite database


* SELECT|sqlite
* COUNT|sqlite
* SUM|sqlite
* fetchone|sqlite

{% embed include file="src/examples/sqlite/sql_select_aggregate.py" %}


If expecting only one row, call the fetchone method.
If the result set might be empty, then the fetchone might return None. Check for it!


