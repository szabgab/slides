package main

import (
	"fmt"
	"sync"
)

func count(n int, name string) {
	for i := 1; i <= n; i++ {
		fmt.Printf("%v %v\n", name, i)
	}
	wg.Done()

}

var wg sync.WaitGroup

func main() {
	fmt.Println("Start")

	wg.Add(1)

	go count(1000, "Apple")
	go count(5, "Banana")

	wg.Wait()
	fmt.Println("End")
}
