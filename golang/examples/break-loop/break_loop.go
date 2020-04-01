package main

import (
	"fmt"
)

func main() {
	i := 0
	for {
		fmt.Println(i)
		i++
		if i > 5 {
			break
		}
		fmt.Println("tail")
	}
	fmt.Println("after loop")
}
