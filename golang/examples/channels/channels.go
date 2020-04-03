package main

import (
	"fmt"
)

func main() {
	fmt.Println("Start")
	c := make(chan string)
	go func() {
		count(5, "Apple", c)
	}()

	//	msg := <-c
	// fmt.Print(msg)
	// for {
	// 	msg, open := <-c
	// 	if !open {
	// 		break
	// 	}
	// 	fmt.Print(msg)
	// }
	for msg := range c {
		fmt.Print(msg)
	}
	fmt.Println("End")
}

func count(n int, name string, c chan string) {
	sum := 0
	for i := 1; i <= n; i++ {
		c <- fmt.Sprintf("%v %v\n", name, i)
		sum += i
	}
	close(c)
}
