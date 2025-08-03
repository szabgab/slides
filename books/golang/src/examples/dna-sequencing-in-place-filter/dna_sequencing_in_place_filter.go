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

	i := 0
	for j := 0; j < len(sequences); j++ {
		if sequences[j] != "" {
			sequences[i] = sequences[j]
			i++
		}
	}
	sequences = sequences[:i]
	fmt.Println(sequences)
	fmt.Printf("%v, %v\n", len(sequences), cap(sequences)) // 4, 6

	sort.Slice(sequences, func(i, j int) bool {
		return len(sequences[i]) > len(sequences[j])
	})
	fmt.Println(sequences)
	fmt.Printf("%v, %v\n", len(sequences), cap(sequences)) // 4, 6
}
