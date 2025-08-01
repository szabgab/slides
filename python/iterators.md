# Iterators
{id: iterators}


## iterator - pairwise
{id: iterator-pairwise}

![](examples/iterators/pairwise_manual.py)


## iterator - grouped
{id: iterator-grouped}

![](examples/iterators/grouped_manual.py)
![](examples/iterators/grouped_manual.out)


## itertools - groupby
{id: itertools-groupby}

Group elements

![](examples/iterators/groupby.py)

## itertools - izip
{id: itertools-izip}
{i: izip}

Python 3 does not need this any more as the built-in zip is already an iterator.

Combine two unbounded lists

![](examples/iterators/izip.py)


## mixing iterators
{id: iterators-mixer}
{i: izip}

Combine three unbounded lists

![](examples/iterators/mixer.py)


## mixing iterators
{id: iterators-mixer-iterators}

![](examples/iterators/my_iterators.py)

## itertools - pairwise
{id: itertools-pairwise}
{i: iter}
{i: izip}

![](examples/iterators/pairwise.py)


Every 2 element from a list. We are using the exact same iterator object in both places of the izip() call,
so very time izip() wants to return a tuple, it will fetch two elements from the same iterator.

[Iterating over every two elements in a list](http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list)

## itertools - grouped
{id: itertools-grouped}

Every N element from a list

![](examples/iterators/grouped.py)


## alter iterator
{id: iterators-alter}

Is this interesting at all ?

![](examples/iterators/alter.py)

## Exercise: iterators - count
{id: exercise-reimplement-count}

* Reimplement the count functions of itertools using iterator class.

(We have this as one of the example)



