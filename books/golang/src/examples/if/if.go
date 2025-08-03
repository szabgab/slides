package main

import (
	"fmt"
)

func main() {
	var name string
	fmt.Print("What is the name of this langauage? ")
	fmt.Scan(&name)

	if name == "Go" {
		fmt.Println("Yes, that's the answer!")
	} else {
		fmt.Println("Well..")
	}
}
