# PyTest compare lists

{% embed include file="src/examples/pytest/test_lists.py" %}

```
$ pytest test_lists.py

    def test_long_lists():
>       assert get_list('a') == get_list('b')
E       AssertionError: assert ['0', '1', '2...'4', '5', ...]
            == ['0', '1', '2'...'4', '5', ...]
E         At index 100 diff: 'a' != 'b'
E         Use -v to get the full diff
```



