package main

import (
	"fmt"
)

func main() {
	fmt.Println("before")
	a, b := 1, 0
	c := a / b
	fmt.Println(c)
	fmt.Println("after")
}
