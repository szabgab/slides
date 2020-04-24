package main

import (
	"fmt"
	"time"
)

func main() {
	before := time.Now()
	fmt.Printf("%T\n", before)
	fmt.Println(before.UnixNano())

	time.Sleep(1000000) // 1 ms

	after := time.Now()
	fmt.Println(after.UnixNano())

	elapsed := after.Sub(before)
	fmt.Printf("Elapsed: %T  %v\n", elapsed, elapsed)
}
