# Testing for warnings

* Test::Warn
* warnings
* exception


Test code that should give a warning, and check if that is the correct warning.

So once we have tested our nicely behaving code we can also test our warnings and errors.
For this we are going to use several additional modules from CPAN. As they all use the
Test::Builder backend we can use them along with our standard Test::More setup.


{% embed include file="src/examples/test-warn/t/fibonacci_negative_tested.t" %}

```
prove -lv t/fibonacci_negative_tested.t
```

{% embed include file="src/examples/test-warn/t/fibonacci_negative_tested.out" %}


