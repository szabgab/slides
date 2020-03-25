package main

import (
	"fmt"
)

func main() {
	var dwarfs = []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}

	fmt.Println(dwarfs)
	fmt.Println(dwarfs[0])
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))
}
