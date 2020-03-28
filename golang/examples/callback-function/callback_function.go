package main

import (
	"fmt"
)

func main() {
	// fmt.Printf("%T\n", hello)  // func()
	run(hello)
	run(world)
}

func hello() {
	fmt.Println("Hello")
}

func world() {
	fmt.Println("World!")
}

func run(f func()) {
	f()
}
