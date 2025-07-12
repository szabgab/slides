# Home-made fixture with yield


{% embed include file="src/examples/fixture_inject_around/conftest.py" %}

{% embed include file="src/examples/fixture_inject_around/test_app.py" %}

```
$ pytest -sq
Before
In test
{'name': 'Foo Bar'}
.After

1 passed in 0.02 seconds
```


