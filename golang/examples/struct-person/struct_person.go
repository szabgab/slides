package main

import (
	"fmt"
)

type Person struct {
	id       int
	name     string
	email    string
	shoeSize float32
}

func main() {
	joe := Person{
		id:       1,
		name:     "Joe",
		email:    "joe@joehome.com",
		shoeSize: 42.5,
	}
	fmt.Println(joe)
	fmt.Println(joe.id)
	fmt.Println(joe.id)
	fmt.Println(joe.email)
	fmt.Println(joe.shoeSize)

	fmt.Println()
	people := []Person{}
	fmt.Println(people)
	people = append(people, joe)
	fmt.Println(people)
}
