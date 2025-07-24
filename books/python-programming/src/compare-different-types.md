# Do NOT Compare different types!

{% embed include file="src/examples/boolean/compare.py" %}

In `Python 2` please be careful and only compare the same types.
Otherwise the result will look strange.


```
Yes
No
Yes
No
```

In `Python 3`, comparing different types raises exception:

{% embed include file="src/examples/boolean/compare.out" %}


