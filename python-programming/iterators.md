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
{i: __next__}

* __iter__
* next in Python 2
* __next__ in Python 3
* raise StopIteration

![](examples/classes/range/it.py)
![](examples/classes/range/count.py)
![](examples/classes/range/count.out)


## Unbound iterator
{id: unbound-iterator}

![](examples/classes/unbound/fibonacci.py)
![](examples/classes/unbound/fib.py)
![](examples/classes/unbound/fib.out)

## itertools or yield
{id: itertools}
{i: itertools}
{i: yield}

<a href="http://docs.python.org/3/library/itertools.html">itertools</a>

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


## alter iterator
{id: iterators-alter}
![](examples/iterators/alter.py)


## Exercise: iterators - limit Fibonacci
{id: exercise-iterators-limit}

Change the Iterator version of the Fibonacci series so optionally you will be able to provide
a parameter called "limit" to the constructor. If the limit is provided, the iterator should stop
when the value passes the limit.


## Exercise: iterators - Fibonacci less memory
{id: exercise-iterators-only}

Change the Iterator version of the Fibonacci series so it will NOT hold the previous values in memory.


## Exercise: read char
{id: exercise-iterators-read-char}


Create an iterator that given a filename will return an object that on every iteration will
return a single character. As an option let the user skip newlines, or maybe any pre-defined character.

## Exercise: read section
{id: exercise-read-section}

* Create an iterator that given the name of a file like the following, will return once section at a time.
* It will return a list one each iteration and each element of the list will be a line from the current section.
* Other ideas what should be returned on each iteration?

![](examples/iterators/sections/planets.txt)

## Exercise: compare files
{id: exercise-compare-files}

Compare two files line-by-line, and create a 3rd file listing the lines that are different.

![](examples/iterators/first.txt)
![](examples/iterators/second.txt)

Expected output:

![](examples/iterators/diff.txt)

## Solution: iterators - limit Fibonacci
{id: solution-iterators-limit}

![](examples/classes/limit/fibonacci.py)
![](examples/classes/limit/fib.py)


## Solution: iterators - Fibonacci less memory
{id: solution-iterators-only}

![](examples/classes/only/fibonacci.py)
![](examples/classes/only/fib.py)

## Solution: read section
{id: solution-read-section}

![](examples/iterators/sections/read_section.py)

## Solution: compare files
{id: solution-compare-files}

![](examples/iterators/diff.py)

```
python diff.py first.txt second.txt diff.txt
```

