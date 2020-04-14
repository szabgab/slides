package main

import "fmt"

func main() {
	a := 1
	fmt.Printf("before %v\n", a)
	inc(a)
	fmt.Printf("after %v\n", a)
}

func inc(val int) {
	fmt.Printf("val in inc: %v\n", val)
	val++
	fmt.Printf("val in inc: %v\n", val)
}
