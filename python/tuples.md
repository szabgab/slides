# Tuples
{id: tuples}


## Create tuple
{id: tuple}
{i: tuple}
{i: ()}

Tuple

* A tuple is a fixed-length immutable list. It cannot change its size or content.
* Can be accessed by **index**, using the **slice** notation.
* A tuple is denoted with parentheses: (1,2,3)

![](examples/tuples/tuple.py)
![](examples/tuples/tuple.out)

List


* Elements of a list can be changed via their index or via the list slice notation.
* A list can grow and shrink using **append** and **pop** methods or using the **slice** notation.
* A list is denoted with square brackets:   [1, 2, 3]

![](examples/tuples/list.py)
![](examples/tuples/list.out)


{aside}
Tuples are rarely used. There are certain places where Python or some module require tuple (instead of list) or return a tuple (instead of a list)
and in each place it will be explained. Otherwise you don't need to use tuples.

e.g. keys of dictionaries can be tuple (but not lists).
{/aside}

## Convert list to tuple and tuple to list
{id: convert-list-to-tuple}

![](examples/tuples/totuple.py)
![](examples/tuples/totuple.out)

## Enumerate returns tuples
{id: enumerate-lists-tuples}
{i: enumerate}
{i: tuple}

![](examples/tuples/enumerate_tuple.py)
![](examples/tuples/enumerate_tuple.out)


## Change a tuple
{id: change-a-tuple}

![](examples/tuples/change_tuple.py)


## Sort tuples
{id: sort-tuples}

![](examples/tuples/sort_tuples.py)

## Sort tuples by specific elements
{id: sort-tuples-by-specific-element}

Sorting tuples or list, or other complex structures

![](examples/tuples/sort_tuples_by_specific_elements.py)

## Sort and secondary sort
{id: sort-and-secondary-sort}

{aside}
We have a list of words. It is easy to sort them by length, but what will be the order among the words
that have the same length?

A sort using a lambda-function that returns a tuple can provide the secondary sort order.
{/aside}

![](examples/tuples/sort_by_two_keys.py)



