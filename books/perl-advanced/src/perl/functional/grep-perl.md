# grep

* grep
* filter


The `grep` keyword in Perl is a generalization of the Unix/Linux grep tool. Given a condition and a list of values it will return a, usually shorter, list
of elements that will return true if used in the expression. In other language the similar tool is called `filter`.

In this example we have an array of numbers and an expression comparing `$_` which holds the current value as grep iterates over the elements of the array. If the current value
is greater or equal than 5 then it will be passed to the left hand side, if it is less than 5 then it will be filtered out.

Note, there is no comma after the curly braces.


```
ARRAY = grep BLOCK LIST
```
{% embed include file="src/examples/functional/grep_perl.pl" %}


