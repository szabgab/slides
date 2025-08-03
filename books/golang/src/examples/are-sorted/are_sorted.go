package main

import (
	"fmt"
	"sort"
)

func main() {
	dwarfs := []string{"Doc", "Happy", "Grumpy"}
	fmt.Println(dwarfs)
	fmt.Println(sort.StringsAreSorted(dwarfs))

	sort.Strings(dwarfs)
	fmt.Println(dwarfs)
	fmt.Println(sort.StringsAreSorted(dwarfs))
	fmt.Println()

	greekNames := []string{"Alpha", "Beta"}
	fmt.Println(sort.StringsAreSorted(greekNames))
	fmt.Println()

	scores := []int{17, 3, 42, 28}
	fmt.Println(scores)
	fmt.Println(sort.IntsAreSorted(scores))
}
