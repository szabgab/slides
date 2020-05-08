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
		time.Sleep(1000000000)
		out <- dbl
	}
}

func main() {
	jobs := make(chan int, 6)
	results := make(chan int)

	go double(jobs, results)
	// go double(ch1, ch2)
	// go double(ch1, ch2)
	numbers := []int{3, 7, 11, 8, 12, 4}
	start := time.Now()
	for _, n := range numbers {
		jobs <- n
	}

	for i := 0; i < len(numbers); i++ {
		res := <-results
		fmt.Println(res)
	}

	end := time.Now()
	fmt.Printf("Elapsed time: %v\n", end.Sub(start))
	close(jobs)
	fmt.Println("done")
}
