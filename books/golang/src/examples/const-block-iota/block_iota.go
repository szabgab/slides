package main

import (
	"fmt"
)

const (
	a = iota
	b = iota
	c = iota
)

const (
	d = iota
	e
	f
)

func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println()

	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
}
