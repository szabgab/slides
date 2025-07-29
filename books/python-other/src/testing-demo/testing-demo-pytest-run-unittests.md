# Testing demo: pytest run unittest

Pytest can also run the unit-test. You don't even need to tell it anything special.
It will introspect the test code and if it notices tests-classes that are based on unittest
it will execute them using the unittest module.


```
$ pytest test_one_with_unittest.py
$ pytest test_with_unittest.py
```



