package main

import (
	"fmt"
)

func main() {
	fmt.Println("Start")
	c := make(chan string)

	go count(5, "Apple", c)

	for msg := range c {
		fmt.Print(msg)
	}
	fmt.Println("End")
}

func count(n int, name string, c chan string) {
	for i := 1; i <= n; i++ {
		c <- fmt.Sprintf("%v %v\n", name, i)
	}
	close(c)
}
