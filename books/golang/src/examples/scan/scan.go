package main

import (
	"fmt"
)

func main() {
	var name string // declare variable as a string without assignment
	fmt.Print("Your name: ")
	fmt.Scan(&name)
	fmt.Printf("Hello %s, how are you?\n", name)
	fmt.Printf("Type %T\n", name) // string
}
