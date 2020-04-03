package main

import "fmt"

func main() {
	a := "Hello"
	la := len(a)
	fmt.Printf("%v  %v\n", a, la)

	b := ""
	lb := len(b)
	fmt.Printf("%v  %v\n", b, lb)

	c := "Hello World!"
	lc := len(c)
	fmt.Printf("%v  %v\n", c, lc)

}
