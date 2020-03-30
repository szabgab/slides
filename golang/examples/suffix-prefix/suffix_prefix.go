package main

import (
	"fmt"
	"strings"
)

func main() {
	text := "Some text here"
	fmt.Println(text)
	fmt.Println(strings.HasSuffix(text, "here"))
	fmt.Println(strings.HasPrefix(text, "here"))
	fmt.Println(strings.HasPrefix(text, "So"))

	fmt.Println(strings.Contains(text, "text"))

}
