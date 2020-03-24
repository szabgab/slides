package main

import (
	"fmt"
)

func main() {
	var name string
	fmt.Print("Your name: ")
	fmt.Scan(&name)
	fmt.Printf("Hello %s, how are you?\n", name)
	fmt.Printf("Length of the name is: %d\n", len(name))
}
