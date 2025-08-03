package main

import "fmt"

func main() {
	run(false)
	fmt.Println("--------")
	run(true)
}

func run(early bool) {
	fmt.Println("first")
	defer fmt.Println("do at the end")
	fmt.Println("second")
	if early {
		return
	}

	fmt.Println("last")
}
