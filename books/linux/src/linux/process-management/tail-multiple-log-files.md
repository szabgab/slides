# tail multiple log files

```
$ (while [ 1 ]; do (echo -n "one "; date; sleep 1); done) &gt; one.txt &amp;
$ (while [ 1 ]; do (echo -n "two "; date; sleep 1); done) &gt; two.txt &amp;

$ tail -f one.txt -f two.txt
$ multitail one.txt two.txt
```

