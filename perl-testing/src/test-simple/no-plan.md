# Forget about your "plan", use "no_plan"


* plan
* no_plan

{% embed include file="src/examples/test-simple/tests/t22.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t22.pl.out" %}


The 1..6 is now at the end.





This is one of the solutions and in some cases it is hard to avoid it,
but it is not a really good solution. Those who advocate never to put
'no_plan' in your test say that checking if the exact number of unit
tests were executed is an additional control over our test suite.
Without a 'plan' you can never be sure if - after a successful execution -
the OKs you see were all the units there, or if the test script aborted
in the middle and you have not executed all of the units.

There are also people who say it is not that important to have a plan but
personally I am in the first camp. I think the plan is important.




There is 'done_testing' we'll cover later on.



