# Stop running current test script



When running a test script sometimes we reach a
failure that is so problematic you cannot go on testing.
This can be in the scope of a single test script in which case
you would call exit() to abort the current test script or it can
be so bad that all the testing should stop. In that case you should call
BAIL_OUT(). That will indicate the harness that it should not call
any other test script.


{% embed include file="src/examples/test-more/t/exit.t" %}

```
prove t/exit.t t/other.t
```

{% embed include file="src/examples/test-more/t/exit.out" %}



