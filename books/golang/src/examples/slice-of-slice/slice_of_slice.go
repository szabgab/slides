package main

import (
	"fmt"
)

func main() {
	var dwarfs = []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}

	a := dwarfs[:]
	b := dwarfs[2:4]

	fmt.Println(dwarfs)
	fmt.Println(a)
	fmt.Println(b)

	dwarfs[2] = "Snowwhite"
	fmt.Println()
	fmt.Println(dwarfs)
	fmt.Println(a)
	fmt.Println(b)
}
