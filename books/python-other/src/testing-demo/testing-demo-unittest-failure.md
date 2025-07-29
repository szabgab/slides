# Testing demo: Unittest failure


When we get the report on the incorrect results when adding 3 and 3, we can added another test-case.
We could have added another assertion to the `test_math` function or we could have created a separare
class with its own function, but in this case we opted creating a separate test-function.

We won't go into the pros and contras of each strategy now as we are only interested in the basic technique.

If we run the tests now the output will indicate that it ran 2 test-cases and one of them failed. It even shows
use some details about the expected value and the actual value that can be really useful understanding the
source of the problem.

Note there is also `.F` in the output. The dot indicates the test-function that passed, the F indicates
the test-function that failed.

The exit code is again different from 0.

BTW this exit-code is used by the various CI systems to understand the results of the tests.


{% embed include file="src/examples/testing-demo/test_with_unittest.py" %}

{% embed include file="src/examples/testing-demo/test_with_unittest.out)

```
$ python -m unittest test_with_unittest.py
$ echo $?
1
```

```
> python -m unittest test_with_unittest.py
> echo %ERRORLEVEL%
1
```


