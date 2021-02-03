# Pytest assert
{id: pytest-assert}

## PyTest failure reports
{id: pytest-failure-reports}

* Reporting success is boring
* Reporting failure can be interesting: assert + introspection



## PyTest compare numbers
{id: pytest-compare-numbers}
![](examples/pytest/test_number_equal.py)

```
    $ pytest test_number_equal.py

    def test_string_equal():
        assert double(2) == 4
>       assert double(21) == 42
E       assert 23 == 42
E        +  where 23 = double(21)
```



## PyTest compare numbers relatively
{id: pytest-compare-numbers-relatively}

![](examples/pytest/test_number_less_than.py)

```
$ pytest test_number_less_than.py
```

![](examples/pytest/test_number_less_than.out)


## PyTest compare strings
{id: pytest-compare-strings}

![](examples/pytest/test_string_equal.py)

```
$ pytest test_string_equal.py
```

![](examples/pytest/test_string_equal.out)


## PyTest compare long strings
{id: pytest-compare-long-strings}

![](examples/pytest/test_long_strings.py)

```
$ pytest test_long_strings.py
```

![](examples/pytest/test_long_strings.out)


## PyTest is one string in another strings
{id: pytest-in-strings}

Shows ~250 characters

![](examples/pytest/test_substring.py)
![](examples/pytest/test_substring.txt)


## PyTest test any expression
{id: pytest-any-expression}

![](examples/pytest/test_expression_equal.py)

```
$ pytest test_expression_equal.py

    def test_expression_equal():
        a = 3
>       assert a % 2 == 0
E       assert (3 % 2) == 0
```



## PyTest element in list
{id: pytest-element-in-list}

![](examples/pytest/test_in_list.py)

```
$ pytest test_in_list.py

    def test_in_list():
>       assert "dog" in get_list()
E       AssertionError: assert 'dog' in ['monkey', 'cat']
E        +  where ['monkey', 'cat'] = get_list()
```




## PyTest compare short lists
{id: pytest-compare-short-lists}
![](examples/pytest/test_short_lists.py)


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


## PyTest compare short lists - verbose output
{id: pytest-compare-short-lists-verbose-output}

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

## PyTest compare lists
{id: pytest-compare-lists}

![](examples/pytest/test_lists.py)

```
$ pytest test_lists.py

    def test_long_lists():
>       assert get_list('a') == get_list('b')
E       AssertionError: assert ['0', '1', '2...'4', '5', ...]
            == ['0', '1', '2'...'4', '5', ...]
E         At index 100 diff: 'a' != 'b'
E         Use -v to get the full diff
```


## PyTest compare dictionaries - different values
{id: pytest-compare-dictionaries}

![](examples/pytest/test_dictionaries.py)

![](examples/pytest/test_dictionaries.out)

## PyTest compare dictionaries  - missing-keys
{id: pytest-compare-dictionaries-missing-keys}

![](examples/pytest/test_dictionaries_missing_keys.py)
![](examples/pytest/test_dictionaries_missing_keys.out)


