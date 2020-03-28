package main

import (
	"fmt"
)

const pi float32 = 3

func main() {
	fmt.Println(pi)
	const pi float32 = 3.14
	fmt.Println(pi)
}
