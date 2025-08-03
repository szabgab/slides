package main

import "fmt"

func main() {
	grades := make(map[string]int)
	grades["Mary"] = 99
	grades["Jane"] = 88
	grades["Bob"] = 93

	for key, value := range grades {
		fmt.Printf("%-4s  %d\n", key, value)
	}
}
