# Create tuple


* tuple
* ()

Tuple

* A tuple is a fixed-length immutable list. It cannot change its size or content.
* Can be accessed by **index**, using the **slice** notation.
* A tuple is denoted with parentheses: (1,2,3)

{% embed include file="src/examples/tuples/tuple.py" %}

**Output:**

{% embed include file="src/examples/tuples/tuple.out" %}

List


* Elements of a list can be changed via their index or via the list slice notation.
* A list can grow and shrink using **append** and **pop** methods or using the **slice** notation.
* A list is denoted with square brackets:   [1, 2, 3]

{% embed include file="src/examples/tuples/list.py" %}

**Output:**

{% embed include file="src/examples/tuples/list.out" %}



Tuples are rarely used. There are certain places where Python or some module require tuple (instead of list) or return a tuple (instead of a list)
and in each place it will be explained. Otherwise you don't need to use tuples.

e.g. keys of dictionaries can be tuple (but not lists).


