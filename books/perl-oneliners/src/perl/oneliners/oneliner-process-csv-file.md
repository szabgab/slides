# One-liner: print the 3rd field of every line in a CSV file

* CSV
* -n
* -a
* -F

You have a number of csv files, you want to print the 3rd field of each row of each file.

```
perl -n -a -F, -e 'print "$F[2]\n"' *.csv
```


```
-n  = loop over lines but do NOT print them
-a  = autosplit by ' '
-F, = replace the split string by ','
```

You want to make sure all the rows are 4 elements long.
Print out file name and line number of all the bad rows.

```
perl -a -F, -n -e 'print "$ARGV:$.\n" if @F != 4' data.csv
```


