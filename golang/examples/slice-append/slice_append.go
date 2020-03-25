package main

import (
	"fmt"
)

func main() {
	dwarfs := []string{}
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
