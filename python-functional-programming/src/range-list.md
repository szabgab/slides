# range with list

Using the **list** function we can tell the **range** object to generate the whole list immediately. Either using
the variable that holds the **range** object, or wrapping the **range()** call in a **list()** call.

The `sys` module provides function called **sys.getsizeof()** that returns the size of a Python object in the memory. As you can see the size of the range object is 48 bytes
while the size of the 3-element list is 112 bytes. It seems the range object uses less memory than even such a short lists.
On the next page we'll see a more detailed analyzis.

{% embed include file="src/examples/functional/range_list.py" %}


* range
* list
* getsizeof


