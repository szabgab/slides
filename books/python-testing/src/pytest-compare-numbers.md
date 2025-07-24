# PyTest compare numbers

{% embed include file="src/examples/pytest/test_number_equal.py" %}

```
    $ pytest test_number_equal.py

    def test_string_equal():
        assert double(2) == 4
>       assert double(21) == 42
E       assert 23 == 42
E        +  where 23 = double(21)
```



