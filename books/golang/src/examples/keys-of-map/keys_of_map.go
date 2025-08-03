package main

import (
	"fmt"
)

func main() {
	scores := map[string]int{"Alma": 23, "Cecilia": 12, "Berta": 78, "David": 37}
	fmt.Println(len(scores))
	fmt.Println(scores)

	names := make([]string, 0, len(scores))
	for name := range scores {
		names = append(names, name)
	}
	fmt.Println(names)
	for _, name := range names {
		fmt.Println(name)
	}
}
