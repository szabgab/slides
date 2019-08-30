# Go-lang
{id: index}


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
* [other editors and IDEs](https://golang.org/doc/editors.html)


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

## Hello Foo
{id: hello-foo}

![](examples/hello_foo/hello_foo.go)


## Comments
{id: comments}

![](examples/comments/comments.go)


## Show variable type
{id: show-variable-type}

![](examples/show-type/show-type.go)


## Types
{id: types}

```
int - unspecified size (but mn 32 bit)
int8
int16
int32
int64
big packages.
uint16    (unsigned integer)
byte
complex64    1 + 2i    or just 3i
complex128
real(n)
imag(n)
complex(r, i)
string (any utf-8 character)
```

## Variables have types
{id: variables-have-types}

![](examples/variable/variable.go)

```
# command-line-arguments
./variable.go:8:7: cannot use 42 (type int) as type string in assignment
```

## Variable declaration
{id: variable-declaration}

![](examples/variable-declaration/declaration.go)


## Converting values to other types
{id: converting-types}

```
float32()
int()
string()

import strconv

strconv.Itoa
```

## Boolean values
{id: boolean-values}


var n bool = true
false


Default values of variables is 0 (false, empty string??)


## Integer-based operations
{id: integer-based-operations}

7/3  is 2 in Go as type does not change during operation
7%3  remainder



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

## golang read from stdin (keyboard)
{id: read-from-stdin}

Read from the stdin (standard input) Get input from the keyboard in golang

![](examples/read_from_stdin/read_from_stdin.go)

## golang read from stdin (keyboard) with error handling
{id: read-from-stdin-with-error-handling}

![](examples/read_from_stdin_with_error_handling/read_from_stdin_with_error_handling.go)

## Solution: rectangular
{id: solution-rectangular}

![](examples/rectangular/rectangular.go)


## Read file line by line
{id: read-file-line-by-line}

![](examples/read_file_line_by_line/read_file_line_by_line.go)

## Read file as one string (slurp)
{id: read-file-as-one-string}

![](examples/slurp_file/slurp_file.go)


## Sprintf and Sprintln
{id: sprintf}

![](examples/sprintf/sprintf.go)

![](examples/sprintln/sprintln.go)

## Scan input strings
{id: scan}

![](examples/scan/scan.go)


## Arrays
{id: arrays}

![](examples/array/array.go)

## Slice
{id: slice}


![](examples/slice/slice.go)


## Slice append
{id: slice-append}

![](examples/slice_append/slice_append.go)

[](https://tour.golang.org/moretypes/15)

## matrix
{id: matrix}

```
    var matrix [3][3]int = [3][3]int{ [3]int{1, 0, 0}, [3]int{0, 1, 0}, [3]int{0, 0, 1} }
    fmt.Println(matrix)
```

## Random with seed
{id: random-with-seed}

![](examples/random_with_seed/random_with_seed.go)


## golang: single and double quotes
{id: single-and-double-quotes}

* single quote is for single characters
* double quote is for strings

## golang http get request
{id: http-get-request}

![](examples/http_get/http_get.go)


## Include and distribute external files
{id: external-files}

How to include external files (e.g. images, html templates) in a golang application.

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

## Sum of numbers in a file
{id: sum-of-numbers}

![](examples/sum/sum.go)

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

## go workspace layout
{id: go-workspace-layout}

```
src/
bin/
pkg/
```

## Args - (argv) command line arguments
{id: args-command-line-arguments}


![](examples/cli/cli.go)

```
go run examples/cli/cli.go  hello world
```


## Create hello function
{id: hello-function}

![](examples/functions/hello_foo.go)

## Function with return value
{id: function-sith-return}

![](examples/function_return/comp.go)

## Simple test
{id: simple-test}

![](examples/simple_test/comp.go)

![](examples/simple_test/comp_test.go)

To run the tests:

```
got test -run ''
```

## Exit early with error code
{id: exit-early}

![](examples/exit/code.go)

## if statement
{id: if-statement}

![](examples/if/if.go)

## for loop
{id: for-loop}

![](examples/loop/loop.go)

## Resources
{id: resources}

* [Golang tour](https://tour.golang.org/welcome/1)
* [Video](https://www.youtube.com/watch?v=YS4e4q9oBaU)
* [Video](https://youtu.be/YS4e4q9oBaU?t=6927)

