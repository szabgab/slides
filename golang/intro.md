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

https://www.digitalocean.com/community/tutorials/how-to-build-go-executables-for-multiple-platforms-on-ubuntu-16-04


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

## Arrays
{id: arrays}


## Include and distribute external files
{id: external-files}

How to include external files (e.g. images, html templates) in a golang application.


## Hello World
{id: hello-world}

![](examples/hello_world.go)

go run src/hello_world.go
go buil src/hello_world.go
./hello_world



-----------------

package main

import "fmt"

func main() {
    var name = "Foo"
    fmt.Println("Hello", name)
}
---------------------------


Read from the stdin (standard input) Get input from the keyboard in golang


package main

import (
    "fmt"
    "bufio"
    "os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter Your name: ")
    name, _ := reader.ReadString('\n')

    fmt.Println("Hello", name)
}

----------------------------------

$ cat src/rectangular.go
package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)

    fmt.Print("Width: ")
    width, _ := reader.ReadString('\n')
    width = strings.TrimSuffix(width, "\n")

    fmt.Print("Height: ")
    height, _ := reader.ReadString('\n')
    height = strings.TrimSuffix(height, "\n")

    w, _ := strconv.Atoi(width)
    h, _ := strconv.Atoi(height)
    //fmt.Println(w)
    //fmt.Println(h)

    fmt.Println( w * h )
}

------------------------------
package main

import (
    "fmt"
)

func main() {
    //var res int = 42
    var res = [3]int{97, 85, 93}
    //var res = [...]int{97, 85, 93}
    var names [3]string
    fmt.Println(res)
    fmt.Println(res[1])
    fmt.Println(names)
    names[0] = "Mary"
    fmt.Println(names)
}

----------------------------
matrix

    var matrix [3][3]int = [3][3]int{ [3]int{1, 0, 0}, [3]int{0, 1, 0}, [3]int{0, 0, 1} }
    fmt.Println(matrix)



