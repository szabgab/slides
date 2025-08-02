# itertools - pairwise

* iter
* izip

{% embed include file="src/examples/iterators/pairwise.py" %}


Every 2 element from a list. We are using the exact same iterator object in both places of the izip() call,
so very time izip() wants to return a tuple, it will fetch two elements from the same iterator.

[Iterating over every two elements in a list](http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list)



