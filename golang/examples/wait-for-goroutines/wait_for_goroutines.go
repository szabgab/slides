package main

import (
	"fmt"
	"sync"
)

func count(n int, name string) {
	for i := 1; i <= n; i++ {
		fmt.Printf("%v %v\n", name, i)
	}
}

func main() {
	fmt.Println("Start")
	var wg sync.WaitGroup

	wg.Add(1)

	go func() {
		count(5, "Apple")
		wg.Done()
	}()

	wg.Wait()
	fmt.Println("End")
}
