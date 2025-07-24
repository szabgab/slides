# Double numbers

We have a string that has some numbers in it. We would like to double the numbers.

In the first example we can see a relatively simple way of doubling the numbers. We captuter a number using the `(\d+)` expression
that will save the current number in `\1` and then we include it twice: `\1\1`. This will convert a number like 1 to 11.
This is nice, but probably not what we wanted. We wanted to convert 1 to 2 and 34 to 68.

We can't do that with plain regular expressions and substitutions as that is all string-based. The plain substitution can only move around characters,
but it cannot do any complex operations on the and thus cannot compute anything.

However, if the substitution part is a function then Python will call that function passing in the match object and whatever the function returns will
be the replacement string. This function can be a regular function defined with `def` or a `lambda` expression.

In the second example we see the solution with `lambda`-expression.

The 3rd examples is the same solution but in a very step-by-step way with lots of temporary variables. This will hopefully help understand the
`lambda`-expression in the 2nd example.


{% embed include file="src/examples/regex/duplicate_numbers.py" %}



