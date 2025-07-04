# Test for no warnings - the hard way

* warnings


If we can test our code for specific warnings we should also test
that in other places there are no warnings.


{% embed include file="src/examples/test-warn/t/fibonacci_test_warn.t" %}

```
prove -lv t/fibonacci_test_warn.t
```

{% embed include file="src/examples/test-warn/t/fibonacci_test_warn.out" %}



