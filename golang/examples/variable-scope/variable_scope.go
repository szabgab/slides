package main

import (
	"fmt"
)

var x float32 = 3.14

func main() {
	fmt.Printf("%v %T\n", x, x)
	x := true
	fmt.Printf("%v %T\n", x, x)
	if true {
		x := "hello"
		fmt.Printf("%v %T\n", x, x)
	}

	for x := 1; x < 2; x++ {
		fmt.Printf("%v %T\n", x, x)
	}

	showX()

	{
		x := 77
		fmt.Println(x)
	}

	fmt.Printf("%v %T\n", x, x)

	// a, b := 1, 2
	// a, c := 3.2, 4
	// fmt.Println(a, b, c)
}

func showX() {
	fmt.Printf("showX: %v %T\n", x, x)
}
