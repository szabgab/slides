# Traditional xUnit fixtures


{% embed include file="src/examples/traditional/test_fixture.py" %}

```
$ pytest test_fixture.py -s

setup_module

  setup_function
    test_one
    test_one after
  teardown_function

  setup_function
    test_two
  teardown_function

  setup_function
    test_three
    test_three after
  teardown_function

teardown_module
```


