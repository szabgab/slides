# TODO Verbose output


* TODO

```
$ prove -lv t/34.t
```

{% embed include file="src/examples/test-more/t/34.t.prove-v.out" %}


In the eXtreme Programming paradigm the following two key aspects are somewhat
in contradiction:
1) Write your test before you write your code.
2) Make sure your test suit always passes at 100%.

Of course after you already wrote your tests for a new feature but before you
can write the actual code there is a short time period when your test suit will
not pass 100%.

Worse than that, it is also recommended that immediately when you get a bug report
from somewhere you should write a test case that reproduces this bug. Obviously
this test will fail before you fix the bug and will hopefully pass once you fixed it.

In order to make the test suit happy there is a way to tell the harness tool that a test
is *supposed to fail*. That is, we know it will fail. What we can do to achieve this is
to set one or more tests to be in a TODO block.



