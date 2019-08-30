package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n = 42
	var q = float32(n)
	fmt.Printf("%T\n", q)

	var z = 42.23
	var p = int(z)
	fmt.Printf("%T\n", p)

	var x = "42"
	var r, _ = strconv.Atoi(x)
	fmt.Printf("%d %T\n", r, r)
}
