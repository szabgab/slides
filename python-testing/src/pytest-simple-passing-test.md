# Pytest - simple passing test

We don't need much to test such code. Just the following things:

* Filename startes with `test_`
* A function that starts with `test_`
* Call the test function with some parameters and check if the results are as expected.

Specifically the `assert` function of Python expects to recived a True (or False) value.
If it is True the code keeps running as if nothing has happened.

If it is False and exception is raised.

{% embed include file="src/examples/pytest/math/test_mymath.py" %}

We can run the tests in two different ways. The regular would be to type in `pytest` and the name of the test file.
In some setups this might not work and then we can also run `python -m pytest` and the name of the test file.

```
pytest test_mymath.py
python -m pytest test_mymath.py
```

{% embed include file="src/examples/pytest/math/test_mymath.out" %}

The top of the output shows some information about the environment, (version numbers, plugins) then "collected" tells us how many test-cases were found by pytest.
Each test function is one test case.

Then we see the name of the test file and a single dot indicating that there was one test-case and it was successful.

After the test run we could also see the exit code of the program by typing in `echo $?` on Linux or Mac or `echo %ERRORLEVEL%` on Windows.

```
$ echo $?
0
```

```
> echo %ERRORLEVEL%
0
```


