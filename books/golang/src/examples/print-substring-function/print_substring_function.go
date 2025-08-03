package main

import (
	"fmt"
)

func main() {
	printSubstring("The black cat climbed the green tree", 10, 13)
}

func printSubstring(text string, start, end int) {
	fmt.Println(text[start:end])
}
