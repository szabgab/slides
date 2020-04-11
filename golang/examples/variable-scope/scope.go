package main

import (
	"fmt"
)

var x float32 = 3.14
var y int

func main() {
	fmt.Printf("%v %T\n", x, x)
	x := 23
	fmt.Printf("%v %T\n", x, x)
	if true {
		x := "hello"
		fmt.Printf("%v %T\n", x, x)

	}

	fmt.Printf("%v %T\n", x, x)

	showY()
	setY()
	showY()
}

func setY() {
	y = 42
}
func showY() {
	fmt.Println(y)
}
