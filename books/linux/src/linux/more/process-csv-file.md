# Process CSV file

* perl

{% embed include file="src/examples/linux/process_csv_file.csv" %}

```
perl -n -a -F';' -E '$x += $F[2]; END { say $x }' examples/linux/process_csv_file.csv
```


