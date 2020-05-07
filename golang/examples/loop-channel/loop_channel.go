package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan string)

	go count("one", 1000, ch1)

	for {
		text := <-ch1
		fmt.Println(text)
	}
}

func count(name string, ms int, out chan<- string) {
	i := 0
	for {
		i++
		out <- fmt.Sprintf("%v %v", name, i)
		time.Sleep(time.Duration(1000000 * ms))
	}
}
