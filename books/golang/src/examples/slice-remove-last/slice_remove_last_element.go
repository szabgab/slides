package main

import (
	"fmt"
)

func main() {
	dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	x := dwarfs
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

	// remove last element
	dwarfs = dwarfs[:len(dwarfs)-1]
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

	// shorten the slice (remove from the end)
	dwarfs = dwarfs[0:3]
	fmt.Println(dwarfs)
	fmt.Println(len(dwarfs))
	fmt.Println(cap(dwarfs))

	d := append(dwarfs, "qqrq")
	fmt.Println(d)
	fmt.Println(len(d))
	fmt.Println(cap(d))
	fmt.Println(x)
	fmt.Println(dwarfs)

}
