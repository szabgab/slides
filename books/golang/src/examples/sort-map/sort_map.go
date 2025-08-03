package main

import (
	"fmt"
	"sort"
)

func main() {
	scores := map[string]int{"Alma": 23, "Cecilia": 12, "David": 37, "Berta": 78}
	fmt.Println(len(scores))
	fmt.Println(scores)
	fmt.Println()

	for name, score := range scores {
		fmt.Printf("%-7v %v\n", name, score)
	}
	fmt.Println()

	names := make([]string, 0, len(scores))
	for name := range scores {
		names = append(names, name)
	}
	fmt.Println(names)
	sort.Strings(names)
	fmt.Println(names)
	fmt.Println()

	for _, name := range names {
		fmt.Printf("%-7v %v\n", name, scores[name])
	}
}
