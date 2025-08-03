package main

import (
	"fmt"
)

func main() {
	rn := 'a'
	fmt.Println(rn)

	fmt.Printf("%T\n", rn)
	fmt.Printf("%c\n", rn)

	fmt.Println(rn == rune(97))
	fmt.Println(97 == int32(rn))

	fmt.Printf("char: %c\n", 97) // to display
	fmt.Printf("code: %d\n", rn) // to display
}
