# Iterators - with and without Itertools
{id: iterators-in-python}

## Iterators vs Generators
{id: iterators-vs-generators}

* a generator is an iterator
* an iterator is an iterable

![](examples/advanced/iterable.py)

* Genarators are a simpler way to create an iterable object that iterators, but iterators allow for more complex iterables.
* To create a generator we only need a single function with **yield**.
* To create an iterator we need a class with two methods: **__iter__** and **__next__**

![](examples/advanced/list_vs_generator.py)
![](examples/advanced/list_vs_generator.out)


## Iterators
{id: iterators}
{i: StopIteration }
{i: next}
{i: __iter__}

* __iter__
* next in Python 2
* __next__ in Python 3
* raise StopIteration

![](examples/classes/range/it.py)
![](examples/classes/range/count.py)



## Unbound iterator
{id: unbound-iterator}
![](examples/classes/fibonacci.py)
![](examples/classes/fib.py)


## Exercise: iterators
{id: exercise-iterators-limit}


Change the Iterator version of the Fibonacci series so optionally you will be able to provide
a parameter called "limit" to the constructor. If the limit is provided, the iterator should stop
when the value passes the limit.




## Exercise: iterators (2)
{id: exercise-iterators-only}


Change the Iterator version of the Fibonacci series so it will NOT hold old the previous values
in memory.




## Exercise: read char
{id: exercise-iterators-read-char}


Create an iterator that given a filename will return an object that on every iteration will
return a single character. As an option let the user skip newlines, or maybe any pre-defined character.




## Solution: iterators
{id: solution-iterators-limit}
![](examples/classes/limit/fibonacci.py)
![](examples/classes/limit/fib.py)


## Solution: iterators (2)
{id: solution-iterators-only}
![](examples/classes/only/fibonacci.py)
![](examples/classes/only/fib.py)



## itertools or yield
{id: itertools}
{i: itertools}
{i: yield}


<a href="http://docs.python.org/2/library/itertools.html">itertools</a>




## itertools - count
{id: itertools-count}
{i: count}
![](examples/iterators/count.py)


## iterator (generator) - count (with yield)
{id: iterator-count}
![](examples/iterators/count_manual.py)


## itertools - cycle
{id: itertools-cycle}
{i: cycle}
![](examples/iterators/cycle.py)


## iterator - cycle
{id: iterator-cycle}
![](examples/iterators/cycle_manual.py)


## itertools - izip
{id: itertools-izip}
{i: izip}

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


## alter iterator
{id: iterators-alter}
![](examples/iterators/alter.py)


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


## Exercise: compare files
{id: exercise-compare-files}

Compare two files line-by-line, and create a 3rd file listing the lines that are different




