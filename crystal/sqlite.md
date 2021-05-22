# SQLite
{id: sqlite}

## Try SQLite
{id: try-sqlite}
{i: SQLite}

* You need to install the development package for libsqlite3
* On Ubuntu

```
sudo apt-get install libsqlite3-dev
```

![](examples/sqlite/try_sqlite.cr)


## Multi-counter with SQLite
{id: multi-counter-sqlite}
{i: SQLite}

![](examples/sqlite/multi_counter_sqlite.cr)

Unhandled exception issue: https://github.com/crystal-lang/crystal-sqlite3/issues/52

## SQLite last_id last_insert_id
{id: last-insert-id}
{i: last_id}
{i: last_insert_id}

![](examples/sqlite/last_id.cr)

## SQLite UPDATE row_affected
{id: update-row-affected}

![](examples/sqlite/rows_affected.cr)

## SQLite exception handling (during INSERT)
{id: exception-handling}

* The internal exception handling should be enough, but apparently it is not
* See [this](https://github.com/crystal-lang/crystal-sqlite3/issues/52) report

![](examples/sqlite/insert_exception.cr)
