# Functional Programming in Perl
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

## grep
{id: grep-perl}
{i: grep}
{i: filter}

{aside}
The `grep` keyword in Perl is a generalization of the Unix/Linux grep tool. Given a condition and a list of values it will return a, usually shorter, list
of elements that will return true if used in the expression. In other language the similar tool is called `filter`.

In this example we have an array of numbers and an expression comparing `$_` which holds the current value as grep iterates over the elements of the array. If the current value
is greater or equal than 5 then it will be passed to the left hand side, if it is less than 5 then it will be filtered out.

Note, there is no comma after the curly braces.
{/aside}

```
ARRAY = grep BLOCK LIST
```
![](examples/advanced-perl/grep_perl.pl)

## grep to filter files based on modification date
{id: grep-to-filter-files}
{i: grep}

![](examples/advanced-perl/grep_files.pl)

## Imitating the Unix/Linux grep command in Perl
{id: imitating-the-unix-grep-command}
{i: grep}

![](examples/advanced-perl/unix_grep.pl)


## map
{id: map}
{i: map}

{aside}
`map` will transform the content of a list.


Given a list of values that can come from an array or from calling the `keys` function on a hash or in any other way, we can apply a transformation
on each element and then collect the transformed values on the left hand side of the assignment. e.g. in an array.

On each iteration the current element is placed in the `$_` variable, the code in the block is executed, and the result is passed to the left-hand-side
that collects all the responses.
{/aside}

```
ARRAY = map BLOCK LIST
```
![](examples/advanced-perl/map_perl.pl)


## Use map to filter values
{id: use-map-to-filter-values}

{aside}
I am not sure why would you do this instead of using `grep`, but you can do this and this can bring use to another,
more usefule example.
{/aside}

![](examples/advanced-perl/map_to_filter.pl)

## Map to add more elements
{id: map-to-add-more-elements}

![](examples/advanced-perl/map_to_duplicate.pl)

## Use map to filter and enrich
{id: map-to-filter-and-enrich}

![](examples/advanced-perl/map_filter_and_enrich.pl)

## Create a hash from an array using map
{id: map-create-hash}
{i: map}

* We have a list of values. We would like to build a fast look-up table to check for existence.

{aside}
The time it takes to check if a value can be found in an array is proportional to the length of the array. The complexity is O(n).

If you need to do it a lot of times you might be better off building a hash where the keys are  the items coming from the array. The values
don't matter as we will check the existance of a key. (Alternatively you can set the values of the hash to be 1 and then you can check if the
the value is there.) The time it takes to look up a key in a hash does not depend on the size of the hash. It is O(1). So once we have the hash
the look-up will be much faster. Building the hash is proportional to the number of items in the array.

So if we need to look up a very small number of elements or if the original array is small then probably it is better to just use the array.

If we need a lot of look-ups and there are many elements in the original array then building a temporary look-up hash might be a good idea.

We use more memory but we can gain speed.
{/aside}

![](examples/advanced-perl/map_create_hash.pl)


## Unique values
{id: unique-values}
{i: unique}

You have a list of values with duplications, how can you create a unique list of the values?


![](examples/functional/unique_values.pl)


## Unique values - improved
{id: unique-values-improved}


But actually we don't need to do it in two steps:


![](examples/functional/unique_values_shorter.pl)


## Unique values using grep
{id: unique-values-grep}


Of course there is an even shorter way to write it:

![](examples/functional/unique_values_grep.pl)

In this version you can even assign the values back to the original
array writing:

```
@data = grep { !$seen{$_}++} @data;
```

## Uniq with List::MoreUtils
{id: uniq}
{i: uniq}
{i: distinct}
{i: List::MoreUtils}

{aside}
There are several ways to implement this without using an external module, but why would we want to reinvent the wheel when
there is already a good solution in the List::MoreUtils module?

The only problem, but we see it all over the programming world is that this function called "uniq" would return a list of distinct elements
instead of the ones that were unique in the original list.
{/aside}

* [List::MoreUtils](https://metacpan.org/pod/List::MoreUtils)

![](examples/functional/uniq.pl)

## Closures
{id: closures}
{i: closure}


* [Closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))

```
A subroutine that generates subroutines based on some input values.
```

![](examples/references/incrementer.pl)
![](examples/references/incrementer-generator.pl)

Output:

![](examples/references/incrementer-generator.out)

