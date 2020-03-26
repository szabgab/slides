# Numbers
{id: numbers}

## Integer-based operations
{id: integer-based-operations}
{i: %}

![](examples/numbers-integers/numbers_integers.go)

## Floating-based operations
{id: floating-based-operations}

* No modulo operator

![](examples/numbers-float/numbers_float.go)


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
* Go will always start from the same random seed of 1.

![](examples/random/random.go)


## Random with seed
{id: random-with-seed}
{i: Seed}
{i: time.Now().Unix}


![](examples/random_with_seed/random_with_seed.go)

## Exercise: Number Guessing Game - level 1
{id: exercise-number-guessing-game-level-1}

* This is the first level of a game we are going to build.

* The computer "thinks" a number between 1-20 and the user can guess it. (The computer asks the user for a guess).
* Then the computer tells the user if the guess was correct or if it was smaller or larger than the hidden number.

* In the higher levels of this game the user will be able to guess several times, but for now let's start with this simple version.

## Solution: Number Guessing Game - level 1
{id: solution-number-guessing-game-level-1}


![](examples/game1/game1.go)


