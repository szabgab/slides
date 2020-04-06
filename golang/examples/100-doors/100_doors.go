package main

import "fmt"

func main() {
	for i, open := range doors(10) {
		fmt.Printf("%3v %v\n", i, open)
	}
}

func doors(n int) []bool {
	var doors = make([]bool, n)
	for i := 1; i <= n; i++ {
		d := i
		for d <= n {
			doors[d-1] = !doors[d-1]
			d += i
		}
	}
	return doors
}
