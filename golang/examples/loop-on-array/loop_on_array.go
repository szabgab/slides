package main

import (
	"fmt"
)

func main() {
	dwarfs := [...]string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}

	fmt.Printf("%T\n%v\n", dwarfs, dwarfs)

	for i, name := range dwarfs {
		fmt.Printf("location: %d  name: %s\n", i, name)
	}
}
