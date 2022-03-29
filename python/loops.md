# Loops
{id: python-loops}

## Loops: for-in and while
{id: for-while-loops}

* **for in** - to iterate over a well defined list of values. (characters, range of numbers, shopping list, etc.)
* **while** - repeat an action till some condition is met. (or stopped being met)



## for-in loop on strings
{id: for-loop-on-strings}
{i: for}

![](examples/loops/for.py)
![](examples/loops/for.out)


## for-in loop on list
{id: for-loop-on-list-sample}
{i: for}

![](examples/loops/for_list.py)
![](examples/loops/for_list.out)


## for-in loop on range
{id: for-loop-on-range}
{i: range}

![](examples/loops/for_range.py)
![](examples/loops/for_range.out)


## Iterable, iterator
{id: iterable}

* [iterable](https://docs.python.org/glossary.html#term-iterable)



## for in loop with early end using break
{id: for-break}
{i: break}

![](examples/loops/for_break.py)
![](examples/loops/for_break.out)


## for in loop skipping parts using continue
{id: for-continue}
{i: continue}

![](examples/loops/for_continue.py)
![](examples/loops/for_continue.out)


## for in loop with break and continue
{id: for-break-continue}

![](examples/loops/for_break_continue.py)
![](examples/loops/for_break_continue.out)

## while loop
{id: while-loop}
{i: while}

![](examples/loops/while.py)
![](examples/loops/while.out)


## Infinite while loop
{id: infinite-while-loop}
{i: while}

![](examples/loops/while_infinite.py)
![](examples/loops/while_infinite.out)

* Don't do this!
* Make sure there is a proper end-condition. (exit-condition)
* Use Ctrl-C to stop it

## While with complex expression
{id: while-complex-expression}

![](examples/loops/while_complex_condition.py)
![](examples/loops/while_complex_condition.out)


## While with break
{id: while-with-break}

![](examples/loops/while_break.py)
![](examples/loops/while_break.out)


## While True
{id: while-true}

![](examples/loops/while_true.py)
![](examples/loops/while_true.out)


## Duplicate input call
{id: duplicate-input-call}

![](examples/loops/duplicate_input_call.py)

## Eliminate duplicate input call
{id: eliminate-duplicate-input-call}

![](examples/loops/single_input_call.py)


## do while loop
{id: do-while-loop}
{i: do while}

There is no `do ... while` in Python but we can write code like this to have similar effect.

![](examples/loops/do_while.py)


## while with many continue calls
{id: while-many-continue}
{i: continue}

![](examples/loops/infinite_while_continue.py)


## Break out from multi-level loops
{id: break-from-multi-level-loops}

Not supported in Python. "If you feel the urge to do that, your code is probably too complex. Create functions!"

## For-else
{id: for-break-or-else}

The `else` part will be executed if the loop finished all the iterations without calling `break`.

![](examples/loops/for-else.py)
![](examples/loops/for-else.out)


## Exit vs return vs break and continue
{id: exit-return-break}
{i: exit}
{i: return}
{i: break}
{i: continue}

* **exit** will stop your program no matter where you call it.
* **return** will return from a function (it will stop the specific function only)
* **break** will stop the current "while" or "for" loop
* **continue** will stop the current iteration of the current "while" or "for" loop



## Exercise: Print all the locations in a string
{id: exercise-print-all-the-locations}

* Create a file called **location_in_string.py**
* Given a string like "The black cat climbed the green tree.", print out the location of every "c" character.

Expected:

```
7
10
14
```

## Exercise: Number guessing game
{id: exercise-number-guessing-game}

Level 0

* Create a file called **number_guessing_game_0.py**
* Using the random module the computer "thinks" about a whole number between 1 and 20.
* The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
* The game ends after just one guess.

Level 1

* Create a file called **number_guessing_game_1.py**
* The user can guess several times. The game ends when the user guessed the right number.

Level 2

* Create a file called **number_guessing_game_2.py**
* If the user hits 'x', we leave the game without guessing the number.

Level 3

* Create a file called **number_guessing_game_3.py**
* If the user presses 's', show the hidden value (cheat)

Level 4

* Create a file called **number_guessing_game_4.py**
* Soon we'll have a level in which the hidden value changes after each guess. In order to make that mode easier to track and debug, first we would like to have a "debug mode".
* If the user presses 'd' the game gets into "debug mode": the system starts to show the current number to guess every time, just before asking the user for new input.
* Pressing 'd' again turns off debug mode. (It is a toggle each press on "d" changes the value to to the other possible value.)

Level 5

* Create a file called **number_guessing_game_5.py**
* The 'm' button is another toggle. It is called 'move mode'. When it is 'on', the hidden number changes a little bit after every step (+/-2). Pressing 'm' again will turn this feature off.

Level 6

* Create a file called **number_guessing_game_6.py**
* Let the user play several games.
* Pressing 'n' will skip this game and start a new one. Generates a new number to guess.



## Exercise: Count unique characters
{id: exercise-count-unique}

* Create file called **count_unique_characters.py**
* Given a string on the command line, count how many different characters it has.

```
python count_unique.py abcdaaa
4
```

## Exercise: Convert for-loop to while-loop
{id: exercise-convert-for-loop-to-while-loop}

* Update the following file.
* Given a for-loop as in the following code, convert it to be using a while-loop.

* Range with 3 parameters: from the first number, till the second number, with step the 3rd number range(from, to, step)

![](examples/loops/using_for_loop.py)
![](examples/loops/using_for_loop.out)


## Solution: Print all the locations in a string
{id: solution-print-all-the-locations}

{aside}
When you start thinking about this exercise, you probably call `loc = text.find("c")` and then you wonder how could you find the next element.
After a while it might occur to you that the `find` method can get a second parameter to set the location where we start the search.

Basically you need to call `loc = text.find("c", loc + 1)` but that looks strange. How can you use `loc` (as a parameter of the function) and also
assign to it. However programming languages don't have a problem with this as the assignment happens after the right-hand-side was fully executed.

The problem that now you have two different calls to `find`. The first one and all the subsequent calls.

How could we merge the two calls?

The trick is that you need to have an initial value for the `loc` variable and it has to be -1, so when we call `find` for the first time,
it will start from the first character (index 0).
{/aside}

![](examples/loops/find_loop_one.py)

{aside}
Using an additional variable might make the code easier to read:
{/aside}

![](examples/loops/find_loop.py)


## Solution 1 for Number Guessing
{id: solution-1-number-guessing}

![](examples/loops/number1.py)

## Solution 2 for Number Guessing (x)
{id: solution-2-number-guessing}

{aside}
The main trick is that you check for the input being "x" **before** you try to convert it to an integer.
{/aside}

![](examples/loops/number2.py)


## Solution 3 for Number Guessing (s)
{id: solution-3-number-guessing}

![](examples/loops/number3.py)

## Solution for Number Guessing (debug)
{id: solution-4-number-guessing}

{aside}
One important thing is to remember that you can create a toggle by just calling `not` on a boolean variable every time you'd like to flip the switch.

The other one is that flipping the switch (pressing d) and printing the current value because debug mode is on, are two separate operations that are not directly related
and so they can be implemented separately.
{/aside}


![](examples/loops/number_debug.py)


## Solution for Number Guessing (move)
{id: solution-5-number-guessing}

![](examples/loops/number_move.py)


## Solution for Number Guessing (multi-game)
{id: solution-6-number-guessing}

![](examples/loops/number_multi.py)


## Solution: Count unique characters
{id: solution-count-unique}
{i: set}

![](examples/loops/number_of_different.py)

{aside}
The above solution works, but there is a better solution using sets that we have not learned yet. Nevertheless, let me show you that solution:
{/aside}


![](examples/loops/number_of_different_set.py)


## Solution: Convert for-loop to while-loop
{id: solution-convert-for-loop-to-while-loop}

![](examples/loops/using_while_loop.py)


