# Testing Demo using Test::More (success)

```
cpanm Test::More
```

{% embed include file="src/examples/testing-demo/t/01-add.t" %}

```
$ prove -l t/01-add.t
```


```
t/01-add.t .. ok
All tests successful.
Files=1, Tests=1,  0 wallclock secs ( 0.02 usr  0.00 sys +  0.04 cusr  0.00 csys =  0.06 CPU)
Result: PASS
```


