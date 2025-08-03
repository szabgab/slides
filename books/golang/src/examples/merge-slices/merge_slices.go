package main

import (
	"fmt"
)

func main() {
	a := []int{1, 2, 3}
	b := []int{4, 5, 6}
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println()

	// c := append(a, b)  // cannot use b (type []int) as type int in append
	c := append(a, b...)
	fmt.Println(c)
	fmt.Printf("%T\n", c)
	fmt.Println(len(c))
	fmt.Println(cap(c))
}
