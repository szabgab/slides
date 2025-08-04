# Test with failure

* testing
* test


The previous test was great, but soon people will report that the `add` function does not always work. In fact they will report it never works properly.
If you are lucky they will also supply you with a case for which it did not work properly so you can try to reproduce the problem. You do that by writing another
test case:


The code is still the same:

{% embed include file="src/examples/test-fail/comp2.go" %}

But now we have two separate test cases:

{% embed include file="src/examples/test-fail/comp2_test.go" %}

If we run the tests now:

```
go test
```

We get a failure report in which we can see the line number of the failure and the message. If we prepare our message well, then wen can immediately see the actual value and the expected value that might be able to help us locate the problem.

{% embed include file="src/examples/test-fail/test2.out" %}

If this is not enough we can ask for more verbose output:

```
go test -v
```

{% embed include file="src/examples/test-fail/test2_v.out" %}


