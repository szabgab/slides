package main

import "fmt"

func main() {
	s := "some string"
	fmt.Printf("%v %T\n", s, s)
	b := []byte{65, 66, 66, 65}
	fmt.Printf("%s %T\n", b, b)
}
