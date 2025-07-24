# Multiple expected values revised

* any
* List::MoreUtils

We are going to use the "any" function of List::MoreUtils.

{% embed include file="src/examples/test-perl/t/dice_any.t" %}

Output:

{% embed include file="src/examples/test-perl/t/dice_any.out" %}


This shows that there is some problem but we still don't know what exactly is the problem.
Especially think if this is part of a larger test suit when one of the tests fail.
We would like to see the actual value and maybe even the expected values.



