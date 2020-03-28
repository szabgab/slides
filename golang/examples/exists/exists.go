package main

import "fmt"

func main() {
	grades := make(map[string]int)

	grades["Mary"] = 99
	grades["Jane"] = 88
	grades["Bob"] = 93

	value, ok := grades["Jane"]
	fmt.Println(ok)    // true
	fmt.Println(value) // 88

	value, ok = grades["Bob"]
	fmt.Println(ok)    // true
	fmt.Println(value) // 93

	value, ok = grades["George"]
	fmt.Println(ok)    // false
	fmt.Println(value) // 0
}
