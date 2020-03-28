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
}
