# Functions and Subroutines
{id: subroutines}





## Why to use subroutines?
{id: why-use-subroutines}


We use subroutines in order to



* make the script more modular
* reuse code for repeated tasks
* easier to debug
* easier to maintain



## Subroutines
{id: subroutines-introduction}
{i: sub}
{i: subroutines}
{i: functions}
{i: return}
![](examples/subroutines/subroutines.pl)

* no prototypes needed
* no signature
* parentheses are optional
* functions always return a value



## Variable number of parameters
{id: subroutines-sum}
![](examples/subroutines/sum.pl)


<a href="https://perlmaven.com/subroutines-and-functions-in-perl">Subroutines and functions in Perl</a>




## Recursive subroutines: factorial
{id: recursive-subroutines}
{i: recursive}


Mathematical definition of factorial:



```
n! = n * (n-1) * (n-2) * ... 1

1! = 1
n! = n * (n-1)!
```
![](examples/subroutines/factorial.pl)


## Recursive subroutines: Fibonacci
{id: recursive-subroutines-fibonacci}


Recursive definition of Fibonacci



```
f(1) = 1
f(2) = 1
f(n) = f(n-1) + f(n-2)
```
![](examples/subroutines/fibonacci_recursive.pl)


## Sort using a function
{id: sorting-function}
![](examples/subroutines/sort_with_function.pl)


## Return a list
{id: return-a-list}
{i: return|list}

```
Perl allows us to return any number of values.
```
![](examples/subroutines/fibonacci.pl)


## Return several elements
{id: return-several-elements}
![](examples/subroutines/calc.pl)


## Error handling with eval - files
{id: error-handling-with-eval-files}
{i: eval {};}
{i: die|catching}
{i: try|eval}

* **die** - raise exception or throw exception
* **eval** - catch exception - **try** in other languages)


![](examples/subroutines/eval_files.pl)


## Error handling with eval - two calls
{id: error-handling-with-eval}
![](examples/subroutines/eval.pl)


## Exercise: Subroutines
{id: exercise-subroutines}


Take the solution from the subroutines chapter (examples/files/statistics.pl)
and move the code in a subroutine called main()




Take the solution from the subroutines chapter ( examples/files/write_report_to_file.pl )
and create 3 subroutines. read_file() and write_file() for the two main parts of the script
and main() that will call these two subroutines.




Take ( examples/arrays/color_selector.pl ) and create two functions. One that handles the case
when the user provided a value on the command line, and another function that shows the menu and
accepts the value from there. Maybe also add a main() function to wrap the rest of the code as well.




## Exercise: Number guessing in sub
{id: exercise-number-guessing-in-sub}

```
Take the solution of the improved number guessing game
from examples/arrays/number_guessing.pl
and change it so some parts of it will be functions.

Specifically you can create subs for
1) the moving of the spaceship
2) checking the hit
   How would you indicate the need to 'last' from within the function?
```


## Solution: Number guessing in sub
{id: solution-number-guessing-in-sub}
![](examples/subroutines/number_guessing.pl)




