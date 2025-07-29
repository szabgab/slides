# Testing demo: pytest using classes - failure


Here too we can add additional test-functions to the same test-class.
Executing `pytest` will print `.F` indicating one passing test-function and one failing test function.
We'll get detailed explanation where the failure happened.

The exit-code will be different from 0 helping the CI systems and any other external system
to know that the tests have failed.


{% embed include file="src/examples/testing-demo/test_with_pytest_class_failure.py" %}

{% embed include file="src/examples/testing-demo/test_with_pytest_class_failure.out)

```
$ pytest test_with_pytest_class_failure.py
$ echo $?
1
```

```
> pytest test_with_pytest_class_failure.py
> echo %ERRORLEVEL%
1
```


