# One-liner sum numbers in CSV file


```
perl -n -a -F; -e '$sum += $F[2]; END {print $sum}' examples/perlarrays/process_csv_file.csv

-n  = loop over lines but do NOT print them
-a  = autosplit by ' ' and assign to @F
-F; = replace the split string by ';'
```

The `END` block gets executed at the end of the execution and only once.



