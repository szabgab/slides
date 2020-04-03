package main

import (
	"fmt"
	"strconv"
)

func main() {
	aStr := "2.1"
	bStr := "7.3"
	a, _ := strconv.ParseFloat(aStr, 64)
	b, _ := strconv.ParseFloat(bStr, 64)
	fmt.Println(a + b)
	fmt.Println(a - b)
}
