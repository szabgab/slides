# Introduction to Go-lang
{id: intro}

## Features
{id: features}

{aside}
I don't plan to give you a "pitch" as to why you would want to use Go, but here are a few items that might help you if you need to justify
the time you spend on it.

In general there are many attributes to every programming language and each language is located somewhere else in relation to those different attributes.

I think there are two central areas where Go has advantages over other languages. One of them is the built-in concurrency that makes it easyer to use all the cores that you can find in a modern computer. The other is the cross compilation. Meaning it is easy to write your code on one computer and compile your code
on that computer targeting other operating systems.

If we are alradt talking about compilation, it is also much faster than that of C or other compiled languages while its run-time is as fast as those other compiled language. The fast compile time might not sound as a big deal, but if your compilation takes 10 seconds instead of 5 minutes or two hours, your feedback loop is much faster and thus you can develop faster.

Another advantage that Go has is that it manages the memory for you so unlilke in C you don't have to deal with memory management. On the other hand by giving up on some of the (usually unnecessary) flexibility of Python it is also not as wasteful with memory allocation.

It provides you control over the types of the variables, but in many cases it does not force you to be precise.
{/aside}

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


## Go Designed by
{id: go-designed-by}

* [Robert Griesemer](https://github.com/griesemer)
* [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike)
* [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson)

* At Google

## Open Souce
{id: open-source}

{aside}
To some people, yours truly included, it is important to know tha the go compiler is open source. You can find its source code on GitHub.
{/aside}

* [Source code](https://github.com/golang/go)
* [The Go compiler is written in Go](https://blog.golang.org/go1.5)
* [How to compile the Go compiler](https://golang.org/doc/install/source) way beyond our needs.

## Platforms
{id: platforms}

* Linux
* Mac OSX
* MS Windows
* Some other
* [mobile: Android/iOS](https://github.com/golang/go/wiki/Mobile)


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

* [Apester](https://apester.com/)
* [Cisco](https://www.cisco.com/)
* [Gett](https://gett.com/)
* [Radware](https://www.radware.com/)


## Install Golang
{id: install}

* [Golang home](https://golang.org/)
* [Download](https://golang.org/dl/)
* Install in the standard location offered by the installer!

## Show Installed Version of Golang
{id: version}
{i: version}


* In the CMD window of MS Windows or in your Linux/Mac terminal type:

```
go version
```

```
go version go1.12.9 linux/amd64
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

![](examples/hello-go/hello_world.go)

```
go run hello_world.go
```

![](examples/hello-go/hello_world.out)

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


## Separate directories! - main redeclared in this block
{id: separate-directories}

* Put each example / exercise in a separate directory
* As each package must have only one main() function.

![](examples/same/same_one.go)
![](examples/same/same_two.go)

```
go run .
```

![](examples/same/same.out)



## Exercise: Hello World
{id: exercise-hello-world}


* Install go if you don't have it yet
* Install an editor/IDE with the appropriate plugin for go
* Check if `go version` is running
* Write the Hello World program and run it both from the IDE and from the command line
 

## Hello Foo - Println
{id: hello-foo}
{i: Println}
{i: :=}

![](examples/hello-foo/hello_foo.go)
![](examples/hello-foo/hello_foo.out)

## Hello Bar - Printf
{id: hello-bar-printf}
{i: Printf}
{i: %s}

{aside}
When printing values of variables it might be better to use the Printf function as it allows us to use placeholders like %s. Specifically %s stands for strings.
{/aside}

![](examples/hello-foo-printf/hello_foo_printf.go)
![](examples/hello-foo-printf/hello_foo_printf.out)


## Hello Bar - Printf %v
{id: hello-bar-printf-v}
{i: Printf}
{i: %v}

{aside}
In some case it is better to use %v as it is type-agnostic
{/aside}

![](examples/hello-foo-printf-v/hello_foo_printf_v.go)
![](examples/hello-foo-printf-v/hello_foo_printf_v.out)


## Enforce variables types
{id: enforce-variable-types}

{aside}
Each variable in Go has a type and Go will not let you mix values and variables of 
different types. When we creaed the variable with the `:=`
operator it automatically deducted from the assigned value.
{/aside}

![](examples/variable/variable.go)

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

{aside}
This is just a list of the basic types in Go. You only need to remember that there are different types. For now you can use the defaults offered by Golang. Later, when you get deeper in the language these types allow you to improve the speed and the memory usage of your application by specifying the size of each variable.
{/aside}

{aside}
The numbers indicate the number of bits each variable takes. In languages such Python and Perl you would not need to care about this at all, but you would not have control over these aspects either. (In the Numpy library of Python you do have these distinctions.)
{/aside}

{aside}
As I wrote, don't worry about them for now.
{/aside}

* [basic types](https://tour.golang.org/basics/11)

```
string          (any utf-8 character)

uint            (unsigned integer of 32 or 64 bits - depends on implementation)
uint8           (unsigned integer (0, 255)
uint16          (unsigned integer)
uint32          (unsigned integer)
uint64          (unsigned integer)


int             (signed integer, the same bit-size as uint)
int8            (signed integer (-128, 127))
int16
int32
int64

float32
float64

bool

byte             (alias for uint8)
rune             (alias for int32)

complex(r, i)
complex64       1 + 2i    or just 3i
complex128

real(n)
imag(n)
```


## Show inferred variable type - Printf %T
{id: show-variable-type}
{i: Printf}
{i: %T}

{aside}
When we create a variable with the := assignment, Go automatically decides the type of the variable based on the initial value assigned to it. Using Printf and the %T placeholder you can print out this type.
{/aside}


![](examples/show-type/show_type.go)
![](examples/show-type/show_type.out)


## Show type of variable - reflect.TypeOf
{id: show-typeof}
{i: reflect}
{i: TypeOf}

![](examples/typeof/typeof.go)
![](examples/typeof/typeof.out)

## Variable declaration (var)
{id: variable-declaration}
{i: var}
{i: :=}


* There are 3 ways to declare variables in Go

{aside}
The first one, the one that we have already seen uses the `:=` operator. It declares a variable and immediately assigns a value to it. The type of the variable is deducted from the value assigned to it.
{/aside}

{aside}
The second in our example uses the `var` keyword and explicitely sets the type. `var b int32 = 2` This is used when we would like to fine-tune the type of the variable.
{/aside}


{aside}
In the third example `var a int16` we declare the variable but we don't assign any value to it yet. This is used when need don't know the initial value when we declare the variable. This can happen, for example, when we are looking for some value in a loop, and we would like the result to be available outside of the loop. This is related to the scoping of variables that we'll discuss later.
{/aside}

![](examples/variables/variables.go)
![](examples/variables/variables.out)


## Default values of variables
{id: default-values}
{i: false}

Variables declared without an explicit initial value are given their zero value as default.

* 0 for numeric types.
* "" (the empty string) for strings.
* `false` for the boolean type.

![](examples/zero/zero.go)
![](examples/zero/zero.out)


## Scan input strings from STDIN
{id: scan}
{i: STDIN}
{i: Scan}

{aside}
We'll have a lot more to say about getting input from the user, but in order to be able to write some useful code, let's introduce a simple way to get input from the user. For this we need to declare a variable first to be a `string`. Then we call the `Scan` function and give the variable as a parameter. More precisely we pass a pointer to the variable to the function by prefixing it with `&`. Later we'll discuss pointers as well, for now all you need to know is that `Scan` will wait till the  user types in something and presses ENTER. Then all the content will be in the variable. 
{/aside}

* [fmt.Scan](https://golang.org/pkg/fmt/#Scan)

![](examples/scan/scan.go)


## if else statement
{id: if-else-statement-intro}

{aside}
We'll have a longer discussion about conditinal statements later, but it is quite hard to do anything useful without them so let's have a quick look at an `if - else` construct. Here we check if the value in the `name` variable equals to the string `Go` and depending on the success of this comparision we print something.  
{/aside}

![](examples/if/if.go)


## Error Handling
{id: error-handling}

* functions return the error value


## Converting strings to numbers - strconv, ParseFloat, Atoi, Itoa
{id: converting-strings-to-numbers}
{i: strconv}
{i: Atoi}
{i: Itoa}
{i: ParseFloat}
{i: err}
{i: nil}

{aside}
While internally Go can represent numbers, the communication with the outside world is always using strings. So when we read from a file we always get strings. When we ask the user to type in a number and the user types in a number, we still receive it as a string.
For example as the string `"42"`. So we need a way to convert a string that looks like a number to the numeric representation of Go.
{/aside}

{aside}
This can, of course go wrong. If we ask for an integer and the user types in `"42x"` or even `"FooBar"`. So the conversion might fail. The way Go usually handles errors is by returning a second value which is the special value `nil` if everything went fine, or the error object is something broke. It is the responsibility of the caller to check the error. So in the follwing examples you can see that from each function we accept two values, the actual value we are interested in and another value that we assign to a variable called `err`. It is not a special name, but it is quite common in Go to use the variable name `err` for this purpose.
{/aside}

{aside}
Then in each one of the example we check if the value of `err` is equal to `nil` or if there was an error in the conversion. 
{/aside}


![](examples/convert-string/convert_string.go)

* [strconv](https://golang.org/pkg/strconv/)


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



## Exercise: circle STDIN
{id: exercise-circle-stdin}

Write a program that asks the user for a number, the radius of a circle, and prints out the area and the circumference of the circle.

```
go run circle.go
radius: 2
Area: 
Circumference:
```


## Exercise: rectangular STDIN
{id: exercise-rectangular-stdin}

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

* What happens if we try to divide by 0?

## Solution: circle STDIN
{id: solution-circle-stdin}

![](examples/circle-stdin/circle_stdin.go)


## Solution: circle STDIN with math
{id: solution-circle-stdin-math}
{i: math}

{aside}
Of course you don't need to type in the value if PI yourself. There is a module called `math` that provides you the value at a much better precision. There is also a function called `Pow` that can rasie any number to any power.
{/aside}

* [math](https://golang.org/pkg/math/)

![](examples/circle-stdin-math/circle_stdin_math.go)



## Solution: rectangular STDIN
{id: solution-rectangular-stdin}

![](examples/rectangular-stdin/rectangular_stdin.go)


## Solution: calculator STDIN
{id: solution-calculator-stdin-if}

![](examples/calc-stdin-if/calc_stdin_if.go)


## Solution: calculator STDIN switch
{id: solution-calculator-stdin-switch}
{i: swicth}
{i: case}

![](examples/calc-stdin-switch/calc_stdin_switch.go)

