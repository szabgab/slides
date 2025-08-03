package main

import "fmt"

func main() {
	var first string
	fmt.Print("First string: ")
	fmt.Scan(&first)

	var second string
	fmt.Print("Second string: ")
	fmt.Scan(&second)

	if len(first) > len(second) {
		fmt.Printf("'%v' is longer than '%v'\n", first, second)
		return
	}

	if len(first) < len(second) {
		fmt.Printf("'%v' is longer than '%v'\n", second, first)
		return
	}

	fmt.Printf("'%v' and '%v' are the same length\n", second, first)
}
