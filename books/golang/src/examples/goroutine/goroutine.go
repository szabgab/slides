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
	count(3, "first")
	go count(3, "second")
	go count(3, "third")
	count(3, "fourth")
	fmt.Println("Done")
}
