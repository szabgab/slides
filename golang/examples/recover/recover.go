package main

import (
	"fmt"
)

func main() {
	fmt.Println("Before")
	fmt.Println()

	div(4, 2)
	fmt.Println()
	div(4, 0)

	fmt.Println()
	fmt.Println("After")
}

func div(a, b int) {
	fmt.Println("Start")

	defer func() {
		if err := recover(); err != nil {
			fmt.Printf("Error: %v\n", err)
			//log.Print("Error: ", err)
			//panic(err)
		}
	}()
	res := a / b
	fmt.Println(res)

	fmt.Println("End")
}
