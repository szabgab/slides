package main

import (
	"fmt"
	"strings"
)

func main() {
	text := "This text,has,comma separated,vales"
	fmt.Println(text)

	shortStrings := strings.Split(text, ",")
	fmt.Println(shortStrings)
	fmt.Println(len(shortStrings))

	veryShortStrings := strings.Split(text, "")
	fmt.Println(veryShortStrings)
	fmt.Println(len(veryShortStrings))
}
