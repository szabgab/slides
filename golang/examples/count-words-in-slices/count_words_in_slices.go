package main

import (
	"fmt"
)

func main() {
	celestialObjects := []string{"Moon", "Gas", "Asteroid", "Dwarf", "Asteroid", "Moon", "Asteroid"}
	fmt.Println(celestialObjects)

	count := []int{}
	words := []string{}

	for _, word := range celestialObjects {
		words = append(words, word)
		count = append(count, 1)
	}

	for i, word := range words {
		fmt.Printf("%-10v %v\n", word, count[i])
	}
}

// get the index of an element
// remove element by value
