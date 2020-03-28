package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	text := "Hello World!"
	fmt.Println(text)

	chars := strings.Split(text, "")
	fmt.Println(chars)
	sort.Strings(chars)
	fmt.Println(chars)
}
