# Fixture Autouse with yield

{% embed include file="src/examples/fixture_autouse_around/conftest.py" %}

{% embed include file="src/examples/fixture_autouse_around/test_app.py" %}

```
$ pytest -sq
Before
In test
.After

1 passed in 0.02 seconds
```


