package main

import (
	"fmt"
	"regexp"
)

func main() {
	fmt.Println("Hello")
	var validID = regexp.MustCompile(`^[a-z]+\[[0-9]+\]$`)

	fmt.Println(validID.MatchString("adam[23]"))
}
