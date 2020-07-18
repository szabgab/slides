# Sets
{id: python-sets}

## sets
{id: sets}
{i: set}


* Sets in Python are used when we are primarily interested in operations that we know from the [sets theory](https://en.wikipedia.org/wiki/Set_(mathematics)).
* See also the [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram).
* In day to day speach we often use the word "group" instead of "set" even though they are not the same.
* What are the common elements of two set (two groups).
* Is one group (set) the subset of the other?
* What are all the elements that exist in both groups (sets)?
* What are the elements that exist in exactly one of the groups (sets)?


## set operations
{id: set-operations}
{i: set}
{i: issubset}
{i: intersection}
{i: symmetric_difference}


* set
* issubset
* intersection
* symmetric difference
* union
* relative complement

* [stdtypes: set](http://docs.python.org/library/stdtypes.html#set)


## set intersection
{id: set-intersection}
{i: set}
{i: intersection}

![](examples/sets/intersection.py)

* `intersection` returns the elements that are in both sets.

![](examples/sets/intersection.out)

## set subset
{id: set-subset}
{i: set}
{i: issubset}

![](examples/sets/subset.py)

* `intersection` returns the elements that are in both sets.

![](examples/sets/subset.out)


## set symmetric difference
{id: set-symmetric-difference}
{i: set}
{i: symmetric_difference}

![](examples/sets/difference.py)

* Symmetric diffeerence is all the elements in either one of the sets, but not in both. "the ears of the elephant".

![](examples/sets/difference.out)


## set union
{id: set-union}
{i: set}
{i: union}

![](examples/sets/union.py)

![](examples/sets/union.out)

## set relative complement
{id: set-relative-complement}


![](examples/sets/relative_complement.py)
![](examples/sets/relative_complement.out)


## set examples
{id: set-examples}

![](examples/sets/try_set.py)
![](examples/sets/try_set.out)


## defining an empty set
{id: defining-an-empty-set}

![](examples/sets/empty.py)
![](examples/sets/empty.out)
![](examples/sets/empty2.out)


## Adding an element to a set (add)
{id: adding-an-element-to-a-set}

![](examples/sets/add_elements.py)
![](examples/sets/add_elements.out)

In Python 2:

![](examples/sets/add_elements2.out)


## Merging one set into another set (update)
{id: merging-one-set-into-another-set}

![](examples/sets/merge_sets.py)
![](examples/sets/merge_sets.out)




