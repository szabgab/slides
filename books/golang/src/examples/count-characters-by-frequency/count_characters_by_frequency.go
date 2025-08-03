package main

import (
	"fmt"
	"sort"
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
	chars := make([]string, 0, len(counter))
	for chr := range counter {
		chars = append(chars, chr)
	}

	sort.Slice(chars, func(i, j int) bool {
		return counter[chars[i]] > counter[chars[j]]
	})
	for _, chr := range chars {
		fmt.Printf("%v: %v\n", chr, counter[chr])
	}

}
