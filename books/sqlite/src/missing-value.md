# Missing value

```sql
{{#include ../examples/missing-text-value.sql}}
```

```
$ sqlite3 demo.db < missing-text-value.sql ; rm -f demo.db
Language?|SQL
Database?|SQLite
Meaning of life?|
```

```sql
{{#include ../examples/missing-integer-value.sql}}
```

```
$ sqlite3 demo.db < missing-integer-value.sql ; rm -f demo.db
2+2|4
2-2|0
Meaning of life?|
```


