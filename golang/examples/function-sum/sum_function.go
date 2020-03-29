package main

import (
	"fmt"
)

func main() {
	res := sum(2, 3, 7, 11)
	fmt.Println(res)
}

func sum(num ...int) int {
	fmt.Printf("%T  %v\n", num, num) // slice
	mySum := 0
	for _, v := range num {
		mySum += v
	}
	return mySum
}
