package main

import (
	"fmt"
)

func main() {
	a := []string{"Foo", "Bar"}
	b := a
	c := &a
	d := make([]string, len(a))
	copy(d, a)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println()

	a[0] = "Zorg"
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println()

	a = append(a, "Other")
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)

}
