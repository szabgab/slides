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

	fmt.Println()
	num := 258
	fmt.Printf("%v %T\n", num, num) // 258 int
	num16 := int16(num)
	fmt.Printf("%v %T\n", num16, num16) // 258 int16
	num8 := int8(num)
	fmt.Printf("%v %T\n", num8, num8) // 2 int8 - loss of the high bytes!
}
