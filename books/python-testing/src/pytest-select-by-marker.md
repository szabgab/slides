# PyTest select tests by marker

* --collect-only
* -m
* @pytest.mark


* Use the @pytest.mark.name decorator to tag the tests.

{% embed include file="src/examples/pytest/markers/test_by_marker.py" %}

```
pytest --collect-only -m security test_by_marker.py
    test_ui_forget
    test_database_write
    test_database_forget
```

```
pytest --collect-only -m smoke test_by_marker.py
    test_database_read
    test_ui_access
    test_database_write
```


