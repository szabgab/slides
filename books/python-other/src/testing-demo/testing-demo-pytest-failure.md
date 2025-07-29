# Testing demo: pytest without classes failure

{% embed include file="src/examples/testing-demo/test_with_pytest_failure.py" %}

{% embed include file="src/examples/testing-demo/test_with_pytest_failure.out)

```
$ pytest test_with_pytest.py
$ echo $?
1
```

```
> pytest test_with_pytest.py
> echo %ERRORLEVEL%
1
```



