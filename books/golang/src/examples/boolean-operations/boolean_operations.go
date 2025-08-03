package main

import "fmt"

func main() {
	fmt.Printf("%v\n", true && true)   // true
	fmt.Printf("%v\n", true && false)  // false
	fmt.Printf("%v\n", false && true)  // false
	fmt.Printf("%v\n", false && false) // false

	fmt.Println()
	fmt.Printf("%v\n", true || true)   // true
	fmt.Printf("%v\n", true || false)  // true
	fmt.Printf("%v\n", false || true)  // true
	fmt.Printf("%v\n", false || false) // false

	fmt.Println()
	fmt.Printf("%v\n", !true)  // false
	fmt.Printf("%v\n", !false) // true
}
