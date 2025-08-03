package main

import (
	"fmt"
)

func main() {
	dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

	// remove first element
	first := dwarfs[0]
	fmt.Println(first)

	dwarfs = dwarfs[1:]
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

}
