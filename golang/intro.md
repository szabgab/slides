# Go-lang
{id: index}

## Resources
{id: resources}

* https://www.youtube.com/watch?v=YS4e4q9oBaU
* https://youtu.be/YS4e4q9oBaU?t=6927

* https://golang.org/

## Features
{id: features}

* Strong and statically typed

* Simplicity
* Fast compile times
* Garbage collected
* Built-in concurrency
* Compile to standalone binaries


* main function is the entry point of every program

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

https://code.visualstudio.com/

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




7/3  is 2 in Go as type does not change during operation
7%3  remainder


## bitwise operators
{id: bitwise-operators}

```
&, |, ^, &^
bitshift operators
<<
>>
```









