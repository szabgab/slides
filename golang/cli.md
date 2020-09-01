# CLI
{id: cli}

## Args - (argv) command line arguments
{id: args-command-line-arguments}
{i: Args}
{i: os.Args}

{aside}
os.Args is a slice of strings (we'll talk about slices in later in detail) that contains the values on the command line.

The first element of this slice (index 0) is the path to the executable. If we run this using `go run` then it
will be some strange-looking temporary location.

`len` gives us the number of elements on the command line that will be 1 if there are no parameters on the command line.

Using a square-bracket after the name `os.Args` allows us to access the specific elements in the slice.

Later we'll learn higher level abstractions to read command line parameters, but for now this will be enough.
{/aside}

![](examples/cli/cli.go)

```
go run examples/cli/cli.go  hello world
```

![](examples/cli/cli.out)

## Exit early with exit code
{id: exit-early}
{i: Exit}
{i: os.Exit}

{aside}
In the earlier examples our code stopped running when the last statement in the main function was executed.
This is usually the normal way for your code to end, but there can be various circumstances when you want your program to
stop running even before it reaches the last statement. You can do this by calling the `os.Exit()` function.

You will also have to pass a number to this function which is going to be the exit-code of your program.
If you did not explicitly call `os.Exit()` then go will automatically set the exit-code to be 0. That means success.

In general exit-code 0 means success. Any other number indicates failure. Which number indicates which failure is totally up to
you as a programmer.

The exit code is not printed anywhere on the screen, it is sort-of invisible, but the user of your program can check it by looking at
the value of the `$?` variable on Unix/Linux/Mac systems, or the `%ERRORLEVEL%` variable on MS Windows systems.
{/aside}

![](examples/exit/code.go)

```
echo $0
echo %ERRORLEVEL%
```


## Exercise: rectangular
{id: exercise-rectangular}

Write a program that accepts two numbers on the command line
(the width and the length of a rectangular) and prints the area.

For example:

```
$ go run rectangular.go 3 4
12
```

## Exercise: calculator
{id: ecxercise-calculator}

Write a command-line calculator that works with the 4 basic operators `+-*/` like this:

```
$ go run cacl.go 3 + 4
7

$ go run calc.go 8 / 2
4
```

* Does multiplication also work?
* What happens if we try to divide by 0?


## Solution: rectangular CLI
{id: solution-rectangular}

![](examples/rectangular/rectangular.go)

## TODO: Solution: calculator CLI
{id: solution-calculator-if}

![](examples/calc-with-if/calc_with_if.go)

## TODO: Solution: calculator (switch)
{id: solution-calculator-switch}

![](examples/calc-with-switch/calc_with_switch.go)

* implicit break! (no fall-through)
