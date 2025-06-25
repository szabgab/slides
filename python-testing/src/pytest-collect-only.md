# Pytest dry-run - collect-only

* Find all the test files, test classes, test functions that will be executed.
* But don't run them...
* ...  but they are still loaded into memory so any code in the "body" of the files is executed.

```
pytest --collect-only
```


