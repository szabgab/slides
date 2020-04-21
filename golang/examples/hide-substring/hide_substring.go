package main

import (
	"fmt"
	"strings"
)

func main() {
	input := "0123456789"
	fmt.Println(input)

	// show 4 * characters and then the last 4 characters
	out := "****" + input[len(input)-4:]
	fmt.Println(out)

	// show the first 4 characters and then 4 stars
	out = input[0:4] + "****"
	fmt.Println(out)

	// replace every character, except the last 4 by a *
	out = strings.Repeat("*", len(input)-4) + input[len(input)-4:]
	fmt.Println(out)

	// replace every character, except the first 4 by a *
	out = input[0:4] + strings.Repeat("*", len(input)-4)
	fmt.Println(out)
}
