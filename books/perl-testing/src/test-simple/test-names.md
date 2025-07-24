# Add names to the tests


* names

```
More advantages of Test::Simple - names of the tests.
```


So Test::Simple module makes our life a bit more simple in that we don't have to write
our testing expression. In addition this new "ok" function can actually do some more.
It can get two arguments. The first one indicates success or failure of the test
as explained earlier. The second one is a string which is the name of the test.
When running a test these additional names get printed on the same
line where the counter and the "ok" or "not ok" is printed.
If the names were written carefully, then they can provide an immediate hint on what went wrong.
Sometimes you won't even need to look at the test script itself, right from this comment
you'll know where to look for the bug.


{% embed include file="src/examples/test-simple/tests/t14.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t14.pl.out" %}



