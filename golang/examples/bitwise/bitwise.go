package main

import "fmt"

func main() {
	a := 0b10101001
	b := 0b10010011
	format := "%-6v %3v %10b\n"
	fmt.Printf(format, "a", a, a)
	fmt.Printf(format, "b", b, b)
	fmt.Println()

	not := ^a
	fmt.Printf(format, "not", not, not)

	and := a & b
	fmt.Printf(format, "and", and, and)

	or := a | b
	fmt.Printf(format, "or", or, or)

	xor := a ^ b
	fmt.Printf(format, "xor", xor, xor)

	andNOT := a &^ b
	fmt.Printf(format, "andNOT", andNOT, andNOT)

	left := a << 1
	fmt.Printf(format, "left", left, left)

	right := a >> 1
	fmt.Printf(format, "right", right, right)
}
