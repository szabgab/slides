# Almost manually testing add()

In the first examples we recreate a path similar to what we
took in the Perl introduction so you might skip it or just
flip through the pages.

Let's assume we have a simple PHP library with a bunch of
functions. It is located in our includes directory in the
mylib.php file. It is used by a "web application" called
basic_calc.php that provides a - surprise - calculator
for the web visitor.

In order to test this we create a separate PHP script that
will require the relevant library and call the add()
function supplying various arguments and displaying the results.

Then we eyeball those results to see if they are what they should be.

{% embed include file="src/examples/php/intro/t01.php" %}

Result:

```
2
4
2
```


Not much of an output but if we are careful we'll see that
the third line is incorrect. The problem is that it is a lot
of effort to check if the results are correct.

dirname(__FILE__) just gives the path to the directory of currently executing file
and we know the library we are testing is relative to it.


