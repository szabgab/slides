# Ruby variable interpolation

To further improve the situation we are going to use the interpolation capabilities of Ruby.
We can insert a hashmark (`#`) followed by a variable between a pair of curly braces in a string.
Ruby will replace that whole construct with the value of the variable.


{% embed include file="src/examples/intro/interpolate.rb" %}


Here however the behavior of double-quote and single-quote is different. The interpolation
only works in double-quoted strings. Single-quoted strings will just include the hash-mark,
the opening curly, the variable name and the closing curly.


{% embed include file="src/examples/intro/interpolate.out" %}


