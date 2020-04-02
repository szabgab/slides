package main

import (
	"fmt"
)

func main() {
	text := "Hello World!"
	fmt.Println(text)
	fmt.Println(text[1])
	fmt.Printf("%c\n", text[1])

	text = text[:5] + "-" + text[6:]
	fmt.Println(text)
}
