# Process CSV files


We expect two parameters on the command line. The number of parallel processes to run and how many files to process.
For parallel 0 means not to use the forking mechanizm at all.
We use the number of files instead of accepting the list of files on the command line, becasue it is easier to select a subset of the files this way.


{% embed include file="src/examples/forks/process_csv.pl" %}

```
$ perl process_csv.pl 0 1
Elapsed time 1.51

$ perl process_csv.pl 0 4
Elapsed time 5.92

$ perl process_csv.pl 2 4
Elapsed time 4.02

$ perl process_csv.pl 4 4
Elapsed time 4.01

$ perl process_csv.pl 0 10
Elapsed time 15.18

$ perl process_csv.pl 4 10
Elapsed time 9.05
```


