# range

So what does **range** really return?

Instead of returning the list of numbers (as it used to do in Python 2), now it returns a **range object** that provides "the opportunity to go over
the specific series of numbers" without actually creating the **list** of numbers. Getting an object instead of the whole list has a number of advantages.
One is space. In the next example we'll see how much memory is needed for the object returned by the **range** function and
how much would it take to have the corresponding list of numbers in memory. For now let's see how can we use it:

* `range(start, end, step)`
* `range(start, end)` - step defaults to 1
* `range(end)` - start defaults to 0, step defaults to 1

{% embed include file="src/examples/functional/range.py" %}
{% embed include file="src/examples/functional/range.out" %}



