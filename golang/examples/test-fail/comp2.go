package main

import (
	"fmt"
)

func main() {
	res := add(2, 2)
	fmt.Println(res)
}

func add(a, b int) int {
	return a * b
}
