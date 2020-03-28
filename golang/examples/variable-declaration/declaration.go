package main

import "fmt"

var g int

// g = 1    // syntax error: non-declaration statement outside function body

var i int = 2

// i := 42   // syntax error: non-declaration statement outside function body

func main() {
	g = 1
	i := 42 // type inferred

	fmt.Println(g)
	fmt.Println(i)
}
