package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: fibonacci.go N")
		os.Exit(0)
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Invalid input")
		os.Exit(0)
	}

	var results = fibonacci(n)
	for _, v := range results {
		fmt.Println(v)
	}
}

func fibonacci(n int) []int {
	var fib = []int{}
	if n < 1 {
		fmt.Println("Not supported")
		return fib
	}
	if n == 1 {
		fib = append(fib, 1)
	}
	if n > 1 {
		fib = append(fib, 1, 1)
	}
	for i := 2; i < n; i++ {
		fib = append(fib, fib[i-2]+fib[i-1])
	}

	return fib
}
