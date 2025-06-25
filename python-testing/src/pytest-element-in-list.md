# PyTest element in list

{% embed include file="src/examples/pytest/test_in_list.py" %}

```
$ pytest test_in_list.py

    def test_in_list():
>       assert "dog" in get_list()
E       AssertionError: assert 'dog' in ['monkey', 'cat']
E        +  where ['monkey', 'cat'] = get_list()
```




