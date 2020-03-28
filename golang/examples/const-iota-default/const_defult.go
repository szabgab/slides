package main

import (
	"fmt"
)

const (
	_ = iota
	one
	two
	three
)

const (
	six = iota + 6
	seven
	eight
)

func main() {
	fmt.Println(one)
	fmt.Println(two)
	fmt.Println(three)
	fmt.Println()
	fmt.Println(six)
	fmt.Println(seven)
	fmt.Println(eight)
}
