package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	dna := "ACCGXXCXXGTTACTGGGCXTTGT"
	sequences := strings.Split(dna, "X")
	fmt.Println(sequences)
	fmt.Println(len(sequences)) // 6, this contains 2 empty strings as well

	shortSequences := make([]string, 0, len(sequences))
	fmt.Printf("%v, %v\n", len(shortSequences), cap(shortSequences)) // 0, 6
	for _, val := range sequences {
		if val != "" {
			shortSequences = append(shortSequences, val)
		}
	}
	fmt.Println(shortSequences)
	fmt.Printf("%v, %v\n", len(shortSequences), cap(shortSequences)) // 4, 6

	sort.Slice(shortSequences, func(i, j int) bool {
		return len(shortSequences[i]) > len(shortSequences[j])
	})
	fmt.Println(shortSequences)
	fmt.Printf("%v, %v\n", len(shortSequences), cap(shortSequences)) // 4, 6
}
