# undef, the initial value and defined

```perl
$q = $x + 1;        # is 1 + warning as the default number is 0
$w = $y . "abc";    # is 'abc' + warning as the default string is ""
$z++;               # is 1 - no warning
```


You can check if the variable already has a value or if it still undef:



```perl
if (not defined $x) {   # to avoid warning
     $x = 0;
}
$x = $x + 1;
```



