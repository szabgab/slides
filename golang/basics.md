# Basics
{id: basics}

## Hello Foo - Println
{id: hello-foo}
{i: Println}
{i: :=}

{aside}
In go you can use the `:=` operator to declare a variable and assign a value to it at the same time. Then you can use that variable in a `Println`.
As you might notice, (I did not), the ``Println` function insert a space between the values it prints. For better control about this you can use `Printf`.
{/aside}

![](examples/hello-foo/hello_foo.go)
![](examples/hello-foo/hello_foo.out)

## Hello Bar - Printf
{id: hello-bar-printf}
{i: Printf}
{i: %s}

{aside}
When printing values of variables it might be better to use the Printf function as it allows us to use placeholders like %s and be more precise where would we want to put a space and where don't. These formatting placeholders are similar to what we have in other languages, but Go has a few additional placeholders. Specifically `%s` isn't special. It stands for strings.
{/aside}

![](examples/hello-foo-printf/hello_foo_printf.go)
![](examples/hello-foo-printf/hello_foo_printf.out)


## Hello Bar - Printf %v
{id: hello-bar-printf-v}
{i: Printf}
{i: %v}

{aside}
In some case it is better to use %v as it is type-agnostic. We're going to use it more often during the rest of these pages.
{/aside}

![](examples/hello-foo-printf-v/hello_foo_printf_v.go)
![](examples/hello-foo-printf-v/hello_foo_printf_v.out)


## Enforce variables types
{id: enforce-variable-types}

{aside}
Each variable in Go has a type and Go will not let you mix values and variables of 
different types. When we created the variable with the `:=`
operator Go automatically deducted the type from the assigned value. In this case it was `string`.
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

complex64       1 + 2i    or just 3i
complex128
```


## Show inferred variable type - Printf %T
{id: show-variable-type}
{i: Printf}
{i: %T}

{aside}
When we create a variable with the `:=` assignment, Go automatically decides the type of the variable based on the initial value assigned to it. Using `Printf` and the `%T` placeholder you can print out this type.
{/aside}


![](examples/show-type/show_type.go)
![](examples/show-type/show_type.out)


## Show type of variable - reflect.TypeOf
{id: show-typeof}
{i: reflect}
{i: TypeOf}

{aside}
You can also use the `TypeOf` function of the `reflect` package.
{/aside}

* [reflect](https://golang.org/pkg/reflect/)

![](examples/typeof/typeof.go)
![](examples/typeof/typeof.out)

## get variable type - %T or reflect.TypeOf
{id: get-variable-type}

![](examples/get-type/get_type.go)


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


## Converting string to integer - strconv, Atoi
{id: converting-string-to-integer}
{i: strconv}
{i: Atoi}
{i: err}
{i: nil}

![](examples/convert-string-to-integer/convert_string_to_integer.go)
![](examples/convert-string-to-integer/convert_string_to_integer.out)

* In the first two examples the conversion was successful.
* In the 3rd and 4th examples it failed.
* How can we know?

{aside}
While internally Go can represent numbers, the communication with the outside world is always using strings. So when we read from a file we always get strings. When we ask the user to type in a number and the user types in a number, we still receive it as a string.
For example as the string `"42"`. So we need a way to convert a string that looks like a number to the numeric representation of Go.
{/aside}


## Error Handling
{id: error-handling}

* Functions that can fail will return the error value as the last value.
* We can sweep under the carper by assigning it to `_`.


## Converting string to integer with error handling - strconv, Itoa
{id: converting-string-to-integer-with-error-handling}
{i: strconv}
{i: Itoa}
{i: nil}

* [strconv](https://golang.org/pkg/strconv/)


![](examples/convert-string-to-integer-error-handling/convert_string_to_integer_error_handling.go)
![](examples/convert-string-to-integer-error-handling/convert_string_to_integer_error_handling.out)


{aside}
This can, of course go wrong. If we ask for an integer and the user types in `"42x"` or even `"FooBar"`. So the conversion might fail. The way Go usually handles errors is by returning a second value which is the special value `nil` if everything went fine, or the error object is something broke. It is the responsibility of the caller to check the error. So in the follwing examples you can see that from each function we accept two values, the actual value we are interested in and another value that we assign to a variable called `err`. It is not a special name, but it is quite common in Go to use the variable name `err` for this purpose.
{/aside}

{aside}
Then in each one of the example we check if the value of `err` is equal to `nil` or if there was an error in the conversion. 
{/aside}

## Converting string to float - strconv, ParseFloat
{id: converting-string-to-float}
{i: strconv}
{i: ParseFloat}
{i: err}
{i: nil}

![](examples/convert-string-to-float/convert_string_to_float.go)
![](examples/convert-string-to-float/convert_string_to_float.out)

## Converting integer to string - strconv, Itoa
{id: converting-integer-to-string}
{i: strconv}
{i: Itoa}

![](examples/convert-string/convert_string.go)
![](examples/convert-string/convert_string.out)


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

