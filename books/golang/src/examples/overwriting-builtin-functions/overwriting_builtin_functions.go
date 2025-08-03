package main

import "fmt"

func main() {
	len := len("abc")
	fmt.Println(len)
	// x := len("def")   //  cannot call non-function len (type int)
}
