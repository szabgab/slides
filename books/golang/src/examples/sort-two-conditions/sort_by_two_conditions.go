package main

import (
	"fmt"
	"sort"
)

func main() {
	animals := []string{"snail", "dog", "cow", "elephant", "chicken", "mouse"}
	fmt.Println(animals)

	sort.Slice(animals, func(i, j int) bool {
		if len(animals[i]) != len(animals[j]) {
			return len(animals[i]) < len(animals[j])
		}
		return animals[i] < animals[j]
	})
	fmt.Println(animals)

}
