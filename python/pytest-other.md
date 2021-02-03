# Pytest - other
{id: pytest-other}

## Testing with Pytest
{id: pytested-module}

A module called `mymath` with two functions: `add` and `div`.

![](examples/pytest/mymath.py)


## Testing functions
{id: pytest-module}

![](examples/pytest/test_mymath.py)


## Testing class and methods
{id: pytest-module-class}
![](examples/pytest/test_mymath_class.py)


## Pytest - execute
{id: pytest-run-tests}

```
pytest test_mymath.py
```

![](examples/pytest/test_mymath.out)


## Pytest - execute
{id: pytest-execute}

```
pytest
python -m pytest
```


## Pytest simple module to be tested
{id: pytest-simple-module-to-be-tested}


An anagram is a pair of words containing the exact same letters in different order. For example:



* listen silent
* elvis lives


![](examples/pytest/mymod_1.py)


## Pytest simple tests - success
{id: pytest-simple-success}
{i: assert}
{i: pytest}
![](examples/pytest/test_mymod_1.py)


## Pytest simple tests - success output
{id: pytest-simple-success-output}

```
$ pytest test_mymod_1.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 1 items

test_mymod_1.py .

=================== 1 passed in 0.03 seconds ===================
```


## Pytest simple tests - failure
{id: pytest-simple-failure}

* Failure reported by user: **is_anagram("anagram", "nag a ram")** is expected to return true.
* We write a test case to reproduce the problem. It should fail now.

![](examples/pytest/test_mymod_2.py)


## Pytest simple tests - failure output
{id: pytest-simple-failure-output}

```
$ pytest test_mymod_2.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 2 items

test_mymod_2.py .F

=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
============== 1 failed, 1 passed in 0.09 seconds ==============
```

## PyTest bank deposit
{id: pytest-bank-deposit}
![](examples/pytest/b1/banks.py)


## PyTest expected exceptions (bank deposit)
{id: pytest-expected-exceptions-bank-deposit}
![](examples/pytest/b1/test_bank.py)

```
pytest test_bank.py

test_bank.py .
```


## PyTest expected exceptions (bank deposit) - no exception happens
{id: pytest-expected-exceptions-bank-deposit-no-exception}

Pytest properly reports that there was no exception where an exception was expected.


![](examples/pytest/b2/banks.py)
![](examples/pytest/b2/error.txt)


## PyTest expected exceptions (bank deposit) - different exception is raised
{id: pytest-expected-exceptions-bank-deposit-different-exception}
![](examples/pytest/b3/banks.py)
![](examples/pytest/b3/error.txt)


## PyTest expected exceptions - divide
{id: pytest-expected-exceptions}

* Some older slides I kept them around

![](examples/pytest/test_exceptions.py)


## PyTest expected exceptions output
{id: pytest-expected-exceptions-output}

```
$ pytest test_exceptions.py

test_exceptions.py .
```


## PyTest expected exceptions (text changed)
{id: pytest-expected-exceptions-test-changed}
![](examples/pytest/test_exceptions_text_changed.py)


## PyTest expected exceptions (text changed) output
{id: pytest-expected-exceptions-test-changed-output}

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


## PyTest expected exceptions (other exception)
{id: pytest-expected-exceptions-failure}
![](examples/pytest/test_exceptions_failing.py)


## PyTest expected exceptions (other exception) output
{id: pytest-expected-exceptions-failure-output}

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


## PyTest expected exceptions (no exception)
{id: pytest-expected-exceptions-no-exception}

![](examples/pytest/test_exceptions_missing.py)


## PyTest expected exceptions (no exception) output
{id: pytest-expected-exceptions-no-exception-output}

![](examples/pytest/expected_exception_no_exception.out)


## PyTest compare short lists - output
{id: pytest-compare-short-lists-output}

![](examples/pytest/test_read_ini.py)


