# Measurements on 32 core

On the 32 core CPU-Optimized server on [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)

```
perl count.pl 0 30 10000000
    Elapsed time 7.92
perl count.pl 30 30 10000000
    Elapsed time 0.45

perl process_csv.pl 0 30
    Elapsed time 38.01
perl process_csv.pl 30 30
    Elapsed time 3.02

perl httpget.pl wikipedia.txt 0 80
    Elapsed time 12.93
perl httpget.pl wikipedia.txt 20 80
    Elapsed time 4.06
perl httpget.pl wikipedia.txt 80 80
    Elapsed time 1.11
```


