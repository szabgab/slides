# Go-lang
{id: index}

## Self intro
{id: self-intro}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* Help teams improve their development practices

* [Workshops](https://workshops.code-maven.com/)
* [Training Courses](https://hostlocal.com/)

* [Code Maven Meetup](https://www.meetup.com/Code-Mavens/)

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

```
go version
```

```
go get github.com/nsf/gocode
```

Installs stuff in ~/go  so we might want to add ~/go/bin  to out PATH.
In ~/.bashrc add

```
export PATH=$PATH:~/go/bin
```

then reload it using `source ~/.bashrc`


## Editor/IDE
{id: editor}

* [Visual Studio Code](https://code.visualstudio.com/) (It has plugins for Golang)
* [Other editors and IDEs](https://golang.org/doc/editors.html)


## Hello World
{id: hello-world}

![](examples/hello_world/hello_world.go)

* main function is the entry point of every program

```
go run hello_world.go
```

```
go build hello_world.go
./hello_world
```

* [Annotated Hello World in Go](https://www.353solutions.com/annotated-go)

## Hello Foo - Println
{id: hello-foo}

![](examples/hello_foo/hello_foo.go)

## Hello Foo - Printf
{id: hello-foo-printf}

![](examples/hello_foo_printf/hello_foo_printf.go)


## Comments
{id: comments}

![](examples/comments/comments.go)

## Enforce variables types
{id: enforce-variable-types}

![](examples/variable/variable.go)

```
# command-line-arguments
./variable.go:8:7: cannot use 42 (type int) as type string in assignment
```

* Compile-time error

## Basic Types
{id: basic-types}

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

![](examples/show-type/show-type.go)


## Variable declaration (var)
{id: variable-declaration}

![](examples/variables/variables.go)


## Converting values to other types - float32, int, string
{id: converting-types}

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

![](examples/boolean/boolean.go)

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


## Args - (argv) command line arguments
{id: args-command-line-arguments}


![](examples/cli/cli.go)

```
go run examples/cli/cli.go  hello world
```

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

## Arrays
{id: arrays}

![](examples/array/array.go)

* Length is part of the type!
* Two arrays with different length are also different types

## Arrays automatic length
{id: arrays-automatic-length}

![](examples/array2/array2.go)

## Array: empty and fill
{id: arrays-empty-fill}

![](examples/array-fill/array-fill.go)

## Slice
{id: slice}

![](examples/slice/slice.go)

## Slice append
{id: slice-append}

![](examples/slice_append/slice_append.go)

* [slice internals](https://blog.golang.org/go-slices-usage-and-internals)

## 3-part for loop
{id: 3-part-for-loop}

![](examples/for-loop/for.go)

## while-like for loop
{id: while}

![](examples/while/while.go)

## for loop
{id: for-loop}

![](examples/loop/loop.go)

## for only value (no index)
{id: for-values}

![](examples/for-values/for-values.go)


## infinite loop, break
{id: infinite-loop}

![](examples/infinite-loop/loop.go)


## continue
{id: continue}

![](examples/continue/continue.go)

## Exercise: count digits
{id: exercise-count-digits}

Skeleton:

![](examples/count-digits-exercise/count-digits-exercise.go)

Expected Output:

```
0: 0
1: 1
2: 0
3: 2
4: 0
5: 0
6: 1
7: 3
8: 0
9: 1
```

## Exercise: count digits from string
{id: exercise-count-digits-from-string}

Skeleton:

![](examples/count-digits-skeleton/skeleton.go)

## Solution: count digits
{id: solution-count-digits}

![](examples/count-digits/count-digits.go)

## Solution: count digits from string
{id: solution-count-digits-from-string}

![](examples/count-digits-again/count-digits-again.go)

## Map (hash, dictionary)
{id: map}

![](examples/map/map.go)

## Empty Map
{id: empty-map}

![](examples/empty-map/empty-map.go)

## Map with data
{id: map-with-data}

![](examples/map-with-data/map-with-data.go)

## Delete Map element
{id: delete-map-element}

![](examples/delete-key/delete-key.go)

## Map element exists
{id: map-element-exists}

![](examples/exists/exists.go)

## Exercise count words
{id: exercise-count-words}

![](examples/count-words-skeleton/count-words-skeleton.go)

Expected output:

```
hello: 1
world: 2
how: 2
are: 2
you: 2
and: 1
```

## Solution count words
{id: solution-count-words}

![](examples/count-words/count-words.go)

## Read file line by line (os.Open)
{id: read-file-line-by-line}

![](examples/read_file_line_by_line/read_file_line_by_line.go)

* [OS](https://golang.org/pkg/os/)

## Read file as one string (slurp)
{id: read-file-as-one-string}

![](examples/slurp_file/slurp_file.go)

## Write to file
{id: write-to-file}

![](examples/write/write_file.go)

## Random with seed
{id: random-with-seed}

![](examples/random_with_seed/random_with_seed.go)

## Single and double quotes
{id: single-and-double-quotes}

* Single quote is for single characters
* Double quote is for strings

## Create hello function
{id: hello-function}

![](examples/functions/hello_foo.go)

## Function with return value
{id: function-sith-return}

![](examples/function_return/comp.go)

## Defer
{id: defer}

Every defer statement is executed after the enclosing function ends.
In reverse order. (Similar to END block in Perl, similar to with context in python)

![](examples/defer/defer.go)

```
$ go run defer.go

first
second
third
two
one
```

## Exercise: Fibonacci
{id: exercise-fibonacci}

Implement a function that accepts a positive integer (n) and prints out the first n numbers of the Fibonacci series.

## Solution: Fibonacci
{id: solution-fibonacci}

![](examples/fibonacci/fibonacci.go)

## Solution: Fibonacci recursive
{id: solution-fibonacci-recursive}

![](examples/fibonacci-recursive/fibonacci-recursive.go)

## http get request
{id: http-get-request}

![](examples/http_get/http_get.go)

## Simple test
{id: simple-test}

![](examples/simple_test/comp.go)

![](examples/simple_test/comp_test.go)

To run the tests:

```
got test -run ''
```

## Some advanced topics
{id: advanced-topics}

* struct
* closures
* pointers
* go-routines
* classes (there are no classes)
* methods (attached to types), but no classes
* interfaces
* Stringers - stringification
* Cross compilation
* many standard packages
* many external packages

## Resources
{id: resources}

* [Golang tour](https://tour.golang.org/welcome/1)
* [Video](https://www.youtube.com/watch?v=YS4e4q9oBaU)
* [Video](https://youtu.be/YS4e4q9oBaU?t=6927)

## Exit early with error code
{id: exit-early}

![](examples/exit/code.go)


## Runes
{id: runes}

```
rune - any utf-32 character
r := 'a'   // single quotes!
they are actually int32
var r rune = 'a'
```

## bitwise operators
{id: bitwise-operators}

```
&, |, ^, &^
bitshift operators
<<
>>
```

## Cross compile
{id: cross-compile}

How to compile a golang application and distribute to multiple platforms. How to cross-compile golang application.

```
env GOOS=target-OS GOARCH=target-architecture go build package-import-path
```

[](https://www.digitalocean.com/community/tutorials/how-to-build-go-executables-for-multiple-platforms-on-ubuntu-16-04)


## Constants
{id: constants}

const - constants
constants can be shadowed as well!  (not a good idea to do)
iota  (increment by 1 on every use in every constant block of var)  enumeration

```
var (
    _ = iota
    one
     two
     three
)

var (
    _ = iota + 5
    six
    seven
    eight
)
```

## Read from stdin (keyboard)
{id: read-from-stdin}

Read from the stdin (standard input) Get input from the keyboard in golang

![](examples/read_from_stdin/read_from_stdin.go)

## Read from stdin (keyboard) with error handling
{id: read-from-stdin-with-error-handling}

![](examples/read_from_stdin_with_error_handling/read_from_stdin_with_error_handling.go)


## Scan input strings
{id: scan}

![](examples/scan/scan.go)


## matrix
{id: matrix}

```
    var matrix [3][3]int = [3][3]int{ [3]int{1, 0, 0}, [3]int{0, 1, 0}, [3]int{0, 0, 1} }
    fmt.Println(matrix)
```

## get variable type - %T or reflect.TypeOf
{id: get-variable-type}

![](examples/get-type/get-type.go)

## Skeleton
{id: skeleton}

![](examples/skeleton/skeleton.go)

```
go run skeleton.go
```

## empty file
{id: empty-file}

![](examples/empty/empty.go)

```
go run empty.go

package main: empty.go:1:2: expected 'package', found 'EOF'
```

## Only package main
{id: package-main}

![](examples/package-main/package-main.go)

```
# command-line-arguments
runtime.package-main_main·f: function main is undeclared in the main package
```

## Other package name
{id: other-package-name}

![](examples/qqrq/qqrq.go)

```
go run: cannot run non-main package
```

## go workspace layout
{id: go-workspace-layout}

```
src/
bin/
pkg/
```

## Include and distribute external files
{id: external-files}

How to include external files (e.g. images, html templates) in a golang application.

## Variable declaration outside of functions
{id: variable-declaration-outside-of-functions}

![](examples/variable-declaration/declaration.go)

```
// var i int
// i = 42

// var i int = 42
// i := 42   // (is the same but this one cannot be used on the package level

// var (
//    i = 42
//    j = 23
// )
```

## Solution: rectangular (STDIN)
{id: solution-rectangular-stdin}

![](examples/rectangular-stdin/rectangular.go)

## Sprintf and Sprintln
{id: sprintf}

![](examples/sprintf/sprintf.go)

![](examples/sprintln/sprintln.go)

## Sum of numbers in a file
{id: sum-of-numbers}

![](examples/sum/sum.go)

## goroutine
{id: goroutine}


![](examples/goroutine/goroutine.go)

```
$ go run goroutine.go
Welcome
first 0
first 1
first 2
fourth 0
second 0
second 1
third 0
third 1
second 2
fourth 1
third 2
fourth 2
Done
```

## Exercise: Number Guessing game
{id: number-guessing-game}

The exercise have several levels. Solve them one after the other.

* The computer "thinks" about a random integer between 0 and 200 then asks the player. The player types in an integer. The computer says if it is too small, to big, or direct hit.
* The user can guess multiple times. Exit only when there was a direct hit.
* The user can enter x any time and quite the game.
* The user can enter p any time and the hidden value is printed (cheating)
* Allow the user to change the game to "move" mode by typing "m". In this mode after every guess after we compared the values change the hidden number by -2, -1, 0, 1, or 2. 

## Solution: Number Guessing game - one guess
{id: solution-number-guessing-game-one-guess}


![](examples/game1/game1.go)


## Solution: Number Guessing game - multiple guesses till hit
{id: solution-number-guessing-game-multiple-guesses}

![](examples/game2/game2.go)

## Solution: Number Guessing game - allow x
{id: solution-number-guessing-game-allow-x}

![](examples/game3/game3.go)

## Solution: Number Guessing game - allow m
{id: solution-number-guessing-game-allow-m}

![](examples/game5/game5.go)

## os.stat information about a file or directory
{id: os-stat}

![](examples/file-stat/stat.go)

```
Error: stat hello/world: no such file or directory
```

If the directory where the file can be found is not executable by the user who runs this code, we'll get
the following error:

```
Error: stat hello/world: permission denied
```

## Solution: single counter
{id: solution-single-counter}

![](examples/counter-single/single-counter.go)

## Reading CSV file
{id: reading-csv-file}

![](examples/csv/process_csv_file.csv)

* Sum the numbers in the 3rd column

![](examples/csv/read-csv.go)


```
go run examples/csv/read-csv.go examples/csv/process_csv_file.csv
```


## TODO: JSON
{id: json}

![](examples/json/json-round-trip.go)

## TODO: Solution: multiple counter
{id: solution-multiple-counter}

![](examples/counter-multi/multi-counter.go)


## Logging
{id: logging}

![](examples/logging/logger.go)

* There is a default prefix for each log message
* We can change this prefix using SetFlags
* By default log prints to STDERR (Standard Error)
* Fatal prints the message and exits the script with exit code 1

```
First
2019/10/08 23:47:13 First log
2019/10/08 23:47:13 0x490ef0
2019/10/08 23:47:13 logger.go:14: After setting flags
2019/10/08 23:47:13 logger.go:15: Oups
exit status 1
```

* TODO: log to file
* TODO: log levels?
* TODO: log function names


