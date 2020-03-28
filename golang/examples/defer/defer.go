package main

import "fmt"

func main() {
	fmt.Println("first")
	defer fmt.Println("one")
	fmt.Println("second")
	defer fmt.Println("two")
	fmt.Println("third")
}
