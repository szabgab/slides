package main

import (
	"fmt"
)

func main() {
	// fmt.Printf("%T\n", hello)  // func()
	run(hello)
	run(world)
}

func hello(fullName string) {
	fmt.Printf("Hello %s\n", fullName)
}

func world(name string) {
	fmt.Printf("World! %s\n", name)
}

func run(f func(text string)) {
	f("Foo Bar")
}
