package main

import "fmt"

func main() {
	grades := map[string]int{
		"Mary": 99,
		"Jane": 88,
		"Bob":  93,
	}
	fmt.Printf("%T\n", grades) // map[string]int

	fmt.Println(grades) // map[Bob:93 Jane:88 Mary:99]

	delete(grades, "Jane")

	fmt.Println(grades) // map[Bob:93 Mary:99]
}
