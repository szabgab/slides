# Testing demo - AUT - Application Under Test

Given the following module with a single function, how can we use this function and how can
we test it?

{% embed include file="src/examples/testing-demo/mymath.py" %}


You probably noticed that our function was called `add` and so the expectation is that it will be able to add two numbers.
However the implementation has a bug. It actually multiplies the two numbers. I know it is a very obvious issue,
but it is great as it allows us to see the mechanics of testing without getting distracted by
a complex implementation and a complex problem.

Rest assured, the mechanism of the testing would be the same even if our function was calculating the moon-landing trajectory.



