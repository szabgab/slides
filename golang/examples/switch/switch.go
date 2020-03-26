package main

import (
	"fmt"
)

func main() {
	a := 1
	switch a {
	case 1:
		fmt.Println("one")
		fmt.Println("still one")
	case 2:
		fmt.Println("two")
		fmt.Println("still two")
	default:
		fmt.Println("Default")
	}
}
