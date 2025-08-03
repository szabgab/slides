package main

import (
	"fmt"
)

func main() {
	a := 3.0
	b := 7.0

	sum := a + b
	diff := a - b
	div := b / a
	mul := a * b

	fmt.Printf("sum %v\n", sum)
	fmt.Printf("diff %v\n", diff)
	fmt.Printf("mul %v\n", mul)
	fmt.Printf("div %v\n", div)
}
