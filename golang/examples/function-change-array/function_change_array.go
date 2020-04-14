package main

import "fmt"

func main() {
	a := [...]int{4, 7, 12}
	fmt.Printf("before %v\n", a)
	change(a)
	fmt.Printf("after %v\n", a)
	reallyChange(&a)
	fmt.Printf("end %v\n", a)
}

func change(val [3]int) {
	fmt.Printf("val in change: %v\n", val)
	val[1] = 42
	fmt.Printf("val in change: %v\n", val)
}

func reallyChange(val *[3]int) {
	fmt.Printf("val in reallyChange: %v\n", val)
	val[1] = 42
	fmt.Printf("val in reallyChange: %v\n", val)
}
