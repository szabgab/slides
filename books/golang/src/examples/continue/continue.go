package main

import (
	"fmt"
)

func main() {
	i := 0
	for {
		fmt.Println("")
		i++
		fmt.Printf("A: %v\n", i)
		if i > 4 {
			break
		}
		fmt.Printf("B: %v\n", i)
		if i == 3 {
			continue
		}
		fmt.Printf("C: %v\n", i)
	}
	fmt.Println("after loop")
}
