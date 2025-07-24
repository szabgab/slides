# PyTest expected exceptions (other exception) output

```
    $ pytest test_exceptions_failing.py

    def test_zero_division():
        with pytest.raises(ValueError) as e:
>           divide(1, 0)

test_exceptions_failing.py:10:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

a = 1, b = 0

    def divide(a, b):
    #    if b == 0:
    #        raise ValueError('Cannot divide by Zero')
>       return a / b
E       ZeroDivisionError: division by zero
```


