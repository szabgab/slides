package main

import (
	"fmt"
)

func main() {
	name := "Foo"
	res := fmt.Sprintf("Hello %v", name)
	fmt.Println("World")
	fmt.Print(res)
}
