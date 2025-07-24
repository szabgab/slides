# Print expected values as well



So the problem is that the test runner has to compute the expected
results every time she runs the test script.

A slight improvement will be to show the expected
results next to the actual values.

{% embed include file="src/examples/php/intro/t02.php" %}


Result:

```
2 == 2
4 == 4
2 == 3
```


This is still hard to follow when there are lots
of cases or even a few cases with large output but it seems to be
a step in the good direction.


