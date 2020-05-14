# Iterators - with and without Itertools
{id: iterators}

## Iterators Glossary
{id: iterators-glossary}

* [iterable](https://docs.python.org/glossary.html#term-iterable) (Can be iterated over using a `for` loop.)
* [iterator](https://docs.python.org/glossary.html#term-iterator)
* Every iterator is also iterable
* Iterators are not addressable like lists with the `thing[index]` construct.
* [Iterator Types](https://docs.python.org/library/stdtypes.html#typeiter)
* [The standard type hierarchy](https://docs.python.org/reference/datamodel.html#types)

## What are iterators and iterables?
{id: what-are-iterators-and-iterables}

* All of them are iterables
* Out of these, only the filehandle is an iterator
* (You should always `open` files using the `with` statement and not like this.)

![](examples/iterators/what_are_iterators.py)


## A file-handle is an iterator
{id: file-handle-as-iterator}
{i: collections}
{i: Iterator}
{i: Iterable}
{i: io}
{i: TextIOWrapper}
{i: issubclass}

![](examples/iterators/read_file.py)
![](examples/iterators/read_file.out)


## range is iterable but it is not an iterator
{id: range-is-an-iterator}

The `range` function in Python 3 is not a real "iterator" but it is an "iterable".
In many aspects it behaves as an iterator. Specifically it allows us to iterate over numbers.
[Range Is Not An Iterator](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/)

* [range](https://docs.python.org/library/functions.html#func-range)

![](examples/iterators/range.py)
![](examples/iterators/range.out)


## Iterator: a counter
{id: iterator-counter}
{i: StopIteration }
{i: next}
{i: __iter__}
{i: __next__}

{aside}
We can create a iterator using a class. We are required to implement the `__iter__` method that returns the iterator object
and the `__next__` method that returns the next element in our iteration. We can indicated that the iteration was exhaused
by raising a `StopIteration` exception.
{/aside}


* `__iter__`
* `__next__` (in Python 2 this used to ne `next`)
* `raise StopIteration`

![](examples/iterators/counter.py)

## Using iterator
{id: using-iterator}

![](examples/iterators/simple_iterator.py)
![](examples/iterators/simple_iterator.out)

## The type of the iterator
{id: type-of-iterator}

![](examples/iterators/simple_counter_type.py)
![](examples/iterators/simple_counter_type.out)

## Using iterator with next
{id: using-iterator-with-next}
{i: next}

![](examples/iterators/simple_iterator_next.py)
![](examples/iterators/simple_iterator_next.out)

## Iterator returning multiple values
{id: iterator-returning-multiple-values}

![](examples/iterators/iterator_with_multiple_values.py)
![](examples/iterators/iterator_with_multiple_values.out)

## Range-like iterator
{id: range-like-iterator}

![](examples/iterators/range/it.py)
![](examples/iterators/range/count.py)
![](examples/iterators/range/count.out)


## Unbound or infinite iterator
{id: unbound-iterator}

![](examples/iterators/iterator.py)


## Unbound iterator Fibonacci
{id: unbound-iterator-fibonacci}

![](examples/iterators/unbound/fibonacci.py)
![](examples/iterators/unbound/fib.py)
![](examples/iterators/unbound/fib.out)

## itertools
{id: itertools}
{i: itertools}
{i: yield}

* [itertools](http://docs.python.org/library/itertools.html)

## itertools - count
{id: itertools-count}
{i: count}

* Unbound counter: Count from N to infinity.

![](examples/iterators/count.py)

## itertools - cycle
{id: itertools-cycle}
{i: cycle}

![](examples/iterators/cycle.py)
![](examples/iterators/cycle.out)


## Exercise: iterators - reimplement the range function
{id: exercise-reimplement-the-range-function}

In one of the first slides of this chapter we saw a partial implementation of the `range` function.
Change that code to have a full implementation, that can accept 1, 2, or 3 parameters.

## Exercise: iterators - count
{id: exercise-reimplement-count}

* Reimplement the count functions of itertools using iterator class.

## Exercise: iterators - cycle
{id: exercise-reimplement-cycle}

* Reimplement the cycle functions of itertools using iterator class.

## Exercise: iterators - alter
{id: exercise-iterators-alter}

* Implement the alter functions as an iterator that will return

```
1
-2
3
-4
5
-6
...
```

* Optionally provide a start and end parameters
* start defaults to 1
* end defaults to unlimited

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

## Exercise: collect packets
{id: exercise-collect-packets}

* You get a series of packets (e.g. lines in a file)
* In each line you have several fields: id, seqid, maxseq, content
* id is a unique identifier of a series of packets (lines)
* seqid is the seuence id of a packet in a series. (an integer)
* maxseq is the length of the sequence.
* content is the actual content.

In each iteration return a message that is built up from all the packages in the given sequence.

![](examples/iterators/packets/packets.txt)
![](examples/iterators/packets/packets.out)

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

## Solution: collect packets
{id: solution-collect-packets}

The implementation

![](examples/iterators/packets/packets.py)

The use:

![](examples/iterators/packets/use_packetes.py)

The test to verify it

![](examples/iterators/packets/test_packets.py)

Test cases:

![](examples/iterators/packets/packets.json)
![](examples/iterators/packets/packets1.txt)
![](examples/iterators/packets/packets2.txt)
