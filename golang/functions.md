# Functions
{id: functions}

## Create hello function
{id: hello-function}
{i: func}

![](examples/go-functions/hello_foo.go)

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
{i: <<}
{i: >>}
{i: &}
{i: |}
{i: ^}
{i: &^}

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
{i: const}

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


## Solution: single counter
{id: solution-single-counter}

![](examples/counter-single/single-counter.go)

## Reading CSV file
{id: reading-csv-file}

![](examples/go-csv/process_csv_file.csv)

* Sum the numbers in the 3rd column

![](examples/go-csv/read-csv.go)


```
go run examples/go-csv/read-csv.go examples/csv/process_csv_file.csv
```


## TODO: JSON
{id: json}

![](examples/go-json/json-round-trip.go)

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

## Logging to a file
{id: logging-to-a-file}

* Set the output filehandle using `SetOutput`

![](examples/log-to-file/log2file.go)

* TODO: log levels?
* TODO: log function names

## Split on whitespaces
{id: split-on-whitespaces}


![](examples/split-on-whitespace/split-ws.go)

```
'  hello    space   world 42 '
[hello space world 42]
4
```

* [strings.Fields](https://golang.org/pkg/strings/#Fields)

## Nano
{id: nano}

![](examples/nano/nano.go)

## Reverse Polish Calculator
{id: reverse-polish-calculator}

* TODO: finish this

![](examples/rpc/rpc.go)


