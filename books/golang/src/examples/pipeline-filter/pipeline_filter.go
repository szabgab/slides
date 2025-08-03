package main

import (
	"fmt"
)

func big(in <-chan int, out chan<- int) {
	for {
		number, open := <-in
		if !open {
			close(out)
			break
		}
		if number > 100 {
			out <- number
		}
	}
}

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	go big(ch1, ch2)
	numbers := []int{3, 7, 11, 8, 12, 4}
	for _, n := range numbers {
		ch1 <- n
		res, open := <-ch2
		if !open {
			break
		}
		fmt.Println(res)
	}
	close(ch1)
	fmt.Println("done")
}
