package main

import (
	"fmt"
)

type aPerson struct {
	id       int
	name     string
	shoeSize float32
	children []string
}

func main() {
	joe := aPerson{
		id:       1,
		name:     "Joe",
		shoeSize: 42.5,
		children: []string{"Alpha", "Beta"},
	}
	fmt.Println(joe)
	fmt.Println()

	fmt.Println(joe.id)
	fmt.Println(joe.name)
	fmt.Println(joe.shoeSize)
	fmt.Println(joe.children)
	fmt.Println(joe.children[0])
}
