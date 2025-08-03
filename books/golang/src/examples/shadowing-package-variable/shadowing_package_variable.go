package main

import (
	"fmt"
)

var x float32 = 3.14

func main() {
	fmt.Printf("%v %T\n", x, x)
	x := 23
	fmt.Printf("%v %T\n", x, x)
}
