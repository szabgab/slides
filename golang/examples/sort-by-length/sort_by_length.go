package main

import (
	"fmt"
	"sort"
)

func main() {
	animals := []string{"snail", "dog", "cow", "elephant", "chicken", "mouse"}
	fmt.Println(animals)

	sort.Strings(animals) // abc order
	fmt.Println(animals)

	sort.Slice(animals, func(i, j int) bool { // sort by length
		return len(animals[i]) < len(animals[j])
	})
	fmt.Println(animals)
}
