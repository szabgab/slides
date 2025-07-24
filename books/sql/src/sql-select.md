# SELECT

* SELECT
* FROM

{% embed include file="src/examples/select_all.sql" %}

```
select * from person;
+----------------------+--------+--------+------------+---------------+--------+
| name                 | height | weight | birthday   | occupation    | gender |
+----------------------+--------+--------+------------+---------------+--------+
| Musashimaru Koyo     |   1.92 |    235 | 1971-05-02 | sumo wrestler | male   |
| Tara Nott Cunningham |   1.54 |     48 | 1972-05-10 | weight lifter | female |
| Elisa Di Francisca   |   1.77 |     65 | 1982-12-13 | foil fencer   | female |
| Alfrd Hajos          |   NULL |   NULL | 1878-02-01 | swimmer       | male   |
| Krisztina Egerszegi  |   1.74 |     57 | 1974-08-16 | swimmer       | female |
| Sharran Alexander    |   1.82 |    203 | NULL       | sumo wrestler | female |
+----------------------+--------+--------+------------+---------------+--------+
6 rows in set (0.00 sec)
```



