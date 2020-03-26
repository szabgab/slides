package main

import "fmt"

func main() {
	var flag bool = true
	fmt.Println(flag)        // true
	fmt.Printf("%T\n", flag) // bool

	flag = !flag
	fmt.Println(flag) // false

	other := false
	fmt.Printf("%v %T\n", other, other) // false bool
}
