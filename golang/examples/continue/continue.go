package main

import (
	"fmt"
)

func main() {
	i := 0
	for {
		i++
		if i > 5 {
			break
		}

		if i < 3 {
			continue
		}
		fmt.Println(i)
	}
}
