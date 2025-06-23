# map delaying function call

In this example we have added a call to `print` in the double function in order to see when is it really executed. You can see that the first output
comes from the `print` statement that was **after** the `map` call. Then on each iteration we see the output from inside the "double" function and then the
result from the loop. In a nutshell Python does not execute the "double" function at the point where we called `map`. It only executes it when we iterate over
the resulting object.

{% embed include file="src/examples/functional/map_with_print.py" %}
{% embed include file="src/examples/functional/map_with_print.out" %}


