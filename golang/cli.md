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
