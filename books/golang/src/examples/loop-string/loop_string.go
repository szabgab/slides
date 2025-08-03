package main

import (
	"fmt"
)

func main() {
	text := "Hello World!"
	text = "שלום"
	text = "Gábor Szabó"
	text = "lò mañana 😈 mas"
	text = "¿Còmo estas?"
	fmt.Println(text)

	for i, chr := range text {
		fmt.Printf("index: %2v  chr: %c\n", i, chr)
	}
}
