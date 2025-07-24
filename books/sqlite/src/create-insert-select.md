# CREATE INSERT SELECT


* CREATE
* INSERT
* SELECT

```sql
{{#include ../examples/create-insert-select.sql}}
```

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


