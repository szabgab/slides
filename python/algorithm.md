# Algorithm
{id: algorithm}

## Exercise: Find the odd value
{id: exercise-find-the-odd-value}

* Given a list of values, we know that every value comes in pairs except one. Find where it is:

* f(["a", "a", "b", "b", "c", "d", "d"])  would return 4

## Solution: Find the odd value
{id: solution-find-the-odd-value}

![](examples/algorithms/find_the_odd_value.py)

## Exercise: Generalized find the odd value
{id: exercise-generalized-find-the-odd-value}

* Given a list of values, we know that every value comes in groups of N except one group that has less than N element. Given the list and the number N find where it starts:

* f(["a", "a", "a", "b", "b", "b", "x", "d", "d", "d"], 3)  would return 6
* f(["a", "a", "a", "b", "b", "b", "x", "y", "d", "d", "d"], 3)  would return 6

#
## Solution: Generlized Find the odd value
{id: solution-generalized-find-the-odd-value}

![](examples/algorithms/generalized_find_the_odd_value.py)


## Exercise: Shortest sublist with sum over limit
{id: exercise-shortest-sublist}

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


## Solution: Shortest sublist with sum over limit
{id: solution-shortest-sublist}

![](examples/algorithms/shortest_sublist.py)
