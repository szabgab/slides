package main

import (
	"fmt"
	"sync"
)

var counter int
var wg sync.WaitGroup

func count(n int) {
	for i := 0; i < n; i++ {
		counter++
	}
	wg.Done()
}

func main() {
	for j := 0; j < 3; j++ {
		wg.Add(1)
		go count(10000)
	}
	wg.Wait()

	fmt.Println(counter)
}
