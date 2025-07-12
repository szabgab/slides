# Home-made fixture with tempdir

{% embed include file="src/examples/fixture_inject_tmpdir/test_app.py" %}

{% embed include file="src/examples/fixture_inject_tmpdir/conftest.py" %}

```
$ pytest -qs
{'name': 'Foo Bar', 'email': 'foo@bar.com'}
```


