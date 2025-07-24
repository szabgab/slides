# range

So what does **range** really return?

Instead of returning the list of numbers (as it used to do in Python 2), now it returns a **range object** that provides "the opportunity to go over
the specific series of numbers" without actually creating the **list** of numbers. Getting an object instead of the whole list has a number of advantages.
One is space in the memory. In a later example we'll see how much memory is needed for the object returned by the **range** function and
how much would it take to have the corresponding list of numbers in memory. For now let's see how we can use it. `range` can have 1, 2, or 3 parameters.

* `range(start, end, step)` - Go from `start` (included) to `end` (not included) every `step` value.
* `range(start, end)` - Where `step` defaults to 1.
* `range(end)` - Where `start` defaults to 0, `step` defaults to 1.

## range with 3 parameters

Go from `start` (included) to `end` (not included) every `step` value.

{% embed include file="src/examples/functional/range_3.py" %}

**Output:**

{% embed include file="src/examples/functional/range_3.out" %}

## range with 2 parameters

Go from `start` (included) to `end` (not included) every `step=1`.

{% embed include file="src/examples/functional/range_2.py" %}

**Output:**

{% embed include file="src/examples/functional/range_2.out" %}

## range with 1 parameter

Go from `start=0` (included) to `end` (not included) every `step=1`.

{% embed include file="src/examples/functional/range_1.py" %}

**Output:**

{% embed include file="src/examples/functional/range_1.out" %}


