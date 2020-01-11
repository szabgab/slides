# Functional programming
{id: functional}

## Iterators (Iterables)
{id: iterables}
{i: iterables}

{aside}

You already know that there are all kinds of objects in Python that you can iterate over using the **for in** construct.
For example you can iterate over the characters of a string, or the elements of a list, or whatever **range()** returns.
You can also iterate over the lines of a file
and you have probably seen the construct in other cases as well. The objects that can be iterated over are collectively called
[iterables](https://docs.python.org/3/glossary.html#term-iterable).
You can do all kind of interesting things on such **iterables**. We'll see a few now.
{/aside}

{aside}

Any data type we can iterate over using the for ... in ... construct. (strings, files, tuples, lists, list comprehension)
{/aside}
![](examples/advanced/iterables.py)
![](examples/advanced/iterables.out)


## range
{id: range-iterator}
{i: range}

{aside}

So what does **range** really return?
{/aside}

{aside}

Instead of returning the list of numbers it returns a **range** object that only provides the opportunity to go over
the specific list of numbers without actually creating the list of numbers. It has a number of advantages.
One is space. In the next slide we'll see how much memory is needed for the object returned by the **range** function,
how much would it take to have the corresponding list of numbers in memory.
{/aside}
![](examples/advanced/range.py)
![](examples/advanced/range.out)


## range with list
{id: range-list}
{i: range}
{i: list}
{i: getsizeof}

{aside}

Using the **list** function we can tell the **range** object to generate the whole list immediately. Either using
the variable that already holds the **range** object, or wrapping the range() call in a list() call.
{/aside}

{aside}

You might recall at the beginning of the course we saw the **sys.getsizeof()** function that returns the size of a Python object
in the memory. If you don't recall, no problem, we'll see it used now. As you can see the size of the range object is only 48 bytes
while the size of the 3-element list is already 112 bytes. So it seems the range object is better than even such short lists.
On the next page we'll see a more detailed analyzis.
{/aside}
![](examples/advanced/range_list.py)


## range vs. list size
{id: range-size}
{i: getsizeof}
![](examples/advanced/range_size.py)
![](examples/advanced/range_size.out)



## for loop with transformation
{id: for-loop-transformation}
{i: append}

{aside}
There are many cases when we have a list of some values and we need to apply some transformation to each value and we would
like to get back the list of the resulting values.

A very simple such transformation would be to double each value. Other, more interesting examples might be reversing each string,
computing some more complex function on each number, etc.)

In this example we just double the values and use **append** to add each value the list containing the results.
{/aside}

![](examples/advanced/double.py)
![](examples/advanced/double.out)

{aside}
There are better ways to do this.
{/aside}


## map
{id: map}
{i: map}


map(function, iterable, ...)



{aside}

