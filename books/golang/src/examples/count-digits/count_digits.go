package main

import "fmt"

func main() {
	count := [10]int{}

	digits := [...]int{3, 7, 6, 7, 9, 1, 3, 7, 8, 3, 1, 7, 0, 1, 2, 3}
	fmt.Println(digits)

	for i := 0; i < len(digits); i++ {
		//fmt.Println(digits[i])
		count[digits[i]]++
	}
	for i := 0; i < 10; i++ {
		fmt.Printf("%d: %d\n", i, count[i])
	}
}
