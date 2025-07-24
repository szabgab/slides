# PyTest select tests by name

* --collect-only
* -k

* --collect-only - only list the tests, don't run them yet.
* -k select by name

{% embed include file="src/examples/pytest/test_by_name.py" %}


```
pytest --collect-only test_by_name.py
    test_database_read
    test_database_write
    test_database_forget
    test_ui_access
    test_ui_forget
```


```
pytest --collect-only -k database test_by_name.py
    test_database_forget
    test_database_read
    test_database_write
```


```
pytest --collect-only -k ui test_by_name.py
    test_ui_access
    test_ui_forget
```


```
pytest --collect-only -k forget test_by_name.py
    test_database_forget
    test_ui_forget
```


```
pytest --collect-only -k "forget or read" test_by_name.py
    test_database_read
    test_database_forget
    test_ui_forget
```


