package main

import (
	"fmt"
)

func main() {
	text := "This is a very long text. OK, maybe it is not that long after all."
	counter := make(map[string]int)
	for _, c := range text {
		//fmt.Printf("%v", string(c))
		if string(c) != " " {
			counter[string(c)]++
		}
	}

	fmt.Println(text)
	// sort.Slice(counter, func(i, j string) bool {
	// 	return counter[i] > counter[j]
	// })

	for char, count := range counter {
		fmt.Printf("%v: %v\n", char, count)
	}

}
