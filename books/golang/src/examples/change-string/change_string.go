package main

import (
	"fmt"
)

func main() {
	text := "Hello World!"
	fmt.Println(text)

	// text[5] = "Y" // cannot assign to text[5]

	text = text[:5] + "-" + text[6:]
	fmt.Println(text)
}
