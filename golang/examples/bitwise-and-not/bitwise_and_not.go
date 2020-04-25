package main

import "fmt"

func main() {
	// bit clear (and not) = set where "the first is set AND the second is NOT set"
	fmt.Printf("1 &^ 1 = %v\n", 1&^1)
	fmt.Printf("1 &^ 0 = %v\n", 1&^0)
	fmt.Printf("0 &^ 1 = %v\n", 0&^1)
	fmt.Printf("0 &^ 0 = %v\n", 0&^0)

}
