# Generators and Generator Expressions
{id: generator-experssions}

## Generators Glossary
{id: generators-glossary}

* [generator](https://docs.python.org/glossary.html#term-generator) (a function that returns a "generator iterator")
* [generator-iterator](https://docs.python.org/glossary.html#term-generator-iterator) (an object created by a generator)
* [Generator types](https://docs.python.org/library/stdtypes.html#generator-types)
* [generator-expression](https://docs.python.org/glossary.html#term-generator-expression)

* Generators are basically a way to create iterators without a class.

## Iterators vs Generators
{id: iterators-vs-generators}

* a generator is an iterator
* an iterator is an iterable

![](examples/generators/iterable.py)

* Genarators are a simpler way to create an iterable object than iterators, but iterators allow for more complex iterables.
* To create an iterator we need a class with two methods:  `__iter__` and `__next__`, and a `raise StopIteration`.
* To create a generator we only need a single function with `yield  .

## List comprehension and Generator Expression
{id: list-comprehension-and-generator-expression}

{aside}
However, before learning about `yield` let's see an even simpler way to create a generator. What we call a generator expression.

You are probably already familiar with list comprehensions where you have a an `for` expression inside square brackets. That returns a `list` of values.

If you replace the square brackets with parentheses then you get a **generator expression**.

You can iterate over either of those. So what's the difference?
{/aside}

![](examples/generators/list_vs_generator.py)
![](examples/generators/list_vs_generator.out)


## List comprehension vs Generator Expression - less memory
{id: list-comprehension-vs-generator-expression}
{i: getsizeof}

{aside}
Let's use a bigger range of numbers and create the corresponding list and generator. Then check the size of both of them.
You can see the list is much bigger. That's becuse the list already contains all the elements, while the generator contains
only the promise to give you all the elements.

As we could see in the previous example, this is not an empty promise, you can indeed iterate over the elements of a generator
just as you can iterate over the elements of a list.

However, you cannot access an arbitrary element of a generator because the generator is not **subscriptable**.
{/aside}


![](examples/generators/generator_expression.py)
![](examples/generators/generator_expression.out)

[List Comprehension vs Generator Expressions](https://code-maven.com/list-comprehension-vs-generator-expression)


## List comprehension vs Generator Expression - lazy evaluation
{id: list-comprehension-generator}

{aside}
The second big difference between list comprehension and generator expressions is that the latter has lazy evaluation.
In this example you can see that once we assign to list comprehension to a variable the `sqr` function is called on each element.

In the case of the generator expression, only when we iterate over the elements will Python call the `sqr` function.
If we exit from the loop before we go over all the values than we saved time by not executing the expression on every
element up-front. If the computation is complex and if our list is long, this can have a substantial impact.
{/aside}

![](examples/generators/list_comprehension_generator.py)
![](examples/generators/list_comprehension_generator.out)


## Generator: function with yield - call next
{id: generators-simple-generators-next}
{i: next}
{i: yield}
{i: StopIteration}

{aside}
We can create a function that has multiple `yield` expressions inside.
We call the function and what we get back is a `generator`.
A `generator` is also an `iterator` so we can call the `next` function on it and it will give us the next `yield` value.

If we call it one too many times we get a `StopIteration` exception.
{/aside}

![](examples/generators/simple_generator_next.py)
![](examples/generators/simple_generator_next.out)

## Generators - call next
{id: generators-next}

{aside}
We can also use a `for` loop on the `generator` and then we don't need to worry about the exception.
{/aside}

![](examples/generators/simple_generator_next_other.py)
![](examples/generators/simple_generator_next_other.out)


## Generator with yield
{id: generators-simple-generators}
{i: yield}

{aside}
We don't even need to use a temporary variable for it.
{/aside}

![](examples/generators/simple_generator.py)
![](examples/generators/simple_generator.out)



## Generators - fixed counter
{id: generators-fixed-counter}

![](examples/generators/generator_counter_3.py)
![](examples/generators/generator_counter_3.out)


## Generators - counter
{id: generators-counter}

![](examples/generators/generator_counter.py)
![](examples/generators/generator_counter.out)


## Generators - counter with parameter
{id: generators-counter-parameter}

![](examples/generators/generator_counter_param.py)
![](examples/generators/generator_counter_param.out)


## Generators - my_range
{id: generators-increment}

![](examples/generators/gen.py)
![](examples/generators/gen.out)


## Fibonacci - generator
{id: generators-fibonacci}

![](examples/generators/fibonacci_generator.py)

{aside}

The fibonacci() function is called 5 times. When it reached the 'yield' command it returns the value
as if it was a normal return call, but when the function is called again, it will be executed starting
from the next statement. Hence the word 'after' will be printed after each call.
{/aside}

## Infinite series
{id: infinite-series}

* The Fibonacci was already infinite, let's see a few more.

## Integers
{id: integers}

![](examples/generators/integers.py)
![](examples/generators/integers.out)


## Integers + 3
{id: integers-plus-3}

![](examples/generators/integers_add_3.py)
![](examples/generators/integers_add_3.out)


## Integers + Integers
{id: add-integers}
{i: itertools}
{i: zip}

![](examples/generators/add_integers.py)
![](examples/generators/add_integers.out)


## Filtered Fibonacci
{id: filtered-fibonacci}

![](examples/generators/filtered_fibonacci.py)
![](examples/generators/filtered_fibonacci.out)


## The series.py
{id: series}

This is the module behind the previous examples.

![](examples/generators/series.py)

## generator - unbound count (with yield)
{id: iterator-count}

![](examples/generators/count_manual.py)
![](examples/generators/count_manual.out)

## iterator - cycle
{id: iterator-cycle}

![](examples/generators/cycle_manual.py)
![](examples/generators/cycle_manual.out)


## Exercise: Alternator
{id: exercise-alternator}

Create a generator for the following number series: 1, -2, 3, -4, 5, -6, ...


## Exercise: Prime number generator
{id: exercise-prime-number-generator}

Create a generator that will return the prime numbers:
2, 3, 5, 7, 11, 13, 17, ...


## Exercise: generator
{id: exercise-generator}

Take the two generator examples (increment number and Fibonacci) and change them to provide infinite iterations.
Then try to run them in a for loop. Just make sure you have some other condition to leave the for-loop.


## Exercise: Tower of Hanoi
{id: exercise-tower-of-hanoi}

There are 3 sticks. On the first stick there are n rings of different sizes. The smaller the ring the higher it is on the stick.
Move over all the rings to the 3rd stick by always moving only one ring and making sure that never will there be a large ring on top
of a smaller ring.

* [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)


## Exercise: Binary file reader
{id: exercise-binary-file-reader}

Create a generator that given a filename and a number n will return
the content of the file in chunks of n characters.

## Exercise: File reader with records
{id: exercise-file-reader-with-records}

In a file we have "records" of data. Each record starts with three bytes in which we have the length of the record.
Then the content.

```
8 ABCDEFGH 5 XYZQR
```

Given this source file

![](examples/advanced/rows.txt)

using this code

![](examples/advanced/rows_to_records.py)

we can create this file:

![](examples/advanced/records.txt)

The exercise is to create an iterator/generator that can read such a file record-by-record.

