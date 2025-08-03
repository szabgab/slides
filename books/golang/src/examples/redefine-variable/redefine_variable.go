package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	a, err := strconv.Atoi("23")
	fmt.Println(a)
	if err != nil {
		os.Exit(1)
	}
	b, err := strconv.ParseFloat("3.4", 64)
	if err != nil {
		os.Exit(1)
	}
	fmt.Println(b)
}
