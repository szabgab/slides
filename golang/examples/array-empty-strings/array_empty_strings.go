package main

import (
	"fmt"
)

func main() {
	var names [2]string
	if names[0] == "" {
		fmt.Println("empty") // empty
	}

	fmt.Println(names)      // [  ]
	fmt.Println(names[1])   //
	fmt.Println(len(names)) // 2

	fmt.Printf("%T\n", names) // [2]string

	names[1] = "Bar"
	names[0] = "Foo"

	fmt.Println(names)    // [Foo Bar]
	fmt.Println(names[1]) // Bar
}
