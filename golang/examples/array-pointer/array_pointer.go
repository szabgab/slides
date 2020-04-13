package main

import (
	"fmt"
)

func main() {
	a := [...]string{"Foo", "Bar"}
	b := a
	c := &a
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println()

	a[0] = "Zorg"
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
