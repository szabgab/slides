# Testing demo: pytest without classes


In the previous example we used a test-class to write our tests, but in reality in many cases
we don't need the classes. We could just as well write plain test-functions as in this example.

Test-functions without a class around them are easier to write and understand and they are a lot
simplert to graps. So unless you really need the features a class can provide I'd recommend you use
functions only. After all our test code should be a lot more simple than our application code.


```
pip install pytest
```

{% embed include file="src/examples/testing-demo/test_with_pytest.py" %}

{% embed include file="src/examples/testing-demo/test_with_pytest.out)

```
$ pytest test_with_pytest.py
$ echo $?
0
```

```
> pytest test_with_pytest.py
> echo %ERRORLEVEL%
0
```


