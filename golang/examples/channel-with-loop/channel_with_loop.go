package main

import (
	"fmt"
)

func main() {
	fmt.Println("Start")
	c := make(chan string)

	go count(5, "Apple", c)

	for i := 0; i < 8; i++ {
		msg, open := <-c
		if !open {
			break
		}
		fmt.Println(msg)
	}
	// for msg := range c {
	// 	//fmt.Println(time.Now().UnixNano())
	// 	fmt.Print(msg)
	// 	time.Sleep(1000000000)
	// }
	fmt.Println("End")
}

func count(n int, name string, c chan string) {
	for i := 1; i <= n; i++ {
		c <- fmt.Sprintf("%v %v\n", name, i)
	}
	close(c)
}
