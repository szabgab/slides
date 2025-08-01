# Exercise: Shortest sublist with sum over limit

*  Given a list of integers [10, 12, 35, 7] and a number e.g. 25 return the length of the shortests sublist where the sum of the numbers is greater than or equal to the given number. If no such sublist can be found return -1.

* A few examples:

```
    >>> shortest([], 7)
    -1
    >>> shortest([2, 3], 7)
    -1
    >>> shortest([2, 3], 0)
    0
    >>> shortest([], 0)
    0
    >>> shortest([7, 3], 7)
    1
    >>> shortest([4, 7, 3], 7)
    1
    >>> shortest([1, 23, 1, 1, 10, 11, 12], 30)
    3
    >>> shortest([1, 23, 1, 1, 10, 11, 12], 24)
    2
    >>> shortest([1, 10, 11, 40], 30)
    1
```


