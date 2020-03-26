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

	div_float := float64(b)/float64(a)
	fmt.Printf("div float: %v", div_float)
}
