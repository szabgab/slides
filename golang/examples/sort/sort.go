package main

import (
	"fmt"
	"sort"
)

func main() {
	dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	fmt.Println(dwarfs)

	sort.Strings(dwarfs)
	fmt.Println(dwarfs)

	scores := []int{17, 3, 42, 28}
	fmt.Println(scores)

	sort.Ints(scores)
	fmt.Println(scores)
}
