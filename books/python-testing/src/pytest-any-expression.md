# PyTest test any expression

{% embed include file="src/examples/pytest/test_expression_equal.py" %}

```
$ pytest test_expression_equal.py

    def test_expression_equal():
        a = 3
>       assert a % 2 == 0
E       assert (3 % 2) == 0
```



