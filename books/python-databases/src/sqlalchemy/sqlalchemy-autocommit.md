# SQLAlchemy autocommit

* begin
* commit
* rollback


Unlike the underlying database engines, SQLAlchemy uses autocommit.
That is, usually we don't need to call `commit()`, but if we would like to have a transaction we need to
start it using `begin()` and end it either with `commit()` or with `rollback()`.


