# Test::FailWarnings

* Test::FailWarnings


Test::NoWarnings does not [play well](http://www.dagolden.com/index.php/1905/alternative-to-testnowarnings/)
with **done_testing**, but  [Test::FailWarnings](https://metacpan.org/pod/Test::FailWarnings) does.


{% embed include file="src/examples/test-warn/t/test_failwarnings.t" %}

```
prove -v t/test_failwarnings.t
```

{% embed include file="src/examples/test-warn/t/test_failwarnings.out" %}




