package main

import (
	"fmt"
)

func main() {
	a := "\n"
	b := '\n'
	fmt.Printf("string: '%v'\n", a)
	fmt.Printf("rune: '%v'\n", b) // 10

	c := "\r"
	d := '\r'
	fmt.Printf("string: '%v'\n", c)
	fmt.Printf("rune: '%v'\n", d) // 13
}
