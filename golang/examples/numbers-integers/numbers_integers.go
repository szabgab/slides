package main

import (
	"fmt"
)

func main() {
	a := 3
	b := 7

	sum := a + b
	diff := a - b
	div := b / a
	mul := a * b
	mod := b % a

	fmt.Printf("sum %v\n", sum)
	fmt.Printf("diff %v\n", diff)
	fmt.Printf("mul %v\n", mul)
	fmt.Printf("div %v\n", div) // integer divided by integer is integer
	fmt.Printf("modulus %v\n", mod)

	divFloat := float64(b) / float64(a)
	fmt.Printf("div float: %v\n", divFloat)

	x := 1
	fmt.Printf("x: %v\n", x)
	x += 2 // x = x + 2
	fmt.Printf("x: %v\n", x)
	x++ // x = x + 1
	fmt.Printf("x: %v\n", x)
	x-- // x = x -1
	fmt.Printf("x: %v\n", x)

	// no prefix autoincrement and autodecrement
	// ++x
	// --x
}
