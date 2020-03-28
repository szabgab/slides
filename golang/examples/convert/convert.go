package main

import (
	"fmt"
)

func main() {
	n := 65
	q := float32(n)
	fmt.Printf("%v %T\n", n, n) //  65 int
	fmt.Printf("%v %T\n", q, q) // 65 float32

	z := 42.23
	p := int(z)
	fmt.Printf("%v %T\n", z, z) // 42.23 float64
	fmt.Printf("%v %T\n", p, p) // 42 int

	ns := string(n)
	fmt.Printf("%v %T\n", ns, ns) // A, string
}
