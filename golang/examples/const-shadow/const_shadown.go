package main

import (
	"fmt"
)

const pi float32 = 3

func main() {
	fmt.Println(pi)
	const pi float32 = 3.14
	//pi := 3.14
	//pi = 7.1
	// static analyzer?
	fmt.Println(pi)
}
