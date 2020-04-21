package main

import "fmt"

func main() {
	grades := make(map[string]int)

	grades["Mary"] = 99
	grades["Joe"] = 0
	fmt.Println(grades["Mary"])
	fmt.Println(grades["Joe"])
	fmt.Println(grades["Jane"])

}
