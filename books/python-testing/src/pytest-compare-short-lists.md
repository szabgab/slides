# PyTest compare short lists

{% embed include file="src/examples/pytest/test_short_lists.py" %}


```
$ pytest test_short_lists.py
```

```
    def test_short_lists():
>       assert get_lista() == get_listx()
E       AssertionError: assert ('a', 'b', 'c') == ('x', 'b', 'y')
E         At index 0 diff: 'a' != 'x'
E         Use -v to get the full diff
```


