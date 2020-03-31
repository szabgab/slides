package main

import (
	"fmt"
)

func main() {
	name := "Foo"
	age := 42.5
	married := true
	children := 2
	really := 2i

	fmt.Printf("%T\n", name)     // string
	fmt.Printf("%T\n", age)      // float64
	fmt.Printf("%T\n", married)  // bool
	fmt.Printf("%T\n", children) // int
	fmt.Printf("%T\n", really)   // complex128
}
