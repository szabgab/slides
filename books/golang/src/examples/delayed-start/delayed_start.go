package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int)
	go start(ch)
	fmt.Println("now")
	ch <- 23
	time.Sleep(1000)
	ch <- 19
	time.Sleep(1000)
	ch <- 42

	time.Sleep(10000000)
	fmt.Println("end")
}

func start(in <-chan int) {
	fmt.Println("start")

	var port int
	received := time.Now()
LOOP:
	for {
		select {
		case port = <-in:
			received = time.Now()
			fmt.Printf("received port %v at %v\n", port, received)
		default:
			now := time.Now()
			elapsed := now.Sub(received)
			if elapsed > 1000000 {
				if port != 0 {
					fmt.Printf("delayed start on port %v\n", port)

				} else {
					fmt.Println("No port received")
				}
				break LOOP
			}
		}
		time.Sleep(1000)
	}
	fmt.Println("start done")
}
