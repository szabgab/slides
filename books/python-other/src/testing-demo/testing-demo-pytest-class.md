# Testing demo: pytest using classes

* pytest
* assert


In our third example we are going to use the `pytest` module. The only drawback of the pytest module is that it does not
come with the installation of Python itself. It is not a huge issue though as you probably install hundreds of other
modules as well.

These days Pytest seems like the most popular testing library for Python.

We'll have several examples using Pytest.

In order to use it you'd create a file with a name that starts with `test_` prefix. We need to import the module we are testing
but we don't need to import pytest. Actually we don't even use pytest inside the code. (At least not in the simple use-cases.)
In the file you need to create a class starting with `Test`, but this class does not need to inherit from any special class.
In the class we can have one or more test-functions starting with the prefix `test_`.
In the function we call the function we are testing and we compare the results to the expected results.

We use the built-in `assert` function of Python to check if the results were true.

No need to learn various specialized assert-statements as we had in the `unittest` module.

We run the test using the `pytest` command.

We'll get some output. Here too the single dot after the name of the test file indicates that there was one successful test function.

The exit-code of this execution in 0 as was the case with unittest.


```
pip install pytest
```

{% embed include file="src/examples/testing-demo/test_with_pytest_class.py" %}

{% embed include file="src/examples/testing-demo/test_with_pytest_class.out)

```
$ pytest test_with_pytest_class.py
$ echo $?
0
```

```
> pytest test_with_pytest_class.py
> echo %ERRORLEVEL%
0
```


