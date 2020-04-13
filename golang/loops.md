# Loops
{id: loops}


## 3-part for loop
{id: 3-part-for-loop}
{i: for}

![](examples/for-loop/for.go)
![](examples/for-loop/for.out)

## while-like for loop
{id: while}
{i: while}

![](examples/while/while.go)
![](examples/while/while.out)


## infinite loop
{id: infinite-loop}

* You don't have to put a condition in the `for` loop, but that will create an infinite loop.
* If you happen to run this on the command line, you can press Ctrl-C to stop this program. 
* In this case you will need to use `break` or some other way to exit the loop.

![](examples/infinite-loop/infinte_loop.go)

![](examples/infinite-loop/infinte_loop.out)

## break out from loop
{id: break}
{i: break}


![](examples/break-loop/break_loop.go)
![](examples/break-loop/break_loop.out)


## continue
{id: continue}
{i: continue}

![](examples/continue/continue.go)
![](examples/continue/continue.out)


## loop on two variables
{id: loop-on-two-variables}


![](examples/loop-on-two/loop_on_two.go)
![](examples/loop-on-two/loop_on_two.out)


## break out from internal loop (labels)
{id: break-out-from-internal-loop}

![](examples/for-label/for_label.go)


## Exercise: One-dimensional spacefight
{id: exercise-one-dimensional-spacefight}

The game have several levels. Solve them one after the other.

* The computer "thinks" about a random integer between 1 and 20 then asks the player. The player types in an integer. The computer says if it is too small, to big, or direct hit.
* The user can guess multiple times. Exit only when there was a direct hit.
* The user can enter x any time and quite the game.
* The user can enter p any time and the hidden value is printed (cheating)
* Allow the user to change the game to "move" mode by typing "m". In this mode after every guess after we compared the values change the hidden number by -2, -1, 0, 1, or 2.
* If the user enters "d" we switch to the "debug-mode" of the game. In this mode, before every turn we print the current hidden value.

## Exercise: FizzBuzz
{id: exercise-fizzbuzz}

Write a program that prints the numbers from 1 to 100.
For multiples of 3 print "Fizz" instead of the number. For multiples of 5 print "Buzz". For
numbers which are multiples of both three and five print "FizzBuzz".


Expected output:

![](examples/fizzbuzz-main/fizzbuzz_main.out)


## Solution: One-dimensional spacefight - multiple guesses till hit
{id: solution-one-dimensinal-spacefight-multiple-guesses}

![](examples/game2/game2.go)

## Solution: One-dimensional spacefight - allow x
{id: solution-one-dimensional-spacefight-allow-x}

![](examples/game3/game3.go)

## Solution: One-dimensional spacefight - allow m
{id: solution-one-dimensiona-spacefight-allow-m}

![](examples/game5/game5.go)

## Solution: FizzBuzz
{id: solution-fizzbuzz}

![](examples/fizzbuzz-main/fizzbuzz_main.go)
