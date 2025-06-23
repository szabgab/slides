# range with list

range
list
getsizeof

Using the **list** function we can tell the **range** object to generate the whole list immediately. Either using
the variable that holds the **range** object, or wrapping the **range()** call in a **list()** call.

You might recall at the beginning of the course we saw the **sys.getsizeof()** function that returns the size of a Python object
in the memory. If you don't recall, no problem, we'll see it used now. As you can see the size of the range object is only 48 bytes
while the size of the 3-element list is already 112 bytes. It seems the range object is better than even such a short lists.
On the next page we'll see a more detailed analyzis.

{% embed include file="src/examples/functional/range_list.py" %}



