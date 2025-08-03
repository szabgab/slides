package main

import "fmt"

func main() {
	s := "«ABC»"
	fmt.Println("s = ", s)
	fmt.Println(len(s))
	fmt.Println("byte", 0b11111111)
	π := 3.14
	fmt.Println(π)
	r1 := '™'
	fmt.Printf("%%c %c\n", r1)
	fmt.Println(r1)

	r2 := '\x6A'
	fmt.Printf("%c %v\n", r2, r2)

	r3 := '\u2122'
	fmt.Printf("\\u%04x %c %v\n", r3, r3, r3)
	fmt.Println(r3)

	r4 := '\U00002122'
	fmt.Printf("\\U%08x %c %v\n", r4, r4, r4)
	fmt.Println(r4)

	// https://golang.org/pkg/unicode/
	// release notes: https://golang.org/doc/go1.14 (at the end)

	s = "Peace שלום سلام"

	// `\pL` letter    `\pN`  number (also arabic numbers)
}
