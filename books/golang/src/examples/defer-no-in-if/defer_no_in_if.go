package main

import (
	"fmt"
)

func main() {
	if true {
		fmt.Println("Before")
		defer fmt.Println("Middle")
		fmt.Println("After")	
	}

	fmt.Println("Outside")
}
