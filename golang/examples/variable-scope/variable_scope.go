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

}

func showX() {
	fmt.Printf("showX: %v %T\n", x, x)
}
