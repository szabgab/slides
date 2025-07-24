# map delaying function call

Not only the size that we already saw with the **range** case, but also the processing time saved by
not calculating the results till you actually need it.

Let's see how it works, before getting in more explanation.

{% embed include file="src/examples/functional/map_with_print.py" %}

**Output:**

{% embed include file="src/examples/functional/map_with_print.out" %}

Imagine a case where you apply several expensive (time consuming) transformations to some original list and then you iterate over the end-results
looking for the first value that matches some condition. What if you find the value you were looking for after only a few iteration. Then
making all that expensive calculations to the whole list was a waste of time.

This lazy evaluation can help you save both memory and time and you always have the option to force the immediate calculation by calling the **list**
function.



In this example we have added a call to `print` in the double function in order to see when is it really executed. You can see that the first output
comes from the `print` statement that was **after** the `map` call. Then on each iteration we see the output from inside the "double" function and then the
result from the loop. In a nutshell Python does not execute the "double" function at the point where we called `map`. It only executes it when we iterate over
the resulting object.


