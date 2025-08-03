package main

import (
	"fmt"
)

func main() {
	dwarfs := make([]string, 0, 10)
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

	dwarfs = append(dwarfs, "Happy")
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

	dwarfs = append(dwarfs, "Grumpy", "Sleepy")
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))
}
