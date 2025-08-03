package main

import (
	"fmt"
)

func main() {
	people := make(map[string]int)
	people["Ann"] = 1
	people["George"] = 23
	people["Rose"] = 345

	for name, number := range people {
		fmt.Printf("%v | %v\n", name, number)
	}
	fmt.Println()
	for name, number := range people {
		fmt.Printf("%-6v | %v\n", name, number)
	}
	fmt.Println()
	for name, number := range people {
		fmt.Printf("%-6v | %3v\n", name, number)
	}
}
