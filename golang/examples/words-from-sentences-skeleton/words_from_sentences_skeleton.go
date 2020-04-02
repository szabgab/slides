package main

import (
	"fmt"
)

func main() {
	// source:
	lines := []string{
		"grape banana mango",
		"nut orange peach",
		"apple nut banana apple mango",
	}
	fmt.Println(lines)

	// result:
	fruits := []string{"grape", "banana", "mango", "nut", "orange", "peach", "apple", "nut", "banana", "apple", "mango"}
	fmt.Println(fruits)
	for _, fruit := range fruits {
		fmt.Println(fruit)
	}
}
