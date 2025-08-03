package main

import (
	"fmt"
)

func main() {
	a := "cat"
	b := "dog"
	fmt.Println(a == b)
	fmt.Println(a < b)
	fmt.Println()

	smile := "😄"
	angry := "😠"

	fmt.Println(smile == angry)
	fmt.Println(smile < angry)
	fmt.Println(smile > angry)

}
