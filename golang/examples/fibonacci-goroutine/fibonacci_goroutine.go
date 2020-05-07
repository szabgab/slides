package main

import (
	"fmt"
)

func fibo(n int, out chan<- int) {
	out <- 1

	if n == 1 {
		close(out)
		return
	}

	out <- 1
	if n == 2 {
		close(out)
		return
	}
	a := 1
	b := 1
	for i := 3; i <= n; i++ {
		a, b = b, a+b
		out <- b
	}
	close(out)
}

func main() {
	ch := make(chan int)

	n := 10
	go fibo(n, ch)

	for res := range ch {
		fmt.Println(res)
	}
	fmt.Println("done")
}
