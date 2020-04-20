package main

import (
	"fmt"
	"sort"
)

func main() {
	scores := map[string]int{"Alma": 23, "Cecilia": 12, "Berta": 78}
	fmt.Println(len(scores))
	scores["David"] = 37
	fmt.Println(len(scores))
	fmt.Println(scores)

	for name, score := range scores {
		fmt.Printf("%-7v %v\n", name, score)
	}

	names := make([]string, 0, len(scores))
	for name := range scores {
		names = append(names, name)
	}
	fmt.Println(names)
	sort.Strings(names)
	fmt.Println(names)
	for _, name := range names {
		fmt.Printf("%-7v %v\n", name, scores[name])
	}

	sort.Slice(names, func(i, j int) bool {
		return scores[names[i]] < scores[names[j]]
	})
	for _, name := range names {
		fmt.Printf("%-7v %v\n", name, scores[name])
	}
}
