package main

import "fmt"

func main() {
	n := 2i + 3
	fmt.Printf("%v %T\n", n, n)
	r := real(n)
	fmt.Printf("%v %T\n", r, r)
	i := imag(n)
	fmt.Printf("%v %T\n", i, i)
	fmt.Println()

	z := 1i
	fmt.Printf("%v %T\n", z, z)
	v := z * z
	fmt.Printf("%v %T\n", v, v)
	fmt.Println(v == -1)
	fmt.Println()

	c := complex(4, 5)
	fmt.Printf("%v %T\n", c, c)
}
