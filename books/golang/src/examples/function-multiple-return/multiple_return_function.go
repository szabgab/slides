package main

import "fmt"

func main() {
	fmt.Println("Hello World")
	a, b := calc(3, 2)
	fmt.Printf("%v and %v\n", a, b)
}

func calc(a, b int) (int, int) {
	return a + b, a - b
}
