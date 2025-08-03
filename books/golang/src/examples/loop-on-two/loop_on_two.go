package main

import (
	"fmt"
)

func main() {
	for i, j := 1, 5; i+j < 20; i, j = i+1, j+2 {
		fmt.Printf("%v  %v\n", i, j)
	}
}
