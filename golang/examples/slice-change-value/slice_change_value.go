package main

import (
	"fmt"
)

func main() {
	var dwarfs = []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}

	fmt.Println(dwarfs)
	fmt.Println(dwarfs[1])
	dwarfs[1] = "Snowwhite"

	fmt.Println(dwarfs)
	fmt.Println(dwarfs[1])

	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))
}
