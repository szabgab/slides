package main

import (
	"fmt"
)

type aPerson struct {
	name  string
	email string
}

func main() {
	joe := aPerson{
		name:  "Joe",
		email: "joe@joehome.com",
	}

	jane := aPerson{
		name:  "Jane",
		email: "jane@janehome.com",
	}

	people := []aPerson{}
	fmt.Println(people)

	people = append(people, joe, jane)
	fmt.Println(people)
}
