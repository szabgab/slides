package main

import (
	"fmt"
)

func main() {
	hello("Foo")
}

func hello(text string) {
	fmt.Printf("Hello %s\n", text)
}
