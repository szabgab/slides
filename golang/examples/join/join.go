package main

import (
	"fmt"
	"strings"
)

func main() {
	shortStrings := []string{"abc", "def", "hello", "world"}
	text := strings.Join(shortStrings, "-")
	fmt.Println(text)
}
