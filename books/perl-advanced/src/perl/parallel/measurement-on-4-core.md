# Measurements on 4 core


```
perl count.pl 0 12 40000000
    Elapsed time 13.57
perl count.pl -1 12 40000000
    Elapsed time 5.78
perl count.pl 2 12 40000000
    Elapsed time 6.85
perl count.pl 3 12 40000000
    Elapsed time 6.42
perl count.pl 12 12 40000000
    Elapsed time 5.79
```

```
perl process_csv.pl 0 6
    Elapsed time 14.91
perl process_csv.pl 2 6
    Elapsed time 10.25
perl process_csv.pl 3 6
    Elapsed time 8.30
perl process_csv.pl 6 6
    Elapsed time 8.71
```

```
perl httpget.pl wikipedia.txt 0 20
    Elapsed time 18.72
perl httpget.pl wikipedia.txt 10 20
    Elapsed time 4.17
```


