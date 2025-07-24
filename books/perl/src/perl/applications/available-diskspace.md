# Reporting file system diskspace usage (df)

* df

{% embed include file="src/examples/applications/diskspace.pl" %}

```
$ perl diskspace.pl ; df /
Total Size:             48062440 K
Available:              38720692 K
Used:                   9341748 K
Percent Full:           20 %
Total available to me:  36279216 K

Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/sda1             48062440   9341748  36279216  21% /
```


