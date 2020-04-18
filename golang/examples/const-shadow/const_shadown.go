package main

import (
	"fmt"
)

const pi float32 = 1.1

func main() {
	fmt.Println(pi)

	const pi float32 = 2.2
	fmt.Println(pi)

	{
		pi := 3.3
		fmt.Println(pi)
		pi = 4.4
		fmt.Println(pi)

	}
	fmt.Println(pi)
}
