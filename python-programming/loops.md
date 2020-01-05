# Loops
{id: python-loops}

## Loops: for-in and while
{id: for-while-loops}

* **for in** - to iterate over a well defined list of values. (characters, range of numbers, shopping list, etc.)
* **while** - repeate an action till some condition is met. (or stopped being met)



## for-in loop on strings
{id: for-loop-on-strings}
{i: for}
![](examples/strings/for.py)
![](examples/strings/for.out)


## for-in loop on list
{id: for-loop-on-list-sample}
{i: for}
![](examples/strings/for_list.py)
![](examples/strings/for_list.out)


## for-in loop on range
{id: for-loop-on-range}
{i: range}
![](examples/strings/for_range.py)
![](examples/strings/for_range.out)


## Iterable, iterator
{id: iterable}

* [iterable](https://docs.python.org/3/glossary.html#term-iterable)



## for in loop with early end using break
{id: for-break}
{i: break}
![](examples/strings/for_break.py)
![](examples/strings/for_break.out)


## for in loop skipping parts using continue
{id: for-continue}
{i: continue}
![](examples/strings/for_continue.py)
![](examples/strings/for_continue.out)


## for in loop with break and continue
{id: for-break-continue}
![](examples/strings/for_break_continue.py)
![](examples/strings/for_break_continue.out)


## while loop
{id: while-loop}
{i: while}
![](examples/strings/while.py)
![](examples/strings/while.out)



## Infinite while loop
{id: infinite-while-loop}
{i: while}
![](examples/strings/while_infinite.py)
![](examples/strings/while_infinite.out)

* Don't do this!
* Make sure there is a proper end-condition. (exit-condition)
* Use Ctrl-C to stop it



## While with complex expression
{id: while-complex-expression}
![](examples/strings/while_complex_condition.py)


## While with break
{id: while-with-break}
![](examples/strings/while_break.py)


## While True
{id: while-true}
![](examples/strings/while_true.py)


## Duplicate input call
{id: duplicate-input-call}
![](examples/strings/duplicate_input_call.py)


## Eliminate duplicate input call
{id: eliminate-duplicate-input-call}
![](examples/strings/single_input_call.py)


## do while loop
{id: do-while-loop}
{i: do while}


There is no <b>do ... while</b> in Python but we can write code like this to have similar effect.


![](examples/strings/do_while.py)


## while with many continue calls
{id: while-many-continue}
{i: continue}
![](examples/strings/infinite_while_continue.py)


## Break out from multi-level loops
{id: break-from-multi-level-loops}

Not supported in Python. "If you feel the urge to do that, your code is probably too complex. create functions!"



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

Given a string like "The black cat climbed the green tree.", print out the location of every "c" charcater.



## Exercise: Number guessing game
{id: exercise-number-guessing-game}

Level 0


* Using the random module the computer "thinks" about a whole number between 1 and 20.
* The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
* The game ends after just one guess.



Level 1


* The user can guess several times. The game ends when the user guessed the right number.



Level 2


* If the user hits 'x', we leave the game without guessing the number.



Level 3


* If the user presses 's', show the hidden value (cheat)
* If the user presses 'd' the game gets into debug mode: the system starts to show the current number to guess every time, just before asking the user for new input. Pressing 'd' again turns off debug mode. (It is a toggle.)



Level 4


* The 'm' button is another toggle. It is called 'move mode'. When it is 'on', the hidden number changes a little bit after every step (+/-2). Pressing 'm' again will turn this feature off.



Level 5


* Let the user play several games.
* Pressing 'n' will skip this game and start a new one. Generates a new number to guess.



## Exercise: MasterMind
{id: exercise-mastermind}

Implement the MasterMind game.

The computer "thinks" a number with 4 different digits.
You guess which digits. For every digit that matched both
in value, and in location the computer gives you a *. For every
digit that matches in value, but not in space the computer gives
you a +. Try to guess the given number in as few guesses as possible.



```
Computer: 2153
You:      2467  *
You:      2715  *++
```


## Exercise: Count unique characters
{id: exercise-count-unique}

Given a string on the command line, count how many differnt characters it has.


```
python count_unique.py abcdaaa
4
```



## Solution: Print all the locations in a string
{id: solution-print-all-the-locations}
![](examples/strings/find_loop.py)


## Solution 1 for Number Guessing
{id: solution-1-number-guessing}
![](examples/strings/number1.py)


## Solution for Number Guessing (debug)
{id: solution-2-number-guessing}
![](examples/strings/number_debug.py)


## Solution for Number Guessing (move)
{id: solution-3-number-guessing}
![](examples/strings/number_move.py)


## Solution for Number Guessing (multi-game)
{id: solution-4-number-guessing}
![](examples/strings/number_multi.py)


## Solution: MasterMind
{id: solution-mastermind}
![](examples/lists/master_mind.py)


## Solution: Count unique characters
{id: solution-count-unique}
![](examples/strings/number_of_different.py)
![](examples/strings/number_of_different_set.py)


## MasterMind to debug
{id: mastermind-to-debug}

Debug the following version of the MasterMind game.

![](examples/loops/MasterMind_to_debug.py)


