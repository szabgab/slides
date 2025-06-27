# Solution: Calculations


* math
* pi
* **


In order to have the math operation work properly we had to put the addition in parentheses. Just as you would in math class.


{% embed include file="src/examples/basics/rectangle_solution.py" %}


In order to calculate the area and the circumference of a circle we need to have `PI` so we created a variable called
`pi` and put in 3.14 which is a very rough estimation. You might want to have a more exact value of PI.


{% embed include file="src/examples/basics/circle_solution.py" %}


Python has lots of modules (aka. libraries, aka. extensions), extra code that you can import and start using.
For example it has a module called `math` that provides all kinds of math-related functions and attributes.

A function does something, an attribute just hold some value. More about this later.

Specifically it has an attribute you can call `math.pi` with the value `3.141592653589793`. A much better proximation of PI.

In the following solution we used that.


* The documentation of the [math](https://docs.python.org/library/math.html) module.

{% embed include file="src/examples/basics/circle_math_solution.py" %}



The expression `r * r` might also bothered your eyes. Well don't worry in Python there is an operator to express exponential values
It is the double star: `**`. This is how we can use it to say r-square: `r ** 2`.


{% embed include file="src/examples/basics/circle_power_solution.py" %}



I don't have much to say about the calculator. I think it is quite straight forward.


{% embed include file="src/examples/basics/calc_solution.py" %}

