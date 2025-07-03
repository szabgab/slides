# Test::Simple - missing test


* count



So why are those numbers necessary?
Imagine you managed to write 200 unit tests. Someone
who does not know about the number runs the test suite and
sees "ok" printed 17 times. It looks like everything is ok. He won't notice
that instead of 200, only 17 tests ran before the test script excited.
Everything was OK up to that point,
but there is a serious problem somewhere. Either in the
application or in the test itself. This can be found only
if the test executer knows how many test have you planned,
and checks if the correct number of tests have been executed.



This is exactly what Test::Simple provides. In the following example
we deliberately commented out the last test that was failing.


{% embed include file="src/examples/test-simple/tests/t12.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t12.pl.out" %}

```
$ echo $?
255
```

```
> echo %ERRORLEVEL%
255
```


