package main

import (
	"fmt"
	"time"
)

func double(in <-chan int, out chan<- int) {
	for {
		number := <-in
		dbl := 2 * number
		//secs := 100000 //rand.Intn(10)
		time.Sleep(10000)
		out <- dbl
	}
}

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

	//go double(ch1, ch2)
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
