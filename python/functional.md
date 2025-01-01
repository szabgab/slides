# Functional programming in Python
{id: functional}

## Programming Paradigms
{id: programming-paradigms}

* [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
* procedural
* object oriented
* declarative (SQL)
* functional

## Functional programming
{id: functional-programming}

* Immutability (variables don't change)
* Separation of data and functions.
* Pure functions (no side-effects)
* First-class functions (you can assign function to another name and you can pass function to other functions and return them as well. We can also manipulate functions)
* Higher order functions: a functions that either takes a function as a parameter or returns a function as a parameter.

## Iterators (Iterables)
{id: iterables}
{i: iterables}

{aside}

You already know that there are all kinds of objects in Python that you can iterate over using the **for in** construct.
For example you can iterate over the characters of a string, or the elements of a list, or whatever **range()** returns.
You can also iterate over the lines of a file
and you have probably seen the **for in** construct in other cases as well. The objects that can be iterated over are collectively called
[iterables](https://docs.python.org/glossary.html#term-iterable).
You can do all kind of interesting things on such **iterables**. We'll see a few now.
{/aside}

* A few data type we can iterate over using the **for ... in ...** construct. (strings, files, tuples, lists, list comprehension)

![](examples/functional/iterables.py)
![](examples/functional/iterables.out)


## range
{id: range-iterator}
{i: range}

{aside}

So what does **range** really return?
{/aside}

{aside}

Instead of returning the list of numbers (as it used to do in Python 2), now it returns a **range object** that provides "the opportunity to go over
the specific series of numbers" without actually creating the **list** of numbers. Getting an object instead of the whole list has a number of advantages.
One is space. In the next example we'll see how much memory is needed for the object returned by the **range** function and
how much would it take to have the corresponding list of numbers in memory. For now let's see how can we use it:
{/aside}

* `range(start, end, step)`
* `range(start, end)` - step defaults to 1
* `range(end)` - start defaults to 0, step defaults to 1

![](examples/functional/range.py)
![](examples/functional/range.out)


## range with list
{id: range-list}
{i: range}
{i: list}
{i: getsizeof}

{aside}
Using the **list** function we can tell the **range** object to generate the whole list immediately. Either using
the variable that holds the **range** object, or wrapping the **range()** call in a **list()** call.
{/aside}

{aside}
You might recall at the beginning of the course we saw the **sys.getsizeof()** function that returns the size of a Python object
in the memory. If you don't recall, no problem, we'll see it used now. As you can see the size of the range object is only 48 bytes
while the size of the 3-element list is already 112 bytes. It seems the range object is better than even such a short lists.
On the next page we'll see a more detailed analyzis.
{/aside}

![](examples/functional/range_list.py)


## range vs. list size
{id: range-size}
{i: getsizeof}

{aside}
Showing that the range object remains the same size regardless of the size of the range, but if we convert it into a list then its
memory footprint is proportional to its size. To the number of elements in it.

In this example we have a loop iterating over **range(21)**, but that's only for the convenience, the interesting part is inside the loop.
On every iteration call **range()** with the current number, then we convert the resulting object into a list of numbert. Finally we print out
the current number and the size of both the object returned by **range()** and the list generated from the object. As you can see the memory usage
of the **range** object remains the same 48 byttes, while the memory usage of the list growth as the list gets longer.
{/aside}

![](examples/functional/range_size.py)
![](examples/functional/range_size.out)

## for loop with transformation
{id: for-loop-transformation}
{i: append}

{aside}
There are many cases when we have a list of some values and we need to apply some transformation to each value. At the end we would
like to have the list of the resulting values.
{/aside}

{aside}
A very simple such transformation would be to double each value. Other, more interesting examples might be reversing each string,
computing some more complex function on each number, etc.)
{/aside}

{aside}
In this example we just double the values and use **append** to add each value to the list containing the results.
{/aside}

![](examples/functional/double.py)
![](examples/functional/double.out)

{aside}
There are better ways to do this.
{/aside}


## map
{id: map}
{i: map}

* `map(function, iterable, ...)`

{aside}
The [map](https://docs.python.org/library/functions.html#map) function of Python applies a function to every item in an iterable and returns an iterator
that can be used to iterate over the results. Wow, how many times I repeated the word iter...something. Instead of trying to untangle that sentence,
let's look at the following example:
{/aside}

{aside}
We have a list of numbers in the brilliantly named variable `numbers` with 1, 2, 3, 4 as the content. We could like to create a list of all the doubles (so that would be 2, 4, 6, 8 in this case)
and then iterate over them printing them on the screen. Sure, you probably have some more complex operation to do on the numbers than simple double them, but in this example I did not want to complicate
that part. Suffice to say that you have some computation to do in every element.
{/aside}

{aside}
So you encapsulate your computation in a regular Python function (in our case the function is called **double**). Then you call **map** and pass to it two parameters. The first parameter is the **double** function itself, the second parameter is the list of the values you would like to work on. `map` will no go over all the values in the **numbers** list, call the **double** function with
each number and provide allow you to iterate over the results. Something like this:
{/aside}


{aside}
double_numbers = [ double(1), double(2), double(3), double(4)]
{/aside}

{aside}
Except, that the above is not true.
{/aside}

{aside}
When Python executes the `double_numbers = map(double, numbers)` line, no computation happens and no resulting list is created. Python only prepars "the possibility to do the computations". In the upcoming examples we'll see what does this sentence really mean, for now let's see what do we have in this example: `double_numbers` contains a **map object*, but when you iterate
over it using the **for num in double_numbers** construct you get the expected values.
{/aside}

{aside}
In the second half of the example you can see the same works on strings as well.
{/aside}


![](examples/functional/map.py)
![](examples/functional/map.out)

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

![](examples/functional/map_list.py)
![](examples/functional/map_list.out)

## size of map
{id: size-of-map}

![](examples/functional/map_size.py)

## map delaying function call
{id: map-delaying-function-call}

{aside}
In this example we have added a call to `print` in the double function in order to see when is it really executed. You can see that the first output
comes from the `print` statement that was **after** the `map` call. Then on each iteration we see the output from inside the "double" function and then the
result from the loop. In a nutshell Python does not execute the "double" function at the point where we called `map`. It only executes it when we iterate over
the resulting object.
{/aside}

![](examples/functional/map_with_print.py)
![](examples/functional/map_with_print.out)

## map on many values
{id: map-on-many-values}

{aside}
Now imagine you have a very long list. I know this is not such a long list, but I trust you can imagin a long list of numbers. We would like to run
some function on each element and then iterate over the results, but what if at one point in the iteration we decide to `break` out of the loop?
{/aside}

![](examples/functional/map_with_many_items.py)
![](examples/functional/map_with_many_items.out)

{aside}
You can see that it did not need to waste time calculating the doubles of all the values, as it was calculating on-demand. You can also see that the object returned
from `map` takes up only 56 bytes. Regardless of the size of the original array.
{/aside}




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
![](examples/functional/double_lambda.py)
![](examples/functional/double_lambda.out)


## What is lambda in Python?
{id: lambda}
{i: lambda}

{aside}
Lambda creates simple anonymous function. It is simple because it can only have one statement in its body. It is anonymous because usually it does not have a name.
{/aside}


{aside}
The usual use is as we saw earlier when we passed it as a parameter to the `map` function. However, in the next example we show that you can assign the
lambda-function to a name and then you could used that name just as any other function you would define using **def**.
{/aside}
![](examples/functional/lambda.py)
![](examples/functional/lambda.out)


## lambda returning tuple
{id: lambda-returning-tuple}

{aside}

A lambda function can return complex data structures as well. e.g. a tuple.
{/aside}
![](examples/functional/lambda_return_tuple.py)
![](examples/functional/lambda_return_tuple.out)


## map returning tuples
{id: map-returning-tuples}
![](examples/functional/map_lambda_tuples.py)
![](examples/functional/map_lambda_tuples.out)


## lambda with two parameters
{id: lambda-with-two-parameters}

{aside}

A **lambda**-function can have more than one parameters:
{/aside}
![](examples/functional/lambda_params.py)
![](examples/functional/lambda_params.out)


## map for more than one iterable
{id: map-for-more}

Lets "add" together two lists of numbers. Using + will just join the two lists together, but we can use the "map" function to add the values pair-wise.

![](examples/functional/map_add.py)
![](examples/functional/map_add.out)


## map on uneven lists
{id: map-uneven-lists}

{aside}

In **Python 3** the iterator stops when the shortest iterable is exhausted.

In **Python 2** it used to extend the shorter lists by **None** values.
{/aside}
![](examples/functional/map_add_shorter.py)
![](examples/functional/map_add_shorter.out)


## replace None (for Python 2)
{id: map-for-more-none}

{aside}
In Python 2 map used to extend the shorter lists by **None** values.
So to avoid exceptions, we had some exra code replacing the None values by 0, using the ternary operator.
{/aside}
![](examples/functional/map_add_none.py)


## map on uneven lists - fixed (for Python 2)
{id: map-uneven-lists-fixed}

{aside}
A nicer fix was this:
{/aside}

![](examples/functional/map_add_shorter_fixed.py)


## map mixed iterators
{id: map-mixed-iterators}

{aside}
**map** works on any iterable, so we might end up passing one list and one string to it.
{/aside}

![](examples/functional/map_mixed.py)
![](examples/functional/map_mixed.out)


## map fetch value from dictionary
{id: map-dict}

![](examples/functional/map_dict.py)
![](examples/functional/map_dict.out)


## Exercise: string to length
{id: exercise-string-to-length}

* Given a list of strings, create an iterable that will provide the length of each string.
* If the input is `['moon', venus', 'jupyter']` then the resulting iterable should return 4, 5, and 7.


## Exercise: row to length
{id: exercise-row-to-length}

* Given a file, create an iterable that will provide the length of each row.
* Can you do it without reading the file?


## Exercise: compare rows
{id: exercise-compare-rows}

* Create an iterable that given two files will return true for each line where the first space in the first file is earlier than the first space in the second file. So

* given: "ab cd"  vs "abc d" the value is true
* given: "ab cd"  vs "ab cd" the value is false
* given: "ab cd"  vs "a bcd" the value is false


## Solution: string to length
{id: solution-string-to-length}

![](examples/functional/map_string_to_len.py)


## Solution: row to length
{id: solution-row-to-length}


![](examples/functional/map_row_to_length.py)


## Solution: compare rows
{id: solution-compare-rows}

![](examples/functional/compare_rows.py)
![](examples/functional/compare_rows.out)

## filter in a loop
{id: filter-in-a-loop}

![](examples/functional/filter_with_loop.py)
![](examples/functional/filter_with_loop.out)

## filter
{id: filter}
{i: filter}

* `filter(function, iterable)`

{aside}
`filter` will return an iterable object that will return all the items of the original iterable that evaluate the function to **True**.
This can have only one iterable!
{/aside}

![](examples/functional/filter_with_function.py)
![](examples/functional/filter_with_function.out)

## filter with lambda
{id: filter-with-lambda}
{i: filter}
{i: grep}

![](examples/functional/filter.py)
![](examples/functional/filter.out)


## filter - map example
{id: filter-map}

![](examples/functional/filter_map.py)
![](examples/functional/filter_map.out)


## filter - map  in one expression
{id: filter-map-one}

![](examples/functional/filter_map_one.py)
![](examples/functional/filter_map_one.out)

## filter a dictionary using dict comprehension
{id: filter-a-dictionary}

We have a dictionary, we would like to create another dictionary based on this one that contains only key-value pairs that meet a certain condition.

![](examples/functional/filter_dictionary.py)
![](examples/functional/filter_dictionary.out)


## Get indices of values
{id: get-indexes-of-values}

{aside}
`filter` can help us get a sublist of values from an iterable, eg. from a list that match some condition.
In this example we see how to get all the names that are exactly 3 characters long.

What if, however if instead of the values themselves, you would like to know their location? The indexes of the
places where these value can be found. In that case, you would run the `filter` on the indexes from 0 till the last
valid index of the list. You can do that using the `range` function.
{/aside}

{aside}
Finally there is another example that shows how to get the indexes of all the names that have an "e" in them.
Just to show you that we can use any arbitray condition there.
{/aside}

![](examples/functional/get_indexes.py)
![](examples/functional/get_indexes.out)


## reduce
{id: reduce}
{i: reduce}

{aside}
In Python 2 it was still part of the language.
{/aside}

`reduce(function, iterable[, initializer])`

![](examples/functional/reduce.py)
![](examples/functional/reduce.out)

The initializer is used as the 0th element returned by the iterable. It is mostly interesting in case the iterable is empty.

## reduce empty list
{id: reduce-empty-list}

![](examples/functional/reduce_empty.py)


## reduce with default
{id: reduce-with-defaiult}
{i: reduce}

![](examples/functional/reduce_with_default.py)
![](examples/functional/reduce_with_default.out)

## reduce list of dictionaries
{id: reduce-list-of-dictionaries}

* Combining `map` and `filter`
* The reduce-only solution requires the default value

![](examples/functional/reduce_list_of_dicts.py)

## zip
{id: zip}
{i: zip}

{aside}
`zip` can iterate over a number of lists (or iterables in general) in parallel. The iteration will stop when the first iterator stops.
{/aside}

![](examples/functional/zip.py)
![](examples/functional/zip.out)

[Monty Python](https://en.wikipedia.org/wiki/Monty_Python)

## Combining two lists using zip
{id: combing-lists-using-zip}
{i: zip}

![](examples/functional/create_list_using_zip.py)
![](examples/functional/create_list_using_zip.out)

## Creating dictionary from two lists using zip
{id: creating-dict-using-zip}
{i: zip}

![](examples/functional/create_dict_using_zip.py)
![](examples/functional/create_dict_using_zip.out)


## all, any
{id: all-any}
{i: all}
{i: any}


* `all(iterable)` - returns True if all the elements of iterable return True
* `any(iterable)` - returns True if any of the elements in iterable return True


![](examples/functional/all_any.py)


## Compare elements of list with scalar
{id: compare-elements-of-list-with-scalar}

![](examples/functional/compare_list_with_scalar.py)


## List comprehension - double
{id: list-comprehension-double}
{i: []}

{aside}
We take the original example where we had a function called double, and this time we
write a different expression to run the function on every element of an iterable.
{/aside}

![](examples/functional/list_comprehension_double.py)


## List comprehension - simple expression
{id: list-comprehension-simple}
{i: []}

![](examples/functional/list_comprehension_simple.py)
![](examples/functional/list_comprehension_simple.out)


## List generator
{id: list-generator}
{i: ()}


Going over the values of the generator will empty the generator.


![](examples/functional/simple_generator.py)
![](examples/functional/simple_generator.out)


## List comprehension
{id: list-comprehension}
{i: mapcar}

![](examples/functional/list_comprehension.py)

{aside}
In LISP this would be a mapcar.
{/aside}


## Dict comprehension
{id: dict-comprehension}

![](examples/functional/dict_comprehension.py)


## Lookup table with lambda
{id: lookup-table}
{i: lambda}

![](examples/functional/lookup_table.py)


## Read lines without newlines
{id: read-lines-without-newlines}
{i: readlines}
{i: map}
{i: lambda}

![](examples/functional/read_lines_without_newlines.py)


## Read key-value pairs
{id: read-key-value-pairs}
{i: readlines}
{i: map}
{i: lambda}
{i: split}
{i: dict}

![](examples/functional/pairs.txt)
![](examples/functional/read_key_value_pairs.py)

```
{'name': 'Foo Bar', 'email': 'foo@bar.com', 'address': 'Foo street 42'}
```

## Create index-to-value mapping in a dictionary based on a list of values
{id: index-to-value-mapping}
{i: zip}
{i: dict}

![](examples/functional/index_to_value.py)
![](examples/functional/index_to_value.out)


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


![](examples/functional/many_validators_skeleton.py)


## Exercise: Calculator using lookup table
{id: exercise-calculator-using-lookup-table}


Write a script that will accept a math expression such as `python calc.py 2 + 3` and will print the result.
Use lookup tables select the implementation of the actual computation. (supporting +, - , *, /) is enought

## Exercise: parse file
{id: exercise-parse-file}

In the following file we have lines:

```
SOURCE/FILENAME.json,TARGET
```

read in the file and create

* a single dictionary where the `SOURCE/FILENAME.json` is the key and the TARGET is the value.
* list of dictionaries in which the keys are 'source', 'filename', and 'target' and the values are from the respective columns (SOURCE, FILENAME.json, and TARGET)

You can solve this `for`-loop or with `map` and list-comprehensions. Do it in both ways.

![](examples/functional/books.txt)


## Solution: min, max, factorial
{id: solution-functional}

![](examples/functional/reduce_solution.py)


## Solution: Prime numbers
{id: solution-prime-numbers}

Calculating the prime numbers

![](examples/functional/primes_with_filter.py)


## Solution: Many validator functions
{id: solution-many-validator-functions}

![](examples/functional/many_validators.py)


## Solution: Calculator using lookup table
{id: solution-calculator-using-lookup-table}
![](examples/functional/calc.py)


## map with condtion
{id: map-with-condition}
{i: map}

{aside}

The conversion function can do anything. It can have a condition inside.
{/aside}
![](examples/functional/map_with_condition.py)


## map with lambda
{id: map-with-lambda}
![](examples/functional/map_lambda.py)


## map with lambda with condition
{id: map-with-lambda-with-condition}
![](examples/functional/map_lambda_condition.py)


## List comprehension - complex
{id: list-comprehension-complex}
![](examples/functional/list_comprehension_numbers.py)


## Change list before iteration over map object
{id: change-list-before-iteration-over-map-object}

{aside}
A small warning. Because **map** only connects to our iterator, but does not iterate over it till it is called,
if we change the content of the underlying iterator, that will be reflected in the results of the iteration over the map object.
{/aside}


![](examples/functional/change_list_before_map.py)
![](examples/functional/change_list_before_map.out)

## Replace list before iteration over map object
{id: replace-list-before-iteration-over-map-object}


![](examples/functional/replace_list_before_map.out)
![](examples/functional/replace_list_before_map.py)

