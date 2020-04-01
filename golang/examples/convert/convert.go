package main

import (
	"fmt"
)

func main() {
	n := 65
	q := float32(n)
	fmt.Printf("%v %T\n", n, n) //  65 int
	fmt.Printf("%v %T\n", q, q) // 65 float32

	f := 42.23
	p := int(f)
	fmt.Printf("%v %T\n", f, f) // 42.23 float64
	fmt.Printf("%v %T\n", p, p) // 42 int

	ns := string(n)
	fmt.Printf("%v %T\n", ns, ns) // A, string

	ns2 := fmt.Sprintf("%d", n)
	fmt.Printf("%v %T\n", ns2, ns2) // 65, string

	fs := fmt.Sprintf("%f", f)
	fmt.Printf("%v %T\n", fs, fs) // 42.230000, string
}
