package main

import (
	"fmt"
)

func main() {
	var word string
	for {
		fmt.Scan(&word)
		if word == "bye" {
			fmt.Println("Bye bye")
			break
		}
		fmt.Println(word)
	}
}
