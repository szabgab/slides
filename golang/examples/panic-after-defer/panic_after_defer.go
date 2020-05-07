package main

import "fmt"

func main() {
	doIt(true)
}

func doIt(earlyStop bool) {
	fmt.Println("Start")
	defer fmt.Println("Deferred")
	if earlyStop {
		panic("This is bad")
	}

	fmt.Println("Finish")
}
