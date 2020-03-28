package main

import (
	"fmt"
)

func main() {
	fmt.Println("before")
	if true {
		panic("We have encountered a problem")
	}
	fmt.Println("after")
}
