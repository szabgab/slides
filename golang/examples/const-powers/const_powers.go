package main

import (
	"fmt"
)

const (
	one = 1 << iota
	two
	four
	eight
	sixteen
)

func main() {
	fmt.Println(one)
	fmt.Println(two)
	fmt.Println(four)
	fmt.Println(eight)
	fmt.Println(sixteen)

	fmt.Println()
	fmt.Println(two | eight)
}
