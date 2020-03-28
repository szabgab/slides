package main

import (
	"fmt"
)

func main() {
	text := "Hello World!"
	fmt.Println(text)

	for i, chr := range text {
		fmt.Printf("index: %2v  chr: %c\n", i, chr)
	}
}
