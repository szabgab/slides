# Functions (subroutines)
{id: python-functions}

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


## Defining a function
{id: functions}
{i: def}
![](examples/functions/params.py)

{aside}
Positional parameters.
{/aside}



## Parameters can be named
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



## Default values
{id: parameter-with-default-values}
![](examples/functions/default.py)

{aside}

Function parameters can have default values. In such case the parameters are optional.
In the function declaration, the parameters with the default values must come last.
In the call, the order among these arguments does not matter, and they are optional anyway.
{/aside}


## Several defaults, using names
{id: defaults-with-names}
{i: non-keyword arg after keyword arg}

{aside}
Parameters with defaults must come at the end of the parameter declaration.
{/aside}

![](examples/functions/named_params_and_defaults.py)

{aside}

There can be several parameters with default values.
They are all optional and can be given in any order after the positional arguments.
{/aside}


## Arbitrary number of arguments
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
The *numbers argument can be preceded by any number of regular arguments
{/aside}

![](examples/functions/super.py)
![](examples/functions/super.py.out)


## Extra key-value pairs in parameters
{id: kw-value-pairs}
{i: **kwargs}
![](examples/functions/kw.py)


## Every parameter option
{id: every-parameter-option}
![](examples/functions/full.py)



## Duplicate declaration of functions (multiple signatures)
{id: duplicate-declaration}
![](examples/functions/duplicate_add.py)

The second declaration silently overrides the first declaration.


[pylint](http://www.pylint.org/) can find such problems, along with a bunch of others.



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



## Exercise: statistics
{id: exercise-statistics}

Write a function that will accept any number of numbers and return a list of values:



* The sum
* Average
* Minimum
* Maximum



## Exercise: recursive
{id: exercise-recursive}


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


## Solution: statistics
{id: solution-statistics}
![](examples/functions/stats.py)


## Exercise: recursive
{id: solution-recursive}
![](examples/functions/dependencies/traversing_dependency_tree.py)



