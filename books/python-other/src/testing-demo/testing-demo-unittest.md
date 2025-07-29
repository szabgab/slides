# Testing demo: Unittest success

* unittest
* TestCase
* assertEqual


Python comes with a built-in module for writing tests. Its name is `unittest` which might be a bit confusing
as this module can be used to any kind of more complex feature-tests and other modules can be also used to write
so called unit-tests.

Unlike the doctests that were part of the actual code, the unittest library calls for separate test files.
It is recommended that the names of files start with the `test_` prefix as that will make it easy for the various testing
tools to locate them.

Inside the file you'd need to import both the `unittest` module and the module that we are testing. `mystest` in this case.

We need a class with a name that starts with `Test` and inherits from `unittest.TestCase`. In the class we can have one or more
testing functions. Each one starts with a `test_` prefix.
Inside the function we can call the function that we are testing and we can compare the result returned by it to some expected value.
We can compare them in various ways using the various assert-methods of the unittest.TestCase. In this example we used the `assertEqual`
method as we wanted to make sure the actual return value equals the expected value.

We can run the tests using `python -m unittest test_one_with_unittest.py`. It will have some output on the screen indicating all the tests
passed. The exit-code will be 0 as expected.


* [unittest](https://docs.python.org/library/unittest.html)

{% embed include file="src/examples/testing-demo/test_one_with_unittest.py" %}


{% embed include file="src/examples/testing-demo/test_one_with_unittest.out)

```
$ python -m unittest test_one_with_unittest.py
$ echo $?
0
```

```
> python -m unittest test_one_with_unittest.py
> echo %ERRORLEVEL%
0
```


