# unexpected warnings Test::NoWarnings, Test::FailWarnings


* Edit the lib/MyTools.pm enable the row with "Some other warning"

```
prove -lv t/fibonacci_no_warnings.t
```


It shows that there were warnings generated during the tests. It even tells us at which test.
The biggest problem with this module is that it does not work together with done_testing() and so it requires that you know how many test you are going to run.



