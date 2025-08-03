package main

import (
	"fmt"
)

func main() {
OUT:
	for i := 1; i < 5; i++ {
		for j := i; j < 5; j++ {
			k := i * j
			if k > 10 {
				break OUT
			}
			fmt.Println(k)
		}
	}
}
