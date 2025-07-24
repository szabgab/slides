# PyTest Fixture setup and teardown output


```
test_fixture.py .F.
```

```
$ pytest -sq test_fixture.py

```


**Output:**

{% embed include file="src/examples/pytest/test_fixture.out" %}

Note, the teardown_function is executed even after failed tests.



