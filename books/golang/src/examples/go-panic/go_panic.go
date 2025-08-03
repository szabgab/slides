package main

import (
	"fmt"
)

func main() {
	fmt.Println("before")

	x := div(6, 2)
	fmt.Println(x)

	fmt.Println("middle")

	y := div(6, 0)
	fmt.Println(y)

	fmt.Println("after")
}

func div(a, b int) int {
	c := a / b
	return c
}
