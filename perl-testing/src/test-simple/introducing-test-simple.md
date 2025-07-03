# Introducing Test::Simple


* Test::Simple



The Perl community has already created several implementations
of the above mentioned ok() function. We'll go with the one in the module called
Test::Simple. Not only will that print "ok" or "not ok" but it will also
include a counter.

In order to use it first we'll need to declare how many test units are we planning
to call, that is, how many times are we planning to call the ok() function.

In return we get extra features such as printing the line numbers of the ok() calls
that failed and getting a final report on the number of failed tests out of the
planned tests.

use Test::Simple, tell it your **plan**, that is the number
of times you are going to call **ok()** and use its built in ok()
function.


{% embed include file="src/examples/test-simple/tests/t10.pl" %}


Output:

{% embed include file="src/examples/test-simple/tests/t10.pl.out" %}


It is more verbose, it has a couple of additional useful pieces of information:
1..3   says how many tests we were planning,
then we get the tests numbered and we even get a small explanation when the test fails.


```
$ echo $?
1
```

```
> echo %ERRORLEVEL%
1
```


