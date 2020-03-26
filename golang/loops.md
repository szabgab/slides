# Loops
{id: loops}


## 3-part for loop
{id: 3-part-for-loop}
{i: for}

![](examples/for-loop/for.go)

## while-like for loop
{id: while}
{i: while}

![](examples/while/while.go)


## infinite loop
{id: infinite-loop}

* You don't have to put a condition in the `for` loop, but that will create an infinite loop.
* In this case you will need to use `break` or some other way to exit the loop.

![](examples/infinite-loop/infinte_loop.go)

## break out from loop
{id: break}
{i: break}


![](examples/break-loop/break_loop.go)


## continue
{id: continue}
{i: continue}

![](examples/continue/continue.go)


## Exercise: Number Guessing game
{id: number-guessing-game}

The exercise have several levels. Solve them one after the other.

* The computer "thinks" about a random integer between 1 and 20 then asks the player. The player types in an integer. The computer says if it is too small, to big, or direct hit.
* The user can guess multiple times. Exit only when there was a direct hit.
* The user can enter x any time and quite the game.
* The user can enter p any time and the hidden value is printed (cheating)
* Allow the user to change the game to "move" mode by typing "m". In this mode after every guess after we compared the values change the hidden number by -2, -1, 0, 1, or 2.
* If the user enters "d" we switch to the "debug-mode" of the game. In this mode, before every turn we print the current hidden value.


## Solution: Number Guessing game - multiple guesses till hit
{id: solution-number-guessing-game-multiple-guesses}

![](examples/game2/game2.go)

## Solution: Number Guessing game - allow x
{id: solution-number-guessing-game-allow-x}

![](examples/game3/game3.go)

## Solution: Number Guessing game - allow m
{id: solution-number-guessing-game-allow-m}

![](examples/game5/game5.go)


