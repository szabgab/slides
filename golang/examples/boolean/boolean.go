package main

import "fmt"

func main() {
	var n bool = true
	fmt.Println(n)        // true
	fmt.Printf("%T\n", n) // bool

	n = !n
	fmt.Println(n) // false
}
