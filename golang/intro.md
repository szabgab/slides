# Go-lang
{id: index}

## Resources
{id: resources}

* [Video](https://www.youtube.com/watch?v=YS4e4q9oBaU)
* [Video](https://youtu.be/YS4e4q9oBaU?t=6927)

* [Golang home](https://golang.org/)
* [Golang tour](https://tour.golang.org/welcome/1)

## Features
{id: features}

* Strong and statically typed

* Simplicity
* Fast compile times
* Garbage collected
* Built-in concurrency
* Compile to standalone binaries

## Install
{id: install}


## Version
{id: version}

```
go version
```

```
go get github.com/nsf/gocode
```

installs in ~/go  so we might want to add ~/go/bin  to out PATH


## go workspace layout
{id: go-workspace-layout}

```
src/
bin/
pkg/
```

## Editor/IDE
{id: editor}

* [Visual Studio](https://code.visualstudio.com/)


## Hello World
{id: hello-world}

![](examples/hello_world.go)

* main function is the entry point of every program

```
go run src/hello_world.go
```

```
go build src/hello_world.go
./hello_world
```

## Hello Foo
{id: hello-foo}

![](examples/hello_foo.go)


## Variable declaration
{id: variable-declaration}

```
var i int
i = 42

var i int = 42
i := 42   // (is the same but this one cannot be used on the package level

var (
   i = 42
   j = 23
)
```

Not using a declared variable is a compile-time error!


Redeclaration and shadowing
Visibility
Naming conventions
Type conversions

lower-case variables are scoped to the current package
upper-case variables are exported from the package and globally visible
block-scoped variables (e.g. in a function) are only visible in the block

theURL
theHTML

Converting values to other types:
float32()
int()
string()

import strconv

strconv.Itoa

Boolean:
var n bool = true
false


Default values of variables is 0 (false, empty string??)

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

strings are just aliases for byte
strings are (generally?) immutable

s := "some string"
b := []byte(s)    // the ascii or utf values of the characters  ???

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

![](examples/read_from_stdin.go)

## golang read from stdin (keyboard) with error handling
{id: read-from-stdin-with-error-handling}

![](examples/read_from_stdin_with_error_handling.go)

## Solution: rectangular
{id: solution-rectangular}

![](examples/rectangular.go)


## Read file line by line
{id: read-file-line-by-line}

![](examples/read_file_line_by_line.go)

## Read file as one string (slurp)
{id: read-file-as-one-string}

![](examples/slurp_file.go)
## Arrays
{id: arrays}

![](examples/array.go)


## golang array append
{id: array-append}

![](examples/array_append.go)

[](https://tour.golang.org/moretypes/15)

## matrix
{id: matrix}

```
    var matrix [3][3]int = [3][3]int{ [3]int{1, 0, 0}, [3]int{0, 1, 0}, [3]int{0, 0, 1} }
    fmt.Println(matrix)
```

## Random with seed
{id: random-with-seed}

![](examples/random_with_seed.go)


## golang: single and double quotes
{id: single-and-double-quotes}

* single quote is for single characters
* double quote is for strings

## golang http get request
{id: http-get-request}

![](examples/http_get.go)


## Include and distribute external files
{id: external-files}

How to include external files (e.g. images, html templates) in a golang application.

## Skeleton
{id: skeleton}

![](examples/skeleton.go)

```
go run skeleton.go
```

## empty file
{id: empty-file}

![](examples/empty.go)

```
go run empty.go

package main: empty.go:1:2: expected 'package', found 'EOF'
```

## Only package main
{id: package-main}

![](examples/package-main.go)

```
# command-line-arguments
runtime.package-main_main·f: function main is undeclared in the main package
```

## Other package name
{id: other-package-name}

![](examples/qqrq.go)

```
go run: cannot run non-main package
```




