# Solution: Print all the locations in a string



When you start thinking about this exercise, you probably call `loc = text.find("c")` and then you wonder how could you find the next element.
After a while it might occur to you that the `find` method can get a second parameter to set the location where we start the search.

Basically you need to call `loc = text.find("c", loc + 1)` but that looks strange. How can you use `loc` (as a parameter of the function) and also
assign to it. However programming languages don't have a problem with this as the assignment happens after the right-hand-side was fully executed.

The problem that now you have two different calls to `find`. The first one and all the subsequent calls.

How could we merge the two calls?

The trick is that you need to have an initial value for the `loc` variable and it has to be -1, so when we call `find` for the first time,
it will start from the first character (index 0).


{% embed include file="src/examples/loops/find_loop_one.py" %}


Using an additional variable might make the code easier to read:


{% embed include file="src/examples/loops/find_loop.py" %}



