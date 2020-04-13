package main

import (
	"fmt"
	"strings"
)

func main() {
	expression := "  hello    space   world 42 "
	fmt.Printf("'%s'\n", expression)
	parts := strings.Fields(expression)
	fmt.Println(parts)
	fmt.Println(len(parts))
	fmt.Println()

	for _, part := range parts {
		fmt.Printf("%v\n", part)
	}
}
