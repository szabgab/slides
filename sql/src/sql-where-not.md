# WHERE not


```
SELECT * FROM person WHERE occupation != "sumo wrestler";

+----------------------+--------+--------+------------+---------------+--------+
| name                 | height | weight | birthday   | occupation    | gender |
+----------------------+--------+--------+------------+---------------+--------+
| Tara Nott Cunningham |   1.54 |     48 | 1972-05-10 | weight lifter | female |
| Elisa Di Francisca   |   1.77 |     65 | 1982-12-13 | foil fencer   | female |
| Alfrd Hajos          |   NULL |   NULL | 1878-02-01 | swimmer       | male   |
| Krisztina Egerszegi  |   1.74 |     57 | 1974-08-16 | swimmer       | female |
+----------------------+--------+--------+------------+---------------+--------+
4 rows in set (0.00 sec)
```


