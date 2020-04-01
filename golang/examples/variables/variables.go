package main

import (
	"fmt"
)

func main() {
	c := 3 // type inferred

	var b int32 = 2

	var a int16
	a = 1

	fmt.Println(a) // 1
	fmt.Println(b) // 2
	fmt.Println(c) // 3

	fmt.Printf("%T\n", a) // int16
	fmt.Printf("%T\n", b) // int32
	fmt.Printf("%T\n", c) // int
}
