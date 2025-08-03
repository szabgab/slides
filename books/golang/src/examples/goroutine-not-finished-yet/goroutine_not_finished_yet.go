package main

import (
	"fmt"
	"time"
)

func count(n int, name string) {
	for i := 0; i < n; i++ {
		fmt.Printf("%s %d\n", name, i)
		time.Sleep(1000)
	}
}

func main() {
	fmt.Println("Welcome")
	go count(30, "first")
	count(3, "second")
	count(3, "third")
	fmt.Println("Done")
}
