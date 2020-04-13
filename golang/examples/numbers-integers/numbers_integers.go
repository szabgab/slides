package main

import (
	"fmt"
	"math"
)

func main() {
	a := 3
	b := 7

	sum := a + b
	diff := a - b
	div := b / a
	mul := a * b
	mod := b % a
	pow := math.Pow(2, 3)
	sqr := math.Pow(9, 0.5)

	fmt.Printf("sum %v\n", sum)
	fmt.Printf("diff %v\n", diff)
	fmt.Printf("mul %v\n", mul)
	fmt.Printf("div %v\n", div) // integer divided by integer is integer
	fmt.Printf("modulus %v\n", mod)
	fmt.Printf("power %v\n", pow)
	fmt.Printf("square %v\n", sqr)

	divFloat := float64(b) / float64(a)
	fmt.Printf("div float: %v\n", divFloat)

	x := 1
	fmt.Printf("x: %v\n", x)
	x += 2 // x = x + 2
	fmt.Printf("x: %v\n", x)
	x++ // x = x + 1
	fmt.Printf("x: %v\n", x)
	x-- // x = x - 1
	fmt.Printf("x: %v\n", x)

	// no prefix autoincrement and autodecrement
	// ++x
	// --x
}
