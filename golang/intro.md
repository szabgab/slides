# Introduction to Go-lang
{id: intro}

## Features
{id: features}

* Built-in concurrency
* Compile to standalone binaries (cross compilation available!)

* Strong and statically typed
* Simplicity
* Fast compile times
* Garbage collected

## Why Golang?
{id: why-golang}


* Concurrency [The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software](http://www.gotw.ca/publications/concurrency-ddj.htm)
* [C10k Problem](https://en.wikipedia.org/wiki/C10k_problem)


## Major Open Source Projects
{id: major-open-source-projects}

* [Docker](https://github.com/docker)
* [Kubernetes](https://github.com/kubernetes/kubernetes)
* [Terraform](https://github.com/hashicorp/terraform)

* [Go topic on GitHub](https://github.com/topics/go)
* [Trending Go projects](https://github.com/trending/go?since=monthly)


## Some companies in Israel
{id: companies-in-israel}

* [Gett](https://gett.com/)
* [Apester](https://apester.com/)
* [Cisco](https://www.cisco.com/)


## Install
{id: install}

* [Golang home](https://golang.org/)
* [Download](https://golang.org/dl/)


## Version
{id: version}
{i: version}

```
go version
```


## Editor/IDE
{id: editor}
{i: editor}
{i: IDE}

* [Visual Studio Code](https://code.visualstudio.com/) (It has plugins for Golang)
* [Other editors and IDEs](https://golang.org/doc/editors.html)


## Hello World
{id: hello-world}
{i: package}
{i: main}
{i: import}
{i: func}
{i: run}
{i: build}
{i: fmt}

![](examples/hello_go/hello_world.go)

* main function is the entry point of every program

{aside}
Every Go program has a main file that must start with "package main" and it must have a function called `main`.

In order to print something to the screen we first need to import the `fmt` class and then inside the "main" function we can write
`fmt.Println("Hello World")`.

We save this with a .go extension. Then we can run it from the command line by typing `go run` and the name of your file.
This will compile the code into a temporary directory and then run it.


If you'd like to crete a distributable version of your code you can type `go build` and the name of your file. That will create an executable
with the same name (just without the extension). This is specific to the Operating System and platform you currently use. Later we'll see how 
{/aside}

```
go run hello_world.go
```

![](examples/hello_go/hello_world.out)


* [fmt.Print](https://golang.org/pkg/fmt/#Print)

```
go build hello_world.go
./hello_world
```

* [Annotated Hello World in Go](https://www.353solutions.com/annotated-go)

## Hello Foo - Println
{id: hello-foo}
{i: Println}
{i: var}

![](examples/hello_foo/hello_foo.go)
![](examples/hello_foo/hello_foo.out)

## Hello Foo - Printf
{id: hello-foo-printf}
{i: Printf}

![](examples/hello_foo_printf/hello_foo_printf.go)
![](examples/hello_foo_printf/hello_foo_printf.out)


## Scan input strings from STDIN
{id: scan}
{i: STDIN}
{i: Scan}

![](examples/scan/scan.go)

* [fmt.Scan](https://golang.org/pkg/fmt/#Scan)

## Args - (argv) command line arguments
{id: args-command-line-arguments}


![](examples/cli/cli.go)

```
go run examples/cli/cli.go  hello world
```

## Comments
{id: comments}
{i: //}

![](examples/comments/comments.go)
![](examples/comments/comments.out)

## Enforce variables types
{id: enforce-variable-types}

![](examples/variable/variable.go)
{i: var}

```
# command-line-arguments
./variable.go:8:7: cannot use 42 (type int) as type string in assignment
```

* Compile-time error

## Basic Types
{id: basic-types}
{i: string}
{i: int}
{i: uint}
{i: float}
{i: bool}
{i: byte}
{i: real}
{i: complex}
{i: imag}


```
string          (any utf-8 character)

int - unspecified size (but mn 32 bit)
int8
int16
int32
int64

uint16          (unsigned integer)

float32
float64

bool

byte

complex(r, i)
complex64       1 + 2i    or just 3i
complex128
real(n)
imag(n)
```

* [basic types](https://tour.golang.org/basics/11)

## Show inferred variable type - Printf %T
{id: show-variable-type}
{i: %T}

![](examples/show-type/show-type.go)


## Variable declaration (var)
{id: variable-declaration}
{i: var}

![](examples/variables/variables.go)


## Converting values to other types - float32, int, string
{id: converting-types}
{i: float32()}
{i: int()}
{i: string()}

* float32()
* int()
* string()

![](examples/convert/convert.go)
      // this will convert a string like "abc" or "2x" to 0 and set err

## Converting strings to numbers - strconv, ParseFloat, Atoi, Itoa
{id: converting-strings-to-numbers}

![](examples/convert-string/convert-string.go)

* [strconv](https://golang.org/pkg/strconv/)

## Boolean values - bool, true, false
{id: boolean-values}

![](examples/go-boolean/boolean.go)

## Default values of variables
{id: default-values}

Variables declared without an explicit initial value are given their zero value as default.

* 0 for numeric types,
* false for the boolean type, and
* "" (the empty string) for strings.

![](examples/zero/zero.go)


## Integer-based operations
{id: integer-based-operations}

7/3  is 2 in Go as type does not change during operation
7%3  remainder



## if statement
{id: if-statement}

![](examples/if/if.go)

## if, else, else if
{id: if-else-statements}

```
if cond {
}

if cond {
} else {
}


if cond {
} else if cond {
} else {
}
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


## Solution: rectangular
{id: solution-rectangular}

![](examples/rectangular/rectangular.go)

## Solution: calculator
{id: solution-calculator-if}

![](examples/calc-with-if/calc.go)

## Solution: calculator (switch)
{id: solution-calculator-switch}

![](examples/calc-with-switch/calc.go)

* implicit break! (no fall-through)

