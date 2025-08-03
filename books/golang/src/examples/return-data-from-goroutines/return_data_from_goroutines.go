package main

import (
	"fmt"
	"sync"
)

func main() {
	fmt.Println("Start")
	var wg sync.WaitGroup

	wg.Add(1)

	go func() {
		res := count(5, "Apple")
		fmt.Printf("Apple: %v\n", res)
		wg.Done()
	}()

	wg.Wait()
	fmt.Println("End")
}

func count(n int, name string) int {
	sum := 0
	for i := 1; i <= n; i++ {
		fmt.Printf("%v %v\n", name, i)
		sum += i
	}
	return sum
}
