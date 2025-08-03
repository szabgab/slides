package main

import "fmt"

func main() {
	grades := make(map[string]int)

	grades["Mary"] = 99
	grades["Joe"] = 0

	value, ok := grades["Mary"]
	fmt.Println(ok)
	fmt.Println(value)
	fmt.Println()

	value, ok = grades["Joe"]
	fmt.Println(ok)
	fmt.Println(value)
	fmt.Println()

	value, ok = grades["Jane"]
	fmt.Println(ok)
	fmt.Println(value)
}
