package main

import (
	"fmt"
)

func main() {
	celestialObjects := []string{"Moon", "Gas", "Asteroid", "Dwarf", "Asteroid", "Moon", "Asteroid"}
	fmt.Println(celestialObjects)

	count := []int{}
	words := []string{}

OBJECTS:
	for _, word := range celestialObjects {
		for i, value := range words {
			if value == word {
				count[i]++
				continue OBJECTS
			}
		}
		words = append(words, word)
		count = append(count, 1)
	}

	for i, word := range words {
		fmt.Printf("%-10v %v\n", word, count[i])
	}
}
