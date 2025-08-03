package main

import (
	"fmt"
)

func main() {
	a := "שלום"
	fmt.Println(a)
	fmt.Println(len(a))
	fmt.Printf("%T %T\n", a, a[0])
	fmt.Printf("%c %v\n", a[0], a[0])
	//fmt.Printf("%v\n", a[0:1])
	fmt.Println()
	txt := "H"
	fmt.Printf("%-2v %T\n", txt, txt)
	rn := 'H'
	fmt.Printf("%2v %T\n", rn, rn)
	fmt.Printf("%c\n", rn)
	fmt.Printf("%v %T\n", txt[0], txt[0])

	text := "Hello World!"
	fmt.Println(text)
	fmt.Printf("%v %T\n", text[0], text[0])
	if text[0] == 'H' {
		fmt.Println("match even thought one of them is uint8 and the other one is int32")
	}
}
