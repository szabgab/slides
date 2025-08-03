package main

import (
	"fmt"
	"strconv"
)

func main() {
	var i int
	i, _ = strconv.Atoi("42")
	fmt.Printf("%v %T\n", i, i) // 42 int

	i, _ = strconv.Atoi("0")
	fmt.Printf("%v %T\n", i, i) // 0 int

	i, _ = strconv.Atoi("23\n")
	fmt.Printf("%v %T\n", i, i) // 0 int

	i, _ = strconv.Atoi("17x")
	fmt.Printf("%v %T\n", i, i) // 0 int
}
