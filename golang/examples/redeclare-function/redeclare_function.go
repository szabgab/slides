package main

import "fmt"

func main() {
}

func say() {
	fmt.Println("Hello World")
}

func say(name string) {
	fmt.Printf("Hello %v\n", name)
}
