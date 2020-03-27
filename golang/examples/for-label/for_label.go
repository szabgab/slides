package main

import (
	"fmt"
)

func main() {
Out:
	for i := 1; i < 5; i++ {
		for j := i; j < 5; j++ {
			k := i * j
			if k > 10 {
				break Out
			}
			fmt.Println(k)
		}
	}
}
