# Test with warnings



First we'll check if the fibonacci function works correctly even when called with
negative numbers.


{% embed include file="src/examples/test-warn/t/fibonacci_negative.t" %}

```
prove -lv t/fibonacci_negative.t
```

{% embed include file="src/examples/test-warn/t/fibonacci_negative.out" %}


In the above code the tests are passing but there is a warning as well.
This is an expected warning so we don't need to worry about it. But then again people
or code using our module might start to rely on this warning. We would like to make sure
it won't disappear or change by mistake.





