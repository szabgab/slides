package main

import (
	"fmt"
	"strings"
)

func main() {
	// source:
	lines := []string{
		"grape banana mango",
		"nut orange peach",
		"apple nut banana apple mango",
	}
	fmt.Println(lines)

	var fruits []string
	// Append words from each line
	for _, line := range lines {
		words := strings.Split(line, " ")
		fmt.Printf("fruits: %v, appending words: %v\n", fruits, words)
		fruits = append(fruits, words...)
	}

	// Print final result
	fmt.Println(fruits)
	for _, fruit := range fruits {
		fmt.Println(fruit)
	}
}
