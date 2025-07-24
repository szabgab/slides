# Declare your plan at execution time

* plan

```
use Test::More tests => 6;

or

use Test::More;
...
plan tests =>  6;
```



No need to tell your plan at load time;




Earlier when we were talking about Test::Simple we had a case when
the test data was placed in an array and the test script looped over
the array executing the function to be tested for each input.




Later we moved the data to an external file which made it even more
difficult to declare the plan so we used lengthy code in the BEGIN block
in order to have the expected number of tests before Test::Simple is loaded
into memory.




With Test::More we have a much better solution. We don't have to
declare the plan on the use Test::More line. We can do that later,
in the run time of the Perl script.


{% embed include file="src/examples/test-more/t/plan_tests.t" %}





