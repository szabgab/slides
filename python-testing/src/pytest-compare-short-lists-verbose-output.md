# PyTest compare short lists - verbose output

```
$ pytest -v test_short_lists.py
```

```
    def test_short_lists():
>       assert get_lista() == get_listx()
E       AssertionError: assert ('a', 'b', 'c') == ('x', 'b', 'y')
E         At index 0 diff: 'a' != 'x'
E         Full diff:
E         - ('a', 'b', 'c')
E         ?   ^         ^
E         + ('x', 'b', 'y')
E         ?   ^         ^
```


