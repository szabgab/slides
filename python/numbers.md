# Numbers
{id: python-numbers}

## Numbers
{id: numbers}

![](examples/numbers/numbers.py)

{aside}
In Python numbers are stored as decimals, but in the source code you can also use hexadecimal, octal, or binary notations.
This is especially useful if the domain you are programming in is using those kinds of numbers.
For example hardware engineers often talk in hexadecimal values.
In that case you won't need to contantly translate between the form used in the current domain and decimal numbers.
{/aside}


## Operators for Numbers
{id: operators-for-numbers}
{i: +=}
{i: -=}
{i: **}
{i: ++}
{i: --}
{i: %}
{i: /}
{i: //}

![](examples/numbers/operators.py)

There is no autoincrement (++) and autodecrement (--) in Python,
because they can be expressed by += 1 and -= 1 respectively.


## Integer division and the __future__
{id: integer-division}
{i: __future__}

![](examples/basics/divide.py)

```
$ python divide.py
1

$ python3 divide.py
1.5
```

![](examples/basics/future_divide.py)

{aside}
If you need to use Python 2, remember that by default division is integer based so 3/2 would return 1.
Importing the 'division' directive from __future__ changes this to the behavior that we usually expect 3/2 being 1.5.
This is also the behavior we have in Python 3.
In case you already use Python 3 and would like to get the "old" behavior, that is to get the integer part of the division, you can
always call the "int" function: int(b/a).
{/aside}


## Pseudo Random Number (unform distribution)
{id: random}
{i: random}

![](examples/numbers/rand.py)

* [random](http://docs.python.org/library/random.html)
* [Pseudo random generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
* Uniform distribution between 0-1


## Fixed random numbers
{id: random-seed}
{i: random}
{i: seed}

![](examples/numbers/random_seed.py)


## Rolling dice - randrange
{id: random-dice}
{i: randrange}
![](examples/numbers/rolling_dice.py)


## Random choice
{id: random-choice}
{i: choice}
![](examples/numbers/random_choice.py)



## built-in method
{id: built-in-method}

* A common mistake. Not calling the method.

![](examples/numbers/get_random.py)

{aside}

When you see a string like the above "built-in method ..." you can be almost certainly sure that you have forgotten the parentheses
at the end of a method call.
{/aside}


## Exception: TypeError: 'module' object is not callable
{id: exception-module-object-is-not-callable}

* A common mistake. Calling the class and not the method.

![](examples/numbers/rnd.py)
![](examples/numbers/rnd.err)


## Fixing the previous code
{id: random-code-fixed}
![](examples/numbers/rnd_fixed.py)
![](examples/numbers/rnd_fixed_again.py)


## Exception: AttributeError: module 'random' has no attribute
{id: exception-attributeerror-module-has-no-attribute}

* A common mistake. Using the wrong filename.


This works fine:

![](examples/my/random.py)

This gives an error

![](examples/my/rnd.py)
![](examples/my/rnd.err)

{aside}

Make sure the names of your files are not the same as the names of any of the python packages.
{/aside}


## Exercise: Number guessing game - level 0
{id: exercise-number-guessing-game-0}

Level 0

* Create a file called **number_guessing_game_0.py**
* Using the random module the computer "thinks" about a whole number between 1 and 20.
* The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if it was the same.
* The game ends after just one guess.

Level 1-

* Other levels in the next chapter.

## Exercise: Fruit salad
{id: exercise-fruit-salad}

* Write a script called **fruit_salad.py** based on the following skeleton, that will pick 3 fruits from a list of fruits like the one we had in one of the earlier slides. Print the 3 names.
* Could you make sure the 3 fruits are different?

* Use the following skeleton:

![](examples/numbers/skeleton_fruit_salad.py)


## Solution: Number guessing game - level 0
{id: solution-number-guessing-game-0}

![](examples/numbers/number0.py)

## Solution: Fruit salad
{id: solution-fruit-salad}
{i: random}
{i: sample}

![](examples/numbers/fruit_salad.py)

* [random.sample](https://docs.python.org/3/library/random.html#random.sample)


