# Numbers
{id: numbers}

## Integer-based operations
{id: integer-based-operations}
{i: %}
{i: ++}
{i: --}
{i: +=}
{i: /=}

![](examples/numbers-integers/numbers_integers.go)
![](examples/numbers-integers/numbers_integers.out)

## Floating-point based operations
{id: floating-based-operations}

* No modulo operator
* No autoincrement and autodecrement

![](examples/numbers-float/numbers_float.go)
![](examples/numbers-float/numbers_float.out)


## Mixed operations
{id: mixed-operations}

* Cannot have operation between differen types

![](examples/numbers-mix/numbers_mix.go)
![](examples/numbers-mix/numbers_mix.out)


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
* You are in the one-dimensional space where you only have distance, but no direction. There is and enemy spaceship you need to shoot down. The distance of the spaceship is represented as an integer number. You shoot by typing in an integer number. 


* The computer "thinks" a number between 1-20 and the user can guess it. (The computer asks the user for a guess).
* Then the computer tells the user if the guess was correct or if it was smaller or larger than the hidden number.

* In the higher levels of this game the user will be able to guess several times, but for now let's start with this simple version.

## Solution: One-dimensiona spacefight - level 1
{id: solution-number-guessing-game-level-1}


![](examples/game1/game1.go)


