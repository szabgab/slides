package main

import (
	"fmt"
	"math/rand"
	"time"
)

func worker(in <-chan int, out chan<- int) {
	for number := range in {
		fmt.Printf("work on %v\n", number)
		delay := rand.Intn(3)
		time.Sleep(time.Duration(1000000 * delay))
		out <- number
	}
	//	close(out)
}

func main() {
	to := make(chan int, 10)
	from := make(chan int, 10)

	max := 10
	go worker(to, from)
	go worker(to, from)
	go worker(to, from)

	for i := 1; i <= max; i++ {
		to <- i
	}
	close(to)

	for i := 1; i <= max; i++ {
		res := <-from
		fmt.Printf("Result: %v\n", res)
	}

	// for res := range from {
	// 	fmt.Printf("Result: %v\n", res)
	// }

	time.Sleep(100000000)
}
