# defined or

* //
* defined-or


How do you set a default value of a scalar?



```
$x = defined $x ? $x : $DEFAULT;

$x ||= $DEFAULT;

$x //= $DEFAULT;
```
{% embed include file="src/examples/feature/defined_or.pl" %}


