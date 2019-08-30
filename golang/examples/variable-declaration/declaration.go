package main

import "fmt"

var g int

// g = 1    // syntax error: non-declaration statement outside function body

var i int = 2

// i := 42   // syntax error: non-declaration statement outside function body

func main() {
	g = 1
	i := 42 // type inferreed

	fmt.Println(g)
	fmt.Println(i)
}

// var i int
// i = 42

// var i int = 42
// i := 42   // (is the same but this one cannot be used on the package level

// var (
//    i = 42
//    j = 23
// )
