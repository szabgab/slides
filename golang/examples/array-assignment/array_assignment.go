package main

import (
	"fmt"
)

func main() {
	var ar = [...]int{1, 2, 3}
	br := ar

	fmt.Println(ar)
	fmt.Println(br)
	ar[1] = 42
	fmt.Println(ar)
	fmt.Println(br)
}
