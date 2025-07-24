# SQLite Transaction - in a bank

* Setup Bank accounts with some initial money.
* Move some money from one account to another - two separate steps. Worked.
* Move some money from one account to another - two separate steps - stop in the middle. Failed.
* Move some money from one account to another - Transaction - stop in the middle. Worked. (money stayed where it was)
* Remove bank

```sql
{{#include ../examples/bank/setup_bank.sql}}
```

```sql
{{#include ../examples/bank/show.sql}}
```

```sql
{{#include ../examples/bank/transfer.sql}}
```

```sql
{{#include ../examples/bank/without_transaction.sql}}
```


```sql
{{#include ../examples/bank/with_transaction.sql}}
```

```sh
{{#include ../examples/bank/steps.sh}}
```


```txt
{{#include ../examples/bank/out.out}}
```


* TODO: loading a large CSV file into the database and running queries.
* TODO: creating a multi-tabe database, dumping it and then loading it and running queries against it.
* TODO: FOREIGN KEY - cascading deletition?