The [map](https://docs.python.org/3/library/functions.html#map) function of python, applies a function to every item in an iterable.
and returns an iterator.
{/aside}
![](examples/advanced/map.py)
![](examples/advanced/map.out)


## map with list
{id: map-with-list}
{i: map}
{i: list}

{aside}

Here too you can use the **list** function to convert all the values at once, but there is an advantage of keeping it as
a **map object**. Not only the size that we already saw with the **range** case, but also the processing time saved by
not calculating the results till you actually need it.
{/aside}

{aside}

Imagine a case where you apply several expensive (time consuming) transformations to some original list and then you iterate over the end-results
looking for the first value that matches some condition. What if you find the value you were looking for after only a few iteration. Then
making all that expensive calculations to the whole list was a waste of time.

This lazy evaluation can help you save both memory and time and you always have the option to force the immediate calculation by calling the **list**
function.
{/aside}
![](examples/advanced/map_list.py)
![](examples/advanced/map_list.out)



## double with lambda
{id: lambda-double}
{i: lambda}

{aside}

There are many other cases besides **map** where we need to pass a function as a parameter to some other function.
Many cases the function we pass is some almost trivial function with a single operation in it.
In those cases creating a named function like the "double" function in the previous examples is an overkill.
{/aside}

{aside}

In this example we also used the **list** function to force the full evaluation of the map object to make it easier to show
the results. Normally you probably would not use the **list** function here.
{/aside}
![](examples/advanced/double_lambda.py)
![](examples/advanced/double_lambda.out)


## What is lambda in Python?
{id: lambda}
{i: lambda}

{aside}
Lambda creates simple anonymous function. It is simple because it can only have one statement in its body. It is anonymous because usually it does not have a name.
{/aside}


{aside}
The usual use is as we saw earlier when we passed it as a parameter to the `map` function. However, in the next example however we show that you can assign the
lambda-function to a name and then you could used that name just as any other function you would define using **def**.
{/aside}
![](examples/advanced/lambda.py)
![](examples/advanced/lambda.out)


## lambda returning tuple
{id: lambda-returning-tuple}

{aside}

A lambda function can return complex data structures as well. e.g. a tuple.
{/aside}
![](examples/advanced/lambda_return_tuple.py)
![](examples/advanced/lambda_return_tuple.out)


## map returning tuples
{id: map-returning-tuples}
![](examples/advanced/map_lambda_tuples.py)
![](examples/advanced/map_lambda_tuples.out)


## lambda with two parameters
{id: lambda-with-two-parameters}

{aside}

A **lambda**-function can have more than one parameters:
{/aside}
![](examples/advanced/lambda_params.py)
![](examples/advanced/lambda_params.out)


## map for more than one iterable
{id: map-for-more}

Lets "add" together two lists of numbers. Using + will just join the two lists together, but we can use the "map" function to add the values pair-wise.

![](examples/advanced/map_add.py)
![](examples/advanced/map_add.out)


## map on uneven lists
{id: map-uneven-lists}

{aside}

In **Python 3** the iterator stops when the shortest iterable is exhausted.

In **Python 2** it used to extend the shorter lists by **None** values.
{/aside}
![](examples/advanced/map_add_shorter.py)
![](examples/advanced/map_add_shorter.out)


## replace None (for Python 2)
{id: map-for-more-none}

{aside}
In Python 2 map used to extend the shorter lists by **None** values.
So to avoid exceptions, we had some exra code replacing the None values by 0, using the ternary operator.
{/aside}
![](examples/advanced/map_add_none.py)


## map on uneven lists - fixed (for Python 2)
{id: map-uneven-lists-fixed}

{aside}
A nicer fix was this:
{/aside}

![](examples/advanced/map_add_shorter_fixed.py)


## map mixed iterators
{id: map-mixed-iterators}

{aside}
**map** works on any iterable, so we might end up passing one list and one string to it.
{/aside}

![](examples/advanced/map_mixed.py)
![](examples/advanced/map_mixed.out)


## map fetch value from dict
{id: map-dict}

![](examples/advanced/map_dict.py)
![](examples/advanced/map_dict.out)


## filter
{id: filter}
{i: filter}

`filter(function, iterable)`

{aside}
Will return an interable object that will return all the items of the original iterable that evaluate the function to **True**.
This can have only one iterable!
{/aside}

![](examples/advanced/filter.py)
![](examples/advanced/filter.out)


## filter - map example
{id: filter-map}

![](examples/advanced/filter_map.py)
![](examples/advanced/filter_map.out)


## filter - map  in one expression
{id: filter-map-one}

![](examples/advanced/filter_map_one.py)
![](examples/advanced/filter_map_one.out)


## reduce
{id: reduce}
{i: reduce}

{aside}
In Python 2 it was still part of the language.
{/aside}

`reduce(function, iterable[, initializer])`

![](examples/advanced/reduce.py)

The initializer is used as the 0th element returned by the iterable. It is mostly interesting in case the iterable is empty.


## zip
{id: zip}
{i: zip}

![](examples/advanced/zip.py)
![](examples/advanced/zip.out)

[Monty Python](https://en.wikipedia.org/wiki/Monty_Python)

## Creating dictionary from two lists using zip
{id: creating-dict-using-zip}
{i: zip}

![](examples/advanced/create_dict_using_zip.py)
![](examples/advanced/create_dict_using_zip.out)


## all, any
{id: all-any}
{i: all}
{i: any}

```
all(iterable) - returns True if all the elements of iterable return True
any(iterable) - returns True if any of the elements in iterable return True
```

![](examples/advanced/all_any.py)


## Compare elements of list with scalar
{id: compare-elements-of-list-with-scalar}

![](examples/advanced/compare_list_with_scalar.py)


## List comprehension - double
{id: list-comprehension-double}
{i: []}

{aside}
We take the original example where we had a function called double, and this time we
write a different expression to run the function on every element of an iterable.
{/aside}

![](examples/lists/list_comprehension_double.py)


## List comprehension - simple expression
{id: list-comprehension-simple}
{i: []}

![](examples/lists/list_comprehension_simple.py)


## List generator
{id: list-generator}
{i: ()}


Going over the values of the generator will empty the generator.


![](examples/lists/simple_generator.py)
![](examples/lists/simple_generator.out)


## List comprehension
{id: list-comprehension}
{i: mapcar}

![](examples/lists/list_comprehension.py)

{aside}
In LISP this would be a mapcar.
{/aside}


## Dict comprehension
{id: dict-comprehension}

![](examples/advanced/dict_comprehension.py)


## Lookup table with lambda
{id: lookup-table}

![](examples/advanced/lookup_table.py)


## Read lines without newlines
{id: read-lines-without-newlines}

![](examples/advanced/read_lines_without_newlines.py)


## Read key-value pairs
{id: read-key-value-pairs}

![](examples/advanced/pairs.txt)
![](examples/advanced/read_key_value_pairs.py)

```
{'name': 'Foo Bar', 'email': 'foo@bar.com', 'address': 'Foo street 42'}
```

## Create index-to-value mapping in a dictionary based on a list of values
{id: index-to-value-mapping}
{i: zip}

![](examples/advanced/index_to_value.py)
![](examples/advanced/index_to_value.out)


## Exercise: min, max, factorial
{id: exercise-functional}

* Implement an expression to calculate "min", and another expression to calculate "max" of lists.
* Implement an expression that will calculate factorial. f(n) should return the value of n! (n! = n * (n-1) * (n-2) * ... * 1)
* Implement an expression that given 2 lists will return a new list in which each element is the max() for each pair from the input lists. E.g. given [1, 3, 6] and [2, 4, 5]  the result is [2, 4, 6]
* Use reduce, map, lambda



## Exercise: Prime numbers
{id: exercise-prime-numbers}

Calculate and print the prime numbers between 2 and N. Use filter.



## Exercise: Many validator functions
{id: exercise-many-validator-functions}


Given several validator functions (that get a parameter and return True or False),
and given a list of values, return a sublist of values that pass all the validation
checks. See the sekeleton:


![](examples/advanced/many_validators_skeleton.py)


## Exercise: Calculator using lookup table
{id: exercise-calculator-using-lookup-table}


Write a script that will accept a math expression such as `python calc.py 2 + 3` and will print the result.
Use lookup tables select the implementation of the actual computation. (supporting +, - , *, /) is enought




## Solution: min, max, factorial
{id: solution-functional}
![](examples/advanced/reduce_solution.py)



## Solution: Prime numbers
{id: solution-prime-numbers}

Calculating the prime numbers

![](examples/advanced/primes_with_filter.py)



## Solution: Many validator functions
{id: solution-many-validator-functions}
![](examples/advanced/many_validators.py)


## Solution: Calculator using lookup table
{id: solution-calculator-using-lookup-table}
![](examples/advanced/calc.py)


## map with condtion
{id: map-with-condition}
{i: map}

{aside}

The conversion function can do anything. It can have a condition inside.
{/aside}
![](examples/advanced/map_with_condition.py)


## map with lambda
{id: map-with-lambda}
![](examples/advanced/map_lambda.py)


## map with lambda with condition
{id: map-with-lambda-with-condition}
![](examples/advanced/map_lambda_condition.py)


## List comprehension - complex
{id: list-comprehension-complex}
![](examples/lists/list_comprehension_numbers.py)



