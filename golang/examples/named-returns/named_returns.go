package main

import "fmt"

func div(a, b int) (result int) {
	result = a / b

	return
}

func main() {
	x := div(6, 2)
	fmt.Println(x)
}
