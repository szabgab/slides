# sort mixed values


{% embed include file="src/examples/lists/sort_mixed.py" %}

In Python 3 it throws an exception.


**Output:**

{% embed include file="src/examples/lists/sort_mixed.out" %}

Python 2 puts the numbers first in numerical order and then the strings in ASCII order.

```
[100, 'foo', 42, 'bar']
[42, 100, 'bar', 'foo']
```


