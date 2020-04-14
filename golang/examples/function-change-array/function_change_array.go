package main

import "fmt"

func main() {
	a := [...]int{4, 7, 12}
	fmt.Printf("before %v\n", a)
	change(a)
	fmt.Printf("after %v\n", a)
}

func change(val [3]int) {
	// fmt.Printf("address of val in inc: %v\n", val)
	// fmt.Printf("val in inc: %v\n", *val)
	// *val++
	fmt.Printf("val in inc: %v\n", val)
}
