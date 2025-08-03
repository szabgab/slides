package main

import (
	"fmt"
	"sort"
)

func main() {
	// input
	fruits := []string{"grape", "banana", "mango", "nut", "orange", "peach", "apple", "nut", "banana", "apple", "mango"}
	fmt.Println(fruits)
	sort.Strings(fruits)

	var uniqueFruits []string
	for i, word := range fruits {
		if i == 0 || fruits[i-1] != word {
			uniqueFruits = append(uniqueFruits, word)
		}
	}
	fmt.Println(uniqueFruits)
}
