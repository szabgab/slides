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
	go count(3, "first")
	fmt.Println("Done")
}
