# Prepare CSV files

Generate CSV data files to be used by the CSV processing task. Each file has rows with the 3rd column being increasing numbers.
The number in the last row of each file contains the seriel number of the file. That will make the sum of the numbers different and we'll be able to verify if the results come from the different files.


{% embed include file="src/examples/forks/prepare_files.pl" %}

```
perl prepare_files.pl 12 2000000
```


