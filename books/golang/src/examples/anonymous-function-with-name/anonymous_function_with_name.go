package main

import "fmt"

func main() {
	f := func() {
		fmt.Println("Hello Anonymous!")
	}
	fmt.Println("Start")
	f()
	fmt.Println("End")
	fmt.Printf("%T", f)
}
