package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Println("Your name:")
	fmt.Scan(&s)
	fmt.Println(len(s))
}
