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
	if b == 0 {
		panic("Do you expect us do divide by 0?")
	}

	c := a / b
	return c
}
