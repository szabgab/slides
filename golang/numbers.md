# Numbers
{id: numbers}

## Integer-based operations
{id: integer-based-operations}
{i: %}
{i: ++}
{i: --}
{i: +=}
{i: /=}
{i: pow}

![](examples/numbers-integers/numbers_integers.go)
![](examples/numbers-integers/numbers_integers.out)

## Floating-point based operations
{id: floating-based-operations}

* No modulo operator
* No autoincrement and autodecrement

![](examples/numbers-float/numbers_float.go)
![](examples/numbers-float/numbers_float.out)

## Precision
{id: precision}

![](examples/precision/precision.go)
![](examples/precision/precision.out)


## Mixed operations
{id: mixed-operations}

* Cannot have operation between differen types

![](examples/numbers-mix/numbers_mix.go)
![](examples/numbers-mix/numbers_mix.out)

## int8
{id: int8}
{i: int8}

![](examples/int8/int8.go)
![](examples/int8/int8.out

## uint8
{id: uint8}
{i: uint8}

![](examples/uint8/uint8.go)
![](examples/uint8/uint8.out)


## Bytes
{id: bytes}
{i: byte}


![](examples/byte/byte.go)
![](examples/byte/byte.out)

## Byte is uint8
{id: byte-uint8}
{i: byte}

* `byte` is just an alias for `uint8`

![](examples/byte-uint8/byte_uint8.go)

## uint16
{id: uint16}
{i: uint16}

![](examples/uint16/uint16.go)
![](examples/uint16/uint16.out)


## uint32
{id: uint32}
{i: uint32}

![](examples/uint32/uint32.go)
![](examples/uint32/uint32.out)

## Converting values to other types - float32, int, string
{id: converting-types}
{i: float32()}
{i: int()}
{i: string()}
{i: Sprintf}
{i: %f}
{i: %d}

* integers to `float32()`
* floats to `int()`
* integers to `string()` but that converts the number to the value it represents in ASCII or Unicode table.
* In order to get the same "look" but as a string we need to use the `Sprintf` function from `fmt`.


![](examples/convert/convert.go)


## Random
{id: random}
{i: rand}
{i: Float64}
{i: Int}
{i: Intn}

* [Pseudo Random](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
* [rand](https://golang.org/pkg/math/rand/)
* Go will always start from the same random seed of 1 meaning that this script will always generate the same "random" numbers.

![](examples/random/random.go)
![](examples/random/random.out)


## Random with seed
{id: random-with-seed}
{i: Seed}
{i: time.Now().Unix}

* In order to generate different random numbers one needs to set the starting point by calling `Seed`.
* A common way to do that is to provide the number of seconds since the epoch.

![](examples/random-with-seed/random_with_seed.go)
![](examples/random-with-seed/random_with_seed.out)

## Exercise: One-dimensional spacefight - level 1
{id: exercise-one-dimensional-spacefight-level-1}

* This is the first level of a game we are going to build.
* You are in the one-dimensional space where you only have distance, but no direction. There is an enemy spaceship you need to shoot down. The distance of the spaceship is represented as an integer number. You shoot by typing in an integer number. 


* The computer "thinks" of a number between 1-20 and the user can guess it. (The computer asks the user for a guess).
* Then the computer tells the user if the guess was correct or if it was smaller or larger than the chosen number.

* In the higher levels of this game the user will be able to guess several times, but for now let's start with this simple version.

## Solution: One-dimensiona spacefight - level 1
{id: solution-number-guessing-game-level-1}


![](examples/game1/game1.go)
