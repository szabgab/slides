# Working on a list

In a slightly more interesting example we have a list of values.
We would like to divide a number by each one of the values.

As you can see one of the values is 0 which will generate and exception.

The loop will finish early.


{% embed include file="src/examples/exceptions/divide_by_zero_list.py" %}


We can't repair the case where the code tries to divide by 0, but it would be nice
if we could get the rest of the results as well.


