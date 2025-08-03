package main

import "fmt"

func main() {
	x := 1
	for i := 0; i <= 8; i++ {
		y := x << i
		fmt.Printf("%3v %9b\n", y, y)
	}
	fmt.Println()

	a := 42
	fmt.Printf("%3v %9b", a, a)

}
