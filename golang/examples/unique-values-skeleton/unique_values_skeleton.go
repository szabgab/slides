package main

import "fmt"

func main() {
	// input
	fruits := []string{"grape", "banana", "mango", "nut", "orange", "peach", "apple", "nut", "banana", "apple", "mango"}
	fmt.Println(fruits)

	// expected output:
	uniqueFruites := []string{"apple", "banana", "grape", "mango", "nut", "orange", "peach"}
	fmt.Println(uniqueFruites)
}
