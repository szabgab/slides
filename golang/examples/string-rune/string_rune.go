package main

import (
	"fmt"
)

func main() {
	txt := "a"
	fmt.Println(txt)
	rn := 'a'
	fmt.Println(rn)

	fmt.Printf("%c\n", rn)

	fmt.Println(rn == rune(97))
	fmt.Println(97 == int(rn))

	text := "Hello World!"
	fmt.Println(text)
	fmt.Println(text[0])
	fmt.Println("H")
	fmt.Println('H')
	if text[0] == 'H' {
		fmt.Println("match")
	}
}
