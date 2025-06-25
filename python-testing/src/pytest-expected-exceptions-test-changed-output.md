# PyTest expected exceptions (text changed) output

```
$ pytest test_exceptions_text_changed.py


    def test_zero_division():
        with pytest.raises(ValueError) as e:
            divide(1, 0)
>       assert str(e.value) == 'Cannot divide by Zero'
E       AssertionError: assert 'Cannot divide by Null' == 'Cannot divide by Zero'
E         - Cannot divide by Null
E         ?                  ^^^^
E         + Cannot divide by Zero
E         ?                  ^^^^
```



