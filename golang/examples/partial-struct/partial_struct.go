package main

import (
	"fmt"
)

type aPerson struct {
	id       int
	name     string
	email    string
	shoeSize float32
}

func main() {
	joe := aPerson{
		id:       1,
		name:     "Joe",
		email:    "joe@joehome.com",
		shoeSize: 42.5,
	}
	fmt.Println(joe)
	fmt.Println()

	jane := aPerson{
		id:   2,
		name: "Jane",
	}
	fmt.Println(jane)
}
