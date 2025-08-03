package main

import "fmt"

func main() {
	fmt.Println("Start")
	run(func() {
		fmt.Println("Hello")
	})
	fmt.Println("End")
}

func run(f func()) {
	fmt.Printf("%T\n", f)
	f()
}
