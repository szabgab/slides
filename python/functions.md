# Functions (subroutines)
{id: functions}

## Why use functions?
{id: why-use-functions}

{aside}
There are two main reasons to use functions.

One of the is code reuse. Instead of copy-paste-ing snippets of code that does the same in multiple areas in the application,
we can create a function with a single copy of the code and call it from multiple location.

Having functions can also make the code easier to understand, easier to test and to maintain.

The functions are supposed to be relatively short, each function dealing with one issue, with one concern.
They should have well defined input and output and without causing side-effects.

There are no clear rules, but the suggestion is that function be somewhere between 4-30 lines of code.
{/aside}

* Code reuse - [DRY - Don't Repeate Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
* Small units of code. (One thought, single responsibility) Easier to understand, test, and maintain.

## Defining simple function
{id: add-functions}
{i: def}
{i: return}

![](examples/functions/add_function.py)

{aside}
The function definition starts with the word "dev" followed by the name of the function ("add" in our example), followed by the list of parameters
in a pair of parentheses, followed by a colon ":". Then the body of the function is indented to the right. The depth of indentation does not matter
but it must be the same for all the lines of the function. When we stop the indentation and start a new expression on the first column, that's what tells
Python that the function defintion has ended.
{/aside}


## Passing positional parameters to a function
{id: use-function-with-positional-parameters}
{i: def}

![](examples/functions/params.py)

{aside}
Positional parameters.
{/aside}



## Function parameters can be named
{id: named-parameters}
{i: named parameter}
{i: keyword argument}

![](examples/functions/named_params.py)

{aside}
The parameters of every function can be passed either as positional parameters or as named parameters.
{/aside}


## Mixing positional and named parameters
{id: mixing-positional-and-named-parameters}

![](examples/functions/named_and_positional_params.py)

![](examples/functions/positional_and_named_params.py)

```
  File "examples/functions/named_and_positional_params.py", line 14
    'gabor@szabgab.com',
    ^
SyntaxError: positional argument follows keyword argument
```

## Default values, optional parameters, optional parameters
{id: parameter-with-default-values}

![](examples/functions/default.py)
![](examples/functions/default.out)

{aside}
Function parameters can have default values. In such case the parameters are optional.
In the function declaration, the parameters with the default values must come last.
In the call, the order among these arguments does not matter, and they are optional anyway.
{/aside}

## Default value in first param
{id: parameter-with-default-value-in-first-param}

![](examples/functions/default_first.py)
![](examples/functions/default_first.out)


## Several defaults, using names
{id: defaults-with-names}
{i: non-keyword arg after keyword arg}

{aside}
Parameters with defaults must come at the end of the parameter declaration.
{/aside}

![](examples/functions/named_params_and_defaults.py)

![](examples/functions/named_and_positional_bad.py)
![](examples/functions/named_and_positional_bad.out)

{aside}
There can be several parameters with default values.
They are all optional and can be given in any order after the positional arguments.
{/aside}


## Arbitrary number of arguments `*`
{id: arbitrary-number-of-arguments}
{i: `*args`}
{i: tuple}

{aside}
The values arrive as `tuple`.
{/aside}

![](examples/functions/sum.py)
![](examples/functions/sum.py.out)


## Fixed parmeters before the others
{id: fixed-and-variable-length-argument-list}

{aside}
The `*numbers` argument can be preceded by any number of regular arguments
{/aside}

![](examples/functions/super.py)
![](examples/functions/super.py.out)

## Arbitrary key-value pairs in parameters `**`
{id: kw-value-pairs}
{i: **kwargs}

![](examples/functions/kw.py)
![](examples/functions/kw.out)


## Extra key-value pairs in parameters
{id: extra-kw-value-pairs}
{i: **kwargs}

![](examples/functions/extra_kw.py)
![](examples/functions/extra_kw.out)


## Every parameter option
{id: every-parameter-option}

![](examples/functions/full.py)


## Duplicate declaration of functions (multiple signatures)
{id: duplicate-declaration}

![](examples/functions/duplicate_add.py)
![](examples/functions/duplicate_add.out)

The second declaration silently overrides the first declaration.

## Pylint duplicate declaration
{id: pylint-duplicate-declaration}

* [pylint](http://www.pylint.org/) can find such problems, along with a bunch of others.

```
pylint -E duplicate_add.py
```

![](examples/functions/lint_duplicate_add.out)

## Return more than one value
{id: return-more-than-one-value}

![](examples/functions/multiple_return.py)

![](examples/functions/multiple_return.out)


## Recursive factorial
{id: recursive-factorial}

```
n! = n * (n-1) ... * 1

0! = 1
n! = n * (n-1)!

f(0) = 1
f(n) = n * f(n-1)
```

![](examples/functions/factorial.py)


## Recursive Fibonacci
{id: recursive-fibonacci}

```
fib(1) = 1
fib(2) = 1
fib(n) = fib(n-1) + fib(n-2)
```

![](examples/functions/fibonacci.py)

{aside}
Python also supports recursive functions.
{/aside}


## Non-recursive Fibonacci
{id: non-recursive-fibonacci}

![](examples/functions/simple_fibonacci.py)


## Unbound recursion
{id: unbound-recursion}

* In order to protect us from unlimited recursion, Python limits the depth of recursion:

![](examples/functions/recursion.py)
![](examples/functions/recursion.out)

## Variable assignment and change - Immutable
{id: remember-assignment}

Details showed on the next slide

![](examples/functions/change.py)


## Variable assignment and change - Mutable
{id: assignment-details}

![](examples/functions/change_details.py)


## Parameter passing of functions
{id: function-parameter-passing}

![](examples/functions/call_by_value.py)


## Passing references
{id: passing-references}

![](examples/functions/reference_passed.py)


## Function documentation
{id: function-documentation}

![](examples/functions/mydocs.py)

{aside}
Immediately after the definition of the function, you can add a string - it can be a """ string to spread multiple lines -
that will include the documentation of the function. This string can be accessed via the __doc__ (2+2 underscores) attribute
of the function. Also, if you 'import' the file - as a module - in the interactive prompt of Python, you will be
able to read this documentation via the **help()** function.  **help(mydocs)** or **help(mydocs.f)**
in the above case.
{/aside}


## Sum ARGV
{id: sum-argv}

![](examples/functions/sum_argv.py)


## Copy-paste code
{id: copy-paste}

![](examples/functions/sums.py)

```
sum of a: 116 average of a: 29.0
sum of b: 154 average of b: 38.5
sum of c: 138 average of c: 34.5
```

Did you notice the bug?


## Copy-paste code fixed
{id: copy-paste-fixed}

![](examples/functions/sums_in_function.py)

```
sum of a: 116 average of a: 29.0
sum of b: 154 average of b: 38.5
sum of c: 138 average of c: 46.0
```


## Copy-paste code further improvement
{id: copy-paste-further-improvement}

![](examples/functions/sums_in_function_dict.py)


## Palindrome
{id: palindrome}

An iterative and a recursive solution

![](examples/functions/palindrome.py)


## Exercise: statistics
{id: exercise-statistics}

Create a file called **statistics.py** that has a function that will accept any number of numbers and return a list of values:

* The sum
* Average
* Minimum
* Maximum

## Exercise: Pascal triangle
{id: exercise-pascal-triangle}

* Create a file called **pascal_triangle.py** that given a number N on the command line will print the first N rows of the Pascal triangle.

## Exercise: Pascal triangle functions
{id: exercise-pascal-triangle-functions}

* Create a file called **pascal_triangle_functions.py** that will do exactly as the previous one, but this time make sure you have these functions:

* A function that given a list of numbers (a row from the triangle, e.g. 1, 3, 3, 1) will return the next row (1, 4, 6, 4, 1). **next_row**
* A function that given a depth N will return a list of the first N rows. **get_triangle**
* A function that will print the triangle. **print_triangle**.


## Exercise: recursive dependency tree
{id: exercise-recursive-dependency-tree}

* Create a file called **recursive_dependency_tree.py**

Give a bunch of files that has list of requirement in them.
Process them recursively and print the resulting full list of requirements

![](examples/functions/dependencies/a.txt)
![](examples/functions/dependencies/b.txt)
![](examples/functions/dependencies/c.txt)

```
$ python traversing_dependency_tree.py a

Processing a
Processing b
Processing e
Processing d
Processing c
Processing f
Processing g
Processing d
```

## Exercise: dependency tree
{id: exercise-dependency-tree}

* Create a file called **dependency_tree.py**

That will process the files holding the dependency tree, but without recursive calls.


## Exercise: Tower of Hanoi
{id: exercise-tower-of-hanoi-recursive}

* Create a script called **tower_of_hanoi.py** providing a solution to [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

There are 3 sticks. On the first stick there are n rings of different sizes. The smaller the ring the higher it is on the stick.
Move over all the rings to the 3rd stick by always moving only one ring and making sure that never will there be a large ring on top
of a smaller ring.


## Exercise: Merge  and Bubble sort
{id: exercise-bubble-sort}

* Implement [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) call it **bubble_sort.py**
* Implement [merge sort](https://en.wikipedia.org/wiki/Merge_sort) call it **merge_sort.py**

## Exercise: Refactor previous solutions to use functions
{id: exercise-refactor-previous-solutions-to-us-functions}

* Go over all of the previous exercises and their solutions (e.g. the games)
* Take one (or more if you like this exercise) and change them to use functions.
* If possible make sure you don't have any variable definitions outside of the functions and that each function has a single job to do.
* For each case use the same filename just add at the end: **with_functions.py**

## Exercise: Number guessing - functions
{id: exercise-number-guessing-game-with-functions}

Take the number guessing game from the earlier chapter and move the internal while() loop
to a function.


## Solution: statistics
{id: solution-statistics}

![](examples/functions/stats.py)

## Solution: Pascal triangle
{id: solution-pascal-triangle}

![](examples/functions/pascal_triangle.py)

## Solution: recursive
{id: solution-recursive}

![](examples/functions/dependencies/traversing_dependency_tree.py)

## Solution: Tower of Hanoi
{id: solution-tower-of-hanoi-recursive}

![](examples/functions/tower_recursive.py)
![](examples/functions/tower.py)

## Solution: Merge and Bubble sort
{id: solution-bubble-sort}

![](examples/functions/bubble_sort.py)

![](examples/functions/iterative_bubble_sort.py)

![](examples/functions/recursive_bubble_sort.py)

