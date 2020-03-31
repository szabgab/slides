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
	var fib []int

	for i := 1; i <= n; i++ {
		fib = append(fib, fibo(i))
	}
	return fib
}

func fibo(n int) int {
	if n == 1 || n == 2 {
		return 1
	}
	return fibo(n-1) + fibo(n-2)
}
