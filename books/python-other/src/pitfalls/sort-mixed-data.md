# Sort mixed data

{% embed include file="src/examples/pitfalls/sort.py" %}

In Python 2 it "works" is some strange way.

```
$ python examples/pitfalls/sort.py
```

{% embed include file="src/examples/pitfalls/sort2.out" %}

In Python 3 in **correctly** throws an exception.


```
air:python gabor$ python3  examples/pitfalls/sort.py
```
{% embed include file="src/examples/pitfalls/sort3.out" %}

