# SQLite
{id: sqlite}

## SQLite in memory example
{id: sqlite-in-memory-example}
{i: memory}
{i: open}
{i: execute}
{i: INSERT}
{i: SELECT}

* [sqlite](https://crates.io/crates/sqlite)

* In this example we use an in-memory database.
* That's useful for the examples and it can be also useful if we have a lot of data on the disk that we would like analyze using SQL statements but we don't need to store the data in a database.

* In general it is not a good idea to have values in the SQL statements, especially not variables, but in this first exampleswe use that for simplicity.

![](examples/sqlite/in-memory-example/Cargo.toml)
![](examples/sqlite/in-memory-example/src/main.rs)
![](examples/sqlite/in-memory-example/out.out)


## SQLite SELECT with placeholder
{id: sqlite-select-with-placeholder}
{i: prepare}
{i: bind_iter}
{i: next}


![](examples/sqlite/in-memory-select-placeholders/src/main.rs)

## SQLite INSERT with placeholder
{id: sqlite-insert-with-placeholder}
{i: prepare}
{i: bind}
{i: next}

![](examples/sqlite/in-memory-insert-placeholders/src/main.rs)

## SQLite Counter
{id: sqlite-counter}

![](examples/sqlite/counter/src/main.rs)

