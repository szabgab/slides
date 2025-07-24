# FastAPI -  Test Hello World

* TestClient
* assert

Writing the web application is nice, but we better also write tests that verify the application works properly.
This will make it easier to verify that none of the changes we introduce later on will break parts that have been
working and tested already.

The key here is to have a file that starts with `test_` that has a function name that starts with `test_` that uses `assert` to check values.

{% embed include file="src/examples/fastapi/hello-world/test_main.py" %}

Just run `pytest` to execute the tests.

```
pytest
```


