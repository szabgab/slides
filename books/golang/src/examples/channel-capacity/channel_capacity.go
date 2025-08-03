package main

import (
	"fmt"
	"time"
)

func sleep() {
	time.Sleep(1000000000)
	fmt.Println("woke up")
}

func main() {
	ch := make(chan string, 2)
	// go sleep()
	ch <- "One"
	ch <- "Two"
	//  ch <- "Three"

	text := <-ch
	fmt.Println(text)

	fmt.Println(<-ch)

	//	fmt.Println(<-ch)
}
