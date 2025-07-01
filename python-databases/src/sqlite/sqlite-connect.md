# Connecting to SQLite database


* connect|sqlite
* cursor|sqlite

This connects to the database in the given file. If the file does not exist yet this will create the file and prepare it to hold
an SQLite database. No tables are created at this point and no data is inserted.

{% embed include file="src/examples/sqlite/sql_connect.py" %}


