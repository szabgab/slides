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
	d := dwarfs
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))
	fmt.Println()

	dwarfs = append(dwarfs, "Grumpy", "Sleepy", "Doc", "Bashful", "Sneezy", "Dopey")
	fmt.Println(d)
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))
	fmt.Println()

	dwarfs = append(dwarfs, "Snow white")
	fmt.Println(d)
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))
}
