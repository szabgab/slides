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

## Go Designed by
{id: go-designed-by}

* [Robert Griesemer](https://github.com/griesemer)
* [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike)
* [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson)

* At Google

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
* [Trending Go projects on Github](https://github.com/trending/go?since=monthly)


* [Directory of Open Source Projects in Go](https://github.com/golang/go/wiki/Projects)

## Some companies in Israel
{id: companies-in-israel}

* [Gett](https://gett.com/)
* [Apester](https://apester.com/)
* [Cisco](https://www.cisco.com/)


## Install Golang
{id: install}

* [Golang home](https://golang.org/)
* [Download](https://golang.org/dl/)


## Show Installed Version of Golang
{id: version}
{i: version}


* In the CMD window of MS Windows or in your Linux/Mac terminal type:

```
go version
```


## Editor/IDE for Golang
{id: editor}
{i: editor}
{i: IDE}

* [Visual Studio Code](https://code.visualstudio.com/) (It has plugins for Golang)
* [Other editors and IDEs](https://golang.org/doc/editors.html)
* Any text editor

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

```
go run hello_world.go
```

![](examples/hello_go/hello_world.out)

* main function is the entry point of every program
* [fmt.Print](https://golang.org/pkg/fmt/#Print)

{aside}
Every Go program has a main file that must start with "package main" and it must have a function called `main`.

In order to print something to the screen we first need to import the `fmt` class and then inside the "main" function we can write
`fmt.Println("Hello World")`.

We save this with a .go extension. Then we can run it from the command line by typing `go run` and the name of your file.
This will compile the code into a temporary directory and then run it.
{/aside}


## Build Hello World exe
{id: build-hello-world}

{aside}
If you'd like to crete a distributable version of your code you can type `go build` and the name of your file. That will create an executable
with the same name (just without the extension). This is specific to the Operating System and platform you currently use. Later we'll see how 
{/aside}


```
go build hello_world.go
./hello_world
```

* [Annotated Hello World in Go](https://www.353solutions.com/annotated-go)


## Exercise: Hello World
{id: exercise-hello-world}


* Install go if you don't have it yet
* Install an editor/IDE with the appropriate plugin for go
* Check if `go version` is running
* Write the Hello World program and run it both from the IDE and from the command line
 

## Hello Foo - Println
{id: hello-foo}
{i: Println}
{i: var}

![](examples/hello_foo/hello_foo.go)
![](examples/hello_foo/hello_foo.out)

## Hello Bar - Printf
{id: hello-bar-printf}
{i: Printf}

![](examples/hello_foo_printf/hello_foo_printf.go)
![](examples/hello_foo_printf/hello_foo_printf.out)

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
{i: Printf}
{i: %T}

![](examples/show-type/show-type.go)


## Variable declaration (var)
{id: variable-declaration}
{i: var}

* There are 3 ways to declare variables

![](examples/variables/variables.go)

## Default values of variables
{id: default-values}

Variables declared without an explicit initial value are given their zero value as default.

* 0 for numeric types,
* false for the boolean type, and
* "" (the empty string) for strings.

![](examples/zero/zero.go)


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
{i: strconv}
{i: Atoi}
{i: Itoa}
{i: ParseFloat}

![](examples/convert-string/convert-string.go)

* [strconv](https://golang.org/pkg/strconv/)



## Scan input strings from STDIN
{id: scan}
{i: STDIN}
{i: Scan}

![](examples/scan/scan.go)

* [fmt.Scan](https://golang.org/pkg/fmt/#Scan)

## if statement
{id: if-statement}

![](examples/if/if.go)


## Error Handling
{id: error-handling}

* functions return the error value

## Scan STDIN convert to number
{id: scan-stdin-convert-to-number}
{i: Scan}
{i: Atoi}
{i: ParseFloat}
{i: Exit}

![](examples/scan-stdin/scan_stdin_convert.go)


## Comments
{id: comments}
{i: //}

![](examples/comments/comments.go)
![](examples/comments/comments.out)






## Exercise: rectangular STDIN
{id: exercise-rectangular-scan-stdin}

Write a program that asks the user for two numbers on STDIN
(the width and the length of a rectangular) and prints the area and the circumference.

For example:

```
$ go run rectangular.go
width: 3
length: 4
Area: 12
Circumference: 14
```

## Exercise: circle STDIN
{id: exercise-circle-scan-stdin}

Write a program that asks the user for a number the radius of a circle and prints out the area and the circumference of the circle.

```
go run circle.go
radius: 2
Area: 
Circumference:
```

## Exercise: calculator STDIN
{id: ecxercise-calculator-stdin}

Write a command-line calculator that works with the 4 basic operators `+-*/` like this:

```
$ go run cacl.go
a: 3
op: +
b: 4
7

$ go run calc.go
a: 8
op: /
b: 2
4
```

* Does multiplication also work?
* What happens if we try to divide by 0?


## Solution: rectangular STDIN
{id: solution-rectangular-scan-stdin}

![](examples/rectangular-scan/rectangular_scan.go)

## Solution: circle STDIN
{id: solution-circle-scan-stdin}

![](examples/circle-scan/circle_scan.go)

## Solution: calculator STDIN
{id: solution-calculator-scan-if}

![](examples/calc-scan-with-if/calc_scan_if.go)

